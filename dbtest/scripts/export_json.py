# import hjson

# from complex.models import Character, Comic, Journey, Magazine, Series, Story
from complex.models import Place


class JsonExporter:
    DEFAULT_OUTPUT = "define_your_file_name"

    @staticmethod
    def check_args(key="", **kwargs):
        if key not in kwargs:
            raise RuntimeError(f"{key} is requierd")
        return kwargs[key]

    @staticmethod
    def replace_file_content(filename, content):
        try:
            fd = open(filename, mode="w", encoding="utf-8")
            fd.write(content)
            fd.close()
        except FileNotFoundError:
            print("ファイルをオープンできませんでした。")

    def __init__(self, filename="", **kwargs) -> None:
        if len(filename):
            self.json_filename = filename
        else:
            self.json_filename = JsonExporter.check_args("filename", **kwargs)
            if not len(self.json_filename):
                self.json_filename = JsonExporter.DEFAULT_OUTPUT

    def start(self):
        content = Place.get_geojson()
        JsonExporter.replace_file_content(self.json_filename, content)


# run() via shell
# (at project dir)$ python manage.py runscript setup_data
def run() -> None:
    task = JsonExporter("zatsumap.geojson")
    task.start()
