# Generated by Django 4.2.4 on 2023-09-19 01:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Character",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="紹介文"),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="名前"
                    ),
                ),
            ],
            options={
                "db_table_comment": "character キャラクター 主要5人、編集部、他 [リソース]",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="Comic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cover_image",
                    models.URLField(
                        blank=True,
                        help_text="版元ドットコムの書誌情報DBより",
                        null=True,
                        verbose_name="書影url",
                    ),
                ),
                (
                    "isbn",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="ISBN13"
                    ),
                ),
                (
                    "issued",
                    models.DateField(
                        help_text="巻末の奥付にある、初版発行日", null=True, verbose_name="発行日"
                    ),
                ),
                ("memo", models.TextField(blank=True, null=True, verbose_name="編集メモ")),
                (
                    "number",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="第n巻 入力するのは数字のみ",
                        null=True,
                        verbose_name="巻数",
                    ),
                ),
                (
                    "obi",
                    models.CharField(
                        blank=True,
                        help_text="特徴的な帯の文言",
                        max_length=255,
                        null=True,
                        verbose_name="オビ",
                    ),
                ),
                ("released", models.DateField(null=True, verbose_name="書店発売日")),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        help_text="例：ざつ旅-That's Journey- 1。※巻数の表記は作品毎に呼び方のバリエーションがある",
                        max_length=255,
                        null=True,
                        verbose_name="各巻タイトル",
                    ),
                ),
            ],
            options={
                "db_table_comment": "comic 単行本 1巻、2巻、…。単巻のみの場合はseries=NULL [リソース]",
                "ordering": ["number"],
            },
        ),
        migrations.CreateModel(
            name="Journey",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "key",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="記号"
                    ),
                ),
                ("memo", models.TextField(blank=True, null=True, verbose_name="編集メモ")),
                (
                    "number",
                    models.PositiveIntegerField(
                        blank=True, help_text="入力は数字のみ", null=True, verbose_name="第〇旅"
                    ),
                ),
            ],
            options={
                "db_table_comment": "journey 第〇旅、番外旅 [イベント]",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="Magazine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cover_image",
                    models.URLField(
                        blank=True,
                        help_text="例: https://dengekimaoh.jp/archives/008/202208/xxxxx.jpg",
                        null=True,
                        verbose_name="雑誌表紙",
                    ),
                ),
                ("memo", models.TextField(blank=True, null=True, verbose_name="編集メモ")),
                (
                    "released",
                    models.DateField(
                        help_text="書店等での発売日 ※タイトルの月の2か月前27日前後",
                        null=True,
                        verbose_name="発売日",
                    ),
                ),
                (
                    "site",
                    models.URLField(
                        blank=True,
                        help_text="例: https://dengekimaoh.jp/magazine/magazine-nnnnn.html",
                        null=True,
                        verbose_name="雑誌リンク",
                    ),
                ),
                (
                    "tag_line",
                    models.CharField(
                        blank=True,
                        help_text="表紙や付録になった号、などを表すタグ",
                        max_length=255,
                        null=True,
                        verbose_name="管理用タグ",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        help_text="雑誌のタイトル 例：電撃マオウ 2020年1月号",
                        max_length=255,
                        null=True,
                        verbose_name="タイトル",
                    ),
                ),
            ],
            options={
                "db_table_comment": "magazine 雑誌連載 マオウ [イベント]",
                "ordering": ["released", "pk"],
            },
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("memo", models.TextField(blank=True, null=True, verbose_name="編集メモ")),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="名前"
                    ),
                ),
            ],
            options={
                "db_table_comment": "person コンテンツの作者 ツイート/写真を撮影した人 [リソース]",
            },
        ),
        migrations.CreateModel(
            name="Place",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="住所"
                    ),
                ),
                (
                    "altitude",
                    models.DecimalField(
                        blank=True,
                        decimal_places=6,
                        max_digits=9,
                        null=True,
                        verbose_name="高度",
                    ),
                ),
                (
                    "latitude",
                    models.DecimalField(
                        blank=True,
                        decimal_places=6,
                        max_digits=8,
                        null=True,
                        verbose_name="緯度",
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        blank=True,
                        decimal_places=6,
                        max_digits=9,
                        null=True,
                        verbose_name="経度",
                    ),
                ),
                ("memo", models.TextField(blank=True, null=True, verbose_name="編集メモ")),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="地点名"
                    ),
                ),
            ],
            options={
                "db_table_comment": "place 場所 東京駅の顔出しパネル、登場店舗、宿泊場所、観光名所、施設、交通拠点 [リソース]",
                "ordering": ["-latitude", "longitude"],
            },
        ),
        migrations.CreateModel(
            name="Route",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("memo", models.TextField(blank=True, null=True, verbose_name="編集メモ")),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="名前"
                    ),
                ),
            ],
            options={
                "db_table_comment": "route 経路 placeを組み合わせて経路とする [リソース]",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="Series",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "author",
                    models.CharField(
                        blank=True,
                        help_text="著者複数名の場合は、代表者をカンマ区切りで列挙する",
                        max_length=255,
                        null=True,
                        verbose_name="著者名",
                    ),
                ),
                (
                    "label",
                    models.CharField(
                        blank=True,
                        help_text="コミック・シリーズのレーベル名称 例：電撃コミックスNEXT",
                        max_length=255,
                        null=True,
                        verbose_name="レーベル",
                    ),
                ),
                (
                    "magazine_title",
                    models.CharField(
                        blank=True,
                        help_text="雑誌連載の誌名か、Web連載のレーベル名称",
                        max_length=255,
                        null=True,
                        verbose_name="連載誌",
                    ),
                ),
                (
                    "publisher",
                    models.CharField(
                        blank=True,
                        help_text="出版社 例：KADOKAWA",
                        max_length=255,
                        null=True,
                        verbose_name="出版社",
                    ),
                ),
                (
                    "rel_series_id",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="モデルにはあえてリレーションを定義せず (単方向リスト)",
                        null=True,
                        verbose_name="関係シリーズ",
                    ),
                ),
                (
                    "short_title",
                    models.CharField(
                        blank=True,
                        help_text="略称や通称で代表的なもの",
                        max_length=255,
                        null=True,
                        verbose_name="略称",
                    ),
                ),
                (
                    "site",
                    models.URLField(
                        blank=True,
                        help_text="公式サイトや他のWebサイトから代表するものを1件",
                        null=True,
                        verbose_name="代表(公式)サイト",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        help_text="正確な作品の名称",
                        max_length=255,
                        null=True,
                        verbose_name="作品名",
                    ),
                ),
            ],
            options={
                "db_table_comment": "series 正シリーズと番外シリーズは、別々に登録する ※巻数が自然数の順列になる [リソース]",
            },
        ),
        migrations.CreateModel(
            name="Step",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("datetime", models.DateTimeField(null=True, verbose_name="日時")),
                (
                    "number",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="順番"
                    ),
                ),
                (
                    "place",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="step",
                        to="complex.place",
                    ),
                ),
                (
                    "route",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="step",
                        to="complex.route",
                    ),
                ),
            ],
            options={
                "db_table_comment": "step 訪問 routeに含まれる地点を訪れた日時 [イベント]",
            },
        ),
        migrations.CreateModel(
            name="Story",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "camera_zoom_level",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="(領域設定用)zoom"
                    ),
                ),
                (
                    "subtitle",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="サブタイトル"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="単話タイトル"
                    ),
                ),
                (
                    "camera_center_place",
                    models.ForeignKey(
                        help_text="place story このストーリーに登場する主な地点をすべて包含するような範囲(四角形)の中心",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="camera_center_place",
                        to="complex.place",
                        verbose_name="(領域設定用)",
                    ),
                ),
                (
                    "comic",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="story",
                        to="complex.comic",
                    ),
                ),
                (
                    "journey",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="story",
                        to="complex.journey",
                    ),
                ),
                (
                    "magazine",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="story",
                        to="complex.magazine",
                    ),
                ),
            ],
            options={
                "db_table_comment": "story 単行本の単話 第〇旅前編、第〇旅後編。コミック未収録もある [イベント]",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="Type_master",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "key",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="属性"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="参照名"
                    ),
                ),
                (
                    "value",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="値"
                    ),
                ),
            ],
            options={
                "db_table_comment": "type_master 分類型の項目の選択肢マスター [リソース]",
                "ordering": ["key", "id"],
            },
        ),
        migrations.CreateModel(
            name="Web_comic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cw_published", models.DateField(null=True, verbose_name="CW公開日")),
                (
                    "cw_url",
                    models.URLField(
                        blank=True, null=True, verbose_name="Comic Walkerリンク"
                    ),
                ),
                ("memo", models.TextField(blank=True, null=True, verbose_name="編集メモ")),
                ("nico_published", models.DateField(null=True, verbose_name="nico公開日")),
                (
                    "nico_url",
                    models.URLField(blank=True, null=True, verbose_name="ニコニコ静画リンク"),
                ),
                (
                    "pages",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="ページ数"
                    ),
                ),
                (
                    "part_number",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="分割の順列"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="各話の名前"
                    ),
                ),
                (
                    "story",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="web_comic",
                        to="complex.story",
                    ),
                ),
            ],
            options={
                "db_table_comment": "web_comic Web連載 第1旅(1)、番外旅、一枚モノ、… [リソース]",
            },
        ),
        migrations.CreateModel(
            name="Venue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="名称"
                    ),
                ),
                (
                    "story",
                    models.ManyToManyField(related_name="venue", to="complex.story"),
                ),
                (
                    "type_master",
                    models.ForeignKey(
                        help_text="type_master venue",
                        limit_choices_to={"key": "venue"},
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="venue",
                        to="complex.type_master",
                        verbose_name="分類",
                    ),
                ),
            ],
            options={
                "db_table_comment": "venue 目的地 会津、松島、那須、… [リソース]",
                "ordering": ["type_master", "name"],
            },
        ),
        migrations.CreateModel(
            name="Tweet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="内容"),
                ),
                (
                    "tweet_id",
                    models.CharField(
                        blank=True,
                        help_text="桁数が大きいため、JSON等では数値型で扱えないことに注意",
                        max_length=255,
                        null=True,
                        verbose_name="Tweet ID",
                    ),
                ),
                ("url", models.URLField(blank=True, null=True, verbose_name="固定URL")),
                (
                    "username",
                    models.CharField(
                        blank=True,
                        help_text="@username は変わる可能性があることに注意",
                        max_length=255,
                        null=True,
                        verbose_name="ツイ主の@username",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="tweet",
                        to="complex.person",
                    ),
                ),
                (
                    "step",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="tweet",
                        to="complex.step",
                    ),
                ),
                (
                    "type_master",
                    models.ForeignKey(
                        help_text="type_master tweet",
                        limit_choices_to={"key": "tweet"},
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="tweet",
                        to="complex.type_master",
                        verbose_name="分類",
                    ),
                ),
            ],
            options={
                "db_table_comment": "tweet Twitter 石坂さん、鈴ヶ森さん、読者等、無関係 [リソース]",
            },
        ),
        migrations.AddField(
            model_name="story",
            name="type_master",
            field=models.ForeignKey(
                help_text="type_master story",
                limit_choices_to={"key": "story"},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="story",
                to="complex.type_master",
                verbose_name="分類",
            ),
        ),
        migrations.CreateModel(
            name="Scene",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("memo", models.TextField(blank=True, null=True, verbose_name="編集メモ")),
                (
                    "page",
                    models.PositiveIntegerField(
                        blank=True, help_text="コミック掲載ページ", null=True, verbose_name="ページ"
                    ),
                ),
                (
                    "character",
                    models.ManyToManyField(
                        related_name="scene", to="complex.character"
                    ),
                ),
                (
                    "place",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="scene",
                        to="complex.place",
                    ),
                ),
                (
                    "story",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="scene",
                        to="complex.story",
                    ),
                ),
                (
                    "type_master",
                    models.ForeignKey(
                        help_text="type_master scene",
                        limit_choices_to={"key": "scene"},
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="scene",
                        to="complex.type_master",
                        verbose_name="分類",
                    ),
                ),
            ],
            options={
                "db_table_comment": "scene シーン 名シーン、ざつ旅ARのマーカー [イベント]",
                "ordering": ["type_master", "pk"],
            },
        ),
        migrations.AddField(
            model_name="route",
            name="story",
            field=models.ManyToManyField(related_name="route", to="complex.story"),
        ),
        migrations.AddField(
            model_name="route",
            name="type_master",
            field=models.ForeignKey(
                help_text="type_master route",
                limit_choices_to={"key": "route"},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="route",
                to="complex.type_master",
                verbose_name="分類",
            ),
        ),
        migrations.AddField(
            model_name="place",
            name="venue",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="place",
                to="complex.venue",
            ),
        ),
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "height",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="画像高さ"
                    ),
                ),
                (
                    "image_src",
                    models.URLField(blank=True, null=True, verbose_name="画像URL"),
                ),
                (
                    "link",
                    models.URLField(blank=True, null=True, verbose_name="参照ページURL"),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="タイトル"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        blank=True,
                        help_text="参照先固有の、撮影者を識別する情報",
                        max_length=255,
                        null=True,
                        verbose_name="撮影者",
                    ),
                ),
                (
                    "width",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="画像幅"
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="photo",
                        to="complex.person",
                    ),
                ),
                (
                    "step",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="photo",
                        to="complex.step",
                    ),
                ),
                (
                    "type_master",
                    models.ForeignKey(
                        help_text="type_master photo",
                        limit_choices_to={"key": "photo"},
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="photo",
                        to="complex.type_master",
                        verbose_name="分類",
                    ),
                ),
            ],
            options={
                "db_table_comment": "photo flickr (google place photo api有料) [リソース]",
            },
        ),
        migrations.AddField(
            model_name="person",
            name="type_master",
            field=models.ForeignKey(
                help_text="type_master person",
                limit_choices_to={"key": "person"},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="person",
                to="complex.type_master",
                verbose_name="分類",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="person",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="journey",
            name="type_master",
            field=models.ForeignKey(
                help_text="type_master journey",
                limit_choices_to={"key": "journey"},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="journey",
                to="complex.type_master",
                verbose_name="分類",
            ),
        ),
        migrations.CreateModel(
            name="Fragment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("memo", models.TextField(blank=True, null=True, verbose_name="編集メモ")),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="名前"
                    ),
                ),
                (
                    "url",
                    models.URLField(blank=True, null=True, verbose_name="参照URL/リンク"),
                ),
                (
                    "character",
                    models.ManyToManyField(
                        related_name="fragment", to="complex.character"
                    ),
                ),
                (
                    "place",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="fragment",
                        to="complex.place",
                    ),
                ),
                (
                    "story",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="fragment",
                        to="complex.story",
                    ),
                ),
                (
                    "type_master",
                    models.ForeignKey(
                        help_text="type_master fragment",
                        limit_choices_to={"key": "fragment"},
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="fragment",
                        to="complex.type_master",
                        verbose_name="分類",
                    ),
                ),
                (
                    "web_comic",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="fragment",
                        to="complex.web_comic",
                    ),
                ),
            ],
            options={
                "db_table_comment": "fragment その他媒体 表紙カラー、店舗特典、ポスター、別冊、雑誌付録。コミック収録と未収録がある [リソース]",
            },
        ),
        migrations.AddField(
            model_name="comic",
            name="series",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="comic",
                to="complex.series",
            ),
        ),
        migrations.AddField(
            model_name="character",
            name="type_master",
            field=models.ForeignKey(
                help_text="type_master character",
                limit_choices_to={"key": "character"},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="character",
                to="complex.type_master",
                verbose_name="分類",
            ),
        ),
    ]
