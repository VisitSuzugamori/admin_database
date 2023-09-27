import re
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    PHOTO_PROF_PATTERN = re.compile(r"^【(.*?)】 by (.*?)$")

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
        self.in_paragraph = False
        self.in_ignore = False
        self.data = {
            "photo": {
                "alt": "",
                "title": "",
                "image_src": "",
                "link": "",
                "username": "",
            },
            "place": {
                "address": "",
            },
            "venue": {
                "name": "",
            },
        }

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag == "p":
            self.in_paragraph = True
        if tag == "img":
            self.parse_photo_img(attrs)
            self.in_ignore = True
        if tag == "a":
            self.parse_photo_link(attrs)
            self.in_ignore = True
        if tag == "div":
            self.in_ignore = True

    def handle_data(self, data: str) -> None:
        if self.in_paragraph is True:
            if len(data.strip()) and data.find("巻 P") != -1:
                self.parse_address(data)
            self.in_paragraph = False
        elif self.in_ignore:
            self.in_ignore = False
        elif len(data.strip()):
            self.parse_photo_prof(data)

    def parse_photo_img(self, attrs: list) -> None:
        self.data["photo"]["alt"] = MyHTMLParser.retrieve_attr(attrs, "alt", "")
        self.data["photo"]["image_src"] = MyHTMLParser.retrieve_attr(attrs, "src", "")

    def parse_photo_link(self, attrs: list) -> None:
        self.data["photo"]["link"] = MyHTMLParser.retrieve_attr(attrs, "href", "")

    def parse_photo_prof(self, data: str) -> None:
        result = MyHTMLParser.PHOTO_PROF_PATTERN.match(data)
        if isinstance(result, re.Match):
            self.data["photo"]["title"] = result.group(1)
            self.data["photo"]["username"] = result.group(2)

    def parse_address(self, data: str):
        piece = data.split(sep=" ", maxsplit=5)
        piece = self.extend_list(piece, 6)
        self.data["venue"]["name"] = piece[3]
        self.data["place"]["address"] = f"{piece[3]} {piece[4]} {piece[5]}"

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
