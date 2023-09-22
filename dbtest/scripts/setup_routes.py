import re
from urllib.request import urlopen
import hjson
import jageocoder
from complex.models import (
    Comic,
    Photo,
    Place,
    Route,
    Scene,
    Series,
    Step,
    Story,
    Tweet,
    Type_master,
    Venue,
)

from ._my_html_parser import MyHTMLParser


class RouteImporter:
    VSJSTMPL = "https://visitsuzugamori.github.io/{key}/config.js"
    ZATSUTABI = "ざつ旅"
    FIRST_NUMBER_REGEXP = re.compile(r"^P(\d+)(\D|$)", re.ASCII)

    @staticmethod
    def parse_chapter_id(str: str) -> dict:
        parts = str.split(sep="-", maxsplit=3)
        if len(parts) < 2:
            return {}
        data = {
            "comic": {},
            "scene": {},
        }
        if parts[0].endswith("巻"):
            data["comic"]["number"] = int(parts[0].replace("巻", ""))
        if parts[1].startswith("P"):
            m = RouteImporter.FIRST_NUMBER_REGEXP.match(parts[1])
            # print(parts[1], m)
            if isinstance(m, re.Match):
                data["scene"]["page"] = int(m.group(1))
        return data

    @staticmethod
    def parse_location(location: dict) -> dict:
        if (
            "center" in location
            and isinstance(location["center"], list)
            and len(location["center"]) == 2
        ):
            return {
                "longitude": location["center"][0],
                "latitude": location["center"][1],
                "altitude": 0,
            }
        else:
            return {}

    def __init__(self) -> None:
        self.comics = {}
        self.type_master_ref = {}
        self.series = Series.objects.filter(short_title=RouteImporter.ZATSUTABI).get()
        if not jageocoder.is_initialized():
            jageocoder.init()

    def get_story(self):
        type_story_main = self.recall_type_master(
            key="story",
            value="本編",
        )
        return Story.objects.filter(type_master=type_story_main).all()

    def get_vsjs_url(self, story: Story) -> str:
        key = str(story.journey.key)  # type: ignore
        if str(story.title).endswith("前編"):
            key += "-1"
        elif str(story.title).endswith("後編"):
            key += "-2"
        return RouteImporter.VSJSTMPL.format(key=key)

    def get_json(self, story: Story) -> dict:
        page = urlopen(self.get_vsjs_url(story))
        html = page.read()
        str = html.decode()
        raw_data = str.removeprefix("const config = ").removesuffix(";\n")
        json = hjson.loads(raw_data)
        return json

    def recall_comic(self, number: int) -> Comic:
        if number not in self.comics:
            comic, created = Comic.objects.get_or_create(
                number=number, series=self.series
            )
            if not isinstance(comic, Comic):
                raise RuntimeError("database problem @comic")
            self.comics[number] = comic
        return self.comics[number]

    def recall_type_master(self, key: str, value: str) -> Type_master:
        name = f"{key}:{value}"
        if name not in self.type_master_ref:
            type_master = Type_master.objects.filter(
                key=key,
                value=value,
            ).get()
            if not isinstance(type_master, Type_master):
                raise RuntimeError("database problem @type_master")
            self.type_master_ref[name] = type_master
        return self.type_master_ref[name]

    def recall_default_route(self, story: Story) -> Route:
        type_route = self.recall_type_master(
            key="route",
            value="マップ取り込み",
        )
        route = Route.objects.filter(
            type_master=type_route,
            story=story,
        ).get()
        if not isinstance(route, Route):
            raise RuntimeError("database problem @route")
        return route

    def upsert_venue(self, data: dict, story: Story) -> Venue | None:
        type_venue_pref = self.recall_type_master(
            key="venue",
            value="都道府県",
        )
        type_venue_city = self.recall_type_master(
            key="venue",
            value="市区町村、政令市の行政区",
        )
        venue = None
        for item, type_ref in (
            (
                data["pref"],
                type_venue_pref,
            ),
            (
                data["city"],
                type_venue_city,
            ),
        ):
            venue, created = Venue.objects.get_or_create(
                type_master=type_ref,
                name=item,
            )
            if isinstance(venue, Venue):
                venue.story.add(story)
                venue.save()
            else:
                raise RuntimeError("database problem @venue")
        return venue

    def upsert_place(self, item: dict, venue: Venue) -> Place:
        place, created = Place.objects.get_or_create(
            venue=venue,
            name=item["name"],
            address=item["address"],
            latitude=item["latitude"],
            longitude=item["longitude"],
            altitude=item["altitude"],
        )
        if isinstance(place, Place):
            return place
        raise RuntimeError("database problem @place")

    def upsert_scene(self, page: int, story: Story, place: Place) -> Scene:
        if page < 1:
            raise RuntimeError("missing page num @scene")
        type_scene = self.recall_type_master(
            key="scene",
            value="本編より",
        )
        scene, created = Scene.objects.get_or_create(
            page=page,
            story=story,
            place=place,
            type_master=type_scene,
        )
        if isinstance(scene, Scene):
            return scene
        raise RuntimeError("database problem @scene")

    def upsert_step(self, route: Route, place: Place) -> Step:
        step, created = Step.objects.get_or_create(
            route=route,
            place=place,
            number=self._step_count,  # "順番"
            # datetime "日時"
        )
        if isinstance(step, Step):
            self._step_count += 1
            return step
        raise RuntimeError("database problem @step")

    def upsert_tweet(self, id_str: str, step: Step) -> None:
        if len(id_str) < 1:
            return None
        type_tweet = self.recall_type_master(
            key="tweet",
            value="一般",
        )
        tw, created = Tweet.objects.get_or_create(
            tweet_id=id_str,
            step=step,
            type_master=type_tweet,
        )
        if isinstance(tw, Tweet):
            return None
        raise RuntimeError("database problem @tweet")

    def upsert_photo(self, item: dict, step: Step) -> None:
        if len(item["image_src"]) < 1 and len(item["link"]) < 1:
            return None
        type_photo = self.recall_type_master(
            key="photo",
            value="Flickr",
        )
        if "title" in item and len(item["title"]):
            title = item["title"]
        elif "alt" in item and len(item["alt"]):
            title = item["alt"]
        elif "username" in item and len(item["username"]):
            title = f'by @{item["username"]}'
        else:
            title = ""
        photo, created = Photo.objects.get_or_create(
            step=step,
            type_master=type_photo,
            title=title,
            link=item["link"],
            image_src=item["image_src"],
            username=item["username"],
        )
        if isinstance(photo, Photo):
            return None
        raise RuntimeError("database problem @photo")

    @staticmethod
    def parse_address(data: list) -> dict:
        names = {
            "pref": "",
            "city": "",
            "address": "",
        }
        if not isinstance(data, list) or len(data) < 1:
            return names
        names["pref"] = data.pop(0)
        while len(data):
            elem = data.pop(0)
            if elem.endswith("郡"):
                names["city"] += elem
            elif (
                elem.endswith("市")
                or elem.endswith("区")
                or elem.endswith("町")
                or elem.endswith("村")
            ):
                names["city"] += elem
                names["address"] = f'{names["pref"]} {names["city"]} ' + "".join(data)
                break
        return names

    def update_geo(self, data: dict) -> dict:
        level = 6
        try:
            geo = jageocoder.reverse(
                data["place"]["longitude"], data["place"]["latitude"], level
            )
            ga = RouteImporter.parse_address(geo[0]["candidate"]["fullname"])
            data["venue"] |= ga
            data["place"]["address"] = ga["address"]
        except Exception as e:
            print(e)
        finally:
            print(data)
        return data

    def update_database(self, story: Story, data: dict):
        data = self.update_geo(data)
        # comic = self.recall_comic(int(data["comic"]["number"]))
        venue = self.upsert_venue(data["venue"], story)
        place = self.upsert_place(data["place"], venue)
        # print(place, end=" ")

        if "page" in data["scene"]:
            self.upsert_scene(data["scene"]["page"], story, place)

        # Route Step
        route = self.recall_default_route(story)
        step = self.upsert_step(route, place)

        self.upsert_tweet(data["tweet"], step)
        self.upsert_photo(data["photo"], step)

    def start(self):
        for story in self.get_story():
            json = self.get_json(story)
            if len(json["chapters"]) < 1:
                continue
            print(json["title"], end="")
            self._step_count = 1
            for chapter in json["chapters"]:
                dom_parser = MyHTMLParser()
                dom_parser.feed(chapter["description"])
                dom_parser.close()
                data = dom_parser.extract()
                dom_parser.reset()
                data |= self.parse_chapter_id(chapter["id"])
                data["place"] |= self.parse_location(chapter["location"])
                data["place"]["name"] = chapter["title"]
                data["tweet"] = chapter["tweet_id"]
                self.update_database(story, data)
                print(f":{self._step_count}", end="")
            print("<")
        jageocoder.free()

    def test(self):
        res = jageocoder.reverse(133.3109506, 35.5603343, 7)
        print(res)


def run():
    task = RouteImporter()
    task.start()
    # task.test()


"""
_keys = [
    "title",
    "subtitle",
    "byline",
    "footer",
    "chapters",
]
_chapters_keys = [
    "id", # '5巻-P136-東京駅'
    "title", # 東京駅
    "image",
    "tweet_id", # '1356727800854536194'
    "description", <p>5巻 P136  東京都千代田区 丸の内一丁目9</p> ...
    "location", {
        center: [139.7671248, 35.6812362],
        zoom: 14,
        pitch: 60,
        bearing: 0},
]

<div class="tweetContainer" id="tweet1356783562016522241"></div>
<p>5巻 P142  東京都渋谷区 千駄ケ谷一丁目35</p>
<p>5巻 P144  東京都渋谷区 代々木神園町4</p>
<p>
    <img alt="a food stand on a night"
        src="https://live.staticflickr.com/65535/52615354247_c2b0f0e9f0_z.jpg">
</p>
<p>
    photo from
    <a rel="noopener"
        href="https://www.flickr.com/search/?lat=35.6791113&amp;lon=139.694663&amp;radius=0.1&amp;has_geo=1&amp;view_all=1">
        Flickr
    </a>
    【a food stand on a night】 by cat_in_136
</p>
"""
