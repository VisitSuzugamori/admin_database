# Generated by Django 4.2.4 on 2023-09-21 00:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("complex", "0002_alter_character_type_master_alter_comic_isbn_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="magazine",
            options={"ordering": ["released", "title"]},
        ),
        migrations.AlterField(
            model_name="story",
            name="camera_center_place",
            field=models.ForeignKey(
                blank=True,
                help_text="place story このストーリーに登場する主な地点をすべて包含するような範囲(四角形)の中心",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="camera_center_place",
                to="complex.place",
                verbose_name="(領域設定用)",
            ),
        ),
        migrations.AlterField(
            model_name="story",
            name="comic",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="story",
                to="complex.comic",
            ),
        ),
        migrations.AlterField(
            model_name="story",
            name="journey",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="story",
                to="complex.journey",
            ),
        ),
    ]
