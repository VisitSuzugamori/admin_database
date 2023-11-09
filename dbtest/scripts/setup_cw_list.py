import re
from urllib.request import urlopen

from complex.models import (
    Web_comic,
    Comic,
    Series,
    Story,
    Type_master,
)

from ._comic_walker_index_parser import ComicWalkerIndexParser


class CwLinkImporter:
    CW = "https://comic-walker.com/contents/detail/KDCW_AM01200853010000_68/"
    ZATSUTABI = "ざつ旅"
    FIRST_NUMBER_REGEXP = re.compile(r"^P(\d+)(\D|$)", re.ASCII)
    FILENAME = "./cw_list.html"

    @staticmethod
    def parse_chapter_id(str: str) -> dict:
        parts = str.split(sep="-", maxsplit=3)
        if len(parts) < 2:
            return {}
        data = {
            "comic": {},
            "scene": {},
        }
        return data

    def __init__(self) -> None:
        self.comics = {}
        self.type_master_ref = {}
        self.series = Series.objects.filter(short_title=CwLinkImporter.ZATSUTABI).get()

    def get_story(self):
        type_story_main = self.recall_type_master(
            key="story",
            value="本編",
        )
        return Story.objects.filter(type_master=type_story_main).all()

    def get_content(self) -> str:
        try:
            return self.read_file_content()
        except FileNotFoundError:
            try:
                return self.get_online()
            except urllib.error.URLError as err:
                print(err.reason)
        raise RuntimeError("error occurred during input")

    def read_file_content(self):
        fd = open(CwLinkImporter.FILENAME, mode="r", encoding="utf-8")
        content = fd.read()
        fd.close()
        return content

    def get_online(self) -> str:
        page = urlopen(CwLinkImporter.CW)
        html = page.read()
        raw_data = html.decode()
        return raw_data

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

    def recall_default_route(self):
        type_route = self.recall_type_master(
            key="route",
            value="マップ取り込み",
        )
        route = Comic.objects.filter(
            type_master=type_route,

        ).get()
        if not isinstance(route, Route):
            raise RuntimeError("database problem @route")
        return route


    def update_database(self, data: dict):
        # comic = self.recall_comic(int(data["comic"]["number"]))
        # print(place, end=" ")
        pass

    def start(self):
        dom_parser = ComicWalkerIndexParser()
        dom_parser.feed(self.get_content())
        dom_parser.close()
        data = dom_parser.extract()
        dom_parser.reset()
        self.update_database(data)


def run():
    task = CwLinkImporter()
    task.start()
