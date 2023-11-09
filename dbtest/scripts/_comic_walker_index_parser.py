import re
from html.parser import HTMLParser


class ComicWalkerIndexParser(HTMLParser):
    TJ_PATTERN = re.compile(r"第(\d+)旅", re.ASCII)
    ZATSU_FULL = "ざつ旅-That's Journey-"
    MARU_NUM = {
        "①": 1,
        "②": 2,
        "③": 3,
        "④": 4,
        "⑤": 5,
        "⑥": 6,
        "⑦": 7,
        "⑧": 8,
        "⑨": 9,
    }

    @staticmethod
    def is_extra(subject: str) -> bool:
        return "番外旅" in subject

    @staticmethod
    def is_prequel(subject: str) -> bool:
        return "前編" in subject

    @staticmethod
    def is_sequel(subject: str) -> bool:
        return "後編" in subject

    @staticmethod
    def is_bonus(subject: str) -> bool:
        return "おまけ" in subject

    @staticmethod
    def is_zatutabi(subject: str) -> bool:
        return subject.startswith(ComicWalkerIndexParser.ZATSU_FULL)

    @staticmethod
    def find_story_num(subject: str) -> int:
        m = re.search(ComicWalkerIndexParser.TJ_PATTERN, subject)
        if isinstance(m, re.Match):
            return int(m.group(1))
        return 0

    @staticmethod
    def find_sub_num(subject: str) -> int:
        for maru, num in ComicWalkerIndexParser.MARU_NUM.items():
            if maru in subject:
                return int(num)
        return 0

    @staticmethod
    def retrieve_attr(mix: list, name: str, default) -> str:
        default_type = type(default)
        if len(mix) < 1:
            return default_type("")
        for item in mix:
            if len(item) > 1 and item[0] == name:
                return item[1]
        return default_type("")

    def __init__(self) -> None:
        HTMLParser.__init__(self)
        self.in_list = False
        self.data = {
            "web_comic": [],
        }

    def handle_starttag(self, tag: str, attrs: list) -> None:
        # ul#reversible
        if tag == "ul":
            elm = next(filter(lambda x: x[0] == "id" and x[1] == "reversible", attrs), None)
            if elm is not None:
                self.in_list = True
        if tag == "a" and self.in_list:
            self.parse_link(attrs)

    def handle_endtag(self, tag: str) -> None:
        if tag == "ul" and self.in_list:
            self.in_list = False

    def parse_link(self, attrs: list) -> None:
        if not ComicWalkerIndexParser.is_zatutabi:
            return None
        title = ComicWalkerIndexParser.retrieve_attr(attrs, "title", "")
        title = title.removeprefix(ComicWalkerIndexParser.ZATSU_FULL).lstrip()
        cw_link = ComicWalkerIndexParser.retrieve_attr(attrs, "href", "")
        story_num = ComicWalkerIndexParser.find_story_num(title)
        sub_num = ComicWalkerIndexParser.find_sub_num(title)
        is_extra = ComicWalkerIndexParser.is_extra(title)
        is_prequel = ComicWalkerIndexParser.is_prequel(title)
        is_sequel = ComicWalkerIndexParser.is_sequel(title)
        is_bonus = ComicWalkerIndexParser.is_bonus(title)
        is_announcement = False

        # patch
        if story_num == 0 and not is_extra:
            is_announcement = True
        # patch 22-1-0 北海道道東前編おまけ　あの瞬間
        if "北海道道東前編おまけ" in title:
            story_num = 22

        data = {
            "title": title,
            "cw_link": cw_link,
            "story_num": story_num,
            "sub_num": sub_num,
            "is_extra": is_extra,
            "is_prequel": is_prequel,
            "is_sequel": is_sequel,
            "is_bonus": is_bonus,
            "is_announcement": is_announcement,
        }

        print(data)
        self.data["web_comic"].append(data)

    @staticmethod
    def extend_list(input, *args):
        if len(args) < 1:
            num_of_cols = 1
        else:
            num_of_cols = int(args[0])
        output = list(input)
        num = len(output)
        if num > num_of_cols:
            raise RuntimeError("out of range for list extends")
        elif num < num_of_cols:
            output.extend([""] * (num_of_cols - num))
        return output

    def extract(self) -> dict:
        return self.data
