from complex.models import Type_master


class TypeMasterImporter:
    DEFAULT_ITEMS = {
        "character": [
            "主要登場人物",
            "主要登場人物の家族・関係者",
            "編集部",
            "旅先の出会い",
            "モブ",
            "その他",
        ],
        "fragment": [
            "告知絵",
            "店舗特典",
            "表紙",
            "別冊付録",
            "付録(クリアファイル等)",
            "広報ポスター",
            "ファン・アート",
            "その他",
        ],
        "journey": [
            "本編",
            "番外旅",
            "その他",
        ],
        "person": [
            "読者",
            "関係者",
            "一般",
            "その他",
        ],
        "photo": [
            "Flickr",
            "オフィシャル",
            "素材",
            "取材・撮影",
            "聖地巡礼、舞台訪問、追走",
            "一般",
            "無関係",
            "その他",
        ],
        "route": [
            "マップ取り込み",
            "調整済",
            "システム",
            "その他",
        ],
        "scene": [
            "ざつ旅AR",
            "本編より",
            "本編以外の原作",
            "ファン・アート",
            "その他",
        ],
        "story": [
            "本編",
            "番外旅",
            "番外旅 おうちで料理",
            "鈴ヶ森ちかの雑誌掲載作品等",
            "その他",
        ],
        "tweet": [
            "鈴ヶ森さん",
            "石坂ケンタさん",
            "アニメ制作関連",
            "本作品公式コラボレーション",
            "掲載店舗・施設、現地の観光協会、自治体広報、等",
            "編集部、出版社広報、等",
            "聖地巡礼、舞台訪問、追走",
            "一般",
            "無関係",
            "その他",
        ],
        "venue": [
            "都道府県",
            "市区町村、政令市の行政区",
            "大字、町名等の細かい行政界",
            "著名観光地",
            "ランドマーク",
            "温泉、銭湯、足湯",
            "飲食店、宿泊施設、土産物店、農水産物直売等",
            "鉄道駅、バス停、道の駅等",
            "特徴的な建造物",
            "施設・設備",
            "水準点、看板等",
            "橋梁、トンネル、土木構造物",
            "自然の景観",
            "道路・街道",
            "航空路",
            "船舶航路",
            "鉄道路線",
            "バス路線",
            "その他",
        ],
    }

    @classmethod
    def make(cls):
        Type_master.objects.get_or_create(
            id=0,
            name="default",
            key="-",
            value="***",
        )
        for key, values in TypeMasterImporter.DEFAULT_ITEMS.items():
            for value in values:
                name = f"{key}:{value}"
                obj, created = Type_master.objects.get_or_create(
                    name=name,
                    key=key,
                    value=value,
                )
                if created:
                    print(":", end="")
                else:
                    print(".", end="")


# run() via shell
# (at project dir)$ python manage.py runscript setup_data
def run():
    return TypeMasterImporter.make()
