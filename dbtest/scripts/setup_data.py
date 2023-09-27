from urllib.request import urlopen

import hjson
from complex.models import (
    Character,
    Comic,
    Journey,
    Magazine,
    Place,
    Route,
    Series,
    Story,
    Type_master,
    Venue,
)


class Importer:
    VS = "https://visitsuzugamori.github.io/VisitSuzugamori.json"
    SITE = "https://dengekimaoh.jp/series_info/zatsutabi/"
    CHARACTER = (
        "鈴ヶ森ちか",
        "蓮沼暦",
        "鵜木ゆい",
        "天空橋りり",
        "糀谷冬音",
        "吉本",
        "梅屋敷彩",
    )
    TYPE_MASTER_PREPARE = {
        "character_main": {"key": "character", "value": "主要登場人物"},
        "story_main": {"key": "story", "value": "本編"},
        "story_extra": {"key": "story", "value": "番外旅"},
        "story_other": {"key": "story", "value": "その他"},
        "route_vs": {"key": "route", "value": "マップ取り込み"},
        "venue_administrative": {"key": "venue", "value": "市区町村、政令市の行政区"},
        "venue_other": {"key": "venue", "value": "その他"},
        "journey_main": {"key": "journey", "value": "本編"},
    }

    def __init__(self, json_data) -> None:
        self.json_data = json_data
        self.series: Series | None = None
        self.comics = {}
        self.stories = {}
        self.magazines = {}
        self.journey = {}
        self.places = {}
        self.type_master_ref = {}
        self.prepare()

    def prepare(self) -> None:
        for name, kv in Importer.TYPE_MASTER_PREPARE.items():
            self.type_master_ref[name] = Type_master.objects.filter(
                key=kv["key"],
                value=kv["value"],
            ).get()

    def setup_series(self) -> None:
        item = self.json_data["series"]
        series, created = Series.objects.get_or_create(
            title=item["title"],
            short_title=item["short_title"],
            author=item["auther"],
            publisher=item["publish"],
            label=item["label"],
            magazine_title=item["magazine"],
            site=Importer.SITE,
        )
        self.series = series

    def setup_character(self) -> None:
        for one in self.CHARACTER:
            Character.objects.get_or_create(
                name=one,
                type_master=self.type_master_ref["character_main"],
            )

    def setup_comic(self) -> None:
        if self.series is None:
            return
        for number, item in self.json_data["books"].items():
            item_date = item["published"].partition("T")[0]
            comic, created = Comic.objects.get_or_create(
                series=self.series,
                number=number,
                title=f"{self.series.title} {number}",
                obi=item["obi"],
                issued=item_date,
                released=item_date,
                cover_image=item["cover_image_url"],
                isbn=item["isbn"],
            )
            self.comics[int(number)] = comic

    def setup_stories(self) -> None:
        for item in self.json_data["stories"].values():
            self.setup_story_item(item, "main")

    def setup_extra_stories(self) -> None:
        for item in self.json_data["extra_stories"].values():
            self.setup_story_item(item, "extra")

    def setup_story_item(self, item, type="") -> None:
        # recall comic
        if "books" in item and str(item["books"]).find("巻") != -1:
            book_number = int(str(item["books"]).rstrip("巻"))
            comic = self.comics[book_number]
        else:
            comic = None

        # Magazine
        magazine = self.setup_magazine(item)

        # Journey
        journey = self.setup_journey(item)

        # Place(camera)
        if "camera" in item and "center" in item["camera"]:
            place = self.setup_place(item["camera"]["center"])
        else:
            place = None

        # create story
        if "subtitle" in item:
            sub = str(item["subtitle"])
        else:
            sub = ""
        if "camera" in item and "zoom" in item["camera"]:
            zlevel = item["camera"]["zoom"]
        else:
            zlevel = None

        if type == "main":
            type_ref = self.type_master_ref["story_main"]
        elif type == "extra" and item["title"].startswith("番外旅"):
            type_ref = self.type_master_ref["story_extra"]
        else:
            type_ref = self.type_master_ref["story_other"]

        story, created = Story.objects.get_or_create(
            title=item["title"],
            subtitle=sub,
        )
        if created and isinstance(story, Story):
            story.camera_zoom_level = zlevel
            story.camera_center_place = place  # type: ignore
            story.magazine = magazine  # type: ignore
            story.comic = comic
            story.journey = journey  # type: ignore
            story.type_master = type_ref
            story.save()
            print(":", end="")
        else:
            print(".", end="")
        self.stories[item["title"]] = story

        # update Place(camera)
        if isinstance(place, Place):
            place.name = f"{story.title} (camera)"
            place.save()

        # Venue
        self.setup_venue(item, story, comic)

        # Route
        self.setup_route(story)

    def setup_web_comic(self, story):
        # rel story FK
        # title "各話の名前"
        # part_number "分割の順列"
        pass

    def setup_route(self, story) -> None:
        route, created = Route.objects.get_or_create(
            name=f"{story.title} (default)",
            type_master=self.type_master_ref["route_vs"],
        )
        route.story.add(story)
        route.save()

    def setup_magazine(self, item) -> None | Magazine:
        # published: "2019, 電撃マオウ 5月号",
        if "published" in item and item["published"].find("電撃マオウ") != -1:
            mag, created = Magazine.objects.get_or_create(title=item["published"])
            self.magazines[item["published"]] = mag
            return mag
        else:
            return None

    def setup_journey(self, item) -> None | Journey:
        # index: 1, key: "TJ01", v: "第1旅",
        if "index" in item and int(item["index"]) > 0:
            number = int(item["index"])
            key = "TJ{:02}".format(number)
            journey, created = Journey.objects.get_or_create(
                number=number,
                key=key,
                type_master=self.type_master_ref["journey_main"],
            )
            self.journey[number] = journey
            return journey
        else:
            return None

    def setup_place(self, point) -> Place:
        place, created = Place.objects.get_or_create(
            latitude=point[1],
            longitude=point[0],
            altitude=0,
        )
        return place

    def setup_venue(self, item, story, comic) -> None:
        # place: "郡山市 会津若松市",
        if "place" not in item:
            return None
        piece = item["place"].split(" ")
        for name in piece:
            self.setup_venue_item(name, story, comic)

    def setup_venue_item(self, name, story, comic) -> None:
        if story.type_master == self.type_master_ref["story_main"]:
            type_ref = self.type_master_ref["venue_administrative"]
        elif (
            name.endswith("市")
            or name.endswith("町")
            or name.endswith("村")
            or name.endswith("区")
        ):
            type_ref = self.type_master_ref["venue_administrative"]
        else:
            type_ref = self.type_master_ref["venue_other"]

        venue, created = Venue.objects.get_or_create(
            name=name,
            type_master=type_ref,
        )
        venue.story.add(story)
        venue.save()


# run() via shell
# (at project dir)$ python manage.py runscript setup_data
def run() -> None:
    # json_fd = open("./vs.json", "r")
    # vsdata = json.load(json_fd)
    # json_fd.close()

    page = urlopen(Importer.VS)
    html = page.read()
    str = html.decode()
    json = hjson.loads(str)

    task = Importer(json)
    task.setup_series()
    task.setup_character()
    task.setup_comic()
    task.setup_stories()
    task.setup_extra_stories()
