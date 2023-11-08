#!/usr/bin/env python


# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones intact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# manage.py dumpscript complex
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script
import os, sys
from django.db import transaction

class BasicImportHelper:

    def pre_import(self):
        pass

    @transaction.atomic
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        # You will probably want to call this method from save_or_locate()
        # Example:
        #   new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        # You may change this function to do specific lookup for specific objects
        #
        # original_class class of the django orm's object that needs to be located
        # original_pk_name the primary key of original_class
        # the_class      parent class of original_class which contains obj_content
        # pk_name        the primary key of original_class
        # pk_value       value of the primary_key
        # obj_content    content of the object which was not exported.
        #
        # You should use obj_content to locate the object on the target db
        #
        # An example where original_class and the_class are different is
        # when original_class is Farmer and the_class is Person. The table
        # may refer to a Farmer but you will actually need to locate Person
        # in order to instantiate that Farmer
        #
        # Example:
        #   if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #       pk_name="name"
        #       pk_value=obj_content[pk_name]
        #   if the_class == StaffGroup:
        #       pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    # From Python 3.3 we can check e.name - string match is for backward compatibility.
    if 'import_helper' in str(e):
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
    from dateutil.tz import tzoffset
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    # Initial Imports
    from accounts.models import CustomUser

    # Processing model: complex.models.Series

    from complex.models import Series

    complex_series_1 = Series()
    complex_series_1.author = '石坂 ケンタ'
    complex_series_1.label = '電撃コミックスNEXT'
    complex_series_1.magazine_title = '電撃マオウ'
    complex_series_1.publisher = 'KADOKAWA'
    complex_series_1.rel_series_id = None
    complex_series_1.short_title = 'ざつ旅'
    complex_series_1.site = 'https://dengekimaoh.jp/series_info/zatsutabi/'
    complex_series_1.title = "ざつ旅-That's Journey-"
    complex_series_1 = importer.save_or_locate(complex_series_1)

    # Processing model: complex.models.Comic

    from complex.models import Comic

    complex_comic_1 = Comic()
    complex_comic_1.cover_image = 'https://www.hanmoto.com/bd/img/9784049128253.jpg'
    complex_comic_1.isbn = '978-4-04-912825-3'
    complex_comic_1.issued = dateutil.parser.parse("2019-09-27")
    complex_comic_1.memo = None
    complex_comic_1.number = 1
    complex_comic_1.obi = 'ここではない、どこか。そこに私が待っている——。'
    complex_comic_1.released = dateutil.parser.parse("2019-09-27")
    complex_comic_1.series = complex_series_1
    complex_comic_1.title = "ざつ旅-That's Journey- 1"
    complex_comic_1 = importer.save_or_locate(complex_comic_1)

    complex_comic_2 = Comic()
    complex_comic_2.cover_image = 'https://www.hanmoto.com/bd/img/9784049130454.jpg'
    complex_comic_2.isbn = '978-4-04-913045-4'
    complex_comic_2.issued = dateutil.parser.parse("2020-02-10")
    complex_comic_2.memo = None
    complex_comic_2.number = 2
    complex_comic_2.obi = '旅は、ざつでいい。ざつがいい。'
    complex_comic_2.released = dateutil.parser.parse("2020-02-10")
    complex_comic_2.series = complex_series_1
    complex_comic_2.title = "ざつ旅-That's Journey- 2"
    complex_comic_2 = importer.save_or_locate(complex_comic_2)

    complex_comic_3 = Comic()
    complex_comic_3.cover_image = 'https://www.hanmoto.com/bd/img/9784049132991.jpg'
    complex_comic_3.isbn = '978-4-04-913299-1'
    complex_comic_3.issued = dateutil.parser.parse("2020-07-27")
    complex_comic_3.memo = None
    complex_comic_3.number = 3
    complex_comic_3.obi = '——また、行きます。'
    complex_comic_3.released = dateutil.parser.parse("2020-07-27")
    complex_comic_3.series = complex_series_1
    complex_comic_3.title = "ざつ旅-That's Journey- 3"
    complex_comic_3 = importer.save_or_locate(complex_comic_3)

    complex_comic_4 = Comic()
    complex_comic_4.cover_image = 'https://www.hanmoto.com/bd/img/9784049135916.jpg'
    complex_comic_4.isbn = '978-4-04-913591-6'
    complex_comic_4.issued = dateutil.parser.parse("2020-12-26")
    complex_comic_4.memo = None
    complex_comic_4.number = 4
    complex_comic_4.obi = '「いままで」から「これから」へ——'
    complex_comic_4.released = dateutil.parser.parse("2020-12-26")
    complex_comic_4.series = complex_series_1
    complex_comic_4.title = "ざつ旅-That's Journey- 4"
    complex_comic_4 = importer.save_or_locate(complex_comic_4)

    complex_comic_5 = Comic()
    complex_comic_5.cover_image = 'https://www.hanmoto.com/bd/img/9784049138023.jpg'
    complex_comic_5.isbn = '978-4-04-913802-3'
    complex_comic_5.issued = dateutil.parser.parse("2021-05-27")
    complex_comic_5.memo = None
    complex_comic_5.number = 5
    complex_comic_5.obi = '明日もちょっといい日になる。'
    complex_comic_5.released = dateutil.parser.parse("2021-05-27")
    complex_comic_5.series = complex_series_1
    complex_comic_5.title = "ざつ旅-That's Journey- 5"
    complex_comic_5 = importer.save_or_locate(complex_comic_5)

    complex_comic_6 = Comic()
    complex_comic_6.cover_image = 'https://www.hanmoto.com/bd/img/9784049141207.jpg'
    complex_comic_6.isbn = '978-4-04-914120-7'
    complex_comic_6.issued = dateutil.parser.parse("2021-12-25")
    complex_comic_6.memo = None
    complex_comic_6.number = 6
    complex_comic_6.obi = '出会った景色が目的地。'
    complex_comic_6.released = dateutil.parser.parse("2021-12-25")
    complex_comic_6.series = complex_series_1
    complex_comic_6.title = "ざつ旅-That's Journey- 6"
    complex_comic_6 = importer.save_or_locate(complex_comic_6)

    complex_comic_7 = Comic()
    complex_comic_7.cover_image = 'https://www.hanmoto.com/bd/img/9784049144307.jpg'
    complex_comic_7.isbn = '978-4-04-914430-7'
    complex_comic_7.issued = dateutil.parser.parse("2022-05-27")
    complex_comic_7.memo = None
    complex_comic_7.number = 7
    complex_comic_7.obi = 'ここに来たから できた思い出。'
    complex_comic_7.released = dateutil.parser.parse("2022-05-27")
    complex_comic_7.series = complex_series_1
    complex_comic_7.title = "ざつ旅-That's Journey- 7"
    complex_comic_7 = importer.save_or_locate(complex_comic_7)

    complex_comic_8 = Comic()
    complex_comic_8.cover_image = 'https://www.hanmoto.com/bd/img/9784049147100.jpg'
    complex_comic_8.isbn = '978-4-04-914710-0'
    complex_comic_8.issued = dateutil.parser.parse("2022-12-26")
    complex_comic_8.memo = None
    complex_comic_8.number = 8
    complex_comic_8.obi = 'この非日常は誰かの日常で。'
    complex_comic_8.released = dateutil.parser.parse("2022-12-26")
    complex_comic_8.series = complex_series_1
    complex_comic_8.title = "ざつ旅-That's Journey- 8"
    complex_comic_8 = importer.save_or_locate(complex_comic_8)

    complex_comic_9 = Comic()
    complex_comic_9.cover_image = 'https://www.hanmoto.com/bd/img/9784049150162_600.jpg'
    complex_comic_9.isbn = '9784049150162'
    complex_comic_9.issued = dateutil.parser.parse("2023-05-26")
    complex_comic_9.memo = 'https://dengekimaoh.jp/product/zatsutabi/322301000349.html'
    complex_comic_9.number = 9
    complex_comic_9.obi = '本当に好き。だから歩ける。'
    complex_comic_9.released = dateutil.parser.parse("2023-05-26")
    complex_comic_9.series = complex_series_1
    complex_comic_9.title = "ざつ旅-That's Journey- 9"
    complex_comic_9 = importer.save_or_locate(complex_comic_9)

    # Processing model: complex.models.Magazine

    from complex.models import Magazine

    complex_magazine_1 = Magazine()
    complex_magazine_1.cover_image = None
    complex_magazine_1.memo = ''
    complex_magazine_1.released = dateutil.parser.parse("2005-10-27")
    complex_magazine_1.site = None
    complex_magazine_1.tag_line = None
    complex_magazine_1.title = '電撃マオウ？ 不明'
    complex_magazine_1 = importer.save_or_locate(complex_magazine_1)

    complex_magazine_2 = Magazine()
    complex_magazine_2.cover_image = None
    complex_magazine_2.memo = ''
    complex_magazine_2.released = dateutil.parser.parse("2019-03-27")
    complex_magazine_2.site = 'https://www.fujisan.co.jp/product/1281681477/b/1803535/'
    complex_magazine_2.tag_line = '新連載'
    complex_magazine_2.title = '電撃マオウ 2019年5月号'
    complex_magazine_2 = importer.save_or_locate(complex_magazine_2)

    complex_magazine_3 = Magazine()
    complex_magazine_3.cover_image = None
    complex_magazine_3.memo = ''
    complex_magazine_3.released = dateutil.parser.parse("2019-04-27")
    complex_magazine_3.site = 'https://www.fujisan.co.jp/product/1281681477/b/1811359/'
    complex_magazine_3.tag_line = None
    complex_magazine_3.title = '電撃マオウ 2019年6月号'
    complex_magazine_3 = importer.save_or_locate(complex_magazine_3)

    complex_magazine_4 = Magazine()
    complex_magazine_4.cover_image = None
    complex_magazine_4.memo = ''
    complex_magazine_4.released = dateutil.parser.parse("2019-05-27")
    complex_magazine_4.site = 'https://www.fujisan.co.jp/product/1281681477/b/1825565/'
    complex_magazine_4.tag_line = None
    complex_magazine_4.title = '電撃マオウ 2019年7月号'
    complex_magazine_4 = importer.save_or_locate(complex_magazine_4)

    complex_magazine_5 = Magazine()
    complex_magazine_5.cover_image = None
    complex_magazine_5.memo = ''
    complex_magazine_5.released = dateutil.parser.parse("2019-06-27")
    complex_magazine_5.site = 'https://www.fujisan.co.jp/product/1281681477/b/1846565/'
    complex_magazine_5.tag_line = None
    complex_magazine_5.title = '電撃マオウ 2019年8月号'
    complex_magazine_5 = importer.save_or_locate(complex_magazine_5)

    complex_magazine_6 = Magazine()
    complex_magazine_6.cover_image = None
    complex_magazine_6.memo = ''
    complex_magazine_6.released = dateutil.parser.parse("2019-07-26")
    complex_magazine_6.site = 'https://www.fujisan.co.jp/product/1281681477/b/1852543/'
    complex_magazine_6.tag_line = None
    complex_magazine_6.title = '電撃マオウ 2019年9月号'
    complex_magazine_6 = importer.save_or_locate(complex_magazine_6)

    complex_magazine_7 = Magazine()
    complex_magazine_7.cover_image = None
    complex_magazine_7.memo = ''
    complex_magazine_7.released = dateutil.parser.parse("2019-09-27")
    complex_magazine_7.site = 'https://www.fujisan.co.jp/product/1281681477/b/1865344/'
    complex_magazine_7.tag_line = None
    complex_magazine_7.title = '電撃マオウ 2019年10月号'
    complex_magazine_7 = importer.save_or_locate(complex_magazine_7)

    complex_magazine_8 = Magazine()
    complex_magazine_8.cover_image = None
    complex_magazine_8.memo = ''
    complex_magazine_8.released = dateutil.parser.parse("2019-09-27")
    complex_magazine_8.site = 'https://www.fujisan.co.jp/product/1281681477/b/1878719/'
    complex_magazine_8.tag_line = None
    complex_magazine_8.title = '電撃マオウ 2019年11月号'
    complex_magazine_8 = importer.save_or_locate(complex_magazine_8)

    complex_magazine_9 = Magazine()
    complex_magazine_9.cover_image = None
    complex_magazine_9.memo = ''
    complex_magazine_9.released = dateutil.parser.parse("2019-10-26")
    complex_magazine_9.site = 'https://www.fujisan.co.jp/product/1281681477/b/1890948/'
    complex_magazine_9.tag_line = None
    complex_magazine_9.title = '電撃マオウ 2019年12月号'
    complex_magazine_9 = importer.save_or_locate(complex_magazine_9)

    complex_magazine_10 = Magazine()
    complex_magazine_10.cover_image = None
    complex_magazine_10.memo = ''
    complex_magazine_10.released = dateutil.parser.parse("2019-11-27")
    complex_magazine_10.site = 'https://www.fujisan.co.jp/product/1281681477/b/1901845/'
    complex_magazine_10.tag_line = None
    complex_magazine_10.title = '電撃マオウ 2020年1月号'
    complex_magazine_10 = importer.save_or_locate(complex_magazine_10)

    complex_magazine_11 = Magazine()
    complex_magazine_11.cover_image = None
    complex_magazine_11.memo = ''
    complex_magazine_11.released = dateutil.parser.parse("2019-12-26")
    complex_magazine_11.site = 'https://www.fujisan.co.jp/product/1281681477/b/1920608/'
    complex_magazine_11.tag_line = None
    complex_magazine_11.title = '電撃マオウ 2020年2月号'
    complex_magazine_11 = importer.save_or_locate(complex_magazine_11)

    complex_magazine_12 = Magazine()
    complex_magazine_12.cover_image = None
    complex_magazine_12.memo = ''
    complex_magazine_12.released = dateutil.parser.parse("2020-01-27")
    complex_magazine_12.site = 'https://www.fujisan.co.jp/product/1281681477/b/1924654/'
    complex_magazine_12.tag_line = None
    complex_magazine_12.title = '電撃マオウ 2020年3月号'
    complex_magazine_12 = importer.save_or_locate(complex_magazine_12)

    complex_magazine_13 = Magazine()
    complex_magazine_13.cover_image = None
    complex_magazine_13.memo = ''
    complex_magazine_13.released = dateutil.parser.parse("2020-02-27")
    complex_magazine_13.site = 'https://www.fujisan.co.jp/product/1281681477/b/1936699/'
    complex_magazine_13.tag_line = None
    complex_magazine_13.title = '電撃マオウ 2020年4月号'
    complex_magazine_13 = importer.save_or_locate(complex_magazine_13)

    complex_magazine_14 = Magazine()
    complex_magazine_14.cover_image = None
    complex_magazine_14.memo = ''
    complex_magazine_14.released = dateutil.parser.parse("2020-03-27")
    complex_magazine_14.site = 'https://www.fujisan.co.jp/product/1281681477/b/1950108/'
    complex_magazine_14.tag_line = None
    complex_magazine_14.title = '電撃マオウ 2020年5月号'
    complex_magazine_14 = importer.save_or_locate(complex_magazine_14)

    complex_magazine_15 = Magazine()
    complex_magazine_15.cover_image = None
    complex_magazine_15.memo = ''
    complex_magazine_15.released = dateutil.parser.parse("2020-04-27")
    complex_magazine_15.site = 'https://www.fujisan.co.jp/product/1281681477/b/1963258/'
    complex_magazine_15.tag_line = None
    complex_magazine_15.title = '電撃マオウ 2020年6月号'
    complex_magazine_15 = importer.save_or_locate(complex_magazine_15)

    complex_magazine_16 = Magazine()
    complex_magazine_16.cover_image = None
    complex_magazine_16.memo = ''
    complex_magazine_16.released = dateutil.parser.parse("2020-05-27")
    complex_magazine_16.site = 'https://www.fujisan.co.jp/product/1281681477/b/1976477/'
    complex_magazine_16.tag_line = None
    complex_magazine_16.title = '電撃マオウ 2020年7月号'
    complex_magazine_16 = importer.save_or_locate(complex_magazine_16)

    complex_magazine_17 = Magazine()
    complex_magazine_17.cover_image = None
    complex_magazine_17.memo = ''
    complex_magazine_17.released = dateutil.parser.parse("2020-06-27")
    complex_magazine_17.site = 'https://www.fujisan.co.jp/product/1281681477/b/1988616/'
    complex_magazine_17.tag_line = None
    complex_magazine_17.title = '電撃マオウ 2020年8月号'
    complex_magazine_17 = importer.save_or_locate(complex_magazine_17)

    complex_magazine_18 = Magazine()
    complex_magazine_18.cover_image = None
    complex_magazine_18.memo = ''
    complex_magazine_18.released = dateutil.parser.parse("2020-07-27")
    complex_magazine_18.site = 'https://www.fujisan.co.jp/product/1281681477/b/2000104/'
    complex_magazine_18.tag_line = None
    complex_magazine_18.title = '電撃マオウ 2020年9月号'
    complex_magazine_18 = importer.save_or_locate(complex_magazine_18)

    complex_magazine_19 = Magazine()
    complex_magazine_19.cover_image = None
    complex_magazine_19.memo = ''
    complex_magazine_19.released = dateutil.parser.parse("2020-08-27")
    complex_magazine_19.site = 'https://www.fujisan.co.jp/product/1281681477/b/2019534/'
    complex_magazine_19.tag_line = None
    complex_magazine_19.title = '電撃マオウ 2020年10月号'
    complex_magazine_19 = importer.save_or_locate(complex_magazine_19)

    complex_magazine_20 = Magazine()
    complex_magazine_20.cover_image = None
    complex_magazine_20.memo = ''
    complex_magazine_20.released = dateutil.parser.parse("2020-09-27")
    complex_magazine_20.site = 'https://dengekimaoh.jp/magazine/magazine-10043.html'
    complex_magazine_20.tag_line = '表紙 コミック発売'
    complex_magazine_20.title = '電撃マオウ 2020年11月号'
    complex_magazine_20 = importer.save_or_locate(complex_magazine_20)

    complex_magazine_21 = Magazine()
    complex_magazine_21.cover_image = None
    complex_magazine_21.memo = ''
    complex_magazine_21.released = dateutil.parser.parse("2020-10-27")
    complex_magazine_21.site = 'https://dengekimaoh.jp/magazine/magazine-10042.html'
    complex_magazine_21.tag_line = None
    complex_magazine_21.title = '電撃マオウ 2020年12月号'
    complex_magazine_21 = importer.save_or_locate(complex_magazine_21)

    complex_magazine_22 = Magazine()
    complex_magazine_22.cover_image = None
    complex_magazine_22.memo = ''
    complex_magazine_22.released = dateutil.parser.parse("2020-11-27")
    complex_magazine_22.site = 'https://dengekimaoh.jp/magazine/magazine-10041.html'
    complex_magazine_22.tag_line = None
    complex_magazine_22.title = '電撃マオウ 2021年1月号'
    complex_magazine_22 = importer.save_or_locate(complex_magazine_22)

    complex_magazine_23 = Magazine()
    complex_magazine_23.cover_image = None
    complex_magazine_23.memo = ''
    complex_magazine_23.released = dateutil.parser.parse("2020-12-26")
    complex_magazine_23.site = 'https://www.fujisan.co.jp/product/1281681477/b/2057229/'
    complex_magazine_23.tag_line = None
    complex_magazine_23.title = '電撃マオウ 2021年2月号'
    complex_magazine_23 = importer.save_or_locate(complex_magazine_23)

    complex_magazine_24 = Magazine()
    complex_magazine_24.cover_image = None
    complex_magazine_24.memo = ''
    complex_magazine_24.released = dateutil.parser.parse("2021-01-27")
    complex_magazine_24.site = 'https://dengekimaoh.jp/magazine/magazine-10040.html'
    complex_magazine_24.tag_line = None
    complex_magazine_24.title = '電撃マオウ 2021年3月号'
    complex_magazine_24 = importer.save_or_locate(complex_magazine_24)

    complex_magazine_25 = Magazine()
    complex_magazine_25.cover_image = None
    complex_magazine_25.memo = ''
    complex_magazine_25.released = dateutil.parser.parse("2021-02-26")
    complex_magazine_25.site = 'https://dengekimaoh.jp/magazine/magazine-10039.html'
    complex_magazine_25.tag_line = None
    complex_magazine_25.title = '電撃マオウ 2021年4月号'
    complex_magazine_25 = importer.save_or_locate(complex_magazine_25)

    complex_magazine_26 = Magazine()
    complex_magazine_26.cover_image = None
    complex_magazine_26.memo = ''
    complex_magazine_26.released = dateutil.parser.parse("2021-03-27")
    complex_magazine_26.site = 'https://dengekimaoh.jp/magazine/magazine-10038.html'
    complex_magazine_26.tag_line = None
    complex_magazine_26.title = '電撃マオウ 2021年5月号'
    complex_magazine_26 = importer.save_or_locate(complex_magazine_26)

    complex_magazine_27 = Magazine()
    complex_magazine_27.cover_image = None
    complex_magazine_27.memo = ''
    complex_magazine_27.released = dateutil.parser.parse("2021-04-27")
    complex_magazine_27.site = 'https://dengekimaoh.jp/magazine/magazine-10037.html'
    complex_magazine_27.tag_line = None
    complex_magazine_27.title = '電撃マオウ 2021年6月号'
    complex_magazine_27 = importer.save_or_locate(complex_magazine_27)

    complex_magazine_28 = Magazine()
    complex_magazine_28.cover_image = None
    complex_magazine_28.memo = ''
    complex_magazine_28.released = dateutil.parser.parse("2021-05-27")
    complex_magazine_28.site = 'https://dengekimaoh.jp/magazine/magazine-10036.html'
    complex_magazine_28.tag_line = '表紙 付録 コミック発売'
    complex_magazine_28.title = '電撃マオウ 2021年7月号'
    complex_magazine_28 = importer.save_or_locate(complex_magazine_28)

    complex_magazine_29 = Magazine()
    complex_magazine_29.cover_image = None
    complex_magazine_29.memo = ''
    complex_magazine_29.released = dateutil.parser.parse("2021-06-27")
    complex_magazine_29.site = 'https://dengekimaoh.jp/magazine/magazine-10035.html'
    complex_magazine_29.tag_line = None
    complex_magazine_29.title = '電撃マオウ 2021年8月号'
    complex_magazine_29 = importer.save_or_locate(complex_magazine_29)

    complex_magazine_30 = Magazine()
    complex_magazine_30.cover_image = None
    complex_magazine_30.memo = ''
    complex_magazine_30.released = dateutil.parser.parse("2021-07-21")
    complex_magazine_30.site = 'https://dengekimaoh.jp/magazine/magazine-10034.html'
    complex_magazine_30.tag_line = None
    complex_magazine_30.title = '電撃マオウ 2021年9月号'
    complex_magazine_30 = importer.save_or_locate(complex_magazine_30)

    complex_magazine_31 = Magazine()
    complex_magazine_31.cover_image = None
    complex_magazine_31.memo = ''
    complex_magazine_31.released = dateutil.parser.parse("2021-08-27")
    complex_magazine_31.site = 'https://dengekimaoh.jp/magazine/magazine-10033.html'
    complex_magazine_31.tag_line = None
    complex_magazine_31.title = '電撃マオウ 2021年10月号'
    complex_magazine_31 = importer.save_or_locate(complex_magazine_31)

    complex_magazine_32 = Magazine()
    complex_magazine_32.cover_image = None
    complex_magazine_32.memo = ''
    complex_magazine_32.released = dateutil.parser.parse("2021-09-27")
    complex_magazine_32.site = 'https://dengekimaoh.jp/magazine/magazine-10125.html'
    complex_magazine_32.tag_line = None
    complex_magazine_32.title = '電撃マオウ 2021年11月号'
    complex_magazine_32 = importer.save_or_locate(complex_magazine_32)

    complex_magazine_33 = Magazine()
    complex_magazine_33.cover_image = 'https://dengekimaoh.jp/archives/014/202110/54389a5937747dc3f8e7fe67e555c89d1d9157cf951f61b7825f9976b2418794.jpg'
    complex_magazine_33.memo = ''
    complex_magazine_33.released = dateutil.parser.parse("2021-10-20")
    complex_magazine_33.site = 'https://dengekimaoh.jp/news/special/20211019.html'
    complex_magazine_33.tag_line = '付録 青騎士'
    complex_magazine_33.title = '電撃マオウ Encounter with the [Der Blaue Reiter] (『青騎士』第4号 特別小冊子)'
    complex_magazine_33 = importer.save_or_locate(complex_magazine_33)

    complex_magazine_34 = Magazine()
    complex_magazine_34.cover_image = None
    complex_magazine_34.memo = ''
    complex_magazine_34.released = dateutil.parser.parse("2021-10-27")
    complex_magazine_34.site = 'https://dengekimaoh.jp/magazine/magazine-10126.html'
    complex_magazine_34.tag_line = '表紙 コミック発売'
    complex_magazine_34.title = '電撃マオウ 2021年12月号'
    complex_magazine_34 = importer.save_or_locate(complex_magazine_34)

    complex_magazine_35 = Magazine()
    complex_magazine_35.cover_image = None
    complex_magazine_35.memo = ''
    complex_magazine_35.released = dateutil.parser.parse("2021-11-27")
    complex_magazine_35.site = 'https://dengekimaoh.jp/magazine/magazine-10261.html'
    complex_magazine_35.tag_line = None
    complex_magazine_35.title = '電撃マオウ 2022年1月号'
    complex_magazine_35 = importer.save_or_locate(complex_magazine_35)

    complex_magazine_36 = Magazine()
    complex_magazine_36.cover_image = None
    complex_magazine_36.memo = ''
    complex_magazine_36.released = dateutil.parser.parse("2021-12-25")
    complex_magazine_36.site = 'https://dengekimaoh.jp/magazine/magazine-10359.html'
    complex_magazine_36.tag_line = None
    complex_magazine_36.title = '電撃マオウ 2022年2月号'
    complex_magazine_36 = importer.save_or_locate(complex_magazine_36)

    complex_magazine_37 = Magazine()
    complex_magazine_37.cover_image = None
    complex_magazine_37.memo = ''
    complex_magazine_37.released = dateutil.parser.parse("2022-01-27")
    complex_magazine_37.site = 'https://dengekimaoh.jp/magazine/magazine-10429.html'
    complex_magazine_37.tag_line = None
    complex_magazine_37.title = '電撃マオウ 2022年3月号'
    complex_magazine_37 = importer.save_or_locate(complex_magazine_37)

    complex_magazine_38 = Magazine()
    complex_magazine_38.cover_image = None
    complex_magazine_38.memo = ''
    complex_magazine_38.released = dateutil.parser.parse("2022-02-26")
    complex_magazine_38.site = 'https://dengekimaoh.jp/magazine/magazine-10559.html'
    complex_magazine_38.tag_line = None
    complex_magazine_38.title = '電撃マオウ 2022年4月号'
    complex_magazine_38 = importer.save_or_locate(complex_magazine_38)

    complex_magazine_39 = Magazine()
    complex_magazine_39.cover_image = None
    complex_magazine_39.memo = ''
    complex_magazine_39.released = dateutil.parser.parse("2022-03-26")
    complex_magazine_39.site = 'https://dengekimaoh.jp/magazine/magazine-10667.html'
    complex_magazine_39.tag_line = None
    complex_magazine_39.title = '電撃マオウ 2022年5月号'
    complex_magazine_39 = importer.save_or_locate(complex_magazine_39)

    complex_magazine_40 = Magazine()
    complex_magazine_40.cover_image = None
    complex_magazine_40.memo = ''
    complex_magazine_40.released = dateutil.parser.parse("2022-04-27")
    complex_magazine_40.site = 'https://dengekimaoh.jp/magazine/magazine-11802.html'
    complex_magazine_40.tag_line = None
    complex_magazine_40.title = '電撃マオウ 2022年6月号'
    complex_magazine_40 = importer.save_or_locate(complex_magazine_40)

    complex_magazine_41 = Magazine()
    complex_magazine_41.cover_image = None
    complex_magazine_41.memo = ''
    complex_magazine_41.released = dateutil.parser.parse("2022-05-26")
    complex_magazine_41.site = 'https://dengekimaoh.jp/magazine/magazine-11895.html'
    complex_magazine_41.tag_line = '表紙 付録 コミック発売'
    complex_magazine_41.title = '電撃マオウ 2022年7月号'
    complex_magazine_41 = importer.save_or_locate(complex_magazine_41)

    complex_magazine_42 = Magazine()
    complex_magazine_42.cover_image = None
    complex_magazine_42.memo = ''
    complex_magazine_42.released = dateutil.parser.parse("2022-06-27")
    complex_magazine_42.site = 'https://dengekimaoh.jp/magazine/magazine-12020.html'
    complex_magazine_42.tag_line = None
    complex_magazine_42.title = '電撃マオウ 2022年8月号'
    complex_magazine_42 = importer.save_or_locate(complex_magazine_42)

    complex_magazine_43 = Magazine()
    complex_magazine_43.cover_image = None
    complex_magazine_43.memo = ''
    complex_magazine_43.released = dateutil.parser.parse("2022-07-27")
    complex_magazine_43.site = 'https://dengekimaoh.jp/magazine/magazine-12139.html'
    complex_magazine_43.tag_line = None
    complex_magazine_43.title = '電撃マオウ 2022年9月号'
    complex_magazine_43 = importer.save_or_locate(complex_magazine_43)

    complex_magazine_44 = Magazine()
    complex_magazine_44.cover_image = None
    complex_magazine_44.memo = ''
    complex_magazine_44.released = dateutil.parser.parse("2022-08-26")
    complex_magazine_44.site = 'https://dengekimaoh.jp/magazine/magazine-12240.html'
    complex_magazine_44.tag_line = None
    complex_magazine_44.title = '電撃マオウ 2022年10月号'
    complex_magazine_44 = importer.save_or_locate(complex_magazine_44)

    complex_magazine_45 = Magazine()
    complex_magazine_45.cover_image = None
    complex_magazine_45.memo = ''
    complex_magazine_45.released = dateutil.parser.parse("2022-09-27")
    complex_magazine_45.site = 'https://dengekimaoh.jp/magazine/magazine-12387.html'
    complex_magazine_45.tag_line = None
    complex_magazine_45.title = '電撃マオウ 2022年11月号'
    complex_magazine_45 = importer.save_or_locate(complex_magazine_45)

    complex_magazine_46 = Magazine()
    complex_magazine_46.cover_image = None
    complex_magazine_46.memo = ''
    complex_magazine_46.released = dateutil.parser.parse("2022-10-27")
    complex_magazine_46.site = 'https://dengekimaoh.jp/magazine/magazine-12533.html'
    complex_magazine_46.tag_line = None
    complex_magazine_46.title = '電撃マオウ 2022年12月号'
    complex_magazine_46 = importer.save_or_locate(complex_magazine_46)

    complex_magazine_47 = Magazine()
    complex_magazine_47.cover_image = None
    complex_magazine_47.memo = ''
    complex_magazine_47.released = dateutil.parser.parse("2022-11-26")
    complex_magazine_47.site = 'https://dengekimaoh.jp/magazine/magazine-12616.html'
    complex_magazine_47.tag_line = None
    complex_magazine_47.title = '電撃マオウ 2023年1月号'
    complex_magazine_47 = importer.save_or_locate(complex_magazine_47)

    complex_magazine_48 = Magazine()
    complex_magazine_48.cover_image = None
    complex_magazine_48.memo = ''
    complex_magazine_48.released = dateutil.parser.parse("2022-12-26")
    complex_magazine_48.site = 'https://dengekimaoh.jp/magazine/magazine-12776.html'
    complex_magazine_48.tag_line = '表紙 コミック発売'
    complex_magazine_48.title = '電撃マオウ 2023年2月号'
    complex_magazine_48 = importer.save_or_locate(complex_magazine_48)

    complex_magazine_49 = Magazine()
    complex_magazine_49.cover_image = None
    complex_magazine_49.memo = ''
    complex_magazine_49.released = dateutil.parser.parse("2023-01-27")
    complex_magazine_49.site = 'https://dengekimaoh.jp/magazine/magazine-12846.html'
    complex_magazine_49.tag_line = None
    complex_magazine_49.title = '電撃マオウ 2023年3月号'
    complex_magazine_49 = importer.save_or_locate(complex_magazine_49)

    complex_magazine_50 = Magazine()
    complex_magazine_50.cover_image = None
    complex_magazine_50.memo = ''
    complex_magazine_50.released = dateutil.parser.parse("2023-02-27")
    complex_magazine_50.site = 'https://dengekimaoh.jp/magazine/magazine-13031.html'
    complex_magazine_50.tag_line = None
    complex_magazine_50.title = '電撃マオウ 2023年4月号'
    complex_magazine_50 = importer.save_or_locate(complex_magazine_50)

    complex_magazine_51 = Magazine()
    complex_magazine_51.cover_image = None
    complex_magazine_51.memo = ''
    complex_magazine_51.released = dateutil.parser.parse("2023-03-27")
    complex_magazine_51.site = 'https://dengekimaoh.jp/magazine/magazine-13229.html'
    complex_magazine_51.tag_line = None
    complex_magazine_51.title = '電撃マオウ 2023年5月号'
    complex_magazine_51 = importer.save_or_locate(complex_magazine_51)

    complex_magazine_52 = Magazine()
    complex_magazine_52.cover_image = None
    complex_magazine_52.memo = ''
    complex_magazine_52.released = dateutil.parser.parse("2023-04-26")
    complex_magazine_52.site = 'https://dengekimaoh.jp/magazine/magazine-14153.html'
    complex_magazine_52.tag_line = None
    complex_magazine_52.title = '電撃マオウ 2023年6月号'
    complex_magazine_52 = importer.save_or_locate(complex_magazine_52)

    complex_magazine_53 = Magazine()
    complex_magazine_53.cover_image = None
    complex_magazine_53.memo = "アニメ化企画進行中！\r\n『ざつ旅 -That's Journey-』が表紙＆巻頭で登場！\r\n付録 ざつ旅AR第2弾のマーカーになる、ざつ旅クリアファイル"
    complex_magazine_53.released = dateutil.parser.parse("2023-05-26")
    complex_magazine_53.site = 'https://dengekimaoh.jp/magazine/magazine-14303.html'
    complex_magazine_53.tag_line = '表紙 付録 アニメ化 コミック発売'
    complex_magazine_53.title = '電撃マオウ 2023年7月号'
    complex_magazine_53 = importer.save_or_locate(complex_magazine_53)

    complex_magazine_54 = Magazine()
    complex_magazine_54.cover_image = None
    complex_magazine_54.memo = ''
    complex_magazine_54.released = dateutil.parser.parse("2023-06-27")
    complex_magazine_54.site = 'https://dengekimaoh.jp/magazine/magazine-14517.html'
    complex_magazine_54.tag_line = None
    complex_magazine_54.title = '電撃マオウ 2023年8月号'
    complex_magazine_54 = importer.save_or_locate(complex_magazine_54)

    complex_magazine_55 = Magazine()
    complex_magazine_55.cover_image = None
    complex_magazine_55.memo = ''
    complex_magazine_55.released = dateutil.parser.parse("2023-07-27")
    complex_magazine_55.site = 'https://dengekimaoh.jp/magazine/magazine-14879.html'
    complex_magazine_55.tag_line = None
    complex_magazine_55.title = '電撃マオウ 2023年9月号'
    complex_magazine_55 = importer.save_or_locate(complex_magazine_55)

    complex_magazine_56 = Magazine()
    complex_magazine_56.cover_image = None
    complex_magazine_56.memo = ''
    complex_magazine_56.released = dateutil.parser.parse("2023-08-25")
    complex_magazine_56.site = 'https://dengekimaoh.jp/magazine/magazine-14986.html'
    complex_magazine_56.tag_line = None
    complex_magazine_56.title = '電撃マオウ 2023年10月号'
    complex_magazine_56 = importer.save_or_locate(complex_magazine_56)

    complex_magazine_57 = Magazine()
    complex_magazine_57.cover_image = None
    complex_magazine_57.memo = ''
    complex_magazine_57.released = dateutil.parser.parse("2023-09-27")
    complex_magazine_57.site = None
    complex_magazine_57.tag_line = None
    complex_magazine_57.title = '電撃マオウ 2023年11月号'
    complex_magazine_57 = importer.save_or_locate(complex_magazine_57)

    complex_magazine_58 = Magazine()
    complex_magazine_58.cover_image = None
    complex_magazine_58.memo = ''
    complex_magazine_58.released = dateutil.parser.parse("2023-10-27")
    complex_magazine_58.site = None
    complex_magazine_58.tag_line = None
    complex_magazine_58.title = '電撃マオウ 2023年12月号'
    complex_magazine_58 = importer.save_or_locate(complex_magazine_58)

    # Processing model: complex.models.Type_master

    from complex.models import Type_master

    complex_type_master_1 = Type_master()
    complex_type_master_1.key = '-'
    complex_type_master_1.name = 'default'
    complex_type_master_1.value = '***'
    complex_type_master_1 = importer.save_or_locate(complex_type_master_1)

    complex_type_master_2 = Type_master()
    complex_type_master_2.key = 'character'
    complex_type_master_2.name = 'character:主要登場人物'
    complex_type_master_2.value = '主要登場人物'
    complex_type_master_2 = importer.save_or_locate(complex_type_master_2)

    complex_type_master_3 = Type_master()
    complex_type_master_3.key = 'character'
    complex_type_master_3.name = 'character:主要登場人物の家族・関係者'
    complex_type_master_3.value = '主要登場人物の家族・関係者'
    complex_type_master_3 = importer.save_or_locate(complex_type_master_3)

    complex_type_master_4 = Type_master()
    complex_type_master_4.key = 'character'
    complex_type_master_4.name = 'character:編集部'
    complex_type_master_4.value = '編集部'
    complex_type_master_4 = importer.save_or_locate(complex_type_master_4)

    complex_type_master_5 = Type_master()
    complex_type_master_5.key = 'character'
    complex_type_master_5.name = 'character:旅先の出会い'
    complex_type_master_5.value = '旅先の出会い'
    complex_type_master_5 = importer.save_or_locate(complex_type_master_5)

    complex_type_master_6 = Type_master()
    complex_type_master_6.key = 'character'
    complex_type_master_6.name = 'character:モブ'
    complex_type_master_6.value = 'モブ'
    complex_type_master_6 = importer.save_or_locate(complex_type_master_6)

    complex_type_master_7 = Type_master()
    complex_type_master_7.key = 'character'
    complex_type_master_7.name = 'character:その他'
    complex_type_master_7.value = 'その他'
    complex_type_master_7 = importer.save_or_locate(complex_type_master_7)

    complex_type_master_8 = Type_master()
    complex_type_master_8.key = 'fragment'
    complex_type_master_8.name = 'fragment:告知絵'
    complex_type_master_8.value = '告知絵'
    complex_type_master_8 = importer.save_or_locate(complex_type_master_8)

    complex_type_master_9 = Type_master()
    complex_type_master_9.key = 'fragment'
    complex_type_master_9.name = 'fragment:店舗特典'
    complex_type_master_9.value = '店舗特典'
    complex_type_master_9 = importer.save_or_locate(complex_type_master_9)

    complex_type_master_10 = Type_master()
    complex_type_master_10.key = 'fragment'
    complex_type_master_10.name = 'fragment:表紙'
    complex_type_master_10.value = '表紙'
    complex_type_master_10 = importer.save_or_locate(complex_type_master_10)

    complex_type_master_11 = Type_master()
    complex_type_master_11.key = 'fragment'
    complex_type_master_11.name = 'fragment:別冊付録'
    complex_type_master_11.value = '別冊付録'
    complex_type_master_11 = importer.save_or_locate(complex_type_master_11)

    complex_type_master_12 = Type_master()
    complex_type_master_12.key = 'fragment'
    complex_type_master_12.name = 'fragment:付録(クリアファイル等)'
    complex_type_master_12.value = '付録(クリアファイル等)'
    complex_type_master_12 = importer.save_or_locate(complex_type_master_12)

    complex_type_master_13 = Type_master()
    complex_type_master_13.key = 'fragment'
    complex_type_master_13.name = 'fragment:広報ポスター'
    complex_type_master_13.value = '広報ポスター'
    complex_type_master_13 = importer.save_or_locate(complex_type_master_13)

    complex_type_master_14 = Type_master()
    complex_type_master_14.key = 'fragment'
    complex_type_master_14.name = 'fragment:ファン・アート'
    complex_type_master_14.value = 'ファン・アート'
    complex_type_master_14 = importer.save_or_locate(complex_type_master_14)

    complex_type_master_15 = Type_master()
    complex_type_master_15.key = 'fragment'
    complex_type_master_15.name = 'fragment:その他'
    complex_type_master_15.value = 'その他'
    complex_type_master_15 = importer.save_or_locate(complex_type_master_15)

    complex_type_master_16 = Type_master()
    complex_type_master_16.key = 'journey'
    complex_type_master_16.name = 'journey:本編'
    complex_type_master_16.value = '本編'
    complex_type_master_16 = importer.save_or_locate(complex_type_master_16)

    complex_type_master_17 = Type_master()
    complex_type_master_17.key = 'journey'
    complex_type_master_17.name = 'journey:番外旅'
    complex_type_master_17.value = '番外旅'
    complex_type_master_17 = importer.save_or_locate(complex_type_master_17)

    complex_type_master_18 = Type_master()
    complex_type_master_18.key = 'journey'
    complex_type_master_18.name = 'journey:その他'
    complex_type_master_18.value = 'その他'
    complex_type_master_18 = importer.save_or_locate(complex_type_master_18)

    complex_type_master_19 = Type_master()
    complex_type_master_19.key = 'person'
    complex_type_master_19.name = 'person:読者'
    complex_type_master_19.value = '読者'
    complex_type_master_19 = importer.save_or_locate(complex_type_master_19)

    complex_type_master_20 = Type_master()
    complex_type_master_20.key = 'person'
    complex_type_master_20.name = 'person:関係者'
    complex_type_master_20.value = '関係者'
    complex_type_master_20 = importer.save_or_locate(complex_type_master_20)

    complex_type_master_21 = Type_master()
    complex_type_master_21.key = 'person'
    complex_type_master_21.name = 'person:一般'
    complex_type_master_21.value = '一般'
    complex_type_master_21 = importer.save_or_locate(complex_type_master_21)

    complex_type_master_22 = Type_master()
    complex_type_master_22.key = 'person'
    complex_type_master_22.name = 'person:その他'
    complex_type_master_22.value = 'その他'
    complex_type_master_22 = importer.save_or_locate(complex_type_master_22)

    complex_type_master_23 = Type_master()
    complex_type_master_23.key = 'photo'
    complex_type_master_23.name = 'photo:Flickr'
    complex_type_master_23.value = 'Flickr'
    complex_type_master_23 = importer.save_or_locate(complex_type_master_23)

    complex_type_master_24 = Type_master()
    complex_type_master_24.key = 'photo'
    complex_type_master_24.name = 'photo:オフィシャル'
    complex_type_master_24.value = 'オフィシャル'
    complex_type_master_24 = importer.save_or_locate(complex_type_master_24)

    complex_type_master_25 = Type_master()
    complex_type_master_25.key = 'photo'
    complex_type_master_25.name = 'photo:素材'
    complex_type_master_25.value = '素材'
    complex_type_master_25 = importer.save_or_locate(complex_type_master_25)

    complex_type_master_26 = Type_master()
    complex_type_master_26.key = 'photo'
    complex_type_master_26.name = 'photo:取材・撮影'
    complex_type_master_26.value = '取材・撮影'
    complex_type_master_26 = importer.save_or_locate(complex_type_master_26)

    complex_type_master_27 = Type_master()
    complex_type_master_27.key = 'photo'
    complex_type_master_27.name = 'photo:聖地巡礼、舞台訪問、追走'
    complex_type_master_27.value = '聖地巡礼、舞台訪問、追走'
    complex_type_master_27 = importer.save_or_locate(complex_type_master_27)

    complex_type_master_28 = Type_master()
    complex_type_master_28.key = 'photo'
    complex_type_master_28.name = 'photo:一般'
    complex_type_master_28.value = '一般'
    complex_type_master_28 = importer.save_or_locate(complex_type_master_28)

    complex_type_master_29 = Type_master()
    complex_type_master_29.key = 'photo'
    complex_type_master_29.name = 'photo:無関係'
    complex_type_master_29.value = '無関係'
    complex_type_master_29 = importer.save_or_locate(complex_type_master_29)

    complex_type_master_30 = Type_master()
    complex_type_master_30.key = 'photo'
    complex_type_master_30.name = 'photo:その他'
    complex_type_master_30.value = 'その他'
    complex_type_master_30 = importer.save_or_locate(complex_type_master_30)

    complex_type_master_31 = Type_master()
    complex_type_master_31.key = 'route'
    complex_type_master_31.name = 'route:マップ取り込み'
    complex_type_master_31.value = 'マップ取り込み'
    complex_type_master_31 = importer.save_or_locate(complex_type_master_31)

    complex_type_master_32 = Type_master()
    complex_type_master_32.key = 'route'
    complex_type_master_32.name = 'route:調整済'
    complex_type_master_32.value = '調整済'
    complex_type_master_32 = importer.save_or_locate(complex_type_master_32)

    complex_type_master_33 = Type_master()
    complex_type_master_33.key = 'route'
    complex_type_master_33.name = 'route:システム'
    complex_type_master_33.value = 'システム'
    complex_type_master_33 = importer.save_or_locate(complex_type_master_33)

    complex_type_master_34 = Type_master()
    complex_type_master_34.key = 'route'
    complex_type_master_34.name = 'route:その他'
    complex_type_master_34.value = 'その他'
    complex_type_master_34 = importer.save_or_locate(complex_type_master_34)

    complex_type_master_35 = Type_master()
    complex_type_master_35.key = 'scene'
    complex_type_master_35.name = 'scene:ざつ旅AR'
    complex_type_master_35.value = 'ざつ旅AR'
    complex_type_master_35 = importer.save_or_locate(complex_type_master_35)

    complex_type_master_36 = Type_master()
    complex_type_master_36.key = 'scene'
    complex_type_master_36.name = 'scene:本編より'
    complex_type_master_36.value = '本編より'
    complex_type_master_36 = importer.save_or_locate(complex_type_master_36)

    complex_type_master_37 = Type_master()
    complex_type_master_37.key = 'scene'
    complex_type_master_37.name = 'scene:本編以外の原作'
    complex_type_master_37.value = '本編以外の原作'
    complex_type_master_37 = importer.save_or_locate(complex_type_master_37)

    complex_type_master_38 = Type_master()
    complex_type_master_38.key = 'scene'
    complex_type_master_38.name = 'scene:ファン・アート'
    complex_type_master_38.value = 'ファン・アート'
    complex_type_master_38 = importer.save_or_locate(complex_type_master_38)

    complex_type_master_39 = Type_master()
    complex_type_master_39.key = 'scene'
    complex_type_master_39.name = 'scene:その他'
    complex_type_master_39.value = 'その他'
    complex_type_master_39 = importer.save_or_locate(complex_type_master_39)

    complex_type_master_40 = Type_master()
    complex_type_master_40.key = 'story'
    complex_type_master_40.name = 'story:本編'
    complex_type_master_40.value = '本編'
    complex_type_master_40 = importer.save_or_locate(complex_type_master_40)

    complex_type_master_41 = Type_master()
    complex_type_master_41.key = 'story'
    complex_type_master_41.name = 'story:番外旅'
    complex_type_master_41.value = '番外旅'
    complex_type_master_41 = importer.save_or_locate(complex_type_master_41)

    complex_type_master_42 = Type_master()
    complex_type_master_42.key = 'story'
    complex_type_master_42.name = 'story:番外旅 おうちで料理'
    complex_type_master_42.value = '番外旅 おうちで料理'
    complex_type_master_42 = importer.save_or_locate(complex_type_master_42)

    complex_type_master_43 = Type_master()
    complex_type_master_43.key = 'story'
    complex_type_master_43.name = 'story:鈴ヶ森ちかの雑誌掲載作品等'
    complex_type_master_43.value = '鈴ヶ森ちかの雑誌掲載作品等'
    complex_type_master_43 = importer.save_or_locate(complex_type_master_43)

    complex_type_master_44 = Type_master()
    complex_type_master_44.key = 'story'
    complex_type_master_44.name = 'story:その他'
    complex_type_master_44.value = 'その他'
    complex_type_master_44 = importer.save_or_locate(complex_type_master_44)

    complex_type_master_45 = Type_master()
    complex_type_master_45.key = 'tweet'
    complex_type_master_45.name = 'tweet:鈴ヶ森さん'
    complex_type_master_45.value = '鈴ヶ森さん'
    complex_type_master_45 = importer.save_or_locate(complex_type_master_45)

    complex_type_master_46 = Type_master()
    complex_type_master_46.key = 'tweet'
    complex_type_master_46.name = 'tweet:石坂ケンタさん'
    complex_type_master_46.value = '石坂ケンタさん'
    complex_type_master_46 = importer.save_or_locate(complex_type_master_46)

    complex_type_master_47 = Type_master()
    complex_type_master_47.key = 'tweet'
    complex_type_master_47.name = 'tweet:アニメ制作関連'
    complex_type_master_47.value = 'アニメ制作関連'
    complex_type_master_47 = importer.save_or_locate(complex_type_master_47)

    complex_type_master_48 = Type_master()
    complex_type_master_48.key = 'tweet'
    complex_type_master_48.name = 'tweet:本作品公式コラボレーション'
    complex_type_master_48.value = '本作品公式コラボレーション'
    complex_type_master_48 = importer.save_or_locate(complex_type_master_48)

    complex_type_master_49 = Type_master()
    complex_type_master_49.key = 'tweet'
    complex_type_master_49.name = 'tweet:掲載店舗・施設、現地の観光協会、自治体広報、等'
    complex_type_master_49.value = '掲載店舗・施設、現地の観光協会、自治体広報、等'
    complex_type_master_49 = importer.save_or_locate(complex_type_master_49)

    complex_type_master_50 = Type_master()
    complex_type_master_50.key = 'tweet'
    complex_type_master_50.name = 'tweet:編集部、出版社広報、等'
    complex_type_master_50.value = '編集部、出版社広報、等'
    complex_type_master_50 = importer.save_or_locate(complex_type_master_50)

    complex_type_master_51 = Type_master()
    complex_type_master_51.key = 'tweet'
    complex_type_master_51.name = 'tweet:聖地巡礼、舞台訪問、追走'
    complex_type_master_51.value = '聖地巡礼、舞台訪問、追走'
    complex_type_master_51 = importer.save_or_locate(complex_type_master_51)

    complex_type_master_52 = Type_master()
    complex_type_master_52.key = 'tweet'
    complex_type_master_52.name = 'tweet:一般'
    complex_type_master_52.value = '一般'
    complex_type_master_52 = importer.save_or_locate(complex_type_master_52)

    complex_type_master_53 = Type_master()
    complex_type_master_53.key = 'tweet'
    complex_type_master_53.name = 'tweet:無関係'
    complex_type_master_53.value = '無関係'
    complex_type_master_53 = importer.save_or_locate(complex_type_master_53)

    complex_type_master_54 = Type_master()
    complex_type_master_54.key = 'tweet'
    complex_type_master_54.name = 'tweet:その他'
    complex_type_master_54.value = 'その他'
    complex_type_master_54 = importer.save_or_locate(complex_type_master_54)

    complex_type_master_55 = Type_master()
    complex_type_master_55.key = 'venue'
    complex_type_master_55.name = 'venue:都道府県'
    complex_type_master_55.value = '都道府県'
    complex_type_master_55 = importer.save_or_locate(complex_type_master_55)

    complex_type_master_56 = Type_master()
    complex_type_master_56.key = 'venue'
    complex_type_master_56.name = 'venue:市区町村、政令市の行政区'
    complex_type_master_56.value = '市区町村、政令市の行政区'
    complex_type_master_56 = importer.save_or_locate(complex_type_master_56)

    complex_type_master_57 = Type_master()
    complex_type_master_57.key = 'venue'
    complex_type_master_57.name = 'venue:大字、町名等の細かい行政界'
    complex_type_master_57.value = '大字、町名等の細かい行政界'
    complex_type_master_57 = importer.save_or_locate(complex_type_master_57)

    complex_type_master_58 = Type_master()
    complex_type_master_58.key = 'venue'
    complex_type_master_58.name = 'venue:著名観光地'
    complex_type_master_58.value = '著名観光地'
    complex_type_master_58 = importer.save_or_locate(complex_type_master_58)

    complex_type_master_59 = Type_master()
    complex_type_master_59.key = 'venue'
    complex_type_master_59.name = 'venue:ランドマーク'
    complex_type_master_59.value = 'ランドマーク'
    complex_type_master_59 = importer.save_or_locate(complex_type_master_59)

    complex_type_master_60 = Type_master()
    complex_type_master_60.key = 'venue'
    complex_type_master_60.name = 'venue:温泉、銭湯、足湯'
    complex_type_master_60.value = '温泉、銭湯、足湯'
    complex_type_master_60 = importer.save_or_locate(complex_type_master_60)

    complex_type_master_61 = Type_master()
    complex_type_master_61.key = 'venue'
    complex_type_master_61.name = 'venue:飲食店、宿泊施設、土産物店、農水産物直売等'
    complex_type_master_61.value = '飲食店、宿泊施設、土産物店、農水産物直売等'
    complex_type_master_61 = importer.save_or_locate(complex_type_master_61)

    complex_type_master_62 = Type_master()
    complex_type_master_62.key = 'venue'
    complex_type_master_62.name = 'venue:鉄道駅、バス停、道の駅等'
    complex_type_master_62.value = '鉄道駅、バス停、道の駅等'
    complex_type_master_62 = importer.save_or_locate(complex_type_master_62)

    complex_type_master_63 = Type_master()
    complex_type_master_63.key = 'venue'
    complex_type_master_63.name = 'venue:特徴的な建造物'
    complex_type_master_63.value = '特徴的な建造物'
    complex_type_master_63 = importer.save_or_locate(complex_type_master_63)

    complex_type_master_64 = Type_master()
    complex_type_master_64.key = 'venue'
    complex_type_master_64.name = 'venue:施設・設備'
    complex_type_master_64.value = '施設・設備'
    complex_type_master_64 = importer.save_or_locate(complex_type_master_64)

    complex_type_master_65 = Type_master()
    complex_type_master_65.key = 'venue'
    complex_type_master_65.name = 'venue:水準点、看板等'
    complex_type_master_65.value = '水準点、看板等'
    complex_type_master_65 = importer.save_or_locate(complex_type_master_65)

    complex_type_master_66 = Type_master()
    complex_type_master_66.key = 'venue'
    complex_type_master_66.name = 'venue:橋梁、トンネル、土木構造物'
    complex_type_master_66.value = '橋梁、トンネル、土木構造物'
    complex_type_master_66 = importer.save_or_locate(complex_type_master_66)

    complex_type_master_67 = Type_master()
    complex_type_master_67.key = 'venue'
    complex_type_master_67.name = 'venue:自然の景観'
    complex_type_master_67.value = '自然の景観'
    complex_type_master_67 = importer.save_or_locate(complex_type_master_67)

    complex_type_master_68 = Type_master()
    complex_type_master_68.key = 'venue'
    complex_type_master_68.name = 'venue:道路・街道'
    complex_type_master_68.value = '道路・街道'
    complex_type_master_68 = importer.save_or_locate(complex_type_master_68)

    complex_type_master_69 = Type_master()
    complex_type_master_69.key = 'venue'
    complex_type_master_69.name = 'venue:航空路'
    complex_type_master_69.value = '航空路'
    complex_type_master_69 = importer.save_or_locate(complex_type_master_69)

    complex_type_master_70 = Type_master()
    complex_type_master_70.key = 'venue'
    complex_type_master_70.name = 'venue:船舶航路'
    complex_type_master_70.value = '船舶航路'
    complex_type_master_70 = importer.save_or_locate(complex_type_master_70)

    complex_type_master_71 = Type_master()
    complex_type_master_71.key = 'venue'
    complex_type_master_71.name = 'venue:鉄道路線'
    complex_type_master_71.value = '鉄道路線'
    complex_type_master_71 = importer.save_or_locate(complex_type_master_71)

    complex_type_master_72 = Type_master()
    complex_type_master_72.key = 'venue'
    complex_type_master_72.name = 'venue:バス路線'
    complex_type_master_72.value = 'バス路線'
    complex_type_master_72 = importer.save_or_locate(complex_type_master_72)

    complex_type_master_73 = Type_master()
    complex_type_master_73.key = 'venue'
    complex_type_master_73.name = 'venue:その他'
    complex_type_master_73.value = 'その他'
    complex_type_master_73 = importer.save_or_locate(complex_type_master_73)

    # Processing model: complex.models.Journey

    from complex.models import Journey

    complex_journey_1 = Journey()
    complex_journey_1.key = 'TJ01'
    complex_journey_1.memo = None
    complex_journey_1.number = 1
    complex_journey_1.type_master = complex_type_master_16
    complex_journey_1 = importer.save_or_locate(complex_journey_1)

    complex_journey_2 = Journey()
    complex_journey_2.key = 'TJ02'
    complex_journey_2.memo = None
    complex_journey_2.number = 2
    complex_journey_2.type_master = complex_type_master_16
    complex_journey_2 = importer.save_or_locate(complex_journey_2)

    complex_journey_3 = Journey()
    complex_journey_3.key = 'TJ03'
    complex_journey_3.memo = None
    complex_journey_3.number = 3
    complex_journey_3.type_master = complex_type_master_16
    complex_journey_3 = importer.save_or_locate(complex_journey_3)

    complex_journey_4 = Journey()
    complex_journey_4.key = 'TJ04'
    complex_journey_4.memo = None
    complex_journey_4.number = 4
    complex_journey_4.type_master = complex_type_master_16
    complex_journey_4 = importer.save_or_locate(complex_journey_4)

    complex_journey_5 = Journey()
    complex_journey_5.key = 'TJ05'
    complex_journey_5.memo = None
    complex_journey_5.number = 5
    complex_journey_5.type_master = complex_type_master_16
    complex_journey_5 = importer.save_or_locate(complex_journey_5)

    complex_journey_6 = Journey()
    complex_journey_6.key = 'TJ06'
    complex_journey_6.memo = None
    complex_journey_6.number = 6
    complex_journey_6.type_master = complex_type_master_16
    complex_journey_6 = importer.save_or_locate(complex_journey_6)

    complex_journey_7 = Journey()
    complex_journey_7.key = 'TJ07'
    complex_journey_7.memo = None
    complex_journey_7.number = 7
    complex_journey_7.type_master = complex_type_master_16
    complex_journey_7 = importer.save_or_locate(complex_journey_7)

    complex_journey_8 = Journey()
    complex_journey_8.key = 'TJ08'
    complex_journey_8.memo = None
    complex_journey_8.number = 8
    complex_journey_8.type_master = complex_type_master_16
    complex_journey_8 = importer.save_or_locate(complex_journey_8)

    complex_journey_9 = Journey()
    complex_journey_9.key = 'TJ09'
    complex_journey_9.memo = None
    complex_journey_9.number = 9
    complex_journey_9.type_master = complex_type_master_16
    complex_journey_9 = importer.save_or_locate(complex_journey_9)

    complex_journey_10 = Journey()
    complex_journey_10.key = 'TJ10'
    complex_journey_10.memo = None
    complex_journey_10.number = 10
    complex_journey_10.type_master = complex_type_master_16
    complex_journey_10 = importer.save_or_locate(complex_journey_10)

    complex_journey_11 = Journey()
    complex_journey_11.key = 'TJ11'
    complex_journey_11.memo = None
    complex_journey_11.number = 11
    complex_journey_11.type_master = complex_type_master_16
    complex_journey_11 = importer.save_or_locate(complex_journey_11)

    complex_journey_12 = Journey()
    complex_journey_12.key = 'TJ12'
    complex_journey_12.memo = None
    complex_journey_12.number = 12
    complex_journey_12.type_master = complex_type_master_16
    complex_journey_12 = importer.save_or_locate(complex_journey_12)

    complex_journey_13 = Journey()
    complex_journey_13.key = 'TJ13'
    complex_journey_13.memo = None
    complex_journey_13.number = 13
    complex_journey_13.type_master = complex_type_master_16
    complex_journey_13 = importer.save_or_locate(complex_journey_13)

    complex_journey_14 = Journey()
    complex_journey_14.key = 'TJ14'
    complex_journey_14.memo = None
    complex_journey_14.number = 14
    complex_journey_14.type_master = complex_type_master_16
    complex_journey_14 = importer.save_or_locate(complex_journey_14)

    complex_journey_15 = Journey()
    complex_journey_15.key = 'TJ15'
    complex_journey_15.memo = None
    complex_journey_15.number = 15
    complex_journey_15.type_master = complex_type_master_16
    complex_journey_15 = importer.save_or_locate(complex_journey_15)

    complex_journey_16 = Journey()
    complex_journey_16.key = 'TJ16'
    complex_journey_16.memo = None
    complex_journey_16.number = 16
    complex_journey_16.type_master = complex_type_master_16
    complex_journey_16 = importer.save_or_locate(complex_journey_16)

    complex_journey_17 = Journey()
    complex_journey_17.key = 'TJ17'
    complex_journey_17.memo = None
    complex_journey_17.number = 17
    complex_journey_17.type_master = complex_type_master_16
    complex_journey_17 = importer.save_or_locate(complex_journey_17)

    complex_journey_18 = Journey()
    complex_journey_18.key = 'TJ18'
    complex_journey_18.memo = None
    complex_journey_18.number = 18
    complex_journey_18.type_master = complex_type_master_16
    complex_journey_18 = importer.save_or_locate(complex_journey_18)

    complex_journey_19 = Journey()
    complex_journey_19.key = 'TJ19'
    complex_journey_19.memo = None
    complex_journey_19.number = 19
    complex_journey_19.type_master = complex_type_master_16
    complex_journey_19 = importer.save_or_locate(complex_journey_19)

    complex_journey_20 = Journey()
    complex_journey_20.key = 'TJ20'
    complex_journey_20.memo = None
    complex_journey_20.number = 20
    complex_journey_20.type_master = complex_type_master_16
    complex_journey_20 = importer.save_or_locate(complex_journey_20)

    complex_journey_21 = Journey()
    complex_journey_21.key = 'TJ21'
    complex_journey_21.memo = None
    complex_journey_21.number = 21
    complex_journey_21.type_master = complex_type_master_16
    complex_journey_21 = importer.save_or_locate(complex_journey_21)

    complex_journey_22 = Journey()
    complex_journey_22.key = 'TJ22'
    complex_journey_22.memo = None
    complex_journey_22.number = 22
    complex_journey_22.type_master = complex_type_master_16
    complex_journey_22 = importer.save_or_locate(complex_journey_22)

    complex_journey_23 = Journey()
    complex_journey_23.key = 'TJ23'
    complex_journey_23.memo = None
    complex_journey_23.number = 23
    complex_journey_23.type_master = complex_type_master_16
    complex_journey_23 = importer.save_or_locate(complex_journey_23)

    complex_journey_24 = Journey()
    complex_journey_24.key = 'TJ24'
    complex_journey_24.memo = None
    complex_journey_24.number = 24
    complex_journey_24.type_master = complex_type_master_16
    complex_journey_24 = importer.save_or_locate(complex_journey_24)

    complex_journey_25 = Journey()
    complex_journey_25.key = 'TJ25'
    complex_journey_25.memo = None
    complex_journey_25.number = 25
    complex_journey_25.type_master = complex_type_master_16
    complex_journey_25 = importer.save_or_locate(complex_journey_25)

    complex_journey_26 = Journey()
    complex_journey_26.key = 'TJ26'
    complex_journey_26.memo = None
    complex_journey_26.number = 26
    complex_journey_26.type_master = complex_type_master_16
    complex_journey_26 = importer.save_or_locate(complex_journey_26)

    complex_journey_27 = Journey()
    complex_journey_27.key = 'TJ27'
    complex_journey_27.memo = None
    complex_journey_27.number = 27
    complex_journey_27.type_master = complex_type_master_16
    complex_journey_27 = importer.save_or_locate(complex_journey_27)

    complex_journey_28 = Journey()
    complex_journey_28.key = 'TJ28'
    complex_journey_28.memo = None
    complex_journey_28.number = 28
    complex_journey_28.type_master = complex_type_master_16
    complex_journey_28 = importer.save_or_locate(complex_journey_28)

    complex_journey_29 = Journey()
    complex_journey_29.key = 'TJ29'
    complex_journey_29.memo = ''
    complex_journey_29.number = 29
    complex_journey_29.type_master = complex_type_master_16
    complex_journey_29 = importer.save_or_locate(complex_journey_29)

    complex_journey_30 = Journey()
    complex_journey_30.key = 'TJ30'
    complex_journey_30.memo = ''
    complex_journey_30.number = 30
    complex_journey_30.type_master = complex_type_master_16
    complex_journey_30 = importer.save_or_locate(complex_journey_30)

    complex_journey_31 = Journey()
    complex_journey_31.key = 'TJ31'
    complex_journey_31.memo = ''
    complex_journey_31.number = 31
    complex_journey_31.type_master = complex_type_master_16
    complex_journey_31 = importer.save_or_locate(complex_journey_31)

    # Processing model: complex.models.Character

    from complex.models import Character

    complex_character_1 = Character()
    complex_character_1.description = '主人公、漫画家志望\r\n初出時、大学生。その後卒業→漫画家。\r\n高校生時代は、剣道部に所属し、漫画家のアシスタントも同時にこなす。\r\n健脚、料理、小型二輪免許所持\r\n両親が住む実家は、大田区内らしい。'
    complex_character_1.name = '鈴ヶ森ちか'
    complex_character_1.type_master = complex_type_master_2
    complex_character_1 = importer.save_or_locate(complex_character_1)

    complex_character_2 = Character()
    complex_character_2.description = 'ちかの相棒（同年代）、学生時代にバイト経験あり。\r\n小学校の先生を志望。卒業後に小学生の教員になる。'
    complex_character_2.name = '蓮沼暦'
    complex_character_2.type_master = complex_type_master_2
    complex_character_2 = importer.save_or_locate(complex_character_2)

    complex_character_3 = Character()
    complex_character_3.description = '高校生→その後学生、ちかの後輩\r\n剣道、歴女、石垣\r\n糀谷作品のファン'
    complex_character_3.name = '鵜木ゆい'
    complex_character_3.type_master = complex_type_master_2
    complex_character_3 = importer.save_or_locate(complex_character_3)

    complex_character_4 = Character()
    complex_character_4.description = '冬音の友人、酒豪、普通自動車免許\r\n少女漫画家、商業誌連載中、アシスタント募集中'
    complex_character_4.name = '天空橋りり'
    complex_character_4.type_master = complex_type_master_2
    complex_character_4 = importer.save_or_locate(complex_character_4)

    complex_character_5 = Character()
    complex_character_5.description = 'ちかの師匠、漫画家、商業誌連載中'
    complex_character_5.name = '糀谷冬音'
    complex_character_5.type_master = complex_type_master_2
    complex_character_5 = importer.save_or_locate(complex_character_5)

    complex_character_6 = Character()
    complex_character_6.description = 'ちかにとっては最初の担当編集。'
    complex_character_6.name = '吉本'
    complex_character_6.type_master = complex_type_master_4
    complex_character_6 = importer.save_or_locate(complex_character_6)

    complex_character_7 = Character()
    complex_character_7.description = 'ちかの現在の担当編集。打倒吉本を掲げる。'
    complex_character_7.name = '梅屋敷彩'
    complex_character_7.type_master = complex_type_master_4
    complex_character_7 = importer.save_or_locate(complex_character_7)

    # Processing model: complex.models.Person

    from complex.models import Person

    complex_person_1 = Person()
    complex_person_1.memo = ''
    complex_person_1.name = 'naoto'
    complex_person_1.type_master = complex_type_master_19
    complex_person_1.user =  importer.locate_object(CustomUser, "id", CustomUser, "id", 1, {'id': 1, 'password': 'pbkdf2_sha256$600000$aRKbpEZ1ZtG84OpfERTMzh$Ma9FcJrmMSpB94tUIvCZTPQqQkSMV0DalhHRizKp7wE=', 'last_login': dateutil.parser.parse("2023-09-21T02:07:46+00:00"), 'is_superuser': True, 'username': 'naoto', 'first_name': '', 'last_name': '', 'email': 'naoto@example.com', 'is_staff': True, 'is_active': True, 'date_joined': dateutil.parser.parse("2023-09-19T01:13:35+00:00")} ) 
    complex_person_1 = importer.save_or_locate(complex_person_1)

    # Processing model: complex.models.Scene

    from complex.models import Scene

    complex_scene_1 = Scene()
    complex_scene_1.memo = None
    complex_scene_1.page = 96
    complex_scene_1.type_master = complex_type_master_36
    complex_scene_1 = importer.save_or_locate(complex_scene_1)

    complex_scene_2 = Scene()
    complex_scene_2.memo = None
    complex_scene_2.page = 152
    complex_scene_2.type_master = complex_type_master_36
    complex_scene_2 = importer.save_or_locate(complex_scene_2)

    complex_scene_3 = Scene()
    complex_scene_3.memo = None
    complex_scene_3.page = 5
    complex_scene_3.type_master = complex_type_master_36
    complex_scene_3 = importer.save_or_locate(complex_scene_3)

    complex_scene_4 = Scene()
    complex_scene_4.memo = None
    complex_scene_4.page = 12
    complex_scene_4.type_master = complex_type_master_36
    complex_scene_4 = importer.save_or_locate(complex_scene_4)

    complex_scene_5 = Scene()
    complex_scene_5.memo = None
    complex_scene_5.page = 1
    complex_scene_5.type_master = complex_type_master_36
    complex_scene_5 = importer.save_or_locate(complex_scene_5)

    complex_scene_6 = Scene()
    complex_scene_6.memo = None
    complex_scene_6.page = 4
    complex_scene_6.type_master = complex_type_master_36
    complex_scene_6 = importer.save_or_locate(complex_scene_6)

    complex_scene_7 = Scene()
    complex_scene_7.memo = None
    complex_scene_7.page = 3
    complex_scene_7.type_master = complex_type_master_36
    complex_scene_7 = importer.save_or_locate(complex_scene_7)

    complex_scene_8 = Scene()
    complex_scene_8.memo = None
    complex_scene_8.page = 1
    complex_scene_8.type_master = complex_type_master_36
    complex_scene_8 = importer.save_or_locate(complex_scene_8)

    complex_scene_9 = Scene()
    complex_scene_9.memo = None
    complex_scene_9.page = 22
    complex_scene_9.type_master = complex_type_master_36
    complex_scene_9 = importer.save_or_locate(complex_scene_9)

    complex_scene_10 = Scene()
    complex_scene_10.memo = None
    complex_scene_10.page = 23
    complex_scene_10.type_master = complex_type_master_36
    complex_scene_10 = importer.save_or_locate(complex_scene_10)

    complex_scene_11 = Scene()
    complex_scene_11.memo = None
    complex_scene_11.page = 24
    complex_scene_11.type_master = complex_type_master_36
    complex_scene_11 = importer.save_or_locate(complex_scene_11)

    complex_scene_12 = Scene()
    complex_scene_12.memo = None
    complex_scene_12.page = 25
    complex_scene_12.type_master = complex_type_master_36
    complex_scene_12 = importer.save_or_locate(complex_scene_12)

    complex_scene_13 = Scene()
    complex_scene_13.memo = None
    complex_scene_13.page = 25
    complex_scene_13.type_master = complex_type_master_36
    complex_scene_13 = importer.save_or_locate(complex_scene_13)

    complex_scene_14 = Scene()
    complex_scene_14.memo = None
    complex_scene_14.page = 26
    complex_scene_14.type_master = complex_type_master_36
    complex_scene_14 = importer.save_or_locate(complex_scene_14)

    complex_scene_15 = Scene()
    complex_scene_15.memo = None
    complex_scene_15.page = 30
    complex_scene_15.type_master = complex_type_master_36
    complex_scene_15 = importer.save_or_locate(complex_scene_15)

    complex_scene_16 = Scene()
    complex_scene_16.memo = None
    complex_scene_16.page = 40
    complex_scene_16.type_master = complex_type_master_36
    complex_scene_16 = importer.save_or_locate(complex_scene_16)

    complex_scene_17 = Scene()
    complex_scene_17.memo = None
    complex_scene_17.page = 40
    complex_scene_17.type_master = complex_type_master_36
    complex_scene_17 = importer.save_or_locate(complex_scene_17)

    complex_scene_18 = Scene()
    complex_scene_18.memo = None
    complex_scene_18.page = 41
    complex_scene_18.type_master = complex_type_master_36
    complex_scene_18 = importer.save_or_locate(complex_scene_18)

    complex_scene_19 = Scene()
    complex_scene_19.memo = None
    complex_scene_19.page = 45
    complex_scene_19.type_master = complex_type_master_36
    complex_scene_19 = importer.save_or_locate(complex_scene_19)

    complex_scene_20 = Scene()
    complex_scene_20.memo = None
    complex_scene_20.page = 51
    complex_scene_20.type_master = complex_type_master_36
    complex_scene_20 = importer.save_or_locate(complex_scene_20)

    complex_scene_21 = Scene()
    complex_scene_21.memo = None
    complex_scene_21.page = 61
    complex_scene_21.type_master = complex_type_master_36
    complex_scene_21 = importer.save_or_locate(complex_scene_21)

    complex_scene_22 = Scene()
    complex_scene_22.memo = None
    complex_scene_22.page = 62
    complex_scene_22.type_master = complex_type_master_36
    complex_scene_22 = importer.save_or_locate(complex_scene_22)

    complex_scene_23 = Scene()
    complex_scene_23.memo = None
    complex_scene_23.page = 63
    complex_scene_23.type_master = complex_type_master_36
    complex_scene_23 = importer.save_or_locate(complex_scene_23)

    complex_scene_24 = Scene()
    complex_scene_24.memo = None
    complex_scene_24.page = 64
    complex_scene_24.type_master = complex_type_master_36
    complex_scene_24 = importer.save_or_locate(complex_scene_24)

    complex_scene_25 = Scene()
    complex_scene_25.memo = None
    complex_scene_25.page = 64
    complex_scene_25.type_master = complex_type_master_36
    complex_scene_25 = importer.save_or_locate(complex_scene_25)

    complex_scene_26 = Scene()
    complex_scene_26.memo = None
    complex_scene_26.page = 65
    complex_scene_26.type_master = complex_type_master_36
    complex_scene_26 = importer.save_or_locate(complex_scene_26)

    complex_scene_27 = Scene()
    complex_scene_27.memo = None
    complex_scene_27.page = 69
    complex_scene_27.type_master = complex_type_master_36
    complex_scene_27 = importer.save_or_locate(complex_scene_27)

    complex_scene_28 = Scene()
    complex_scene_28.memo = None
    complex_scene_28.page = 69
    complex_scene_28.type_master = complex_type_master_36
    complex_scene_28 = importer.save_or_locate(complex_scene_28)

    complex_scene_29 = Scene()
    complex_scene_29.memo = None
    complex_scene_29.page = 76
    complex_scene_29.type_master = complex_type_master_36
    complex_scene_29 = importer.save_or_locate(complex_scene_29)

    complex_scene_30 = Scene()
    complex_scene_30.memo = None
    complex_scene_30.page = 78
    complex_scene_30.type_master = complex_type_master_36
    complex_scene_30 = importer.save_or_locate(complex_scene_30)

    complex_scene_31 = Scene()
    complex_scene_31.memo = None
    complex_scene_31.page = 79
    complex_scene_31.type_master = complex_type_master_36
    complex_scene_31 = importer.save_or_locate(complex_scene_31)

    complex_scene_32 = Scene()
    complex_scene_32.memo = None
    complex_scene_32.page = 81
    complex_scene_32.type_master = complex_type_master_36
    complex_scene_32 = importer.save_or_locate(complex_scene_32)

    complex_scene_33 = Scene()
    complex_scene_33.memo = None
    complex_scene_33.page = 85
    complex_scene_33.type_master = complex_type_master_36
    complex_scene_33 = importer.save_or_locate(complex_scene_33)

    complex_scene_34 = Scene()
    complex_scene_34.memo = None
    complex_scene_34.page = 87
    complex_scene_34.type_master = complex_type_master_36
    complex_scene_34 = importer.save_or_locate(complex_scene_34)

    complex_scene_35 = Scene()
    complex_scene_35.memo = None
    complex_scene_35.page = 92
    complex_scene_35.type_master = complex_type_master_36
    complex_scene_35 = importer.save_or_locate(complex_scene_35)

    complex_scene_36 = Scene()
    complex_scene_36.memo = None
    complex_scene_36.page = 96
    complex_scene_36.type_master = complex_type_master_36
    complex_scene_36 = importer.save_or_locate(complex_scene_36)

    complex_scene_37 = Scene()
    complex_scene_37.memo = None
    complex_scene_37.page = 100
    complex_scene_37.type_master = complex_type_master_36
    complex_scene_37 = importer.save_or_locate(complex_scene_37)

    complex_scene_38 = Scene()
    complex_scene_38.memo = None
    complex_scene_38.page = 103
    complex_scene_38.type_master = complex_type_master_36
    complex_scene_38 = importer.save_or_locate(complex_scene_38)

    complex_scene_39 = Scene()
    complex_scene_39.memo = None
    complex_scene_39.page = 108
    complex_scene_39.type_master = complex_type_master_36
    complex_scene_39 = importer.save_or_locate(complex_scene_39)

    complex_scene_40 = Scene()
    complex_scene_40.memo = None
    complex_scene_40.page = 110
    complex_scene_40.type_master = complex_type_master_36
    complex_scene_40 = importer.save_or_locate(complex_scene_40)

    complex_scene_41 = Scene()
    complex_scene_41.memo = None
    complex_scene_41.page = 111
    complex_scene_41.type_master = complex_type_master_36
    complex_scene_41 = importer.save_or_locate(complex_scene_41)

    complex_scene_42 = Scene()
    complex_scene_42.memo = None
    complex_scene_42.page = 112
    complex_scene_42.type_master = complex_type_master_36
    complex_scene_42 = importer.save_or_locate(complex_scene_42)

    complex_scene_43 = Scene()
    complex_scene_43.memo = None
    complex_scene_43.page = 116
    complex_scene_43.type_master = complex_type_master_36
    complex_scene_43 = importer.save_or_locate(complex_scene_43)

    complex_scene_44 = Scene()
    complex_scene_44.memo = None
    complex_scene_44.page = 117
    complex_scene_44.type_master = complex_type_master_36
    complex_scene_44 = importer.save_or_locate(complex_scene_44)

    complex_scene_45 = Scene()
    complex_scene_45.memo = None
    complex_scene_45.page = 119
    complex_scene_45.type_master = complex_type_master_36
    complex_scene_45 = importer.save_or_locate(complex_scene_45)

    complex_scene_46 = Scene()
    complex_scene_46.memo = None
    complex_scene_46.page = 126
    complex_scene_46.type_master = complex_type_master_36
    complex_scene_46 = importer.save_or_locate(complex_scene_46)

    complex_scene_47 = Scene()
    complex_scene_47.memo = None
    complex_scene_47.page = 130
    complex_scene_47.type_master = complex_type_master_36
    complex_scene_47 = importer.save_or_locate(complex_scene_47)

    complex_scene_48 = Scene()
    complex_scene_48.memo = None
    complex_scene_48.page = 131
    complex_scene_48.type_master = complex_type_master_36
    complex_scene_48 = importer.save_or_locate(complex_scene_48)

    complex_scene_49 = Scene()
    complex_scene_49.memo = None
    complex_scene_49.page = 132
    complex_scene_49.type_master = complex_type_master_36
    complex_scene_49 = importer.save_or_locate(complex_scene_49)

    complex_scene_50 = Scene()
    complex_scene_50.memo = None
    complex_scene_50.page = 134
    complex_scene_50.type_master = complex_type_master_36
    complex_scene_50 = importer.save_or_locate(complex_scene_50)

    complex_scene_51 = Scene()
    complex_scene_51.memo = None
    complex_scene_51.page = 134
    complex_scene_51.type_master = complex_type_master_36
    complex_scene_51 = importer.save_or_locate(complex_scene_51)

    complex_scene_52 = Scene()
    complex_scene_52.memo = None
    complex_scene_52.page = 134
    complex_scene_52.type_master = complex_type_master_36
    complex_scene_52 = importer.save_or_locate(complex_scene_52)

    complex_scene_53 = Scene()
    complex_scene_53.memo = None
    complex_scene_53.page = 142
    complex_scene_53.type_master = complex_type_master_36
    complex_scene_53 = importer.save_or_locate(complex_scene_53)

    complex_scene_54 = Scene()
    complex_scene_54.memo = None
    complex_scene_54.page = 143
    complex_scene_54.type_master = complex_type_master_36
    complex_scene_54 = importer.save_or_locate(complex_scene_54)

    complex_scene_55 = Scene()
    complex_scene_55.memo = None
    complex_scene_55.page = 148
    complex_scene_55.type_master = complex_type_master_36
    complex_scene_55 = importer.save_or_locate(complex_scene_55)

    complex_scene_56 = Scene()
    complex_scene_56.memo = None
    complex_scene_56.page = 150
    complex_scene_56.type_master = complex_type_master_36
    complex_scene_56 = importer.save_or_locate(complex_scene_56)

    complex_scene_57 = Scene()
    complex_scene_57.memo = None
    complex_scene_57.page = 157
    complex_scene_57.type_master = complex_type_master_36
    complex_scene_57 = importer.save_or_locate(complex_scene_57)

    complex_scene_58 = Scene()
    complex_scene_58.memo = None
    complex_scene_58.page = 3
    complex_scene_58.type_master = complex_type_master_36
    complex_scene_58 = importer.save_or_locate(complex_scene_58)

    complex_scene_59 = Scene()
    complex_scene_59.memo = None
    complex_scene_59.page = 6
    complex_scene_59.type_master = complex_type_master_36
    complex_scene_59 = importer.save_or_locate(complex_scene_59)

    complex_scene_60 = Scene()
    complex_scene_60.memo = None
    complex_scene_60.page = 16
    complex_scene_60.type_master = complex_type_master_36
    complex_scene_60 = importer.save_or_locate(complex_scene_60)

    complex_scene_61 = Scene()
    complex_scene_61.memo = None
    complex_scene_61.page = 17
    complex_scene_61.type_master = complex_type_master_36
    complex_scene_61 = importer.save_or_locate(complex_scene_61)

    complex_scene_62 = Scene()
    complex_scene_62.memo = None
    complex_scene_62.page = 17
    complex_scene_62.type_master = complex_type_master_36
    complex_scene_62 = importer.save_or_locate(complex_scene_62)

    complex_scene_63 = Scene()
    complex_scene_63.memo = None
    complex_scene_63.page = 18
    complex_scene_63.type_master = complex_type_master_36
    complex_scene_63 = importer.save_or_locate(complex_scene_63)

    complex_scene_64 = Scene()
    complex_scene_64.memo = None
    complex_scene_64.page = 21
    complex_scene_64.type_master = complex_type_master_36
    complex_scene_64 = importer.save_or_locate(complex_scene_64)

    complex_scene_65 = Scene()
    complex_scene_65.memo = None
    complex_scene_65.page = 22
    complex_scene_65.type_master = complex_type_master_36
    complex_scene_65 = importer.save_or_locate(complex_scene_65)

    complex_scene_66 = Scene()
    complex_scene_66.memo = None
    complex_scene_66.page = 22
    complex_scene_66.type_master = complex_type_master_36
    complex_scene_66 = importer.save_or_locate(complex_scene_66)

    complex_scene_67 = Scene()
    complex_scene_67.memo = None
    complex_scene_67.page = 31
    complex_scene_67.type_master = complex_type_master_36
    complex_scene_67 = importer.save_or_locate(complex_scene_67)

    complex_scene_68 = Scene()
    complex_scene_68.memo = None
    complex_scene_68.page = 32
    complex_scene_68.type_master = complex_type_master_36
    complex_scene_68 = importer.save_or_locate(complex_scene_68)

    complex_scene_69 = Scene()
    complex_scene_69.memo = None
    complex_scene_69.page = 35
    complex_scene_69.type_master = complex_type_master_36
    complex_scene_69 = importer.save_or_locate(complex_scene_69)

    complex_scene_70 = Scene()
    complex_scene_70.memo = None
    complex_scene_70.page = 36
    complex_scene_70.type_master = complex_type_master_36
    complex_scene_70 = importer.save_or_locate(complex_scene_70)

    complex_scene_71 = Scene()
    complex_scene_71.memo = None
    complex_scene_71.page = 37
    complex_scene_71.type_master = complex_type_master_36
    complex_scene_71 = importer.save_or_locate(complex_scene_71)

    complex_scene_72 = Scene()
    complex_scene_72.memo = None
    complex_scene_72.page = 39
    complex_scene_72.type_master = complex_type_master_36
    complex_scene_72 = importer.save_or_locate(complex_scene_72)

    complex_scene_73 = Scene()
    complex_scene_73.memo = None
    complex_scene_73.page = 44
    complex_scene_73.type_master = complex_type_master_36
    complex_scene_73 = importer.save_or_locate(complex_scene_73)

    complex_scene_74 = Scene()
    complex_scene_74.memo = None
    complex_scene_74.page = 47
    complex_scene_74.type_master = complex_type_master_36
    complex_scene_74 = importer.save_or_locate(complex_scene_74)

    complex_scene_75 = Scene()
    complex_scene_75.memo = None
    complex_scene_75.page = 49
    complex_scene_75.type_master = complex_type_master_36
    complex_scene_75 = importer.save_or_locate(complex_scene_75)

    complex_scene_76 = Scene()
    complex_scene_76.memo = None
    complex_scene_76.page = 50
    complex_scene_76.type_master = complex_type_master_36
    complex_scene_76 = importer.save_or_locate(complex_scene_76)

    complex_scene_77 = Scene()
    complex_scene_77.memo = None
    complex_scene_77.page = 52
    complex_scene_77.type_master = complex_type_master_36
    complex_scene_77 = importer.save_or_locate(complex_scene_77)

    complex_scene_78 = Scene()
    complex_scene_78.memo = None
    complex_scene_78.page = 57
    complex_scene_78.type_master = complex_type_master_36
    complex_scene_78 = importer.save_or_locate(complex_scene_78)

    complex_scene_79 = Scene()
    complex_scene_79.memo = None
    complex_scene_79.page = 58
    complex_scene_79.type_master = complex_type_master_36
    complex_scene_79 = importer.save_or_locate(complex_scene_79)

    complex_scene_80 = Scene()
    complex_scene_80.memo = None
    complex_scene_80.page = 58
    complex_scene_80.type_master = complex_type_master_36
    complex_scene_80 = importer.save_or_locate(complex_scene_80)

    complex_scene_81 = Scene()
    complex_scene_81.memo = None
    complex_scene_81.page = 59
    complex_scene_81.type_master = complex_type_master_36
    complex_scene_81 = importer.save_or_locate(complex_scene_81)

    complex_scene_82 = Scene()
    complex_scene_82.memo = None
    complex_scene_82.page = 60
    complex_scene_82.type_master = complex_type_master_36
    complex_scene_82 = importer.save_or_locate(complex_scene_82)

    complex_scene_83 = Scene()
    complex_scene_83.memo = None
    complex_scene_83.page = 62
    complex_scene_83.type_master = complex_type_master_36
    complex_scene_83 = importer.save_or_locate(complex_scene_83)

    complex_scene_84 = Scene()
    complex_scene_84.memo = None
    complex_scene_84.page = 73
    complex_scene_84.type_master = complex_type_master_36
    complex_scene_84 = importer.save_or_locate(complex_scene_84)

    complex_scene_85 = Scene()
    complex_scene_85.memo = None
    complex_scene_85.page = 75
    complex_scene_85.type_master = complex_type_master_36
    complex_scene_85 = importer.save_or_locate(complex_scene_85)

    complex_scene_86 = Scene()
    complex_scene_86.memo = None
    complex_scene_86.page = 78
    complex_scene_86.type_master = complex_type_master_36
    complex_scene_86 = importer.save_or_locate(complex_scene_86)

    complex_scene_87 = Scene()
    complex_scene_87.memo = None
    complex_scene_87.page = 80
    complex_scene_87.type_master = complex_type_master_36
    complex_scene_87 = importer.save_or_locate(complex_scene_87)

    complex_scene_88 = Scene()
    complex_scene_88.memo = None
    complex_scene_88.page = 82
    complex_scene_88.type_master = complex_type_master_36
    complex_scene_88 = importer.save_or_locate(complex_scene_88)

    complex_scene_89 = Scene()
    complex_scene_89.memo = None
    complex_scene_89.page = 93
    complex_scene_89.type_master = complex_type_master_36
    complex_scene_89 = importer.save_or_locate(complex_scene_89)

    complex_scene_90 = Scene()
    complex_scene_90.memo = None
    complex_scene_90.page = 99
    complex_scene_90.type_master = complex_type_master_36
    complex_scene_90 = importer.save_or_locate(complex_scene_90)

    complex_scene_91 = Scene()
    complex_scene_91.memo = None
    complex_scene_91.page = 100
    complex_scene_91.type_master = complex_type_master_36
    complex_scene_91 = importer.save_or_locate(complex_scene_91)

    complex_scene_92 = Scene()
    complex_scene_92.memo = None
    complex_scene_92.page = 101
    complex_scene_92.type_master = complex_type_master_36
    complex_scene_92 = importer.save_or_locate(complex_scene_92)

    complex_scene_93 = Scene()
    complex_scene_93.memo = None
    complex_scene_93.page = 102
    complex_scene_93.type_master = complex_type_master_36
    complex_scene_93 = importer.save_or_locate(complex_scene_93)

    complex_scene_94 = Scene()
    complex_scene_94.memo = None
    complex_scene_94.page = 106
    complex_scene_94.type_master = complex_type_master_36
    complex_scene_94 = importer.save_or_locate(complex_scene_94)

    complex_scene_95 = Scene()
    complex_scene_95.memo = None
    complex_scene_95.page = 108
    complex_scene_95.type_master = complex_type_master_36
    complex_scene_95 = importer.save_or_locate(complex_scene_95)

    complex_scene_96 = Scene()
    complex_scene_96.memo = None
    complex_scene_96.page = 109
    complex_scene_96.type_master = complex_type_master_36
    complex_scene_96 = importer.save_or_locate(complex_scene_96)

    complex_scene_97 = Scene()
    complex_scene_97.memo = None
    complex_scene_97.page = 111
    complex_scene_97.type_master = complex_type_master_36
    complex_scene_97 = importer.save_or_locate(complex_scene_97)

    complex_scene_98 = Scene()
    complex_scene_98.memo = None
    complex_scene_98.page = 111
    complex_scene_98.type_master = complex_type_master_36
    complex_scene_98 = importer.save_or_locate(complex_scene_98)

    complex_scene_99 = Scene()
    complex_scene_99.memo = None
    complex_scene_99.page = 111
    complex_scene_99.type_master = complex_type_master_36
    complex_scene_99 = importer.save_or_locate(complex_scene_99)

    complex_scene_100 = Scene()
    complex_scene_100.memo = None
    complex_scene_100.page = 121
    complex_scene_100.type_master = complex_type_master_36
    complex_scene_100 = importer.save_or_locate(complex_scene_100)

    complex_scene_101 = Scene()
    complex_scene_101.memo = None
    complex_scene_101.page = 121
    complex_scene_101.type_master = complex_type_master_36
    complex_scene_101 = importer.save_or_locate(complex_scene_101)

    complex_scene_102 = Scene()
    complex_scene_102.memo = None
    complex_scene_102.page = 124
    complex_scene_102.type_master = complex_type_master_36
    complex_scene_102 = importer.save_or_locate(complex_scene_102)

    complex_scene_103 = Scene()
    complex_scene_103.memo = None
    complex_scene_103.page = 127
    complex_scene_103.type_master = complex_type_master_36
    complex_scene_103 = importer.save_or_locate(complex_scene_103)

    complex_scene_104 = Scene()
    complex_scene_104.memo = None
    complex_scene_104.page = 132
    complex_scene_104.type_master = complex_type_master_36
    complex_scene_104 = importer.save_or_locate(complex_scene_104)

    complex_scene_105 = Scene()
    complex_scene_105.memo = None
    complex_scene_105.page = 141
    complex_scene_105.type_master = complex_type_master_36
    complex_scene_105 = importer.save_or_locate(complex_scene_105)

    complex_scene_106 = Scene()
    complex_scene_106.memo = None
    complex_scene_106.page = 145
    complex_scene_106.type_master = complex_type_master_36
    complex_scene_106 = importer.save_or_locate(complex_scene_106)

    complex_scene_107 = Scene()
    complex_scene_107.memo = None
    complex_scene_107.page = 146
    complex_scene_107.type_master = complex_type_master_36
    complex_scene_107 = importer.save_or_locate(complex_scene_107)

    complex_scene_108 = Scene()
    complex_scene_108.memo = None
    complex_scene_108.page = 147
    complex_scene_108.type_master = complex_type_master_36
    complex_scene_108 = importer.save_or_locate(complex_scene_108)

    complex_scene_109 = Scene()
    complex_scene_109.memo = None
    complex_scene_109.page = 148
    complex_scene_109.type_master = complex_type_master_36
    complex_scene_109 = importer.save_or_locate(complex_scene_109)

    complex_scene_110 = Scene()
    complex_scene_110.memo = None
    complex_scene_110.page = 151
    complex_scene_110.type_master = complex_type_master_36
    complex_scene_110 = importer.save_or_locate(complex_scene_110)

    complex_scene_111 = Scene()
    complex_scene_111.memo = None
    complex_scene_111.page = 5
    complex_scene_111.type_master = complex_type_master_36
    complex_scene_111 = importer.save_or_locate(complex_scene_111)

    complex_scene_112 = Scene()
    complex_scene_112.memo = None
    complex_scene_112.page = 8
    complex_scene_112.type_master = complex_type_master_36
    complex_scene_112 = importer.save_or_locate(complex_scene_112)

    complex_scene_113 = Scene()
    complex_scene_113.memo = None
    complex_scene_113.page = 10
    complex_scene_113.type_master = complex_type_master_36
    complex_scene_113 = importer.save_or_locate(complex_scene_113)

    complex_scene_114 = Scene()
    complex_scene_114.memo = None
    complex_scene_114.page = 11
    complex_scene_114.type_master = complex_type_master_36
    complex_scene_114 = importer.save_or_locate(complex_scene_114)

    complex_scene_115 = Scene()
    complex_scene_115.memo = None
    complex_scene_115.page = 12
    complex_scene_115.type_master = complex_type_master_36
    complex_scene_115 = importer.save_or_locate(complex_scene_115)

    complex_scene_116 = Scene()
    complex_scene_116.memo = None
    complex_scene_116.page = 14
    complex_scene_116.type_master = complex_type_master_36
    complex_scene_116 = importer.save_or_locate(complex_scene_116)

    complex_scene_117 = Scene()
    complex_scene_117.memo = None
    complex_scene_117.page = 15
    complex_scene_117.type_master = complex_type_master_36
    complex_scene_117 = importer.save_or_locate(complex_scene_117)

    complex_scene_118 = Scene()
    complex_scene_118.memo = None
    complex_scene_118.page = 15
    complex_scene_118.type_master = complex_type_master_36
    complex_scene_118 = importer.save_or_locate(complex_scene_118)

    complex_scene_119 = Scene()
    complex_scene_119.memo = None
    complex_scene_119.page = 19
    complex_scene_119.type_master = complex_type_master_36
    complex_scene_119 = importer.save_or_locate(complex_scene_119)

    complex_scene_120 = Scene()
    complex_scene_120.memo = None
    complex_scene_120.page = 19
    complex_scene_120.type_master = complex_type_master_36
    complex_scene_120 = importer.save_or_locate(complex_scene_120)

    complex_scene_121 = Scene()
    complex_scene_121.memo = None
    complex_scene_121.page = 21
    complex_scene_121.type_master = complex_type_master_36
    complex_scene_121 = importer.save_or_locate(complex_scene_121)

    complex_scene_122 = Scene()
    complex_scene_122.memo = None
    complex_scene_122.page = 25
    complex_scene_122.type_master = complex_type_master_36
    complex_scene_122 = importer.save_or_locate(complex_scene_122)

    complex_scene_123 = Scene()
    complex_scene_123.memo = None
    complex_scene_123.page = 29
    complex_scene_123.type_master = complex_type_master_36
    complex_scene_123 = importer.save_or_locate(complex_scene_123)

    complex_scene_124 = Scene()
    complex_scene_124.memo = None
    complex_scene_124.page = 31
    complex_scene_124.type_master = complex_type_master_36
    complex_scene_124 = importer.save_or_locate(complex_scene_124)

    complex_scene_125 = Scene()
    complex_scene_125.memo = None
    complex_scene_125.page = 32
    complex_scene_125.type_master = complex_type_master_36
    complex_scene_125 = importer.save_or_locate(complex_scene_125)

    complex_scene_126 = Scene()
    complex_scene_126.memo = None
    complex_scene_126.page = 34
    complex_scene_126.type_master = complex_type_master_36
    complex_scene_126 = importer.save_or_locate(complex_scene_126)

    complex_scene_127 = Scene()
    complex_scene_127.memo = None
    complex_scene_127.page = 38
    complex_scene_127.type_master = complex_type_master_36
    complex_scene_127 = importer.save_or_locate(complex_scene_127)

    complex_scene_128 = Scene()
    complex_scene_128.memo = None
    complex_scene_128.page = 47
    complex_scene_128.type_master = complex_type_master_36
    complex_scene_128 = importer.save_or_locate(complex_scene_128)

    complex_scene_129 = Scene()
    complex_scene_129.memo = None
    complex_scene_129.page = 49
    complex_scene_129.type_master = complex_type_master_36
    complex_scene_129 = importer.save_or_locate(complex_scene_129)

    complex_scene_130 = Scene()
    complex_scene_130.memo = None
    complex_scene_130.page = 49
    complex_scene_130.type_master = complex_type_master_36
    complex_scene_130 = importer.save_or_locate(complex_scene_130)

    complex_scene_131 = Scene()
    complex_scene_131.memo = None
    complex_scene_131.page = 51
    complex_scene_131.type_master = complex_type_master_36
    complex_scene_131 = importer.save_or_locate(complex_scene_131)

    complex_scene_132 = Scene()
    complex_scene_132.memo = None
    complex_scene_132.page = 52
    complex_scene_132.type_master = complex_type_master_36
    complex_scene_132 = importer.save_or_locate(complex_scene_132)

    complex_scene_133 = Scene()
    complex_scene_133.memo = None
    complex_scene_133.page = 55
    complex_scene_133.type_master = complex_type_master_36
    complex_scene_133 = importer.save_or_locate(complex_scene_133)

    complex_scene_134 = Scene()
    complex_scene_134.memo = None
    complex_scene_134.page = 57
    complex_scene_134.type_master = complex_type_master_36
    complex_scene_134 = importer.save_or_locate(complex_scene_134)

    complex_scene_135 = Scene()
    complex_scene_135.memo = None
    complex_scene_135.page = 60
    complex_scene_135.type_master = complex_type_master_36
    complex_scene_135 = importer.save_or_locate(complex_scene_135)

    complex_scene_136 = Scene()
    complex_scene_136.memo = None
    complex_scene_136.page = 61
    complex_scene_136.type_master = complex_type_master_36
    complex_scene_136 = importer.save_or_locate(complex_scene_136)

    complex_scene_137 = Scene()
    complex_scene_137.memo = None
    complex_scene_137.page = 62
    complex_scene_137.type_master = complex_type_master_36
    complex_scene_137 = importer.save_or_locate(complex_scene_137)

    complex_scene_138 = Scene()
    complex_scene_138.memo = None
    complex_scene_138.page = 64
    complex_scene_138.type_master = complex_type_master_36
    complex_scene_138 = importer.save_or_locate(complex_scene_138)

    complex_scene_139 = Scene()
    complex_scene_139.memo = None
    complex_scene_139.page = 67
    complex_scene_139.type_master = complex_type_master_36
    complex_scene_139 = importer.save_or_locate(complex_scene_139)

    complex_scene_140 = Scene()
    complex_scene_140.memo = None
    complex_scene_140.page = 69
    complex_scene_140.type_master = complex_type_master_36
    complex_scene_140 = importer.save_or_locate(complex_scene_140)

    complex_scene_141 = Scene()
    complex_scene_141.memo = None
    complex_scene_141.page = 71
    complex_scene_141.type_master = complex_type_master_36
    complex_scene_141 = importer.save_or_locate(complex_scene_141)

    complex_scene_142 = Scene()
    complex_scene_142.memo = None
    complex_scene_142.page = 80
    complex_scene_142.type_master = complex_type_master_36
    complex_scene_142 = importer.save_or_locate(complex_scene_142)

    complex_scene_143 = Scene()
    complex_scene_143.memo = None
    complex_scene_143.page = 81
    complex_scene_143.type_master = complex_type_master_36
    complex_scene_143 = importer.save_or_locate(complex_scene_143)

    complex_scene_144 = Scene()
    complex_scene_144.memo = None
    complex_scene_144.page = 81
    complex_scene_144.type_master = complex_type_master_36
    complex_scene_144 = importer.save_or_locate(complex_scene_144)

    complex_scene_145 = Scene()
    complex_scene_145.memo = None
    complex_scene_145.page = 82
    complex_scene_145.type_master = complex_type_master_36
    complex_scene_145 = importer.save_or_locate(complex_scene_145)

    complex_scene_146 = Scene()
    complex_scene_146.memo = None
    complex_scene_146.page = 85
    complex_scene_146.type_master = complex_type_master_36
    complex_scene_146 = importer.save_or_locate(complex_scene_146)

    complex_scene_147 = Scene()
    complex_scene_147.memo = None
    complex_scene_147.page = 87
    complex_scene_147.type_master = complex_type_master_36
    complex_scene_147 = importer.save_or_locate(complex_scene_147)

    complex_scene_148 = Scene()
    complex_scene_148.memo = None
    complex_scene_148.page = 90
    complex_scene_148.type_master = complex_type_master_36
    complex_scene_148 = importer.save_or_locate(complex_scene_148)

    complex_scene_149 = Scene()
    complex_scene_149.memo = None
    complex_scene_149.page = 91
    complex_scene_149.type_master = complex_type_master_36
    complex_scene_149 = importer.save_or_locate(complex_scene_149)

    complex_scene_150 = Scene()
    complex_scene_150.memo = None
    complex_scene_150.page = 92
    complex_scene_150.type_master = complex_type_master_36
    complex_scene_150 = importer.save_or_locate(complex_scene_150)

    complex_scene_151 = Scene()
    complex_scene_151.memo = None
    complex_scene_151.page = 93
    complex_scene_151.type_master = complex_type_master_36
    complex_scene_151 = importer.save_or_locate(complex_scene_151)

    complex_scene_152 = Scene()
    complex_scene_152.memo = None
    complex_scene_152.page = 98
    complex_scene_152.type_master = complex_type_master_36
    complex_scene_152 = importer.save_or_locate(complex_scene_152)

    complex_scene_153 = Scene()
    complex_scene_153.memo = None
    complex_scene_153.page = 101
    complex_scene_153.type_master = complex_type_master_36
    complex_scene_153 = importer.save_or_locate(complex_scene_153)

    complex_scene_154 = Scene()
    complex_scene_154.memo = None
    complex_scene_154.page = 101
    complex_scene_154.type_master = complex_type_master_36
    complex_scene_154 = importer.save_or_locate(complex_scene_154)

    complex_scene_155 = Scene()
    complex_scene_155.memo = None
    complex_scene_155.page = 103
    complex_scene_155.type_master = complex_type_master_36
    complex_scene_155 = importer.save_or_locate(complex_scene_155)

    complex_scene_156 = Scene()
    complex_scene_156.memo = None
    complex_scene_156.page = 112
    complex_scene_156.type_master = complex_type_master_36
    complex_scene_156 = importer.save_or_locate(complex_scene_156)

    complex_scene_157 = Scene()
    complex_scene_157.memo = None
    complex_scene_157.page = 113
    complex_scene_157.type_master = complex_type_master_36
    complex_scene_157 = importer.save_or_locate(complex_scene_157)

    complex_scene_158 = Scene()
    complex_scene_158.memo = None
    complex_scene_158.page = 113
    complex_scene_158.type_master = complex_type_master_36
    complex_scene_158 = importer.save_or_locate(complex_scene_158)

    complex_scene_159 = Scene()
    complex_scene_159.memo = None
    complex_scene_159.page = 117
    complex_scene_159.type_master = complex_type_master_36
    complex_scene_159 = importer.save_or_locate(complex_scene_159)

    complex_scene_160 = Scene()
    complex_scene_160.memo = None
    complex_scene_160.page = 118
    complex_scene_160.type_master = complex_type_master_36
    complex_scene_160 = importer.save_or_locate(complex_scene_160)

    complex_scene_161 = Scene()
    complex_scene_161.memo = None
    complex_scene_161.page = 121
    complex_scene_161.type_master = complex_type_master_36
    complex_scene_161 = importer.save_or_locate(complex_scene_161)

    complex_scene_162 = Scene()
    complex_scene_162.memo = None
    complex_scene_162.page = 130
    complex_scene_162.type_master = complex_type_master_36
    complex_scene_162 = importer.save_or_locate(complex_scene_162)

    complex_scene_163 = Scene()
    complex_scene_163.memo = None
    complex_scene_163.page = 132
    complex_scene_163.type_master = complex_type_master_36
    complex_scene_163 = importer.save_or_locate(complex_scene_163)

    complex_scene_164 = Scene()
    complex_scene_164.memo = None
    complex_scene_164.page = 133
    complex_scene_164.type_master = complex_type_master_36
    complex_scene_164 = importer.save_or_locate(complex_scene_164)

    complex_scene_165 = Scene()
    complex_scene_165.memo = None
    complex_scene_165.page = 134
    complex_scene_165.type_master = complex_type_master_36
    complex_scene_165 = importer.save_or_locate(complex_scene_165)

    complex_scene_166 = Scene()
    complex_scene_166.memo = None
    complex_scene_166.page = 137
    complex_scene_166.type_master = complex_type_master_36
    complex_scene_166 = importer.save_or_locate(complex_scene_166)

    complex_scene_167 = Scene()
    complex_scene_167.memo = None
    complex_scene_167.page = 137
    complex_scene_167.type_master = complex_type_master_36
    complex_scene_167 = importer.save_or_locate(complex_scene_167)

    complex_scene_168 = Scene()
    complex_scene_168.memo = None
    complex_scene_168.page = 137
    complex_scene_168.type_master = complex_type_master_36
    complex_scene_168 = importer.save_or_locate(complex_scene_168)

    complex_scene_169 = Scene()
    complex_scene_169.memo = None
    complex_scene_169.page = 139
    complex_scene_169.type_master = complex_type_master_36
    complex_scene_169 = importer.save_or_locate(complex_scene_169)

    complex_scene_170 = Scene()
    complex_scene_170.memo = None
    complex_scene_170.page = 139
    complex_scene_170.type_master = complex_type_master_36
    complex_scene_170 = importer.save_or_locate(complex_scene_170)

    complex_scene_171 = Scene()
    complex_scene_171.memo = None
    complex_scene_171.page = 140
    complex_scene_171.type_master = complex_type_master_36
    complex_scene_171 = importer.save_or_locate(complex_scene_171)

    complex_scene_172 = Scene()
    complex_scene_172.memo = None
    complex_scene_172.page = 141
    complex_scene_172.type_master = complex_type_master_36
    complex_scene_172 = importer.save_or_locate(complex_scene_172)

    complex_scene_173 = Scene()
    complex_scene_173.memo = None
    complex_scene_173.page = 142
    complex_scene_173.type_master = complex_type_master_36
    complex_scene_173 = importer.save_or_locate(complex_scene_173)

    complex_scene_174 = Scene()
    complex_scene_174.memo = None
    complex_scene_174.page = 143
    complex_scene_174.type_master = complex_type_master_36
    complex_scene_174 = importer.save_or_locate(complex_scene_174)

    complex_scene_175 = Scene()
    complex_scene_175.memo = None
    complex_scene_175.page = 145
    complex_scene_175.type_master = complex_type_master_36
    complex_scene_175 = importer.save_or_locate(complex_scene_175)

    complex_scene_176 = Scene()
    complex_scene_176.memo = None
    complex_scene_176.page = 146
    complex_scene_176.type_master = complex_type_master_36
    complex_scene_176 = importer.save_or_locate(complex_scene_176)

    complex_scene_177 = Scene()
    complex_scene_177.memo = None
    complex_scene_177.page = 146
    complex_scene_177.type_master = complex_type_master_36
    complex_scene_177 = importer.save_or_locate(complex_scene_177)

    complex_scene_178 = Scene()
    complex_scene_178.memo = None
    complex_scene_178.page = 150
    complex_scene_178.type_master = complex_type_master_36
    complex_scene_178 = importer.save_or_locate(complex_scene_178)

    complex_scene_179 = Scene()
    complex_scene_179.memo = None
    complex_scene_179.page = 9
    complex_scene_179.type_master = complex_type_master_36
    complex_scene_179 = importer.save_or_locate(complex_scene_179)

    complex_scene_180 = Scene()
    complex_scene_180.memo = None
    complex_scene_180.page = 11
    complex_scene_180.type_master = complex_type_master_36
    complex_scene_180 = importer.save_or_locate(complex_scene_180)

    complex_scene_181 = Scene()
    complex_scene_181.memo = None
    complex_scene_181.page = 13
    complex_scene_181.type_master = complex_type_master_36
    complex_scene_181 = importer.save_or_locate(complex_scene_181)

    complex_scene_182 = Scene()
    complex_scene_182.memo = None
    complex_scene_182.page = 14
    complex_scene_182.type_master = complex_type_master_36
    complex_scene_182 = importer.save_or_locate(complex_scene_182)

    complex_scene_183 = Scene()
    complex_scene_183.memo = None
    complex_scene_183.page = 28
    complex_scene_183.type_master = complex_type_master_36
    complex_scene_183 = importer.save_or_locate(complex_scene_183)

    complex_scene_184 = Scene()
    complex_scene_184.memo = None
    complex_scene_184.page = 32
    complex_scene_184.type_master = complex_type_master_36
    complex_scene_184 = importer.save_or_locate(complex_scene_184)

    complex_scene_185 = Scene()
    complex_scene_185.memo = None
    complex_scene_185.page = 33
    complex_scene_185.type_master = complex_type_master_36
    complex_scene_185 = importer.save_or_locate(complex_scene_185)

    complex_scene_186 = Scene()
    complex_scene_186.memo = None
    complex_scene_186.page = 37
    complex_scene_186.type_master = complex_type_master_36
    complex_scene_186 = importer.save_or_locate(complex_scene_186)

    complex_scene_187 = Scene()
    complex_scene_187.memo = None
    complex_scene_187.page = 93
    complex_scene_187.type_master = complex_type_master_36
    complex_scene_187 = importer.save_or_locate(complex_scene_187)

    complex_scene_188 = Scene()
    complex_scene_188.memo = None
    complex_scene_188.page = 96
    complex_scene_188.type_master = complex_type_master_36
    complex_scene_188 = importer.save_or_locate(complex_scene_188)

    complex_scene_189 = Scene()
    complex_scene_189.memo = None
    complex_scene_189.page = 97
    complex_scene_189.type_master = complex_type_master_36
    complex_scene_189 = importer.save_or_locate(complex_scene_189)

    complex_scene_190 = Scene()
    complex_scene_190.memo = None
    complex_scene_190.page = 98
    complex_scene_190.type_master = complex_type_master_36
    complex_scene_190 = importer.save_or_locate(complex_scene_190)

    complex_scene_191 = Scene()
    complex_scene_191.memo = None
    complex_scene_191.page = 100
    complex_scene_191.type_master = complex_type_master_36
    complex_scene_191 = importer.save_or_locate(complex_scene_191)

    complex_scene_192 = Scene()
    complex_scene_192.memo = None
    complex_scene_192.page = 101
    complex_scene_192.type_master = complex_type_master_36
    complex_scene_192 = importer.save_or_locate(complex_scene_192)

    complex_scene_193 = Scene()
    complex_scene_193.memo = None
    complex_scene_193.page = 102
    complex_scene_193.type_master = complex_type_master_36
    complex_scene_193 = importer.save_or_locate(complex_scene_193)

    complex_scene_194 = Scene()
    complex_scene_194.memo = None
    complex_scene_194.page = 105
    complex_scene_194.type_master = complex_type_master_36
    complex_scene_194 = importer.save_or_locate(complex_scene_194)

    complex_scene_195 = Scene()
    complex_scene_195.memo = None
    complex_scene_195.page = 105
    complex_scene_195.type_master = complex_type_master_36
    complex_scene_195 = importer.save_or_locate(complex_scene_195)

    complex_scene_196 = Scene()
    complex_scene_196.memo = None
    complex_scene_196.page = 107
    complex_scene_196.type_master = complex_type_master_36
    complex_scene_196 = importer.save_or_locate(complex_scene_196)

    complex_scene_197 = Scene()
    complex_scene_197.memo = None
    complex_scene_197.page = 109
    complex_scene_197.type_master = complex_type_master_36
    complex_scene_197 = importer.save_or_locate(complex_scene_197)

    complex_scene_198 = Scene()
    complex_scene_198.memo = None
    complex_scene_198.page = 110
    complex_scene_198.type_master = complex_type_master_36
    complex_scene_198 = importer.save_or_locate(complex_scene_198)

    complex_scene_199 = Scene()
    complex_scene_199.memo = None
    complex_scene_199.page = 110
    complex_scene_199.type_master = complex_type_master_36
    complex_scene_199 = importer.save_or_locate(complex_scene_199)

    complex_scene_200 = Scene()
    complex_scene_200.memo = None
    complex_scene_200.page = 117
    complex_scene_200.type_master = complex_type_master_36
    complex_scene_200 = importer.save_or_locate(complex_scene_200)

    complex_scene_201 = Scene()
    complex_scene_201.memo = None
    complex_scene_201.page = 119
    complex_scene_201.type_master = complex_type_master_36
    complex_scene_201 = importer.save_or_locate(complex_scene_201)

    complex_scene_202 = Scene()
    complex_scene_202.memo = None
    complex_scene_202.page = 121
    complex_scene_202.type_master = complex_type_master_36
    complex_scene_202 = importer.save_or_locate(complex_scene_202)

    complex_scene_203 = Scene()
    complex_scene_203.memo = None
    complex_scene_203.page = 121
    complex_scene_203.type_master = complex_type_master_36
    complex_scene_203 = importer.save_or_locate(complex_scene_203)

    complex_scene_204 = Scene()
    complex_scene_204.memo = None
    complex_scene_204.page = 122
    complex_scene_204.type_master = complex_type_master_36
    complex_scene_204 = importer.save_or_locate(complex_scene_204)

    complex_scene_205 = Scene()
    complex_scene_205.memo = None
    complex_scene_205.page = 122
    complex_scene_205.type_master = complex_type_master_36
    complex_scene_205 = importer.save_or_locate(complex_scene_205)

    complex_scene_206 = Scene()
    complex_scene_206.memo = None
    complex_scene_206.page = 122
    complex_scene_206.type_master = complex_type_master_36
    complex_scene_206 = importer.save_or_locate(complex_scene_206)

    complex_scene_207 = Scene()
    complex_scene_207.memo = None
    complex_scene_207.page = 125
    complex_scene_207.type_master = complex_type_master_36
    complex_scene_207 = importer.save_or_locate(complex_scene_207)

    complex_scene_208 = Scene()
    complex_scene_208.memo = None
    complex_scene_208.page = 126
    complex_scene_208.type_master = complex_type_master_36
    complex_scene_208 = importer.save_or_locate(complex_scene_208)

    complex_scene_209 = Scene()
    complex_scene_209.memo = None
    complex_scene_209.page = 126
    complex_scene_209.type_master = complex_type_master_36
    complex_scene_209 = importer.save_or_locate(complex_scene_209)

    complex_scene_210 = Scene()
    complex_scene_210.memo = None
    complex_scene_210.page = 127
    complex_scene_210.type_master = complex_type_master_36
    complex_scene_210 = importer.save_or_locate(complex_scene_210)

    complex_scene_211 = Scene()
    complex_scene_211.memo = None
    complex_scene_211.page = 128
    complex_scene_211.type_master = complex_type_master_36
    complex_scene_211 = importer.save_or_locate(complex_scene_211)

    complex_scene_212 = Scene()
    complex_scene_212.memo = None
    complex_scene_212.page = 129
    complex_scene_212.type_master = complex_type_master_36
    complex_scene_212 = importer.save_or_locate(complex_scene_212)

    complex_scene_213 = Scene()
    complex_scene_213.memo = None
    complex_scene_213.page = 130
    complex_scene_213.type_master = complex_type_master_36
    complex_scene_213 = importer.save_or_locate(complex_scene_213)

    complex_scene_214 = Scene()
    complex_scene_214.memo = None
    complex_scene_214.page = 130
    complex_scene_214.type_master = complex_type_master_36
    complex_scene_214 = importer.save_or_locate(complex_scene_214)

    complex_scene_215 = Scene()
    complex_scene_215.memo = None
    complex_scene_215.page = 132
    complex_scene_215.type_master = complex_type_master_36
    complex_scene_215 = importer.save_or_locate(complex_scene_215)

    complex_scene_216 = Scene()
    complex_scene_216.memo = None
    complex_scene_216.page = 133
    complex_scene_216.type_master = complex_type_master_36
    complex_scene_216 = importer.save_or_locate(complex_scene_216)

    complex_scene_217 = Scene()
    complex_scene_217.memo = None
    complex_scene_217.page = 134
    complex_scene_217.type_master = complex_type_master_36
    complex_scene_217 = importer.save_or_locate(complex_scene_217)

    complex_scene_218 = Scene()
    complex_scene_218.memo = None
    complex_scene_218.page = 134
    complex_scene_218.type_master = complex_type_master_36
    complex_scene_218 = importer.save_or_locate(complex_scene_218)

    complex_scene_219 = Scene()
    complex_scene_219.memo = None
    complex_scene_219.page = 134
    complex_scene_219.type_master = complex_type_master_36
    complex_scene_219 = importer.save_or_locate(complex_scene_219)

    complex_scene_220 = Scene()
    complex_scene_220.memo = None
    complex_scene_220.page = 135
    complex_scene_220.type_master = complex_type_master_36
    complex_scene_220 = importer.save_or_locate(complex_scene_220)

    complex_scene_221 = Scene()
    complex_scene_221.memo = None
    complex_scene_221.page = 136
    complex_scene_221.type_master = complex_type_master_36
    complex_scene_221 = importer.save_or_locate(complex_scene_221)

    complex_scene_222 = Scene()
    complex_scene_222.memo = None
    complex_scene_222.page = 138
    complex_scene_222.type_master = complex_type_master_36
    complex_scene_222 = importer.save_or_locate(complex_scene_222)

    complex_scene_223 = Scene()
    complex_scene_223.memo = None
    complex_scene_223.page = 145
    complex_scene_223.type_master = complex_type_master_36
    complex_scene_223 = importer.save_or_locate(complex_scene_223)

    complex_scene_224 = Scene()
    complex_scene_224.memo = None
    complex_scene_224.page = 3
    complex_scene_224.type_master = complex_type_master_36
    complex_scene_224 = importer.save_or_locate(complex_scene_224)

    complex_scene_225 = Scene()
    complex_scene_225.memo = None
    complex_scene_225.page = 4
    complex_scene_225.type_master = complex_type_master_36
    complex_scene_225 = importer.save_or_locate(complex_scene_225)

    complex_scene_226 = Scene()
    complex_scene_226.memo = None
    complex_scene_226.page = 7
    complex_scene_226.type_master = complex_type_master_36
    complex_scene_226 = importer.save_or_locate(complex_scene_226)

    complex_scene_227 = Scene()
    complex_scene_227.memo = None
    complex_scene_227.page = 9
    complex_scene_227.type_master = complex_type_master_36
    complex_scene_227 = importer.save_or_locate(complex_scene_227)

    complex_scene_228 = Scene()
    complex_scene_228.memo = None
    complex_scene_228.page = 11
    complex_scene_228.type_master = complex_type_master_36
    complex_scene_228 = importer.save_or_locate(complex_scene_228)

    complex_scene_229 = Scene()
    complex_scene_229.memo = None
    complex_scene_229.page = 12
    complex_scene_229.type_master = complex_type_master_36
    complex_scene_229 = importer.save_or_locate(complex_scene_229)

    complex_scene_230 = Scene()
    complex_scene_230.memo = None
    complex_scene_230.page = 12
    complex_scene_230.type_master = complex_type_master_36
    complex_scene_230 = importer.save_or_locate(complex_scene_230)

    complex_scene_231 = Scene()
    complex_scene_231.memo = None
    complex_scene_231.page = 14
    complex_scene_231.type_master = complex_type_master_36
    complex_scene_231 = importer.save_or_locate(complex_scene_231)

    complex_scene_232 = Scene()
    complex_scene_232.memo = None
    complex_scene_232.page = 14
    complex_scene_232.type_master = complex_type_master_36
    complex_scene_232 = importer.save_or_locate(complex_scene_232)

    complex_scene_233 = Scene()
    complex_scene_233.memo = None
    complex_scene_233.page = 14
    complex_scene_233.type_master = complex_type_master_36
    complex_scene_233 = importer.save_or_locate(complex_scene_233)

    complex_scene_234 = Scene()
    complex_scene_234.memo = None
    complex_scene_234.page = 14
    complex_scene_234.type_master = complex_type_master_36
    complex_scene_234 = importer.save_or_locate(complex_scene_234)

    complex_scene_235 = Scene()
    complex_scene_235.memo = None
    complex_scene_235.page = 15
    complex_scene_235.type_master = complex_type_master_36
    complex_scene_235 = importer.save_or_locate(complex_scene_235)

    complex_scene_236 = Scene()
    complex_scene_236.memo = None
    complex_scene_236.page = 16
    complex_scene_236.type_master = complex_type_master_36
    complex_scene_236 = importer.save_or_locate(complex_scene_236)

    complex_scene_237 = Scene()
    complex_scene_237.memo = None
    complex_scene_237.page = 16
    complex_scene_237.type_master = complex_type_master_36
    complex_scene_237 = importer.save_or_locate(complex_scene_237)

    complex_scene_238 = Scene()
    complex_scene_238.memo = None
    complex_scene_238.page = 17
    complex_scene_238.type_master = complex_type_master_36
    complex_scene_238 = importer.save_or_locate(complex_scene_238)

    complex_scene_239 = Scene()
    complex_scene_239.memo = None
    complex_scene_239.page = 19
    complex_scene_239.type_master = complex_type_master_36
    complex_scene_239 = importer.save_or_locate(complex_scene_239)

    complex_scene_240 = Scene()
    complex_scene_240.memo = None
    complex_scene_240.page = 28
    complex_scene_240.type_master = complex_type_master_36
    complex_scene_240 = importer.save_or_locate(complex_scene_240)

    complex_scene_241 = Scene()
    complex_scene_241.memo = None
    complex_scene_241.page = 29
    complex_scene_241.type_master = complex_type_master_36
    complex_scene_241 = importer.save_or_locate(complex_scene_241)

    complex_scene_242 = Scene()
    complex_scene_242.memo = None
    complex_scene_242.page = 32
    complex_scene_242.type_master = complex_type_master_36
    complex_scene_242 = importer.save_or_locate(complex_scene_242)

    complex_scene_243 = Scene()
    complex_scene_243.memo = None
    complex_scene_243.page = 36
    complex_scene_243.type_master = complex_type_master_36
    complex_scene_243 = importer.save_or_locate(complex_scene_243)

    complex_scene_244 = Scene()
    complex_scene_244.memo = None
    complex_scene_244.page = 40
    complex_scene_244.type_master = complex_type_master_36
    complex_scene_244 = importer.save_or_locate(complex_scene_244)

    complex_scene_245 = Scene()
    complex_scene_245.memo = None
    complex_scene_245.page = 46
    complex_scene_245.type_master = complex_type_master_36
    complex_scene_245 = importer.save_or_locate(complex_scene_245)

    complex_scene_246 = Scene()
    complex_scene_246.memo = None
    complex_scene_246.page = 51
    complex_scene_246.type_master = complex_type_master_36
    complex_scene_246 = importer.save_or_locate(complex_scene_246)

    complex_scene_247 = Scene()
    complex_scene_247.memo = None
    complex_scene_247.page = 52
    complex_scene_247.type_master = complex_type_master_36
    complex_scene_247 = importer.save_or_locate(complex_scene_247)

    complex_scene_248 = Scene()
    complex_scene_248.memo = None
    complex_scene_248.page = 53
    complex_scene_248.type_master = complex_type_master_36
    complex_scene_248 = importer.save_or_locate(complex_scene_248)

    complex_scene_249 = Scene()
    complex_scene_249.memo = None
    complex_scene_249.page = 60
    complex_scene_249.type_master = complex_type_master_36
    complex_scene_249 = importer.save_or_locate(complex_scene_249)

    complex_scene_250 = Scene()
    complex_scene_250.memo = None
    complex_scene_250.page = 61
    complex_scene_250.type_master = complex_type_master_36
    complex_scene_250 = importer.save_or_locate(complex_scene_250)

    complex_scene_251 = Scene()
    complex_scene_251.memo = None
    complex_scene_251.page = 62
    complex_scene_251.type_master = complex_type_master_36
    complex_scene_251 = importer.save_or_locate(complex_scene_251)

    complex_scene_252 = Scene()
    complex_scene_252.memo = None
    complex_scene_252.page = 66
    complex_scene_252.type_master = complex_type_master_36
    complex_scene_252 = importer.save_or_locate(complex_scene_252)

    complex_scene_253 = Scene()
    complex_scene_253.memo = None
    complex_scene_253.page = 68
    complex_scene_253.type_master = complex_type_master_36
    complex_scene_253 = importer.save_or_locate(complex_scene_253)

    complex_scene_254 = Scene()
    complex_scene_254.memo = None
    complex_scene_254.page = 71
    complex_scene_254.type_master = complex_type_master_36
    complex_scene_254 = importer.save_or_locate(complex_scene_254)

    complex_scene_255 = Scene()
    complex_scene_255.memo = None
    complex_scene_255.page = 83
    complex_scene_255.type_master = complex_type_master_36
    complex_scene_255 = importer.save_or_locate(complex_scene_255)

    complex_scene_256 = Scene()
    complex_scene_256.memo = None
    complex_scene_256.page = 84
    complex_scene_256.type_master = complex_type_master_36
    complex_scene_256 = importer.save_or_locate(complex_scene_256)

    complex_scene_257 = Scene()
    complex_scene_257.memo = None
    complex_scene_257.page = 86
    complex_scene_257.type_master = complex_type_master_36
    complex_scene_257 = importer.save_or_locate(complex_scene_257)

    complex_scene_258 = Scene()
    complex_scene_258.memo = None
    complex_scene_258.page = 89
    complex_scene_258.type_master = complex_type_master_36
    complex_scene_258 = importer.save_or_locate(complex_scene_258)

    complex_scene_259 = Scene()
    complex_scene_259.memo = None
    complex_scene_259.page = 102
    complex_scene_259.type_master = complex_type_master_36
    complex_scene_259 = importer.save_or_locate(complex_scene_259)

    complex_scene_260 = Scene()
    complex_scene_260.memo = None
    complex_scene_260.page = 104
    complex_scene_260.type_master = complex_type_master_36
    complex_scene_260 = importer.save_or_locate(complex_scene_260)

    complex_scene_261 = Scene()
    complex_scene_261.memo = None
    complex_scene_261.page = 105
    complex_scene_261.type_master = complex_type_master_36
    complex_scene_261 = importer.save_or_locate(complex_scene_261)

    complex_scene_262 = Scene()
    complex_scene_262.memo = None
    complex_scene_262.page = 108
    complex_scene_262.type_master = complex_type_master_36
    complex_scene_262 = importer.save_or_locate(complex_scene_262)

    complex_scene_263 = Scene()
    complex_scene_263.memo = None
    complex_scene_263.page = 117
    complex_scene_263.type_master = complex_type_master_36
    complex_scene_263 = importer.save_or_locate(complex_scene_263)

    complex_scene_264 = Scene()
    complex_scene_264.memo = None
    complex_scene_264.page = 136
    complex_scene_264.type_master = complex_type_master_36
    complex_scene_264 = importer.save_or_locate(complex_scene_264)

    complex_scene_265 = Scene()
    complex_scene_265.memo = None
    complex_scene_265.page = 137
    complex_scene_265.type_master = complex_type_master_36
    complex_scene_265 = importer.save_or_locate(complex_scene_265)

    complex_scene_266 = Scene()
    complex_scene_266.memo = None
    complex_scene_266.page = 137
    complex_scene_266.type_master = complex_type_master_36
    complex_scene_266 = importer.save_or_locate(complex_scene_266)

    complex_scene_267 = Scene()
    complex_scene_267.memo = None
    complex_scene_267.page = 138
    complex_scene_267.type_master = complex_type_master_36
    complex_scene_267 = importer.save_or_locate(complex_scene_267)

    complex_scene_268 = Scene()
    complex_scene_268.memo = None
    complex_scene_268.page = 139
    complex_scene_268.type_master = complex_type_master_36
    complex_scene_268 = importer.save_or_locate(complex_scene_268)

    complex_scene_269 = Scene()
    complex_scene_269.memo = None
    complex_scene_269.page = 139
    complex_scene_269.type_master = complex_type_master_36
    complex_scene_269 = importer.save_or_locate(complex_scene_269)

    complex_scene_270 = Scene()
    complex_scene_270.memo = None
    complex_scene_270.page = 139
    complex_scene_270.type_master = complex_type_master_36
    complex_scene_270 = importer.save_or_locate(complex_scene_270)

    complex_scene_271 = Scene()
    complex_scene_271.memo = None
    complex_scene_271.page = 140
    complex_scene_271.type_master = complex_type_master_36
    complex_scene_271 = importer.save_or_locate(complex_scene_271)

    complex_scene_272 = Scene()
    complex_scene_272.memo = None
    complex_scene_272.page = 140
    complex_scene_272.type_master = complex_type_master_36
    complex_scene_272 = importer.save_or_locate(complex_scene_272)

    complex_scene_273 = Scene()
    complex_scene_273.memo = None
    complex_scene_273.page = 141
    complex_scene_273.type_master = complex_type_master_36
    complex_scene_273 = importer.save_or_locate(complex_scene_273)

    complex_scene_274 = Scene()
    complex_scene_274.memo = None
    complex_scene_274.page = 141
    complex_scene_274.type_master = complex_type_master_36
    complex_scene_274 = importer.save_or_locate(complex_scene_274)

    complex_scene_275 = Scene()
    complex_scene_275.memo = None
    complex_scene_275.page = 141
    complex_scene_275.type_master = complex_type_master_36
    complex_scene_275 = importer.save_or_locate(complex_scene_275)

    complex_scene_276 = Scene()
    complex_scene_276.memo = None
    complex_scene_276.page = 142
    complex_scene_276.type_master = complex_type_master_36
    complex_scene_276 = importer.save_or_locate(complex_scene_276)

    complex_scene_277 = Scene()
    complex_scene_277.memo = None
    complex_scene_277.page = 142
    complex_scene_277.type_master = complex_type_master_36
    complex_scene_277 = importer.save_or_locate(complex_scene_277)

    complex_scene_278 = Scene()
    complex_scene_278.memo = None
    complex_scene_278.page = 143
    complex_scene_278.type_master = complex_type_master_36
    complex_scene_278 = importer.save_or_locate(complex_scene_278)

    complex_scene_279 = Scene()
    complex_scene_279.memo = None
    complex_scene_279.page = 144
    complex_scene_279.type_master = complex_type_master_36
    complex_scene_279 = importer.save_or_locate(complex_scene_279)

    complex_scene_280 = Scene()
    complex_scene_280.memo = None
    complex_scene_280.page = 144
    complex_scene_280.type_master = complex_type_master_36
    complex_scene_280 = importer.save_or_locate(complex_scene_280)

    complex_scene_281 = Scene()
    complex_scene_281.memo = None
    complex_scene_281.page = 145
    complex_scene_281.type_master = complex_type_master_36
    complex_scene_281 = importer.save_or_locate(complex_scene_281)

    complex_scene_282 = Scene()
    complex_scene_282.memo = None
    complex_scene_282.page = 145
    complex_scene_282.type_master = complex_type_master_36
    complex_scene_282 = importer.save_or_locate(complex_scene_282)

    complex_scene_283 = Scene()
    complex_scene_283.memo = None
    complex_scene_283.page = 146
    complex_scene_283.type_master = complex_type_master_36
    complex_scene_283 = importer.save_or_locate(complex_scene_283)

    complex_scene_284 = Scene()
    complex_scene_284.memo = None
    complex_scene_284.page = 147
    complex_scene_284.type_master = complex_type_master_36
    complex_scene_284 = importer.save_or_locate(complex_scene_284)

    complex_scene_285 = Scene()
    complex_scene_285.memo = None
    complex_scene_285.page = 147
    complex_scene_285.type_master = complex_type_master_36
    complex_scene_285 = importer.save_or_locate(complex_scene_285)

    complex_scene_286 = Scene()
    complex_scene_286.memo = None
    complex_scene_286.page = 148
    complex_scene_286.type_master = complex_type_master_36
    complex_scene_286 = importer.save_or_locate(complex_scene_286)

    complex_scene_287 = Scene()
    complex_scene_287.memo = None
    complex_scene_287.page = 149
    complex_scene_287.type_master = complex_type_master_36
    complex_scene_287 = importer.save_or_locate(complex_scene_287)

    complex_scene_288 = Scene()
    complex_scene_288.memo = None
    complex_scene_288.page = 150
    complex_scene_288.type_master = complex_type_master_36
    complex_scene_288 = importer.save_or_locate(complex_scene_288)

    complex_scene_289 = Scene()
    complex_scene_289.memo = None
    complex_scene_289.page = 150
    complex_scene_289.type_master = complex_type_master_36
    complex_scene_289 = importer.save_or_locate(complex_scene_289)

    complex_scene_290 = Scene()
    complex_scene_290.memo = None
    complex_scene_290.page = 157
    complex_scene_290.type_master = complex_type_master_36
    complex_scene_290 = importer.save_or_locate(complex_scene_290)

    complex_scene_291 = Scene()
    complex_scene_291.memo = None
    complex_scene_291.page = 18
    complex_scene_291.type_master = complex_type_master_36
    complex_scene_291 = importer.save_or_locate(complex_scene_291)

    complex_scene_292 = Scene()
    complex_scene_292.memo = None
    complex_scene_292.page = 18
    complex_scene_292.type_master = complex_type_master_36
    complex_scene_292 = importer.save_or_locate(complex_scene_292)

    complex_scene_293 = Scene()
    complex_scene_293.memo = None
    complex_scene_293.page = 18
    complex_scene_293.type_master = complex_type_master_36
    complex_scene_293 = importer.save_or_locate(complex_scene_293)

    complex_scene_294 = Scene()
    complex_scene_294.memo = None
    complex_scene_294.page = 19
    complex_scene_294.type_master = complex_type_master_36
    complex_scene_294 = importer.save_or_locate(complex_scene_294)

    complex_scene_295 = Scene()
    complex_scene_295.memo = None
    complex_scene_295.page = 38
    complex_scene_295.type_master = complex_type_master_36
    complex_scene_295 = importer.save_or_locate(complex_scene_295)

    complex_scene_296 = Scene()
    complex_scene_296.memo = None
    complex_scene_296.page = 39
    complex_scene_296.type_master = complex_type_master_36
    complex_scene_296 = importer.save_or_locate(complex_scene_296)

    complex_scene_297 = Scene()
    complex_scene_297.memo = None
    complex_scene_297.page = 39
    complex_scene_297.type_master = complex_type_master_36
    complex_scene_297 = importer.save_or_locate(complex_scene_297)

    complex_scene_298 = Scene()
    complex_scene_298.memo = None
    complex_scene_298.page = 40
    complex_scene_298.type_master = complex_type_master_36
    complex_scene_298 = importer.save_or_locate(complex_scene_298)

    complex_scene_299 = Scene()
    complex_scene_299.memo = None
    complex_scene_299.page = 40
    complex_scene_299.type_master = complex_type_master_36
    complex_scene_299 = importer.save_or_locate(complex_scene_299)

    complex_scene_300 = Scene()
    complex_scene_300.memo = None
    complex_scene_300.page = 41
    complex_scene_300.type_master = complex_type_master_36
    complex_scene_300 = importer.save_or_locate(complex_scene_300)

    complex_scene_301 = Scene()
    complex_scene_301.memo = None
    complex_scene_301.page = 42
    complex_scene_301.type_master = complex_type_master_36
    complex_scene_301 = importer.save_or_locate(complex_scene_301)

    complex_scene_302 = Scene()
    complex_scene_302.memo = None
    complex_scene_302.page = 43
    complex_scene_302.type_master = complex_type_master_36
    complex_scene_302 = importer.save_or_locate(complex_scene_302)

    complex_scene_303 = Scene()
    complex_scene_303.memo = None
    complex_scene_303.page = 50
    complex_scene_303.type_master = complex_type_master_36
    complex_scene_303 = importer.save_or_locate(complex_scene_303)

    complex_scene_304 = Scene()
    complex_scene_304.memo = None
    complex_scene_304.page = 54
    complex_scene_304.type_master = complex_type_master_36
    complex_scene_304 = importer.save_or_locate(complex_scene_304)

    complex_scene_305 = Scene()
    complex_scene_305.memo = None
    complex_scene_305.page = 56
    complex_scene_305.type_master = complex_type_master_36
    complex_scene_305 = importer.save_or_locate(complex_scene_305)

    complex_scene_306 = Scene()
    complex_scene_306.memo = None
    complex_scene_306.page = 57
    complex_scene_306.type_master = complex_type_master_36
    complex_scene_306 = importer.save_or_locate(complex_scene_306)

    complex_scene_307 = Scene()
    complex_scene_307.memo = None
    complex_scene_307.page = 32
    complex_scene_307.type_master = complex_type_master_36
    complex_scene_307 = importer.save_or_locate(complex_scene_307)

    complex_scene_308 = Scene()
    complex_scene_308.memo = None
    complex_scene_308.page = 58
    complex_scene_308.type_master = complex_type_master_36
    complex_scene_308 = importer.save_or_locate(complex_scene_308)

    complex_scene_309 = Scene()
    complex_scene_309.memo = None
    complex_scene_309.page = 70
    complex_scene_309.type_master = complex_type_master_36
    complex_scene_309 = importer.save_or_locate(complex_scene_309)

    complex_scene_310 = Scene()
    complex_scene_310.memo = None
    complex_scene_310.page = 71
    complex_scene_310.type_master = complex_type_master_36
    complex_scene_310 = importer.save_or_locate(complex_scene_310)

    complex_scene_311 = Scene()
    complex_scene_311.memo = None
    complex_scene_311.page = 72
    complex_scene_311.type_master = complex_type_master_36
    complex_scene_311 = importer.save_or_locate(complex_scene_311)

    complex_scene_312 = Scene()
    complex_scene_312.memo = None
    complex_scene_312.page = 73
    complex_scene_312.type_master = complex_type_master_36
    complex_scene_312 = importer.save_or_locate(complex_scene_312)

    complex_scene_313 = Scene()
    complex_scene_313.memo = None
    complex_scene_313.page = 73
    complex_scene_313.type_master = complex_type_master_36
    complex_scene_313 = importer.save_or_locate(complex_scene_313)

    complex_scene_314 = Scene()
    complex_scene_314.memo = None
    complex_scene_314.page = 74
    complex_scene_314.type_master = complex_type_master_36
    complex_scene_314 = importer.save_or_locate(complex_scene_314)

    complex_scene_315 = Scene()
    complex_scene_315.memo = None
    complex_scene_315.page = 74
    complex_scene_315.type_master = complex_type_master_36
    complex_scene_315 = importer.save_or_locate(complex_scene_315)

    complex_scene_316 = Scene()
    complex_scene_316.memo = None
    complex_scene_316.page = 80
    complex_scene_316.type_master = complex_type_master_36
    complex_scene_316 = importer.save_or_locate(complex_scene_316)

    complex_scene_317 = Scene()
    complex_scene_317.memo = None
    complex_scene_317.page = 80
    complex_scene_317.type_master = complex_type_master_36
    complex_scene_317 = importer.save_or_locate(complex_scene_317)

    complex_scene_318 = Scene()
    complex_scene_318.memo = None
    complex_scene_318.page = 80
    complex_scene_318.type_master = complex_type_master_36
    complex_scene_318 = importer.save_or_locate(complex_scene_318)

    complex_scene_319 = Scene()
    complex_scene_319.memo = None
    complex_scene_319.page = 81
    complex_scene_319.type_master = complex_type_master_36
    complex_scene_319 = importer.save_or_locate(complex_scene_319)

    complex_scene_320 = Scene()
    complex_scene_320.memo = None
    complex_scene_320.page = 81
    complex_scene_320.type_master = complex_type_master_36
    complex_scene_320 = importer.save_or_locate(complex_scene_320)

    complex_scene_321 = Scene()
    complex_scene_321.memo = None
    complex_scene_321.page = 82
    complex_scene_321.type_master = complex_type_master_36
    complex_scene_321 = importer.save_or_locate(complex_scene_321)

    complex_scene_322 = Scene()
    complex_scene_322.memo = None
    complex_scene_322.page = 82
    complex_scene_322.type_master = complex_type_master_36
    complex_scene_322 = importer.save_or_locate(complex_scene_322)

    complex_scene_323 = Scene()
    complex_scene_323.memo = None
    complex_scene_323.page = 83
    complex_scene_323.type_master = complex_type_master_36
    complex_scene_323 = importer.save_or_locate(complex_scene_323)

    complex_scene_324 = Scene()
    complex_scene_324.memo = None
    complex_scene_324.page = 90
    complex_scene_324.type_master = complex_type_master_36
    complex_scene_324 = importer.save_or_locate(complex_scene_324)

    complex_scene_325 = Scene()
    complex_scene_325.memo = None
    complex_scene_325.page = 92
    complex_scene_325.type_master = complex_type_master_36
    complex_scene_325 = importer.save_or_locate(complex_scene_325)

    complex_scene_326 = Scene()
    complex_scene_326.memo = None
    complex_scene_326.page = 93
    complex_scene_326.type_master = complex_type_master_36
    complex_scene_326 = importer.save_or_locate(complex_scene_326)

    complex_scene_327 = Scene()
    complex_scene_327.memo = None
    complex_scene_327.page = 101
    complex_scene_327.type_master = complex_type_master_36
    complex_scene_327 = importer.save_or_locate(complex_scene_327)

    complex_scene_328 = Scene()
    complex_scene_328.memo = None
    complex_scene_328.page = 132
    complex_scene_328.type_master = complex_type_master_36
    complex_scene_328 = importer.save_or_locate(complex_scene_328)

    complex_scene_329 = Scene()
    complex_scene_329.memo = None
    complex_scene_329.page = 108
    complex_scene_329.type_master = complex_type_master_36
    complex_scene_329 = importer.save_or_locate(complex_scene_329)

    complex_scene_330 = Scene()
    complex_scene_330.memo = None
    complex_scene_330.page = 109
    complex_scene_330.type_master = complex_type_master_36
    complex_scene_330 = importer.save_or_locate(complex_scene_330)

    complex_scene_331 = Scene()
    complex_scene_331.memo = None
    complex_scene_331.page = 116
    complex_scene_331.type_master = complex_type_master_36
    complex_scene_331 = importer.save_or_locate(complex_scene_331)

    complex_scene_332 = Scene()
    complex_scene_332.memo = None
    complex_scene_332.page = 117
    complex_scene_332.type_master = complex_type_master_36
    complex_scene_332 = importer.save_or_locate(complex_scene_332)

    complex_scene_333 = Scene()
    complex_scene_333.memo = None
    complex_scene_333.page = 122
    complex_scene_333.type_master = complex_type_master_36
    complex_scene_333 = importer.save_or_locate(complex_scene_333)

    complex_scene_334 = Scene()
    complex_scene_334.memo = None
    complex_scene_334.page = 122
    complex_scene_334.type_master = complex_type_master_36
    complex_scene_334 = importer.save_or_locate(complex_scene_334)

    complex_scene_335 = Scene()
    complex_scene_335.memo = None
    complex_scene_335.page = 124
    complex_scene_335.type_master = complex_type_master_36
    complex_scene_335 = importer.save_or_locate(complex_scene_335)

    complex_scene_336 = Scene()
    complex_scene_336.memo = None
    complex_scene_336.page = 124
    complex_scene_336.type_master = complex_type_master_36
    complex_scene_336 = importer.save_or_locate(complex_scene_336)

    complex_scene_337 = Scene()
    complex_scene_337.memo = None
    complex_scene_337.page = 125
    complex_scene_337.type_master = complex_type_master_36
    complex_scene_337 = importer.save_or_locate(complex_scene_337)

    complex_scene_338 = Scene()
    complex_scene_338.memo = None
    complex_scene_338.page = 127
    complex_scene_338.type_master = complex_type_master_36
    complex_scene_338 = importer.save_or_locate(complex_scene_338)

    complex_scene_339 = Scene()
    complex_scene_339.memo = None
    complex_scene_339.page = 128
    complex_scene_339.type_master = complex_type_master_36
    complex_scene_339 = importer.save_or_locate(complex_scene_339)

    complex_scene_340 = Scene()
    complex_scene_340.memo = None
    complex_scene_340.page = 135
    complex_scene_340.type_master = complex_type_master_36
    complex_scene_340 = importer.save_or_locate(complex_scene_340)

    complex_scene_341 = Scene()
    complex_scene_341.memo = None
    complex_scene_341.page = 6
    complex_scene_341.type_master = complex_type_master_36
    complex_scene_341 = importer.save_or_locate(complex_scene_341)

    complex_scene_342 = Scene()
    complex_scene_342.memo = None
    complex_scene_342.page = 11
    complex_scene_342.type_master = complex_type_master_36
    complex_scene_342 = importer.save_or_locate(complex_scene_342)

    complex_scene_343 = Scene()
    complex_scene_343.memo = None
    complex_scene_343.page = 13
    complex_scene_343.type_master = complex_type_master_36
    complex_scene_343 = importer.save_or_locate(complex_scene_343)

    complex_scene_344 = Scene()
    complex_scene_344.memo = None
    complex_scene_344.page = 16
    complex_scene_344.type_master = complex_type_master_36
    complex_scene_344 = importer.save_or_locate(complex_scene_344)

    complex_scene_345 = Scene()
    complex_scene_345.memo = None
    complex_scene_345.page = 21
    complex_scene_345.type_master = complex_type_master_36
    complex_scene_345 = importer.save_or_locate(complex_scene_345)

    complex_scene_346 = Scene()
    complex_scene_346.memo = None
    complex_scene_346.page = 21
    complex_scene_346.type_master = complex_type_master_36
    complex_scene_346 = importer.save_or_locate(complex_scene_346)

    complex_scene_347 = Scene()
    complex_scene_347.memo = None
    complex_scene_347.page = 24
    complex_scene_347.type_master = complex_type_master_36
    complex_scene_347 = importer.save_or_locate(complex_scene_347)

    complex_scene_348 = Scene()
    complex_scene_348.memo = None
    complex_scene_348.page = 24
    complex_scene_348.type_master = complex_type_master_36
    complex_scene_348 = importer.save_or_locate(complex_scene_348)

    complex_scene_349 = Scene()
    complex_scene_349.memo = None
    complex_scene_349.page = 25
    complex_scene_349.type_master = complex_type_master_36
    complex_scene_349 = importer.save_or_locate(complex_scene_349)

    complex_scene_350 = Scene()
    complex_scene_350.memo = None
    complex_scene_350.page = 25
    complex_scene_350.type_master = complex_type_master_36
    complex_scene_350 = importer.save_or_locate(complex_scene_350)

    complex_scene_351 = Scene()
    complex_scene_351.memo = None
    complex_scene_351.page = 26
    complex_scene_351.type_master = complex_type_master_36
    complex_scene_351 = importer.save_or_locate(complex_scene_351)

    complex_scene_352 = Scene()
    complex_scene_352.memo = None
    complex_scene_352.page = 27
    complex_scene_352.type_master = complex_type_master_36
    complex_scene_352 = importer.save_or_locate(complex_scene_352)

    complex_scene_353 = Scene()
    complex_scene_353.memo = None
    complex_scene_353.page = 35
    complex_scene_353.type_master = complex_type_master_36
    complex_scene_353 = importer.save_or_locate(complex_scene_353)

    complex_scene_354 = Scene()
    complex_scene_354.memo = None
    complex_scene_354.page = 35
    complex_scene_354.type_master = complex_type_master_36
    complex_scene_354 = importer.save_or_locate(complex_scene_354)

    complex_scene_355 = Scene()
    complex_scene_355.memo = None
    complex_scene_355.page = 36
    complex_scene_355.type_master = complex_type_master_36
    complex_scene_355 = importer.save_or_locate(complex_scene_355)

    complex_scene_356 = Scene()
    complex_scene_356.memo = None
    complex_scene_356.page = 38
    complex_scene_356.type_master = complex_type_master_36
    complex_scene_356 = importer.save_or_locate(complex_scene_356)

    complex_scene_357 = Scene()
    complex_scene_357.memo = None
    complex_scene_357.page = 39
    complex_scene_357.type_master = complex_type_master_36
    complex_scene_357 = importer.save_or_locate(complex_scene_357)

    complex_scene_358 = Scene()
    complex_scene_358.memo = None
    complex_scene_358.page = 39
    complex_scene_358.type_master = complex_type_master_36
    complex_scene_358 = importer.save_or_locate(complex_scene_358)

    complex_scene_359 = Scene()
    complex_scene_359.memo = None
    complex_scene_359.page = 40
    complex_scene_359.type_master = complex_type_master_36
    complex_scene_359 = importer.save_or_locate(complex_scene_359)

    complex_scene_360 = Scene()
    complex_scene_360.memo = None
    complex_scene_360.page = 43
    complex_scene_360.type_master = complex_type_master_36
    complex_scene_360 = importer.save_or_locate(complex_scene_360)

    complex_scene_361 = Scene()
    complex_scene_361.memo = None
    complex_scene_361.page = 45
    complex_scene_361.type_master = complex_type_master_36
    complex_scene_361 = importer.save_or_locate(complex_scene_361)

    complex_scene_362 = Scene()
    complex_scene_362.memo = None
    complex_scene_362.page = 45
    complex_scene_362.type_master = complex_type_master_36
    complex_scene_362 = importer.save_or_locate(complex_scene_362)

    complex_scene_363 = Scene()
    complex_scene_363.memo = None
    complex_scene_363.page = 46
    complex_scene_363.type_master = complex_type_master_36
    complex_scene_363 = importer.save_or_locate(complex_scene_363)

    complex_scene_364 = Scene()
    complex_scene_364.memo = None
    complex_scene_364.page = 46
    complex_scene_364.type_master = complex_type_master_36
    complex_scene_364 = importer.save_or_locate(complex_scene_364)

    complex_scene_365 = Scene()
    complex_scene_365.memo = None
    complex_scene_365.page = 49
    complex_scene_365.type_master = complex_type_master_36
    complex_scene_365 = importer.save_or_locate(complex_scene_365)

    complex_scene_366 = Scene()
    complex_scene_366.memo = None
    complex_scene_366.page = 49
    complex_scene_366.type_master = complex_type_master_36
    complex_scene_366 = importer.save_or_locate(complex_scene_366)

    complex_scene_367 = Scene()
    complex_scene_367.memo = None
    complex_scene_367.page = 50
    complex_scene_367.type_master = complex_type_master_36
    complex_scene_367 = importer.save_or_locate(complex_scene_367)

    complex_scene_368 = Scene()
    complex_scene_368.memo = None
    complex_scene_368.page = 52
    complex_scene_368.type_master = complex_type_master_36
    complex_scene_368 = importer.save_or_locate(complex_scene_368)

    complex_scene_369 = Scene()
    complex_scene_369.memo = None
    complex_scene_369.page = 62
    complex_scene_369.type_master = complex_type_master_36
    complex_scene_369 = importer.save_or_locate(complex_scene_369)

    complex_scene_370 = Scene()
    complex_scene_370.memo = None
    complex_scene_370.page = 63
    complex_scene_370.type_master = complex_type_master_36
    complex_scene_370 = importer.save_or_locate(complex_scene_370)

    complex_scene_371 = Scene()
    complex_scene_371.memo = None
    complex_scene_371.page = 63
    complex_scene_371.type_master = complex_type_master_36
    complex_scene_371 = importer.save_or_locate(complex_scene_371)

    complex_scene_372 = Scene()
    complex_scene_372.memo = None
    complex_scene_372.page = 72
    complex_scene_372.type_master = complex_type_master_36
    complex_scene_372 = importer.save_or_locate(complex_scene_372)

    complex_scene_373 = Scene()
    complex_scene_373.memo = None
    complex_scene_373.page = 75
    complex_scene_373.type_master = complex_type_master_36
    complex_scene_373 = importer.save_or_locate(complex_scene_373)

    complex_scene_374 = Scene()
    complex_scene_374.memo = None
    complex_scene_374.page = 76
    complex_scene_374.type_master = complex_type_master_36
    complex_scene_374 = importer.save_or_locate(complex_scene_374)

    complex_scene_375 = Scene()
    complex_scene_375.memo = None
    complex_scene_375.page = 85
    complex_scene_375.type_master = complex_type_master_36
    complex_scene_375 = importer.save_or_locate(complex_scene_375)

    complex_scene_376 = Scene()
    complex_scene_376.memo = None
    complex_scene_376.page = 86
    complex_scene_376.type_master = complex_type_master_36
    complex_scene_376 = importer.save_or_locate(complex_scene_376)

    complex_scene_377 = Scene()
    complex_scene_377.memo = None
    complex_scene_377.page = 90
    complex_scene_377.type_master = complex_type_master_36
    complex_scene_377 = importer.save_or_locate(complex_scene_377)

    complex_scene_378 = Scene()
    complex_scene_378.memo = None
    complex_scene_378.page = 90
    complex_scene_378.type_master = complex_type_master_36
    complex_scene_378 = importer.save_or_locate(complex_scene_378)

    complex_scene_379 = Scene()
    complex_scene_379.memo = None
    complex_scene_379.page = 92
    complex_scene_379.type_master = complex_type_master_36
    complex_scene_379 = importer.save_or_locate(complex_scene_379)

    complex_scene_380 = Scene()
    complex_scene_380.memo = None
    complex_scene_380.page = 95
    complex_scene_380.type_master = complex_type_master_36
    complex_scene_380 = importer.save_or_locate(complex_scene_380)

    complex_scene_381 = Scene()
    complex_scene_381.memo = None
    complex_scene_381.page = 97
    complex_scene_381.type_master = complex_type_master_36
    complex_scene_381 = importer.save_or_locate(complex_scene_381)

    complex_scene_382 = Scene()
    complex_scene_382.memo = None
    complex_scene_382.page = 99
    complex_scene_382.type_master = complex_type_master_36
    complex_scene_382 = importer.save_or_locate(complex_scene_382)

    complex_scene_383 = Scene()
    complex_scene_383.memo = None
    complex_scene_383.page = 100
    complex_scene_383.type_master = complex_type_master_36
    complex_scene_383 = importer.save_or_locate(complex_scene_383)

    complex_scene_384 = Scene()
    complex_scene_384.memo = None
    complex_scene_384.page = 104
    complex_scene_384.type_master = complex_type_master_36
    complex_scene_384 = importer.save_or_locate(complex_scene_384)

    complex_scene_385 = Scene()
    complex_scene_385.memo = None
    complex_scene_385.page = 107
    complex_scene_385.type_master = complex_type_master_36
    complex_scene_385 = importer.save_or_locate(complex_scene_385)

    complex_scene_386 = Scene()
    complex_scene_386.memo = None
    complex_scene_386.page = 108
    complex_scene_386.type_master = complex_type_master_36
    complex_scene_386 = importer.save_or_locate(complex_scene_386)

    complex_scene_387 = Scene()
    complex_scene_387.memo = None
    complex_scene_387.page = 112
    complex_scene_387.type_master = complex_type_master_36
    complex_scene_387 = importer.save_or_locate(complex_scene_387)

    complex_scene_388 = Scene()
    complex_scene_388.memo = None
    complex_scene_388.page = 115
    complex_scene_388.type_master = complex_type_master_36
    complex_scene_388 = importer.save_or_locate(complex_scene_388)

    complex_scene_389 = Scene()
    complex_scene_389.memo = None
    complex_scene_389.page = 115
    complex_scene_389.type_master = complex_type_master_36
    complex_scene_389 = importer.save_or_locate(complex_scene_389)

    complex_scene_390 = Scene()
    complex_scene_390.memo = None
    complex_scene_390.page = 116
    complex_scene_390.type_master = complex_type_master_36
    complex_scene_390 = importer.save_or_locate(complex_scene_390)

    complex_scene_391 = Scene()
    complex_scene_391.memo = None
    complex_scene_391.page = 116
    complex_scene_391.type_master = complex_type_master_36
    complex_scene_391 = importer.save_or_locate(complex_scene_391)

    complex_scene_392 = Scene()
    complex_scene_392.memo = None
    complex_scene_392.page = 117
    complex_scene_392.type_master = complex_type_master_36
    complex_scene_392 = importer.save_or_locate(complex_scene_392)

    complex_scene_393 = Scene()
    complex_scene_393.memo = None
    complex_scene_393.page = 119
    complex_scene_393.type_master = complex_type_master_36
    complex_scene_393 = importer.save_or_locate(complex_scene_393)

    complex_scene_394 = Scene()
    complex_scene_394.memo = None
    complex_scene_394.page = 119
    complex_scene_394.type_master = complex_type_master_36
    complex_scene_394 = importer.save_or_locate(complex_scene_394)

    complex_scene_395 = Scene()
    complex_scene_395.memo = None
    complex_scene_395.page = 123
    complex_scene_395.type_master = complex_type_master_36
    complex_scene_395 = importer.save_or_locate(complex_scene_395)

    complex_scene_396 = Scene()
    complex_scene_396.memo = None
    complex_scene_396.page = 125
    complex_scene_396.type_master = complex_type_master_36
    complex_scene_396 = importer.save_or_locate(complex_scene_396)

    complex_scene_397 = Scene()
    complex_scene_397.memo = None
    complex_scene_397.page = 126
    complex_scene_397.type_master = complex_type_master_36
    complex_scene_397 = importer.save_or_locate(complex_scene_397)

    complex_scene_398 = Scene()
    complex_scene_398.memo = None
    complex_scene_398.page = 4
    complex_scene_398.type_master = complex_type_master_36
    complex_scene_398 = importer.save_or_locate(complex_scene_398)

    complex_scene_399 = Scene()
    complex_scene_399.memo = None
    complex_scene_399.page = 5
    complex_scene_399.type_master = complex_type_master_36
    complex_scene_399 = importer.save_or_locate(complex_scene_399)

    complex_scene_400 = Scene()
    complex_scene_400.memo = None
    complex_scene_400.page = 6
    complex_scene_400.type_master = complex_type_master_36
    complex_scene_400 = importer.save_or_locate(complex_scene_400)

    complex_scene_401 = Scene()
    complex_scene_401.memo = None
    complex_scene_401.page = 7
    complex_scene_401.type_master = complex_type_master_36
    complex_scene_401 = importer.save_or_locate(complex_scene_401)

    complex_scene_402 = Scene()
    complex_scene_402.memo = None
    complex_scene_402.page = 7
    complex_scene_402.type_master = complex_type_master_36
    complex_scene_402 = importer.save_or_locate(complex_scene_402)

    complex_scene_403 = Scene()
    complex_scene_403.memo = None
    complex_scene_403.page = 8
    complex_scene_403.type_master = complex_type_master_36
    complex_scene_403 = importer.save_or_locate(complex_scene_403)

    complex_scene_404 = Scene()
    complex_scene_404.memo = None
    complex_scene_404.page = 9
    complex_scene_404.type_master = complex_type_master_36
    complex_scene_404 = importer.save_or_locate(complex_scene_404)

    complex_scene_405 = Scene()
    complex_scene_405.memo = None
    complex_scene_405.page = 10
    complex_scene_405.type_master = complex_type_master_36
    complex_scene_405 = importer.save_or_locate(complex_scene_405)

    complex_scene_406 = Scene()
    complex_scene_406.memo = None
    complex_scene_406.page = 10
    complex_scene_406.type_master = complex_type_master_36
    complex_scene_406 = importer.save_or_locate(complex_scene_406)

    complex_scene_407 = Scene()
    complex_scene_407.memo = None
    complex_scene_407.page = 13
    complex_scene_407.type_master = complex_type_master_36
    complex_scene_407 = importer.save_or_locate(complex_scene_407)

    complex_scene_408 = Scene()
    complex_scene_408.memo = None
    complex_scene_408.page = 13
    complex_scene_408.type_master = complex_type_master_36
    complex_scene_408 = importer.save_or_locate(complex_scene_408)

    complex_scene_409 = Scene()
    complex_scene_409.memo = None
    complex_scene_409.page = 14
    complex_scene_409.type_master = complex_type_master_36
    complex_scene_409 = importer.save_or_locate(complex_scene_409)

    complex_scene_410 = Scene()
    complex_scene_410.memo = None
    complex_scene_410.page = 21
    complex_scene_410.type_master = complex_type_master_36
    complex_scene_410 = importer.save_or_locate(complex_scene_410)

    complex_scene_411 = Scene()
    complex_scene_411.memo = None
    complex_scene_411.page = 23
    complex_scene_411.type_master = complex_type_master_36
    complex_scene_411 = importer.save_or_locate(complex_scene_411)

    complex_scene_412 = Scene()
    complex_scene_412.memo = None
    complex_scene_412.page = 23
    complex_scene_412.type_master = complex_type_master_36
    complex_scene_412 = importer.save_or_locate(complex_scene_412)

    complex_scene_413 = Scene()
    complex_scene_413.memo = None
    complex_scene_413.page = 27
    complex_scene_413.type_master = complex_type_master_36
    complex_scene_413 = importer.save_or_locate(complex_scene_413)

    complex_scene_414 = Scene()
    complex_scene_414.memo = None
    complex_scene_414.page = 28
    complex_scene_414.type_master = complex_type_master_36
    complex_scene_414 = importer.save_or_locate(complex_scene_414)

    complex_scene_415 = Scene()
    complex_scene_415.memo = None
    complex_scene_415.page = 29
    complex_scene_415.type_master = complex_type_master_36
    complex_scene_415 = importer.save_or_locate(complex_scene_415)

    complex_scene_416 = Scene()
    complex_scene_416.memo = None
    complex_scene_416.page = 29
    complex_scene_416.type_master = complex_type_master_36
    complex_scene_416 = importer.save_or_locate(complex_scene_416)

    complex_scene_417 = Scene()
    complex_scene_417.memo = None
    complex_scene_417.page = 29
    complex_scene_417.type_master = complex_type_master_36
    complex_scene_417 = importer.save_or_locate(complex_scene_417)

    complex_scene_418 = Scene()
    complex_scene_418.memo = None
    complex_scene_418.page = 29
    complex_scene_418.type_master = complex_type_master_36
    complex_scene_418 = importer.save_or_locate(complex_scene_418)

    complex_scene_419 = Scene()
    complex_scene_419.memo = None
    complex_scene_419.page = 30
    complex_scene_419.type_master = complex_type_master_36
    complex_scene_419 = importer.save_or_locate(complex_scene_419)

    complex_scene_420 = Scene()
    complex_scene_420.memo = None
    complex_scene_420.page = 35
    complex_scene_420.type_master = complex_type_master_36
    complex_scene_420 = importer.save_or_locate(complex_scene_420)

    complex_scene_421 = Scene()
    complex_scene_421.memo = None
    complex_scene_421.page = 53
    complex_scene_421.type_master = complex_type_master_36
    complex_scene_421 = importer.save_or_locate(complex_scene_421)

    complex_scene_422 = Scene()
    complex_scene_422.memo = None
    complex_scene_422.page = 54
    complex_scene_422.type_master = complex_type_master_36
    complex_scene_422 = importer.save_or_locate(complex_scene_422)

    complex_scene_423 = Scene()
    complex_scene_423.memo = None
    complex_scene_423.page = 56
    complex_scene_423.type_master = complex_type_master_36
    complex_scene_423 = importer.save_or_locate(complex_scene_423)

    complex_scene_424 = Scene()
    complex_scene_424.memo = None
    complex_scene_424.page = 57
    complex_scene_424.type_master = complex_type_master_36
    complex_scene_424 = importer.save_or_locate(complex_scene_424)

    complex_scene_425 = Scene()
    complex_scene_425.memo = None
    complex_scene_425.page = 58
    complex_scene_425.type_master = complex_type_master_36
    complex_scene_425 = importer.save_or_locate(complex_scene_425)

    complex_scene_426 = Scene()
    complex_scene_426.memo = None
    complex_scene_426.page = 59
    complex_scene_426.type_master = complex_type_master_36
    complex_scene_426 = importer.save_or_locate(complex_scene_426)

    complex_scene_427 = Scene()
    complex_scene_427.memo = None
    complex_scene_427.page = 61
    complex_scene_427.type_master = complex_type_master_36
    complex_scene_427 = importer.save_or_locate(complex_scene_427)

    complex_scene_428 = Scene()
    complex_scene_428.memo = None
    complex_scene_428.page = 62
    complex_scene_428.type_master = complex_type_master_36
    complex_scene_428 = importer.save_or_locate(complex_scene_428)

    complex_scene_429 = Scene()
    complex_scene_429.memo = None
    complex_scene_429.page = 63
    complex_scene_429.type_master = complex_type_master_36
    complex_scene_429 = importer.save_or_locate(complex_scene_429)

    complex_scene_430 = Scene()
    complex_scene_430.memo = None
    complex_scene_430.page = 64
    complex_scene_430.type_master = complex_type_master_36
    complex_scene_430 = importer.save_or_locate(complex_scene_430)

    complex_scene_431 = Scene()
    complex_scene_431.memo = None
    complex_scene_431.page = 66
    complex_scene_431.type_master = complex_type_master_36
    complex_scene_431 = importer.save_or_locate(complex_scene_431)

    complex_scene_432 = Scene()
    complex_scene_432.memo = None
    complex_scene_432.page = 67
    complex_scene_432.type_master = complex_type_master_36
    complex_scene_432 = importer.save_or_locate(complex_scene_432)

    complex_scene_433 = Scene()
    complex_scene_433.memo = None
    complex_scene_433.page = 73
    complex_scene_433.type_master = complex_type_master_36
    complex_scene_433 = importer.save_or_locate(complex_scene_433)

    complex_scene_434 = Scene()
    complex_scene_434.memo = None
    complex_scene_434.page = 75
    complex_scene_434.type_master = complex_type_master_36
    complex_scene_434 = importer.save_or_locate(complex_scene_434)

    complex_scene_435 = Scene()
    complex_scene_435.memo = None
    complex_scene_435.page = 78
    complex_scene_435.type_master = complex_type_master_36
    complex_scene_435 = importer.save_or_locate(complex_scene_435)

    complex_scene_436 = Scene()
    complex_scene_436.memo = None
    complex_scene_436.page = 81
    complex_scene_436.type_master = complex_type_master_36
    complex_scene_436 = importer.save_or_locate(complex_scene_436)

    complex_scene_437 = Scene()
    complex_scene_437.memo = None
    complex_scene_437.page = 83
    complex_scene_437.type_master = complex_type_master_36
    complex_scene_437 = importer.save_or_locate(complex_scene_437)

    complex_scene_438 = Scene()
    complex_scene_438.memo = None
    complex_scene_438.page = 83
    complex_scene_438.type_master = complex_type_master_36
    complex_scene_438 = importer.save_or_locate(complex_scene_438)

    complex_scene_439 = Scene()
    complex_scene_439.memo = None
    complex_scene_439.page = 85
    complex_scene_439.type_master = complex_type_master_36
    complex_scene_439 = importer.save_or_locate(complex_scene_439)

    complex_scene_440 = Scene()
    complex_scene_440.memo = None
    complex_scene_440.page = 100
    complex_scene_440.type_master = complex_type_master_36
    complex_scene_440 = importer.save_or_locate(complex_scene_440)

    complex_scene_441 = Scene()
    complex_scene_441.memo = None
    complex_scene_441.page = 101
    complex_scene_441.type_master = complex_type_master_36
    complex_scene_441 = importer.save_or_locate(complex_scene_441)

    complex_scene_442 = Scene()
    complex_scene_442.memo = None
    complex_scene_442.page = 102
    complex_scene_442.type_master = complex_type_master_36
    complex_scene_442 = importer.save_or_locate(complex_scene_442)

    complex_scene_443 = Scene()
    complex_scene_443.memo = None
    complex_scene_443.page = 103
    complex_scene_443.type_master = complex_type_master_36
    complex_scene_443 = importer.save_or_locate(complex_scene_443)

    complex_scene_444 = Scene()
    complex_scene_444.memo = None
    complex_scene_444.page = 104
    complex_scene_444.type_master = complex_type_master_36
    complex_scene_444 = importer.save_or_locate(complex_scene_444)

    complex_scene_445 = Scene()
    complex_scene_445.memo = None
    complex_scene_445.page = 104
    complex_scene_445.type_master = complex_type_master_36
    complex_scene_445 = importer.save_or_locate(complex_scene_445)

    complex_scene_446 = Scene()
    complex_scene_446.memo = None
    complex_scene_446.page = 106
    complex_scene_446.type_master = complex_type_master_36
    complex_scene_446 = importer.save_or_locate(complex_scene_446)

    complex_scene_447 = Scene()
    complex_scene_447.memo = None
    complex_scene_447.page = 106
    complex_scene_447.type_master = complex_type_master_36
    complex_scene_447 = importer.save_or_locate(complex_scene_447)

    complex_scene_448 = Scene()
    complex_scene_448.memo = None
    complex_scene_448.page = 107
    complex_scene_448.type_master = complex_type_master_36
    complex_scene_448 = importer.save_or_locate(complex_scene_448)

    complex_scene_449 = Scene()
    complex_scene_449.memo = None
    complex_scene_449.page = 109
    complex_scene_449.type_master = complex_type_master_36
    complex_scene_449 = importer.save_or_locate(complex_scene_449)

    complex_scene_450 = Scene()
    complex_scene_450.memo = None
    complex_scene_450.page = 109
    complex_scene_450.type_master = complex_type_master_36
    complex_scene_450 = importer.save_or_locate(complex_scene_450)

    complex_scene_451 = Scene()
    complex_scene_451.memo = None
    complex_scene_451.page = 110
    complex_scene_451.type_master = complex_type_master_36
    complex_scene_451 = importer.save_or_locate(complex_scene_451)

    complex_scene_452 = Scene()
    complex_scene_452.memo = None
    complex_scene_452.page = 117
    complex_scene_452.type_master = complex_type_master_36
    complex_scene_452 = importer.save_or_locate(complex_scene_452)

    complex_scene_453 = Scene()
    complex_scene_453.memo = None
    complex_scene_453.page = 118
    complex_scene_453.type_master = complex_type_master_36
    complex_scene_453 = importer.save_or_locate(complex_scene_453)

    complex_scene_454 = Scene()
    complex_scene_454.memo = None
    complex_scene_454.page = 121
    complex_scene_454.type_master = complex_type_master_36
    complex_scene_454 = importer.save_or_locate(complex_scene_454)

    complex_scene_455 = Scene()
    complex_scene_455.memo = None
    complex_scene_455.page = 129
    complex_scene_455.type_master = complex_type_master_36
    complex_scene_455 = importer.save_or_locate(complex_scene_455)

    complex_scene_456 = Scene()
    complex_scene_456.memo = None
    complex_scene_456.page = 149
    complex_scene_456.type_master = complex_type_master_36
    complex_scene_456 = importer.save_or_locate(complex_scene_456)

    complex_scene_457 = Scene()
    complex_scene_457.memo = None
    complex_scene_457.page = 135
    complex_scene_457.type_master = complex_type_master_36
    complex_scene_457 = importer.save_or_locate(complex_scene_457)

    complex_scene_458 = Scene()
    complex_scene_458.memo = None
    complex_scene_458.page = 136
    complex_scene_458.type_master = complex_type_master_36
    complex_scene_458 = importer.save_or_locate(complex_scene_458)

    complex_scene_459 = Scene()
    complex_scene_459.memo = None
    complex_scene_459.page = 144
    complex_scene_459.type_master = complex_type_master_36
    complex_scene_459 = importer.save_or_locate(complex_scene_459)

    complex_scene_460 = Scene()
    complex_scene_460.memo = None
    complex_scene_460.page = 152
    complex_scene_460.type_master = complex_type_master_36
    complex_scene_460 = importer.save_or_locate(complex_scene_460)

    # Processing model: complex.models.Photo

    from complex.models import Photo

    complex_photo_1 = Photo()
    complex_photo_1.height = None
    complex_photo_1.image_src = 'https://live.staticflickr.com/65535/51835163956_cc44f1173a_z.jpg'
    complex_photo_1.link = 'https://www.flickr.com/search/?lat=37.5044771&lon=139.9528276&radius=0.1&has_geo=1&view_all=1'
    complex_photo_1.person = None
    complex_photo_1.title = '飯盛山'
    complex_photo_1.type_master = complex_type_master_23
    complex_photo_1.username = 'Chitaka Chou'
    complex_photo_1.width = None
    complex_photo_1 = importer.save_or_locate(complex_photo_1)

    complex_photo_2 = Photo()
    complex_photo_2.height = None
    complex_photo_2.image_src = 'https://live.staticflickr.com/4803/31152003897_11abafdeff_z.jpg'
    complex_photo_2.link = 'https://www.flickr.com/search/?lat=37.4793359&lon=139.9623918&radius=0.1&has_geo=1&view_all=1'
    complex_photo_2.person = None
    complex_photo_2.title = 'IMGP3716'
    complex_photo_2.type_master = complex_type_master_23
    complex_photo_2.username = 'k_natsumoto'
    complex_photo_2.width = None
    complex_photo_2 = importer.save_or_locate(complex_photo_2)

    complex_photo_3 = Photo()
    complex_photo_3.height = None
    complex_photo_3.image_src = 'https://live.staticflickr.com/4818/46109236232_24119b28d9_z.jpg'
    complex_photo_3.link = 'https://www.flickr.com/search/?lat=37.4781468&lon=139.9632406&radius=0.1&has_geo=1&view_all=1'
    complex_photo_3.person = None
    complex_photo_3.title = 'by @Straylight66'
    complex_photo_3.type_master = complex_type_master_23
    complex_photo_3.username = 'Straylight66'
    complex_photo_3.width = None
    complex_photo_3 = importer.save_or_locate(complex_photo_3)

    complex_photo_4 = Photo()
    complex_photo_4.height = None
    complex_photo_4.image_src = 'https://live.staticflickr.com/4874/44274624730_2d8095c7a6_z.jpg'
    complex_photo_4.link = 'https://www.flickr.com/search/?lat=37.478055&lon=139.9610889&radius=0.1&has_geo=1&view_all=1'
    complex_photo_4.person = None
    complex_photo_4.title = 'IMGP3722'
    complex_photo_4.type_master = complex_type_master_23
    complex_photo_4.username = 'k_natsumoto'
    complex_photo_4.width = None
    complex_photo_4 = importer.save_or_locate(complex_photo_4)

    complex_photo_5 = Photo()
    complex_photo_5.height = None
    complex_photo_5.image_src = 'https://live.staticflickr.com/4896/46090961191_9d830306d8_z.jpg'
    complex_photo_5.link = 'https://www.flickr.com/search/?lat=37.4797004&lon=139.9620807&radius=0.1&has_geo=1&view_all=1'
    complex_photo_5.person = None
    complex_photo_5.title = 'IMGP3717'
    complex_photo_5.type_master = complex_type_master_23
    complex_photo_5.username = 'k_natsumoto'
    complex_photo_5.width = None
    complex_photo_5 = importer.save_or_locate(complex_photo_5)

    complex_photo_6 = Photo()
    complex_photo_6.height = None
    complex_photo_6.image_src = 'https://live.staticflickr.com/65535/51835163816_75137605da_z.jpg'
    complex_photo_6.link = 'https://www.flickr.com/search/?lat=37.5045319&lon=139.9539697&radius=0.1&has_geo=1&view_all=1'
    complex_photo_6.person = None
    complex_photo_6.title = '会津さざえ堂'
    complex_photo_6.type_master = complex_type_master_23
    complex_photo_6.username = 'Chitaka Chou'
    complex_photo_6.width = None
    complex_photo_6 = importer.save_or_locate(complex_photo_6)

    complex_photo_7 = Photo()
    complex_photo_7.height = None
    complex_photo_7.image_src = 'https://live.staticflickr.com/65535/52548463287_f97bda8ce7_z.jpg'
    complex_photo_7.link = 'https://www.flickr.com/search/?lat=38.3685502&lon=141.0593616&radius=0.1&has_geo=1&view_all=1'
    complex_photo_7.person = None
    complex_photo_7.title = 'DSCN8153'
    complex_photo_7.type_master = complex_type_master_23
    complex_photo_7.username = 'JohnSeb'
    complex_photo_7.width = None
    complex_photo_7 = importer.save_or_locate(complex_photo_7)

    complex_photo_8 = Photo()
    complex_photo_8.height = None
    complex_photo_8.image_src = 'https://live.staticflickr.com/65535/51796617235_938863c3ca_z.jpg'
    complex_photo_8.link = 'https://www.flickr.com/search/?lat=38.3661732&lon=141.0611304&radius=0.1&has_geo=1&view_all=1'
    complex_photo_8.person = None
    complex_photo_8.title = 'PXL_20220102_032146625'
    complex_photo_8.type_master = complex_type_master_23
    complex_photo_8.username = 'Masosan'
    complex_photo_8.width = None
    complex_photo_8 = importer.save_or_locate(complex_photo_8)

    complex_photo_9 = Photo()
    complex_photo_9.height = None
    complex_photo_9.image_src = 'https://live.staticflickr.com/65535/51796616390_3e13d59f71_z.jpg'
    complex_photo_9.link = 'https://www.flickr.com/search/?lat=38.3654838&lon=141.0622564&radius=0.1&has_geo=1&view_all=1'
    complex_photo_9.person = None
    complex_photo_9.title = 'PXL_20220102_061948005'
    complex_photo_9.type_master = complex_type_master_23
    complex_photo_9.username = 'Masosan'
    complex_photo_9.width = None
    complex_photo_9 = importer.save_or_locate(complex_photo_9)

    complex_photo_10 = Photo()
    complex_photo_10.height = None
    complex_photo_10.image_src = 'https://live.staticflickr.com/65535/52548924066_71fdbe1d39_z.jpg'
    complex_photo_10.link = 'https://www.flickr.com/search/?lat=38.3685198&lon=141.0595572&radius=0.1&has_geo=1&view_all=1'
    complex_photo_10.person = None
    complex_photo_10.title = 'DSCN8154'
    complex_photo_10.type_master = complex_type_master_23
    complex_photo_10.username = 'JohnSeb'
    complex_photo_10.width = None
    complex_photo_10 = importer.save_or_locate(complex_photo_10)

    complex_photo_11 = Photo()
    complex_photo_11.height = None
    complex_photo_11.image_src = 'https://live.staticflickr.com/65535/52771724119_3ebcccbeee_z.jpg'
    complex_photo_11.link = 'https://www.flickr.com/search/?lat=38.3707103&lon=141.065417&radius=0.1&has_geo=1&view_all=1'
    complex_photo_11.person = None
    complex_photo_11.title = 'Godaido Temple/瑞巌寺五大堂'
    complex_photo_11.type_master = complex_type_master_23
    complex_photo_11.username = 'Seiji Yamanushi'
    complex_photo_11.width = None
    complex_photo_11 = importer.save_or_locate(complex_photo_11)

    complex_photo_12 = Photo()
    complex_photo_12.height = None
    complex_photo_12.image_src = 'https://live.staticflickr.com/65535/51329629559_e041c67712_z.jpg'
    complex_photo_12.link = 'https://www.flickr.com/search/?lat=38.3768196&lon=141.0685577&radius=0.1&has_geo=1&view_all=1'
    complex_photo_12.person = None
    complex_photo_12.title = 'IMG_9476.jpg'
    complex_photo_12.type_master = complex_type_master_23
    complex_photo_12.username = 'fasion'
    complex_photo_12.width = None
    complex_photo_12 = importer.save_or_locate(complex_photo_12)

    complex_photo_13 = Photo()
    complex_photo_13.height = None
    complex_photo_13.image_src = 'https://live.staticflickr.com/65535/52771955393_ea3975ec5a_z.jpg'
    complex_photo_13.link = 'https://www.flickr.com/search/?lat=38.3689558&lon=141.0628948&radius=0.1&has_geo=1&view_all=1'
    complex_photo_13.person = None
    complex_photo_13.title = 'Godaido Temple/瑞巌寺五大堂'
    complex_photo_13.type_master = complex_type_master_23
    complex_photo_13.username = 'Seiji Yamanushi'
    complex_photo_13.width = None
    complex_photo_13 = importer.save_or_locate(complex_photo_13)

    complex_photo_14 = Photo()
    complex_photo_14.height = None
    complex_photo_14.image_src = 'https://live.staticflickr.com/65535/52279475892_d5cf57ab50_z.jpg'
    complex_photo_14.link = 'https://www.flickr.com/search/?lat=38.3719519&lon=141.0651719&radius=0.1&has_geo=1&view_all=1'
    complex_photo_14.person = None
    complex_photo_14.title = '松島梅サイダー'
    complex_photo_14.type_master = complex_type_master_23
    complex_photo_14.username = 'Sulivan Mi'
    complex_photo_14.width = None
    complex_photo_14 = importer.save_or_locate(complex_photo_14)

    complex_photo_15 = Photo()
    complex_photo_15.height = None
    complex_photo_15.image_src = 'https://live.staticflickr.com/65535/51828227348_8827632042_z.jpg'
    complex_photo_15.link = 'https://www.flickr.com/search/?lat=38.3683903&lon=141.0588914&radius=0.1&has_geo=1&view_all=1'
    complex_photo_15.person = None
    complex_photo_15.title = '松島海岸駅'
    complex_photo_15.type_master = complex_type_master_23
    complex_photo_15.username = 'Chitaka Chou'
    complex_photo_15.width = None
    complex_photo_15 = importer.save_or_locate(complex_photo_15)

    complex_photo_16 = Photo()
    complex_photo_16.height = None
    complex_photo_16.image_src = 'https://live.staticflickr.com/65535/51980440037_049efca486_z.jpg'
    complex_photo_16.link = 'https://www.flickr.com/search/?lat=36.8742374&lon=137.4814155&radius=0.1&has_geo=1&view_all=1'
    complex_photo_16.person = None
    complex_photo_16.title = 'D71_0559'
    complex_photo_16.type_master = complex_type_master_23
    complex_photo_16.username = 'Lox Pix'
    complex_photo_16.width = None
    complex_photo_16 = importer.save_or_locate(complex_photo_16)

    complex_photo_17 = Photo()
    complex_photo_17.height = None
    complex_photo_17.image_src = 'https://live.staticflickr.com/8007/6971134834_dfb93c105f_z.jpg'
    complex_photo_17.link = 'https://www.flickr.com/search/?lat=36.873683&lon=137.46587&radius=0.1&has_geo=1&view_all=1'
    complex_photo_17.person = None
    complex_photo_17.title = 'SA197449'
    complex_photo_17.type_master = complex_type_master_23
    complex_photo_17.username = 'sheldon0531'
    complex_photo_17.width = None
    complex_photo_17 = importer.save_or_locate(complex_photo_17)

    complex_photo_18 = Photo()
    complex_photo_18.height = None
    complex_photo_18.image_src = 'https://live.staticflickr.com/4554/38146209202_9844d8b073_z.jpg'
    complex_photo_18.link = 'https://www.flickr.com/search/?lat=36.8911258&lon=137.4188529&radius=0.1&has_geo=1&view_all=1'
    complex_photo_18.person = None
    complex_photo_18.title = 'Road Station Ikuji'
    complex_photo_18.type_master = complex_type_master_23
    complex_photo_18.username = 'mega_midget_racer'
    complex_photo_18.width = None
    complex_photo_18 = importer.save_or_locate(complex_photo_18)

    complex_photo_19 = Photo()
    complex_photo_19.height = None
    complex_photo_19.image_src = 'https://live.staticflickr.com/5824/21162919958_c82649f15e_z.jpg'
    complex_photo_19.link = 'https://www.flickr.com/search/?lat=36.8906968&lon=137.4170608&radius=0.1&has_geo=1&view_all=1'
    complex_photo_19.person = None
    complex_photo_19.title = '_DSC2836_DxO'
    complex_photo_19.type_master = complex_type_master_23
    complex_photo_19.username = 'ywakimoto'
    complex_photo_19.width = None
    complex_photo_19 = importer.save_or_locate(complex_photo_19)

    complex_photo_20 = Photo()
    complex_photo_20.height = None
    complex_photo_20.image_src = 'https://live.staticflickr.com/7839/33259767668_b52cd415d5_z.jpg'
    complex_photo_20.link = 'https://www.flickr.com/search/?lat=36.8731542&lon=137.4809156&radius=0.1&has_geo=1&view_all=1'
    complex_photo_20.person = None
    complex_photo_20.title = 'IMG_0107'
    complex_photo_20.type_master = complex_type_master_23
    complex_photo_20.username = 'tokokapo'
    complex_photo_20.width = None
    complex_photo_20 = importer.save_or_locate(complex_photo_20)

    complex_photo_21 = Photo()
    complex_photo_21.height = None
    complex_photo_21.image_src = 'https://live.staticflickr.com/65535/51113923082_d12ccb0951_z.jpg'
    complex_photo_21.link = 'https://www.flickr.com/search/?lat=36.8157746&lon=137.5836311&radius=0.1&has_geo=1&view_all=1'
    complex_photo_21.person = None
    complex_photo_21.title = 'IMG_9227'
    complex_photo_21.type_master = complex_type_master_23
    complex_photo_21.username = 'OOMYV'
    complex_photo_21.width = None
    complex_photo_21 = importer.save_or_locate(complex_photo_21)

    complex_photo_22 = Photo()
    complex_photo_22.height = None
    complex_photo_22.image_src = 'https://live.staticflickr.com/65535/51116169380_d45806f4be_z.jpg'
    complex_photo_22.link = 'https://www.flickr.com/search/?lat=36.8157762&lon=137.5826756&radius=0.1&has_geo=1&view_all=1'
    complex_photo_22.person = None
    complex_photo_22.title = '宇奈月谷'
    complex_photo_22.type_master = complex_type_master_23
    complex_photo_22.username = 'yuki_alm_misa'
    complex_photo_22.width = None
    complex_photo_22 = importer.save_or_locate(complex_photo_22)

    complex_photo_23 = Photo()
    complex_photo_23.height = None
    complex_photo_23.image_src = 'https://live.staticflickr.com/4553/24483665478_ee30f942cf_z.jpg'
    complex_photo_23.link = 'https://www.flickr.com/search/?lat=36.8126191&lon=137.5900726&radius=0.1&has_geo=1&view_all=1'
    complex_photo_23.person = None
    complex_photo_23.title = 'Run through autumn mountains'
    complex_photo_23.type_master = complex_type_master_23
    complex_photo_23.username = 'Teruhide Tomori'
    complex_photo_23.width = None
    complex_photo_23 = importer.save_or_locate(complex_photo_23)

    complex_photo_24 = Photo()
    complex_photo_24.height = None
    complex_photo_24.image_src = 'https://live.staticflickr.com/65535/52167738675_4f92320eea_z.jpg'
    complex_photo_24.link = 'https://www.flickr.com/search/?lat=36.8150247&lon=137.5859364&radius=0.1&has_geo=1&view_all=1'
    complex_photo_24.person = None
    complex_photo_24.title = '宇奈月'
    complex_photo_24.type_master = complex_type_master_23
    complex_photo_24.username = 'Chitaka Chou'
    complex_photo_24.width = None
    complex_photo_24 = importer.save_or_locate(complex_photo_24)

    complex_photo_25 = Photo()
    complex_photo_25.height = None
    complex_photo_25.image_src = 'https://live.staticflickr.com/65535/50951287223_bbe270992c_z.jpg'
    complex_photo_25.link = 'https://www.flickr.com/search/?lat=36.8142871&lon=137.5881562&radius=0.1&has_geo=1&view_all=1'
    complex_photo_25.person = None
    complex_photo_25.title = '610_7136'
    complex_photo_25.type_master = complex_type_master_23
    complex_photo_25.username = 'Lox Pix'
    complex_photo_25.width = None
    complex_photo_25 = importer.save_or_locate(complex_photo_25)

    complex_photo_26 = Photo()
    complex_photo_26.height = None
    complex_photo_26.image_src = 'https://live.staticflickr.com/4485/37467599514_17012cfd8b_z.jpg'
    complex_photo_26.link = 'https://www.flickr.com/search/?lat=36.8913149&lon=137.4184784&radius=0.1&has_geo=1&view_all=1'
    complex_photo_26.person = None
    complex_photo_26.title = 'Road Station Ikuji'
    complex_photo_26.type_master = complex_type_master_23
    complex_photo_26.username = 'mega_midget_racer'
    complex_photo_26.width = None
    complex_photo_26 = importer.save_or_locate(complex_photo_26)

    complex_photo_27 = Photo()
    complex_photo_27.height = None
    complex_photo_27.image_src = 'https://live.staticflickr.com/715/21694861128_40dc0f9dc7_z.jpg'
    complex_photo_27.link = 'https://www.flickr.com/search/?lat=34.3446375&lon=134.122008&radius=0.1&has_geo=1&view_all=1'
    complex_photo_27.person = None
    complex_photo_27.title = '帰り道の電車'
    complex_photo_27.type_master = complex_type_master_23
    complex_photo_27.username = '風の色写真館（讃岐東部の写真集）'
    complex_photo_27.width = None
    complex_photo_27 = importer.save_or_locate(complex_photo_27)

    complex_photo_28 = Photo()
    complex_photo_28.height = None
    complex_photo_28.image_src = 'https://live.staticflickr.com/5149/5677062182_4de4f91ac1_z.jpg'
    complex_photo_28.link = 'https://www.flickr.com/search/?lat=34.345598&lon=134.1223194&radius=0.1&has_geo=1&view_all=1'
    complex_photo_28.person = None
    complex_photo_28.title = 'DSC05066.JPG'
    complex_photo_28.type_master = complex_type_master_23
    complex_photo_28.username = 't.nanba'
    complex_photo_28.width = None
    complex_photo_28 = importer.save_or_locate(complex_photo_28)

    complex_photo_29 = Photo()
    complex_photo_29.height = None
    complex_photo_29.image_src = 'https://live.staticflickr.com/5188/5676949884_00e9b299c8_z.jpg'
    complex_photo_29.link = 'https://www.flickr.com/search/?lat=34.3551328&lon=134.1336543&radius=0.1&has_geo=1&view_all=1'
    complex_photo_29.person = None
    complex_photo_29.title = 'DSC05055.JPG'
    complex_photo_29.type_master = complex_type_master_23
    complex_photo_29.username = 't.nanba'
    complex_photo_29.width = None
    complex_photo_29 = importer.save_or_locate(complex_photo_29)

    complex_photo_30 = Photo()
    complex_photo_30.height = None
    complex_photo_30.image_src = 'https://live.staticflickr.com/65535/48951825247_d8e3c3fc3f_z.jpg'
    complex_photo_30.link = 'https://www.flickr.com/search/?lat=34.3599067&lon=134.1398791&radius=0.1&has_geo=1&view_all=1'
    complex_photo_30.person = None
    complex_photo_30.title = 'Yakuri-ji, the 85th Temple of the Sacred Shikoku Pilgrimage in Kagawa, Japan.'
    complex_photo_30.type_master = complex_type_master_23
    complex_photo_30.username = 'KyotoDreamTrips'
    complex_photo_30.width = None
    complex_photo_30 = importer.save_or_locate(complex_photo_30)

    complex_photo_31 = Photo()
    complex_photo_31.height = None
    complex_photo_31.image_src = 'https://live.staticflickr.com/65535/52203607929_7a82e71d51_z.jpg'
    complex_photo_31.link = 'https://www.flickr.com/search/?lat=34.3497929&lon=134.0469322&radius=0.1&has_geo=1&view_all=1'
    complex_photo_31.person = None
    complex_photo_31.title = 'MarinLiner TakamatsuStation'
    complex_photo_31.type_master = complex_type_master_23
    complex_photo_31.username = 'kirin723'
    complex_photo_31.width = None
    complex_photo_31 = importer.save_or_locate(complex_photo_31)

    complex_photo_32 = Photo()
    complex_photo_32.height = None
    complex_photo_32.image_src = 'https://live.staticflickr.com/65535/52671704441_5b270ca75e_z.jpg'
    complex_photo_32.link = 'https://www.flickr.com/search/?lat=34.3503157&lon=134.0516188&radius=0.1&has_geo=1&view_all=1'
    complex_photo_32.person = None
    complex_photo_32.title = 'Takamatsu-02254'
    complex_photo_32.type_master = complex_type_master_23
    complex_photo_32.username = 'xiquinhosilva'
    complex_photo_32.width = None
    complex_photo_32 = importer.save_or_locate(complex_photo_32)

    complex_photo_33 = Photo()
    complex_photo_33.height = None
    complex_photo_33.image_src = 'https://live.staticflickr.com/65535/50115002776_30c119f009_z.jpg'
    complex_photo_33.link = 'https://www.flickr.com/search/?lat=34.9351213&lon=135.7624568&radius=0.1&has_geo=1&view_all=1'
    complex_photo_33.person = None
    complex_photo_33.title = '珍遊のラーメン'
    complex_photo_33.type_master = complex_type_master_23
    complex_photo_33.username = 'albertus'
    complex_photo_33.width = None
    complex_photo_33 = importer.save_or_locate(complex_photo_33)

    complex_photo_34 = Photo()
    complex_photo_34.height = None
    complex_photo_34.image_src = 'https://live.staticflickr.com/65535/52773794779_307f11239b_z.jpg'
    complex_photo_34.link = 'https://www.flickr.com/search/?lat=34.929136&lon=135.76161&radius=0.1&has_geo=1&view_all=1'
    complex_photo_34.person = None
    complex_photo_34.title = 'Cherry Blossoms Along the Benten Bridge in Fushimi-Ku, Kyoto City-Japan.'
    complex_photo_34.type_master = complex_type_master_23
    complex_photo_34.username = 'KyotoDreamTrips'
    complex_photo_34.width = None
    complex_photo_34 = importer.save_or_locate(complex_photo_34)

    complex_photo_35 = Photo()
    complex_photo_35.height = None
    complex_photo_35.image_src = 'https://live.staticflickr.com/65535/52710428465_30e88a8d65_z.jpg'
    complex_photo_35.link = 'https://www.flickr.com/search/?lat=34.968596&lon=135.768613&radius=0.1&has_geo=1&view_all=1'
    complex_photo_35.person = None
    complex_photo_35.title = '20230126_0126_155235'
    complex_photo_35.type_master = complex_type_master_23
    complex_photo_35.username = 'garychio'
    complex_photo_35.width = None
    complex_photo_35 = importer.save_or_locate(complex_photo_35)

    complex_photo_36 = Photo()
    complex_photo_36.height = None
    complex_photo_36.image_src = 'https://live.staticflickr.com/65535/52658040795_4d9028f3a3_z.jpg'
    complex_photo_36.link = 'https://www.flickr.com/search/?lat=34.9687541&lon=135.7692088&radius=0.1&has_geo=1&view_all=1'
    complex_photo_36.person = None
    complex_photo_36.title = 'by @My Life | my flickr'
    complex_photo_36.type_master = complex_type_master_23
    complex_photo_36.username = 'My Life | my flickr'
    complex_photo_36.width = None
    complex_photo_36 = importer.save_or_locate(complex_photo_36)

    complex_photo_37 = Photo()
    complex_photo_37.height = None
    complex_photo_37.image_src = 'https://live.staticflickr.com/65535/52735273136_58184b10c3_z.jpg'
    complex_photo_37.link = 'https://www.flickr.com/search/?lat=35.5344188&lon=135.1997513&radius=0.1&has_geo=1&view_all=1'
    complex_photo_37.person = None
    complex_photo_37.title = '20221222天橋立'
    complex_photo_37.type_master = complex_type_master_23
    complex_photo_37.username = 'trlintw'
    complex_photo_37.width = None
    complex_photo_37 = importer.save_or_locate(complex_photo_37)

    complex_photo_38 = Photo()
    complex_photo_38.height = None
    complex_photo_38.image_src = 'https://live.staticflickr.com/65535/52629084942_4b13845481_z.jpg'
    complex_photo_38.link = 'https://www.flickr.com/search/?lat=35.534848&lon=135.1992613&radius=0.1&has_geo=1&view_all=1'
    complex_photo_38.person = None
    complex_photo_38.title = 'Miyazu, Kyoto'
    complex_photo_38.type_master = complex_type_master_23
    complex_photo_38.username = 'Kzaral'
    complex_photo_38.width = None
    complex_photo_38 = importer.save_or_locate(complex_photo_38)

    complex_photo_39 = Photo()
    complex_photo_39.height = None
    complex_photo_39.image_src = 'https://live.staticflickr.com/4355/36851438382_019ded72b3_z.jpg'
    complex_photo_39.link = 'https://www.flickr.com/search/?lat=35.5368405&lon=135.1918306&radius=0.1&has_geo=1&view_all=1'
    complex_photo_39.person = None
    complex_photo_39.title = 'Miyazu#27'
    complex_photo_39.type_master = complex_type_master_23
    complex_photo_39.username = 'tetsuo5'
    complex_photo_39.width = None
    complex_photo_39 = importer.save_or_locate(complex_photo_39)

    complex_photo_40 = Photo()
    complex_photo_40.height = None
    complex_photo_40.image_src = 'https://live.staticflickr.com/65535/52629850914_79a597a00a_z.jpg'
    complex_photo_40.link = 'https://www.flickr.com/search/?lat=35.5557202&lon=135.1839285&radius=0.1&has_geo=1&view_all=1'
    complex_photo_40.person = None
    complex_photo_40.title = 'Miyazu, Kyoto'
    complex_photo_40.type_master = complex_type_master_23
    complex_photo_40.username = 'Kzaral'
    complex_photo_40.width = None
    complex_photo_40 = importer.save_or_locate(complex_photo_40)

    complex_photo_41 = Photo()
    complex_photo_41.height = None
    complex_photo_41.image_src = 'https://live.staticflickr.com/65535/52630500321_fea3dcd59e_z.jpg'
    complex_photo_41.link = 'https://www.flickr.com/search/?lat=35.5527779&lon=135.1821171&radius=0.1&has_geo=1&view_all=1'
    complex_photo_41.person = None
    complex_photo_41.title = 'Amanohashidate'
    complex_photo_41.type_master = complex_type_master_23
    complex_photo_41.username = 'tenfast'
    complex_photo_41.width = None
    complex_photo_41 = importer.save_or_locate(complex_photo_41)

    complex_photo_42 = Photo()
    complex_photo_42.height = None
    complex_photo_42.image_src = 'https://live.staticflickr.com/65535/52735530259_a16d47f7a8_z.jpg'
    complex_photo_42.link = 'https://www.flickr.com/search/?lat=35.5698022&lon=135.1918204&radius=0.1&has_geo=1&view_all=1'
    complex_photo_42.person = None
    complex_photo_42.title = '20221222天橋立'
    complex_photo_42.type_master = complex_type_master_23
    complex_photo_42.username = 'trlintw'
    complex_photo_42.width = None
    complex_photo_42 = importer.save_or_locate(complex_photo_42)

    complex_photo_43 = Photo()
    complex_photo_43.height = None
    complex_photo_43.image_src = 'https://live.staticflickr.com/65535/49332254667_d3dfc78c3e_z.jpg'
    complex_photo_43.link = 'https://www.flickr.com/search/?lat=35.5628724&lon=135.1881478&radius=0.1&has_geo=1&view_all=1'
    complex_photo_43.person = None
    complex_photo_43.title = 'P1039247'
    complex_photo_43.type_master = complex_type_master_23
    complex_photo_43.username = 'MakotoUmeda'
    complex_photo_43.width = None
    complex_photo_43 = importer.save_or_locate(complex_photo_43)

    complex_photo_44 = Photo()
    complex_photo_44.height = None
    complex_photo_44.image_src = 'https://live.staticflickr.com/65535/52735593894_7c431c206d_z.jpg'
    complex_photo_44.link = 'https://www.flickr.com/search/?lat=35.5827837&lon=135.1967015&radius=0.1&has_geo=1&view_all=1'
    complex_photo_44.person = None
    complex_photo_44.title = '20221222天橋立'
    complex_photo_44.type_master = complex_type_master_23
    complex_photo_44.username = 'trlintw'
    complex_photo_44.width = None
    complex_photo_44 = importer.save_or_locate(complex_photo_44)

    complex_photo_45 = Photo()
    complex_photo_45.height = None
    complex_photo_45.image_src = 'https://live.staticflickr.com/65535/49332032556_d1a03f0566_z.jpg'
    complex_photo_45.link = 'https://www.flickr.com/search/?lat=35.5634066&lon=135.1879155&radius=0.1&has_geo=1&view_all=1'
    complex_photo_45.person = None
    complex_photo_45.title = 'P1039248'
    complex_photo_45.type_master = complex_type_master_23
    complex_photo_45.username = 'MakotoUmeda'
    complex_photo_45.width = None
    complex_photo_45 = importer.save_or_locate(complex_photo_45)

    complex_photo_46 = Photo()
    complex_photo_46.height = None
    complex_photo_46.image_src = 'https://live.staticflickr.com/3782/13777277115_35530cd29f_z.jpg'
    complex_photo_46.link = 'https://www.flickr.com/search/?lat=36.6485846&lon=140.1381941&radius=0.1&has_geo=1&view_all=1'
    complex_photo_46.person = None
    complex_photo_46.title = 'P4060209'
    complex_photo_46.type_master = complex_type_master_23
    complex_photo_46.username = 'mr_nihei'
    complex_photo_46.width = None
    complex_photo_46 = importer.save_or_locate(complex_photo_46)

    complex_photo_47 = Photo()
    complex_photo_47.height = None
    complex_photo_47.image_src = 'https://live.staticflickr.com/1787/42202655254_803d0b147f_z.jpg'
    complex_photo_47.link = 'https://www.flickr.com/search/?lat=36.6455986&lon=140.1398144&radius=0.1&has_geo=1&view_all=1'
    complex_photo_47.person = None
    complex_photo_47.title = '龍門の滝'
    complex_photo_47.type_master = complex_type_master_23
    complex_photo_47.username = 'cyberwonk'
    complex_photo_47.width = None
    complex_photo_47 = importer.save_or_locate(complex_photo_47)

    complex_photo_48 = Photo()
    complex_photo_48.height = None
    complex_photo_48.image_src = 'https://live.staticflickr.com/899/28052432717_2dd7ab01d2_z.jpg'
    complex_photo_48.link = 'https://www.flickr.com/search/?lat=36.6455502&lon=140.1389247&radius=0.1&has_geo=1&view_all=1'
    complex_photo_48.person = None
    complex_photo_48.title = '那須烏山の町の鳥'
    complex_photo_48.type_master = complex_type_master_23
    complex_photo_48.username = 'cyberwonk'
    complex_photo_48.width = None
    complex_photo_48 = importer.save_or_locate(complex_photo_48)

    complex_photo_49 = Photo()
    complex_photo_49.height = None
    complex_photo_49.image_src = 'https://live.staticflickr.com/65535/52480403172_6aab3e1cc8_z.jpg'
    complex_photo_49.link = 'https://www.flickr.com/search/?lat=36.65687&lon=140.1381&radius=0.1&has_geo=1&view_all=1'
    complex_photo_49.person = None
    complex_photo_49.title = 'DSC01838'
    complex_photo_49.type_master = complex_type_master_23
    complex_photo_49.username = 'shaderjp'
    complex_photo_49.width = None
    complex_photo_49 = importer.save_or_locate(complex_photo_49)

    complex_photo_50 = Photo()
    complex_photo_50.height = None
    complex_photo_50.image_src = 'https://live.staticflickr.com/4814/44985821574_86d5da260f_z.jpg'
    complex_photo_50.link = 'https://www.flickr.com/search/?lat=36.6557618&lon=140.1536827&radius=0.1&has_geo=1&view_all=1'
    complex_photo_50.person = None
    complex_photo_50.title = '栃木県那須烏山市（旧烏山町）'
    complex_photo_50.type_master = complex_type_master_23
    complex_photo_50.username = 'hiro.dir'
    complex_photo_50.width = None
    complex_photo_50 = importer.save_or_locate(complex_photo_50)

    complex_photo_51 = Photo()
    complex_photo_51.height = None
    complex_photo_51.image_src = 'https://live.staticflickr.com/3798/32769801943_d6fcc95e44_z.jpg'
    complex_photo_51.link = 'https://www.flickr.com/search/?lat=36.650852&lon=140.154528&radius=0.1&has_geo=1&view_all=1'
    complex_photo_51.person = None
    complex_photo_51.title = 'いぃぶいいぃ～( ´∀｀)'
    complex_photo_51.type_master = complex_type_master_23
    complex_photo_51.username = 'fox_kawai'
    complex_photo_51.width = None
    complex_photo_51 = importer.save_or_locate(complex_photo_51)

    complex_photo_52 = Photo()
    complex_photo_52.height = None
    complex_photo_52.image_src = 'https://live.staticflickr.com/1481/23651334020_3cc9312bbf_z.jpg'
    complex_photo_52.link = 'https://www.flickr.com/search/?lat=38.4674427&lon=139.2549057&radius=0.1&has_geo=1&view_all=1'
    complex_photo_52.person = None
    complex_photo_52.title = '粟島'
    complex_photo_52.type_master = complex_type_master_23
    complex_photo_52.username = 'GenJapan1986'
    complex_photo_52.width = None
    complex_photo_52 = importer.save_or_locate(complex_photo_52)

    complex_photo_53 = Photo()
    complex_photo_53.height = None
    complex_photo_53.image_src = 'https://live.staticflickr.com/1523/23318769184_5524d4c000_z.jpg'
    complex_photo_53.link = 'https://www.flickr.com/search/?lat=38.4650772&lon=139.2530973&radius=0.1&has_geo=1&view_all=1'
    complex_photo_53.person = None
    complex_photo_53.title = '粟島'
    complex_photo_53.type_master = complex_type_master_23
    complex_photo_53.username = 'GenJapan1986'
    complex_photo_53.width = None
    complex_photo_53 = importer.save_or_locate(complex_photo_53)

    complex_photo_54 = Photo()
    complex_photo_54.height = None
    complex_photo_54.image_src = 'https://live.staticflickr.com/1470/23864490871_61e7b5f642_z.jpg'
    complex_photo_54.link = 'https://www.flickr.com/search/?lat=38.4687521&lon=139.2549858&radius=0.1&has_geo=1&view_all=1'
    complex_photo_54.person = None
    complex_photo_54.title = '粟島'
    complex_photo_54.type_master = complex_type_master_23
    complex_photo_54.username = 'GenJapan1986'
    complex_photo_54.width = None
    complex_photo_54 = importer.save_or_locate(complex_photo_54)

    complex_photo_55 = Photo()
    complex_photo_55.height = None
    complex_photo_55.image_src = 'https://live.staticflickr.com/7717/26464983984_b5026142f6_z.jpg'
    complex_photo_55.link = 'https://www.flickr.com/search/?lat=34.8308664&lon=136.592541&radius=0.1&has_geo=1&view_all=1'
    complex_photo_55.person = None
    complex_photo_55.title = '白子漁港'
    complex_photo_55.type_master = complex_type_master_23
    complex_photo_55.username = 'Shigelli'
    complex_photo_55.width = None
    complex_photo_55 = importer.save_or_locate(complex_photo_55)

    complex_photo_56 = Photo()
    complex_photo_56.height = None
    complex_photo_56.image_src = 'https://live.staticflickr.com/5672/30207698280_03668ae265_z.jpg'
    complex_photo_56.link = 'https://www.flickr.com/search/?lat=34.8277194&lon=136.5919642&radius=0.1&has_geo=1&view_all=1'
    complex_photo_56.person = None
    complex_photo_56.title = '白子漁港'
    complex_photo_56.type_master = complex_type_master_23
    complex_photo_56.username = 'Shigelli'
    complex_photo_56.width = None
    complex_photo_56 = importer.save_or_locate(complex_photo_56)

    complex_photo_57 = Photo()
    complex_photo_57.height = None
    complex_photo_57.image_src = 'https://live.staticflickr.com/65535/52725208823_a50d1c0756_z.jpg'
    complex_photo_57.link = 'https://www.flickr.com/search/?lat=34.4892923&lon=136.7079545&radius=0.1&has_geo=1&view_all=1'
    complex_photo_57.person = None
    complex_photo_57.title = 'Trading stocks and trading in cultural meanings, too'
    complex_photo_57.type_master = complex_type_master_23
    complex_photo_57.username = 'anthroview'
    complex_photo_57.width = None
    complex_photo_57 = importer.save_or_locate(complex_photo_57)

    complex_photo_58 = Photo()
    complex_photo_58.height = None
    complex_photo_58.image_src = 'https://live.staticflickr.com/65535/52724905874_cc1632227b_z.jpg'
    complex_photo_58.link = 'https://www.flickr.com/search/?lat=34.4885003&lon=136.7070889&radius=0.1&has_geo=1&view_all=1'
    complex_photo_58.person = None
    complex_photo_58.title = 'Text, "Caring for your assets for the ages"'
    complex_photo_58.type_master = complex_type_master_23
    complex_photo_58.username = 'burabura aruku'
    complex_photo_58.width = None
    complex_photo_58 = importer.save_or_locate(complex_photo_58)

    complex_photo_59 = Photo()
    complex_photo_59.height = None
    complex_photo_59.image_src = 'https://live.staticflickr.com/65535/52725208788_e9b5679be6_z.jpg'
    complex_photo_59.link = 'https://www.flickr.com/search/?lat=34.4871537&lon=136.7029233&radius=0.1&has_geo=1&view_all=1'
    complex_photo_59.person = None
    complex_photo_59.title = 'The religious culture built up by people pales to the wonder of living things'
    complex_photo_59.type_master = complex_type_master_23
    complex_photo_59.username = 'anthroview'
    complex_photo_59.width = None
    complex_photo_59 = importer.save_or_locate(complex_photo_59)

    complex_photo_60 = Photo()
    complex_photo_60.height = None
    complex_photo_60.image_src = 'https://live.staticflickr.com/65535/52707188706_041e74dfd0_z.jpg'
    complex_photo_60.link = 'https://www.flickr.com/search/?lat=34.4595551&lon=136.7230903&radius=0.1&has_geo=1&view_all=1'
    complex_photo_60.person = None
    complex_photo_60.title = 'Pilgrims pay their respects, decade after decade'
    complex_photo_60.type_master = complex_type_master_23
    complex_photo_60.username = 'anthroview'
    complex_photo_60.width = None
    complex_photo_60 = importer.save_or_locate(complex_photo_60)

    complex_photo_61 = Photo()
    complex_photo_61.height = None
    complex_photo_61.image_src = 'https://live.staticflickr.com/65535/51853952421_549c536b81_z.jpg'
    complex_photo_61.link = 'https://www.flickr.com/search/?lat=34.4853698&lon=136.8444576&radius=0.1&has_geo=1&view_all=1'
    complex_photo_61.person = None
    complex_photo_61.title = 'Mikimoto, Toba, Japan, 1968'
    complex_photo_61.type_master = complex_type_master_23
    complex_photo_61.username = 'east med wanderer'
    complex_photo_61.width = None
    complex_photo_61 = importer.save_or_locate(complex_photo_61)

    complex_photo_62 = Photo()
    complex_photo_62.height = None
    complex_photo_62.image_src = 'https://live.staticflickr.com/4813/47025883411_c9260089dc_z.jpg'
    complex_photo_62.link = 'https://www.flickr.com/search/?lat=34.4847431&lon=136.8439619&radius=0.1&has_geo=1&view_all=1'
    complex_photo_62.person = None
    complex_photo_62.title = 'IMG_0153'
    complex_photo_62.type_master = complex_type_master_23
    complex_photo_62.username = 'masa.nagano'
    complex_photo_62.width = None
    complex_photo_62 = importer.save_or_locate(complex_photo_62)

    complex_photo_63 = Photo()
    complex_photo_63.height = None
    complex_photo_63.image_src = 'https://live.staticflickr.com/852/29822877858_d799723e4d_z.jpg'
    complex_photo_63.link = 'https://www.flickr.com/search/?lat=34.5039814&lon=136.7770851&radius=0.1&has_geo=1&view_all=1'
    complex_photo_63.person = None
    complex_photo_63.title = 'ise_20180209150847'
    complex_photo_63.type_master = complex_type_master_23
    complex_photo_63.username = 'inunami'
    complex_photo_63.width = None
    complex_photo_63 = importer.save_or_locate(complex_photo_63)

    complex_photo_64 = Photo()
    complex_photo_64.height = None
    complex_photo_64.image_src = 'https://live.staticflickr.com/65535/50636333798_8194d9920b_z.jpg'
    complex_photo_64.link = 'https://www.flickr.com/search/?lat=34.5073078&lon=136.7777824&radius=0.1&has_geo=1&view_all=1'
    complex_photo_64.person = None
    complex_photo_64.title = '20201122_いい夫婦旅_167'
    complex_photo_64.type_master = complex_type_master_23
    complex_photo_64.username = 'jinmsk'
    complex_photo_64.width = None
    complex_photo_64 = importer.save_or_locate(complex_photo_64)

    complex_photo_65 = Photo()
    complex_photo_65.height = None
    complex_photo_65.image_src = 'https://live.staticflickr.com/65535/52725209298_c6c2a12dbb_z.jpg'
    complex_photo_65.link = 'https://www.flickr.com/search/?lat=34.4862757&lon=136.7073159&radius=0.1&has_geo=1&view_all=1'
    complex_photo_65.person = None
    complex_photo_65.title = "Ise Jingu's Sengu-kan hosts this Irish music ensemble"
    complex_photo_65.type_master = complex_type_master_23
    complex_photo_65.username = 'anthroview'
    complex_photo_65.width = None
    complex_photo_65 = importer.save_or_locate(complex_photo_65)

    complex_photo_66 = Photo()
    complex_photo_66.height = None
    complex_photo_66.image_src = 'https://live.staticflickr.com/65535/52774017692_54a9628830_z.jpg'
    complex_photo_66.link = 'https://www.flickr.com/search/?lat=35.7036666&lon=139.7533928&radius=0.1&has_geo=1&view_all=1'
    complex_photo_66.person = None
    complex_photo_66.title = '2023-02-24 10.56.56'
    complex_photo_66.type_master = complex_type_master_23
    complex_photo_66.username = 'Just Spooky'
    complex_photo_66.width = None
    complex_photo_66 = importer.save_or_locate(complex_photo_66)

    complex_photo_67 = Photo()
    complex_photo_67.height = None
    complex_photo_67.image_src = 'https://live.staticflickr.com/65535/51621626564_04973ecfd5_z.jpg'
    complex_photo_67.link = 'https://www.flickr.com/search/?lat=34.3999238&lon=132.4758202&radius=0.1&has_geo=1&view_all=1'
    complex_photo_67.person = None
    complex_photo_67.title = 'DSCN4234'
    complex_photo_67.type_master = complex_type_master_23
    complex_photo_67.username = 'Matt-The Mechanic'
    complex_photo_67.width = None
    complex_photo_67 = importer.save_or_locate(complex_photo_67)

    complex_photo_68 = Photo()
    complex_photo_68.height = None
    complex_photo_68.image_src = 'https://live.staticflickr.com/65535/51373328993_57f2969684_z.jpg'
    complex_photo_68.link = 'https://www.flickr.com/search/?lat=34.311502&lon=132.3035106&radius=0.1&has_geo=1&view_all=1'
    complex_photo_68.person = None
    complex_photo_68.title = 'IMG_3840'
    complex_photo_68.type_master = complex_type_master_23
    complex_photo_68.username = 'ylefou2004'
    complex_photo_68.width = None
    complex_photo_68 = importer.save_or_locate(complex_photo_68)

    complex_photo_69 = Photo()
    complex_photo_69.height = None
    complex_photo_69.image_src = 'https://live.staticflickr.com/65535/52706655853_5ec9d10b3c_z.jpg'
    complex_photo_69.link = 'https://www.flickr.com/search/?lat=34.3020862&lon=132.3222151&radius=0.1&has_geo=1&view_all=1'
    complex_photo_69.person = None
    complex_photo_69.title = 'Deer on Miyajima'
    complex_photo_69.type_master = complex_type_master_23
    complex_photo_69.username = 'dean.white'
    complex_photo_69.width = None
    complex_photo_69 = importer.save_or_locate(complex_photo_69)

    complex_photo_70 = Photo()
    complex_photo_70.height = None
    complex_photo_70.image_src = 'https://live.staticflickr.com/65535/52748275910_228fd8b17e_z.jpg'
    complex_photo_70.link = 'https://www.flickr.com/search/?lat=34.2973092&lon=132.3181276&radius=0.1&has_geo=1&view_all=1'
    complex_photo_70.person = None
    complex_photo_70.title = 'PDV_1730.jpg'
    complex_photo_70.type_master = complex_type_master_23
    complex_photo_70.username = 'patrickdevries2003'
    complex_photo_70.width = None
    complex_photo_70 = importer.save_or_locate(complex_photo_70)

    complex_photo_71 = Photo()
    complex_photo_71.height = None
    complex_photo_71.image_src = 'https://live.staticflickr.com/65535/52747865166_6d9198c567_z.jpg'
    complex_photo_71.link = 'https://www.flickr.com/search/?lat=34.2959885&lon=132.3198262&radius=0.1&has_geo=1&view_all=1'
    complex_photo_71.person = None
    complex_photo_71.title = 'PDV_1845.jpg'
    complex_photo_71.type_master = complex_type_master_23
    complex_photo_71.username = 'patrickdevries2003'
    complex_photo_71.width = None
    complex_photo_71 = importer.save_or_locate(complex_photo_71)

    complex_photo_72 = Photo()
    complex_photo_72.height = None
    complex_photo_72.image_src = 'https://live.staticflickr.com/65535/51488631058_30212eaf6f_z.jpg'
    complex_photo_72.link = 'https://www.flickr.com/search/?lat=34.2920477&lon=132.3184736&radius=0.1&has_geo=1&view_all=1'
    complex_photo_72.person = None
    complex_photo_72.title = 'Daishoin banners, Miyajima 大聖院 宮島  広島'
    complex_photo_72.type_master = complex_type_master_23
    complex_photo_72.username = 'Anaguma'
    complex_photo_72.width = None
    complex_photo_72 = importer.save_or_locate(complex_photo_72)

    complex_photo_73 = Photo()
    complex_photo_73.height = None
    complex_photo_73.image_src = 'https://live.staticflickr.com/65535/52742386509_1070f0985f_z.jpg'
    complex_photo_73.link = 'https://www.flickr.com/search/?lat=34.2431335&lon=132.5586395&radius=0.1&has_geo=1&view_all=1'
    complex_photo_73.person = None
    complex_photo_73.title = 'DSCF7662'
    complex_photo_73.type_master = complex_type_master_23
    complex_photo_73.username = 'kanata-t'
    complex_photo_73.width = None
    complex_photo_73 = importer.save_or_locate(complex_photo_73)

    complex_photo_74 = Photo()
    complex_photo_74.height = None
    complex_photo_74.image_src = 'https://live.staticflickr.com/65535/52461571357_6635b8da4f_z.jpg'
    complex_photo_74.link = 'https://www.flickr.com/search/?lat=34.2405577&lon=132.5564318&radius=0.1&has_geo=1&view_all=1'
    complex_photo_74.person = None
    complex_photo_74.title = '広島'
    complex_photo_74.type_master = complex_type_master_23
    complex_photo_74.username = 'TAKEGTX'
    complex_photo_74.width = None
    complex_photo_74 = importer.save_or_locate(complex_photo_74)

    complex_photo_75 = Photo()
    complex_photo_75.height = None
    complex_photo_75.image_src = 'https://live.staticflickr.com/65535/52462086541_f18f92532c_z.jpg'
    complex_photo_75.link = 'https://www.flickr.com/search/?lat=34.2411391&lon=132.5558555&radius=0.1&has_geo=1&view_all=1'
    complex_photo_75.person = None
    complex_photo_75.title = '広島'
    complex_photo_75.type_master = complex_type_master_23
    complex_photo_75.username = 'TAKEGTX'
    complex_photo_75.width = None
    complex_photo_75 = importer.save_or_locate(complex_photo_75)

    complex_photo_76 = Photo()
    complex_photo_76.height = None
    complex_photo_76.image_src = 'https://live.staticflickr.com/65535/52461571332_9c96ea1f8b_z.jpg'
    complex_photo_76.link = 'https://www.flickr.com/search/?lat=34.2415568&lon=132.5574165&radius=0.1&has_geo=1&view_all=1'
    complex_photo_76.person = None
    complex_photo_76.title = '広島'
    complex_photo_76.type_master = complex_type_master_23
    complex_photo_76.username = 'TAKEGTX'
    complex_photo_76.width = None
    complex_photo_76 = importer.save_or_locate(complex_photo_76)

    complex_photo_77 = Photo()
    complex_photo_77.height = None
    complex_photo_77.image_src = 'https://live.staticflickr.com/65535/51165182068_8b5b3cee34_z.jpg'
    complex_photo_77.link = 'https://www.flickr.com/search/?lat=34.4081822&lon=133.1978116&radius=0.1&has_geo=1&view_all=1'
    complex_photo_77.person = None
    complex_photo_77.title = 'A walk in Onomichi'
    complex_photo_77.type_master = complex_type_master_23
    complex_photo_77.username = 'Blue Ridge Walker'
    complex_photo_77.width = None
    complex_photo_77 = importer.save_or_locate(complex_photo_77)

    complex_photo_78 = Photo()
    complex_photo_78.height = None
    complex_photo_78.image_src = 'https://live.staticflickr.com/65535/52531273916_01ef516bf3_z.jpg'
    complex_photo_78.link = 'https://www.flickr.com/search/?lat=34.4106865&lon=133.1969604&radius=0.1&has_geo=1&view_all=1'
    complex_photo_78.person = None
    complex_photo_78.title = 'steps'
    complex_photo_78.type_master = complex_type_master_23
    complex_photo_78.username = 'michalskalski'
    complex_photo_78.width = None
    complex_photo_78 = importer.save_or_locate(complex_photo_78)

    complex_photo_79 = Photo()
    complex_photo_79.height = None
    complex_photo_79.image_src = 'https://live.staticflickr.com/65535/51588496549_797b0d80a9_z.jpg'
    complex_photo_79.link = 'https://www.flickr.com/search/?lat=34.4058259&lon=133.1960287&radius=0.1&has_geo=1&view_all=1'
    complex_photo_79.person = None
    complex_photo_79.title = 'by @mkuratani2009'
    complex_photo_79.type_master = complex_type_master_23
    complex_photo_79.username = 'mkuratani2009'
    complex_photo_79.width = None
    complex_photo_79 = importer.save_or_locate(complex_photo_79)

    complex_photo_80 = Photo()
    complex_photo_80.height = None
    complex_photo_80.image_src = 'https://live.staticflickr.com/65535/52539736049_d00df95154_z.jpg'
    complex_photo_80.link = 'https://www.flickr.com/search/?lat=34.4097831&lon=133.1976363&radius=0.1&has_geo=1&view_all=1'
    complex_photo_80.person = None
    complex_photo_80.title = '2022 Onomichi #2'
    complex_photo_80.type_master = complex_type_master_23
    complex_photo_80.username = 'Yorkey&Rin'
    complex_photo_80.width = None
    complex_photo_80 = importer.save_or_locate(complex_photo_80)

    complex_photo_81 = Photo()
    complex_photo_81.height = None
    complex_photo_81.image_src = 'https://live.staticflickr.com/65535/51885477672_fa3a9e52a7_z.jpg'
    complex_photo_81.link = 'https://www.flickr.com/search/?lat=40.6758222&lon=140.8588135&radius=0.1&has_geo=1&view_all=1'
    complex_photo_81.person = None
    complex_photo_81.title = 'Winter Mt. Hakkoda'
    complex_photo_81.type_master = complex_type_master_23
    complex_photo_81.username = '雷太'
    complex_photo_81.width = None
    complex_photo_81 = importer.save_or_locate(complex_photo_81)

    complex_photo_82 = Photo()
    complex_photo_82.height = None
    complex_photo_82.image_src = 'https://live.staticflickr.com/7886/47193495301_8710185f1e_z.jpg'
    complex_photo_82.link = 'https://www.flickr.com/search/?lat=40.7057577&lon=140.8223047&radius=0.1&has_geo=1&view_all=1'
    complex_photo_82.person = None
    complex_photo_82.title = 'by @mhrs.jp'
    complex_photo_82.type_master = complex_type_master_23
    complex_photo_82.username = 'mhrs.jp'
    complex_photo_82.width = None
    complex_photo_82 = importer.save_or_locate(complex_photo_82)

    complex_photo_83 = Photo()
    complex_photo_83.height = None
    complex_photo_83.image_src = 'https://live.staticflickr.com/65535/51886526308_8646115e88_z.jpg'
    complex_photo_83.link = 'https://www.flickr.com/search/?lat=40.6757743&lon=140.8592116&radius=0.1&has_geo=1&view_all=1'
    complex_photo_83.person = None
    complex_photo_83.title = 'Hakkoda snow monsters'
    complex_photo_83.type_master = complex_type_master_23
    complex_photo_83.username = '雷太'
    complex_photo_83.width = None
    complex_photo_83 = importer.save_or_locate(complex_photo_83)

    complex_photo_84 = Photo()
    complex_photo_84.height = None
    complex_photo_84.image_src = 'https://live.staticflickr.com/65535/50036012223_af7d118d43_z.jpg'
    complex_photo_84.link = 'https://www.flickr.com/search/?lat=40.6330178&lon=140.9245271&radius=0.1&has_geo=1&view_all=1'
    complex_photo_84.person = None
    complex_photo_84.title = 'Yachi onsen, one of the secret onsen of Aomori'
    complex_photo_84.type_master = complex_type_master_23
    complex_photo_84.username = 'Hans ter Horst Photography'
    complex_photo_84.width = None
    complex_photo_84 = importer.save_or_locate(complex_photo_84)

    complex_photo_85 = Photo()
    complex_photo_85.height = None
    complex_photo_85.image_src = 'https://live.staticflickr.com/65535/51821101050_191b79fcd7_z.jpg'
    complex_photo_85.link = 'https://www.flickr.com/search/?lat=41.2827427&lon=141.1899038&radius=0.1&has_geo=1&view_all=1'
    complex_photo_85.person = None
    complex_photo_85.title = 'mutsu_20210812191321'
    complex_photo_85.type_master = complex_type_master_23
    complex_photo_85.username = 'inunami'
    complex_photo_85.width = None
    complex_photo_85 = importer.save_or_locate(complex_photo_85)

    complex_photo_86 = Photo()
    complex_photo_86.height = None
    complex_photo_86.image_src = 'https://live.staticflickr.com/8804/18253098982_9ee3a980c3_z.jpg'
    complex_photo_86.link = 'https://www.flickr.com/search/?lat=41.3260657&lon=141.0962272&radius=0.1&has_geo=1&view_all=1'
    complex_photo_86.person = None
    complex_photo_86.title = 'Sanzu no Kawa'
    complex_photo_86.type_master = complex_type_master_23
    complex_photo_86.username = 'mega_midget_racer'
    complex_photo_86.width = None
    complex_photo_86 = importer.save_or_locate(complex_photo_86)

    complex_photo_87 = Photo()
    complex_photo_87.height = None
    complex_photo_87.image_src = 'https://live.staticflickr.com/65535/51547085772_622db872a4_z.jpg'
    complex_photo_87.link = 'https://www.flickr.com/search/?lat=41.327247&lon=141.0907618&radius=0.1&has_geo=1&view_all=1'
    complex_photo_87.person = None
    complex_photo_87.title = 'Brána do zásvětí'
    complex_photo_87.type_master = complex_type_master_23
    complex_photo_87.username = 'hermitvoita'
    complex_photo_87.width = None
    complex_photo_87 = importer.save_or_locate(complex_photo_87)

    complex_photo_88 = Photo()
    complex_photo_88.height = None
    complex_photo_88.image_src = 'https://live.staticflickr.com/65535/50327664441_0856db8fa1_z.jpg'
    complex_photo_88.link = 'https://www.flickr.com/search/?lat=41.3264966&lon=141.086011&radius=0.1&has_geo=1&view_all=1'
    complex_photo_88.person = None
    complex_photo_88.title = '恐山'
    complex_photo_88.type_master = complex_type_master_23
    complex_photo_88.username = 'himeti'
    complex_photo_88.width = None
    complex_photo_88 = importer.save_or_locate(complex_photo_88)

    complex_photo_89 = Photo()
    complex_photo_89.height = None
    complex_photo_89.image_src = 'https://live.staticflickr.com/65535/51548121888_2ae021f18a_z.jpg'
    complex_photo_89.link = 'https://www.flickr.com/search/?lat=41.3283697&lon=141.0917047&radius=0.1&has_geo=1&view_all=1'
    complex_photo_89.person = None
    complex_photo_89.title = 'Pekelná krajina'
    complex_photo_89.type_master = complex_type_master_23
    complex_photo_89.username = 'hermitvoita'
    complex_photo_89.width = None
    complex_photo_89 = importer.save_or_locate(complex_photo_89)

    complex_photo_90 = Photo()
    complex_photo_90.height = None
    complex_photo_90.image_src = 'https://live.staticflickr.com/7756/18265270976_87be1e78a7_z.jpg'
    complex_photo_90.link = 'https://www.flickr.com/search/?lat=41.3145659&lon=141.1264919&radius=0.1&has_geo=1&view_all=1'
    complex_photo_90.person = None
    complex_photo_90.title = 'Osorezan Hiyamizu springs'
    complex_photo_90.type_master = complex_type_master_23
    complex_photo_90.username = 'mega_midget_racer'
    complex_photo_90.width = None
    complex_photo_90 = importer.save_or_locate(complex_photo_90)

    complex_photo_91 = Photo()
    complex_photo_91.height = None
    complex_photo_91.image_src = 'https://live.staticflickr.com/65535/50085149401_a59c3fd84f_z.jpg'
    complex_photo_91.link = 'https://www.flickr.com/search/?lat=33.4580493&lon=135.7718515&radius=0.1&has_geo=1&view_all=1'
    complex_photo_91.person = None
    complex_photo_91.title = '潮岬 本州最南端 (1)'
    complex_photo_91.type_master = complex_type_master_23
    complex_photo_91.username = 'OOMYV'
    complex_photo_91.width = None
    complex_photo_91 = importer.save_or_locate(complex_photo_91)

    complex_photo_92 = Photo()
    complex_photo_92.height = None
    complex_photo_92.image_src = 'https://live.staticflickr.com/65535/51180350109_7198a86e97_z.jpg'
    complex_photo_92.link = 'https://www.flickr.com/search/?lat=33.4378491&lon=135.754685&radius=0.1&has_geo=1&view_all=1'
    complex_photo_92.person = None
    complex_photo_92.title = 'V zajetí koníčku'
    complex_photo_92.type_master = complex_type_master_23
    complex_photo_92.username = 'hermitvoita'
    complex_photo_92.width = None
    complex_photo_92 = importer.save_or_locate(complex_photo_92)

    complex_photo_93 = Photo()
    complex_photo_93.height = None
    complex_photo_93.image_src = 'https://live.staticflickr.com/65535/51178871612_be0a4772d2_z.jpg'
    complex_photo_93.link = 'https://www.flickr.com/search/?lat=33.4375625&lon=135.7544642&radius=0.1&has_geo=1&view_all=1'
    complex_photo_93.person = None
    complex_photo_93.title = 'Pohled zpátky na pevninu'
    complex_photo_93.type_master = complex_type_master_23
    complex_photo_93.username = 'hermitvoita'
    complex_photo_93.width = None
    complex_photo_93 = importer.save_or_locate(complex_photo_93)

    complex_photo_94 = Photo()
    complex_photo_94.height = None
    complex_photo_94.image_src = 'https://live.staticflickr.com/65535/52629608621_2a3a0f73e2_z.jpg'
    complex_photo_94.link = 'https://www.flickr.com/search/?lat=33.4362401&lon=135.7621203&radius=0.1&has_geo=1&view_all=1'
    complex_photo_94.person = None
    complex_photo_94.title = 'Cape Shionomisaki, Wakayama'
    complex_photo_94.type_master = complex_type_master_23
    complex_photo_94.username = 'Kzaral'
    complex_photo_94.width = None
    complex_photo_94 = importer.save_or_locate(complex_photo_94)

    complex_photo_95 = Photo()
    complex_photo_95.height = None
    complex_photo_95.image_src = 'https://live.staticflickr.com/65535/52630081853_4d5540ab10_z.jpg'
    complex_photo_95.link = 'https://www.flickr.com/search/?lat=33.474975&lon=135.782048&radius=0.1&has_geo=1&view_all=1'
    complex_photo_95.person = None
    complex_photo_95.title = 'JR Kushimoto Station'
    complex_photo_95.type_master = complex_type_master_23
    complex_photo_95.username = 'Kzaral'
    complex_photo_95.width = None
    complex_photo_95 = importer.save_or_locate(complex_photo_95)

    complex_photo_96 = Photo()
    complex_photo_96.height = None
    complex_photo_96.image_src = 'https://live.staticflickr.com/65535/52630088168_6b5c97a8d2_z.jpg'
    complex_photo_96.link = 'https://www.flickr.com/search/?lat=33.437806&lon=135.7613677&radius=0.1&has_geo=1&view_all=1'
    complex_photo_96.person = None
    complex_photo_96.title = 'Cape Shionomisaki, Wakayama'
    complex_photo_96.type_master = complex_type_master_23
    complex_photo_96.username = 'Kzaral'
    complex_photo_96.width = None
    complex_photo_96 = importer.save_or_locate(complex_photo_96)

    complex_photo_97 = Photo()
    complex_photo_97.height = None
    complex_photo_97.image_src = 'https://live.staticflickr.com/65535/52630087808_2859291296_z.jpg'
    complex_photo_97.link = 'https://www.flickr.com/search/?lat=33.7254244&lon=135.9946972&radius=0.1&has_geo=1&view_all=1'
    complex_photo_97.person = None
    complex_photo_97.title = 'JR Shingu Station'
    complex_photo_97.type_master = complex_type_master_23
    complex_photo_97.username = 'Kzaral'
    complex_photo_97.width = None
    complex_photo_97 = importer.save_or_locate(complex_photo_97)

    complex_photo_98 = Photo()
    complex_photo_98.height = None
    complex_photo_98.image_src = 'https://live.staticflickr.com/65535/51530861199_e88faf506e_z.jpg'
    complex_photo_98.link = 'https://www.flickr.com/search/?lat=33.834421&lon=135.7723926&radius=0.1&has_geo=1&view_all=1'
    complex_photo_98.person = None
    complex_photo_98.title = '20190929'
    complex_photo_98.type_master = complex_type_master_23
    complex_photo_98.username = 'trlintw'
    complex_photo_98.width = None
    complex_photo_98 = importer.save_or_locate(complex_photo_98)

    complex_photo_99 = Photo()
    complex_photo_99.height = None
    complex_photo_99.image_src = 'https://live.staticflickr.com/65535/52630081833_a673835edd_z.jpg'
    complex_photo_99.link = 'https://www.flickr.com/search/?lat=33.4745935&lon=135.7817317&radius=0.1&has_geo=1&view_all=1'
    complex_photo_99.person = None
    complex_photo_99.title = 'JR Kushimoto Station'
    complex_photo_99.type_master = complex_type_master_23
    complex_photo_99.username = 'Kzaral'
    complex_photo_99.width = None
    complex_photo_99 = importer.save_or_locate(complex_photo_99)

    complex_photo_100 = Photo()
    complex_photo_100.height = None
    complex_photo_100.image_src = 'https://live.staticflickr.com/65535/49525320797_4017b59316_z.jpg'
    complex_photo_100.link = 'https://www.flickr.com/search/?lat=39.4064505&lon=141.173865&radius=0.1&has_geo=1&view_all=1'
    complex_photo_100.person = None
    complex_photo_100.title = '20200201_141144'
    complex_photo_100.type_master = complex_type_master_23
    complex_photo_100.username = 'honhong1598'
    complex_photo_100.width = None
    complex_photo_100 = importer.save_or_locate(complex_photo_100)

    complex_photo_101 = Photo()
    complex_photo_101.height = None
    complex_photo_101.image_src = 'https://live.staticflickr.com/65535/49525097561_0de473f11b_z.jpg'
    complex_photo_101.link = 'https://www.flickr.com/search/?lat=39.4058926&lon=141.1728086&radius=0.1&has_geo=1&view_all=1'
    complex_photo_101.person = None
    complex_photo_101.title = '20200201_141240'
    complex_photo_101.type_master = complex_type_master_23
    complex_photo_101.username = 'honhong1598'
    complex_photo_101.width = None
    complex_photo_101 = importer.save_or_locate(complex_photo_101)

    complex_photo_102 = Photo()
    complex_photo_102.height = None
    complex_photo_102.image_src = 'https://live.staticflickr.com/65535/49525100391_19659df9aa_z.jpg'
    complex_photo_102.link = 'https://www.flickr.com/search/?lat=39.3992073&lon=141.1626699&radius=0.1&has_geo=1&view_all=1'
    complex_photo_102.person = None
    complex_photo_102.title = '20200201_111209'
    complex_photo_102.type_master = complex_type_master_23
    complex_photo_102.username = 'honhong1598'
    complex_photo_102.width = None
    complex_photo_102 = importer.save_or_locate(complex_photo_102)

    complex_photo_103 = Photo()
    complex_photo_103.height = None
    complex_photo_103.image_src = 'https://live.staticflickr.com/65535/49525100341_f78ece8444_z.jpg'
    complex_photo_103.link = 'https://www.flickr.com/search/?lat=39.3994579&lon=141.1645876&radius=0.1&has_geo=1&view_all=1'
    complex_photo_103.person = None
    complex_photo_103.title = '20200201_111234'
    complex_photo_103.type_master = complex_type_master_23
    complex_photo_103.username = 'honhong1598'
    complex_photo_103.width = None
    complex_photo_103 = importer.save_or_locate(complex_photo_103)

    complex_photo_104 = Photo()
    complex_photo_104.height = None
    complex_photo_104.image_src = 'https://live.staticflickr.com/941/43657100852_6b19ac31f3_z.jpg'
    complex_photo_104.link = 'https://www.flickr.com/search/?lat=39.3858944&lon=141.1171042&radius=0.1&has_geo=1&view_all=1'
    complex_photo_104.person = None
    complex_photo_104.title = 'iwate_20180308104442'
    complex_photo_104.type_master = complex_type_master_23
    complex_photo_104.username = 'inunami'
    complex_photo_104.width = None
    complex_photo_104 = importer.save_or_locate(complex_photo_104)

    complex_photo_105 = Photo()
    complex_photo_105.height = None
    complex_photo_105.image_src = 'https://live.staticflickr.com/936/29833720138_6147cf5771_z.jpg'
    complex_photo_105.link = 'https://www.flickr.com/search/?lat=39.385832&lon=141.11711&radius=0.1&has_geo=1&view_all=1'
    complex_photo_105.person = None
    complex_photo_105.title = 'iwate_20180308110616'
    complex_photo_105.type_master = complex_type_master_23
    complex_photo_105.username = 'inunami'
    complex_photo_105.width = None
    complex_photo_105 = importer.save_or_locate(complex_photo_105)

    complex_photo_106 = Photo()
    complex_photo_106.height = None
    complex_photo_106.image_src = 'https://live.staticflickr.com/65535/52730372849_8a7f277584_z.jpg'
    complex_photo_106.link = 'https://www.flickr.com/search/?lat=39.4365493&lon=141.0159616&radius=0.1&has_geo=1&view_all=1'
    complex_photo_106.person = None
    complex_photo_106.title = 'Park near Osawa Onsen (大沢温泉), Hanamaki, Iwate'
    complex_photo_106.type_master = complex_type_master_23
    complex_photo_106.username = 'Hans ter Horst Photography'
    complex_photo_106.width = None
    complex_photo_106 = importer.save_or_locate(complex_photo_106)

    complex_photo_107 = Photo()
    complex_photo_107.height = None
    complex_photo_107.image_src = 'https://live.staticflickr.com/7004/13589732694_59d414253f_z.jpg'
    complex_photo_107.link = 'https://www.flickr.com/search/?lat=39.4256925&lon=141.0151992&radius=0.1&has_geo=1&view_all=1'
    complex_photo_107.person = None
    complex_photo_107.title = '朝から露天風呂なう(・∀・)'
    complex_photo_107.type_master = complex_type_master_23
    complex_photo_107.username = 'ともぞう'
    complex_photo_107.width = None
    complex_photo_107 = importer.save_or_locate(complex_photo_107)

    complex_photo_108 = Photo()
    complex_photo_108.height = None
    complex_photo_108.image_src = 'https://live.staticflickr.com/65535/52761979961_681864c8be_z.jpg'
    complex_photo_108.link = 'https://www.flickr.com/search/?lat=39.0017355&lon=141.102596&radius=0.1&has_geo=1&view_all=1'
    complex_photo_108.person = None
    complex_photo_108.title = 'Chusonji Temple/中尊寺'
    complex_photo_108.type_master = complex_type_master_23
    complex_photo_108.username = 'Seiji Yamanushi'
    complex_photo_108.width = None
    complex_photo_108 = importer.save_or_locate(complex_photo_108)

    complex_photo_109 = Photo()
    complex_photo_109.height = None
    complex_photo_109.image_src = 'https://live.staticflickr.com/8117/8660594588_bcde83f159_z.jpg'
    complex_photo_109.link = 'https://www.flickr.com/search/?lat=39.3894289&lon=141.1091143&radius=0.1&has_geo=1&view_all=1'
    complex_photo_109.person = None
    complex_photo_109.title = '花巻交通デハ3'
    complex_photo_109.type_master = complex_type_master_23
    complex_photo_109.username = 'OOMYV'
    complex_photo_109.width = None
    complex_photo_109 = importer.save_or_locate(complex_photo_109)

    complex_photo_110 = Photo()
    complex_photo_110.height = None
    complex_photo_110.image_src = 'https://live.staticflickr.com/65535/50192567213_b75a7e68bd_z.jpg'
    complex_photo_110.link = 'https://www.flickr.com/search/?lat=35.3866419&lon=132.690256&radius=0.1&has_geo=1&view_all=1'
    complex_photo_110.person = None
    complex_photo_110.title = 'Former Taisha Station, Shimane  出雲大社\u3000旧大社駅\u3000島根'
    complex_photo_110.type_master = complex_type_master_23
    complex_photo_110.username = 'Anaguma'
    complex_photo_110.width = None
    complex_photo_110 = importer.save_or_locate(complex_photo_110)

    complex_photo_111 = Photo()
    complex_photo_111.height = None
    complex_photo_111.image_src = 'https://live.staticflickr.com/1950/44167435245_d0405283e0_z.jpg'
    complex_photo_111.link = 'https://www.flickr.com/search/?lat=35.391579&lon=132.6872784&radius=0.1&has_geo=1&view_all=1'
    complex_photo_111.person = None
    complex_photo_111.title = 'IMG_5777'
    complex_photo_111.type_master = complex_type_master_23
    complex_photo_111.username = 'cmc700123'
    complex_photo_111.width = None
    complex_photo_111 = importer.save_or_locate(complex_photo_111)

    complex_photo_112 = Photo()
    complex_photo_112.height = None
    complex_photo_112.image_src = 'https://live.staticflickr.com/65535/52380541785_777f2ac617_z.jpg'
    complex_photo_112.link = 'https://www.flickr.com/search/?lat=35.3952169&lon=132.6867573&radius=0.1&has_geo=1&view_all=1'
    complex_photo_112.person = None
    complex_photo_112.title = '20220921_鳥取大山登山＆山口帰省_171'
    complex_photo_112.type_master = complex_type_master_23
    complex_photo_112.username = 'jinmsk'
    complex_photo_112.width = None
    complex_photo_112 = importer.save_or_locate(complex_photo_112)

    complex_photo_113 = Photo()
    complex_photo_113.height = None
    complex_photo_113.image_src = 'https://live.staticflickr.com/65535/52380541775_e180419a8c_z.jpg'
    complex_photo_113.link = 'https://www.flickr.com/search/?lat=35.3962535&lon=132.6863131&radius=0.1&has_geo=1&view_all=1'
    complex_photo_113.person = None
    complex_photo_113.title = '20220921_鳥取大山登山＆山口帰省_170'
    complex_photo_113.type_master = complex_type_master_23
    complex_photo_113.username = 'jinmsk'
    complex_photo_113.width = None
    complex_photo_113 = importer.save_or_locate(complex_photo_113)

    complex_photo_114 = Photo()
    complex_photo_114.height = None
    complex_photo_114.image_src = 'https://live.staticflickr.com/65535/51353236080_11e7daf080_z.jpg'
    complex_photo_114.link = 'https://www.flickr.com/search/?lat=35.3967051&lon=132.6863743&radius=0.1&has_geo=1&view_all=1'
    complex_photo_114.person = None
    complex_photo_114.title = '出雲大社'
    complex_photo_114.type_master = complex_type_master_23
    complex_photo_114.username = 'Chitaka Chou'
    complex_photo_114.width = None
    complex_photo_114 = importer.save_or_locate(complex_photo_114)

    complex_photo_115 = Photo()
    complex_photo_115.height = None
    complex_photo_115.image_src = 'https://live.staticflickr.com/65535/52380122316_517035343e_z.jpg'
    complex_photo_115.link = 'https://www.flickr.com/search/?lat=35.3994106&lon=132.6852047&radius=0.1&has_geo=1&view_all=1'
    complex_photo_115.person = None
    complex_photo_115.title = '20220921_鳥取大山登山＆山口帰省_163'
    complex_photo_115.type_master = complex_type_master_23
    complex_photo_115.username = 'jinmsk'
    complex_photo_115.width = None
    complex_photo_115 = importer.save_or_locate(complex_photo_115)

    complex_photo_116 = Photo()
    complex_photo_116.height = None
    complex_photo_116.image_src = 'https://live.staticflickr.com/65535/52380541675_bd124e5dbb_z.jpg'
    complex_photo_116.link = 'https://www.flickr.com/search/?lat=35.4012055&lon=132.6855211&radius=0.1&has_geo=1&view_all=1'
    complex_photo_116.person = None
    complex_photo_116.title = '20220921_鳥取大山登山＆山口帰省_166'
    complex_photo_116.type_master = complex_type_master_23
    complex_photo_116.username = 'jinmsk'
    complex_photo_116.width = None
    complex_photo_116 = importer.save_or_locate(complex_photo_116)

    complex_photo_117 = Photo()
    complex_photo_117.height = None
    complex_photo_117.image_src = 'https://live.staticflickr.com/65535/52380122361_0586a0e209_z.jpg'
    complex_photo_117.link = 'https://www.flickr.com/search/?lat=35.4014929&lon=132.6848802&radius=0.1&has_geo=1&view_all=1'
    complex_photo_117.person = None
    complex_photo_117.title = '20220921_鳥取大山登山＆山口帰省_164'
    complex_photo_117.type_master = complex_type_master_23
    complex_photo_117.username = 'jinmsk'
    complex_photo_117.width = None
    complex_photo_117 = importer.save_or_locate(complex_photo_117)

    complex_photo_118 = Photo()
    complex_photo_118.height = None
    complex_photo_118.image_src = 'https://live.staticflickr.com/65535/52380541615_dd014fe2dc_z.jpg'
    complex_photo_118.link = 'https://www.flickr.com/search/?lat=35.4015453&lon=132.6844634&radius=0.1&has_geo=1&view_all=1'
    complex_photo_118.person = None
    complex_photo_118.title = '20220921_鳥取大山登山＆山口帰省_165'
    complex_photo_118.type_master = complex_type_master_23
    complex_photo_118.username = 'jinmsk'
    complex_photo_118.width = None
    complex_photo_118 = importer.save_or_locate(complex_photo_118)

    complex_photo_119 = Photo()
    complex_photo_119.height = None
    complex_photo_119.image_src = 'https://live.staticflickr.com/65535/51820613402_82c2847af9_z.jpg'
    complex_photo_119.link = 'https://www.flickr.com/search/?lat=35.4003035&lon=132.6719106&radius=0.1&has_geo=1&view_all=1'
    complex_photo_119.person = None
    complex_photo_119.title = 'Bentenjima'
    complex_photo_119.type_master = complex_type_master_23
    complex_photo_119.username = '雷太'
    complex_photo_119.width = None
    complex_photo_119 = importer.save_or_locate(complex_photo_119)

    complex_photo_120 = Photo()
    complex_photo_120.height = None
    complex_photo_120.image_src = 'https://live.staticflickr.com/65535/51330606547_2db1d4cfec_z.jpg'
    complex_photo_120.link = 'https://www.flickr.com/search/?lat=35.4673633&lon=133.0460423&radius=0.1&has_geo=1&view_all=1'
    complex_photo_120.person = None
    complex_photo_120.title = '松江しんじ湖温泉駅'
    complex_photo_120.type_master = complex_type_master_23
    complex_photo_120.username = 'Chitaka Chou'
    complex_photo_120.width = None
    complex_photo_120 = importer.save_or_locate(complex_photo_120)

    complex_photo_121 = Photo()
    complex_photo_121.height = None
    complex_photo_121.image_src = 'https://live.staticflickr.com/65535/52684494168_cfa96b0c51_z.jpg'
    complex_photo_121.link = 'https://www.flickr.com/search/?lat=35.4661714&lon=133.0453378&radius=0.1&has_geo=1&view_all=1'
    complex_photo_121.person = None
    complex_photo_121.title = 'REDJI_0120'
    complex_photo_121.type_master = complex_type_master_23
    complex_photo_121.username = 'doggo1981'
    complex_photo_121.width = None
    complex_photo_121 = importer.save_or_locate(complex_photo_121)

    complex_photo_122 = Photo()
    complex_photo_122.height = None
    complex_photo_122.image_src = 'https://live.staticflickr.com/65535/52385530138_d79ee78aa1_z.jpg'
    complex_photo_122.link = 'https://www.flickr.com/search/?lat=35.5625098&lon=133.3076796&radius=0.1&has_geo=1&view_all=1'
    complex_photo_122.person = None
    complex_photo_122.title = 'by @zhangtreddy'
    complex_photo_122.type_master = complex_type_master_23
    complex_photo_122.username = 'zhangtreddy'
    complex_photo_122.width = None
    complex_photo_122 = importer.save_or_locate(complex_photo_122)

    complex_photo_123 = Photo()
    complex_photo_123.height = None
    complex_photo_123.image_src = 'https://live.staticflickr.com/5585/15117064830_54b2dcc3f0_z.jpg'
    complex_photo_123.link = 'https://www.flickr.com/search/?lat=35.4731536&lon=133.0660854&radius=0.1&has_geo=1&view_all=1'
    complex_photo_123.person = None
    complex_photo_123.title = 'C56131 松江市北公園'
    complex_photo_123.type_master = complex_type_master_23
    complex_photo_123.username = 'OOMYV'
    complex_photo_123.width = None
    complex_photo_123 = importer.save_or_locate(complex_photo_123)

    complex_photo_124 = Photo()
    complex_photo_124.height = None
    complex_photo_124.image_src = 'https://live.staticflickr.com/8553/8703296687_8ae7abd38a_z.jpg'
    complex_photo_124.link = 'https://www.flickr.com/search/?lat=35.534707&lon=133.164644&radius=0.1&has_geo=1&view_all=1'
    complex_photo_124.person = None
    complex_photo_124.title = '七類-境港_まんばら'
    complex_photo_124.type_master = complex_type_master_23
    complex_photo_124.username = 'zushonos'
    complex_photo_124.width = None
    complex_photo_124 = importer.save_or_locate(complex_photo_124)

    complex_photo_125 = Photo()
    complex_photo_125.height = None
    complex_photo_125.image_src = 'https://live.staticflickr.com/65535/52605230819_0ac60e4883_z.jpg'
    complex_photo_125.link = 'https://www.flickr.com/search/?lat=35.5603343&lon=133.3109506&radius=0.1&has_geo=1&view_all=1'
    complex_photo_125.person = None
    complex_photo_125.title = "God's Light Shining on the Sea"
    complex_photo_125.type_master = complex_type_master_23
    complex_photo_125.username = 'Selector Jonathon Photography'
    complex_photo_125.width = None
    complex_photo_125 = importer.save_or_locate(complex_photo_125)

    complex_photo_126 = Photo()
    complex_photo_126.height = None
    complex_photo_126.image_src = 'https://live.staticflickr.com/65535/52603709508_90d3d159a7_z.jpg'
    complex_photo_126.link = 'https://www.flickr.com/search/?lat=35.5623016&lon=133.3074953&radius=0.1&has_geo=1&view_all=1'
    complex_photo_126.person = None
    complex_photo_126.title = 'Benten Wharf Night Light Joyato Lighthouse'
    complex_photo_126.type_master = complex_type_master_23
    complex_photo_126.username = 'Selector Jonathon Photography'
    complex_photo_126.width = None
    complex_photo_126 = importer.save_or_locate(complex_photo_126)

    complex_photo_127 = Photo()
    complex_photo_127.height = None
    complex_photo_127.image_src = 'https://live.staticflickr.com/65535/52385600209_d4978425e1_z.jpg'
    complex_photo_127.link = 'https://www.flickr.com/search/?lat=35.5623182&lon=133.3062224&radius=0.1&has_geo=1&view_all=1'
    complex_photo_127.person = None
    complex_photo_127.title = 'by @zhangtreddy'
    complex_photo_127.type_master = complex_type_master_23
    complex_photo_127.username = 'zhangtreddy'
    complex_photo_127.width = None
    complex_photo_127 = importer.save_or_locate(complex_photo_127)

    complex_photo_128 = Photo()
    complex_photo_128.height = None
    complex_photo_128.image_src = 'https://live.staticflickr.com/65535/52613545123_bff8fece9e_z.jpg'
    complex_photo_128.link = 'https://www.flickr.com/search/?lat=35.5672984&lon=133.3254458&radius=0.1&has_geo=1&view_all=1'
    complex_photo_128.person = None
    complex_photo_128.title = '(Jizo Zaki) Mihonoseki Lighthouse (1898)'
    complex_photo_128.type_master = complex_type_master_23
    complex_photo_128.username = 'Selector Jonathon Photography'
    complex_photo_128.width = None
    complex_photo_128 = importer.save_or_locate(complex_photo_128)

    complex_photo_129 = Photo()
    complex_photo_129.height = None
    complex_photo_129.image_src = 'https://live.staticflickr.com/65535/52613546543_442b3fd80e_z.jpg'
    complex_photo_129.link = 'https://www.flickr.com/search/?lat=35.567285&lon=133.325638&radius=0.1&has_geo=1&view_all=1'
    complex_photo_129.person = None
    complex_photo_129.title = '(Jizo Zaki) Mihonoseki Lighthouse (1898)'
    complex_photo_129.type_master = complex_type_master_23
    complex_photo_129.username = 'Selector Jonathon Photography'
    complex_photo_129.width = None
    complex_photo_129 = importer.save_or_locate(complex_photo_129)

    complex_photo_130 = Photo()
    complex_photo_130.height = None
    complex_photo_130.image_src = 'https://live.staticflickr.com/65535/52613319599_48eb480a1c_z.jpg'
    complex_photo_130.link = 'https://www.flickr.com/search/?lat=35.5672491&lon=133.3250483&radius=0.1&has_geo=1&view_all=1'
    complex_photo_130.person = None
    complex_photo_130.title = '(Jizo Zaki) Mihonoseki Lighthouse (1898)'
    complex_photo_130.type_master = complex_type_master_23
    complex_photo_130.username = 'Selector Jonathon Photography'
    complex_photo_130.width = None
    complex_photo_130 = importer.save_or_locate(complex_photo_130)

    complex_photo_131 = Photo()
    complex_photo_131.height = None
    complex_photo_131.image_src = 'https://live.staticflickr.com/4915/45647025832_485320f344_z.jpg'
    complex_photo_131.link = 'https://www.flickr.com/search/?lat=35.5642081&lon=133.3198608&radius=0.1&has_geo=1&view_all=1'
    complex_photo_131.person = None
    complex_photo_131.title = '前往美保關的路上, Study 2'
    complex_photo_131.type_master = complex_type_master_23
    complex_photo_131.username = 'Zale Yu'
    complex_photo_131.width = None
    complex_photo_131 = importer.save_or_locate(complex_photo_131)

    complex_photo_132 = Photo()
    complex_photo_132.height = None
    complex_photo_132.image_src = 'https://live.staticflickr.com/65535/51717127371_81b24897e1_z.jpg'
    complex_photo_132.link = 'https://www.flickr.com/search/?lat=35.8149406&lon=139.128745&radius=0.1&has_geo=1&view_all=1'
    complex_photo_132.person = None
    complex_photo_132.title = 'Hatonosu Gorge in Autumn'
    complex_photo_132.type_master = complex_type_master_23
    complex_photo_132.username = 'Masa Loner'
    complex_photo_132.width = None
    complex_photo_132 = importer.save_or_locate(complex_photo_132)

    complex_photo_133 = Photo()
    complex_photo_133.height = None
    complex_photo_133.image_src = 'https://live.staticflickr.com/65535/51755191618_3238ffea75_z.jpg'
    complex_photo_133.link = 'https://www.flickr.com/search/?lat=35.8110763&lon=139.1239406&radius=0.1&has_geo=1&view_all=1'
    complex_photo_133.person = None
    complex_photo_133.title = '211106_Yashicaflex_009'
    complex_photo_133.type_master = complex_type_master_23
    complex_photo_133.username = 'Matsui Hiroyuki'
    complex_photo_133.width = None
    complex_photo_133 = importer.save_or_locate(complex_photo_133)

    complex_photo_134 = Photo()
    complex_photo_134.height = None
    complex_photo_134.image_src = 'https://live.staticflickr.com/5332/9431836387_d15f4c8cff_z.jpg'
    complex_photo_134.link = 'https://www.flickr.com/search/?lat=35.8085032&lon=139.1138905&radius=0.1&has_geo=1&view_all=1'
    complex_photo_134.person = None
    complex_photo_134.title = '豪雨襲来！ Σ(‾□‾ノ)ノ'
    complex_photo_134.type_master = complex_type_master_23
    complex_photo_134.username = 'mortardesign'
    complex_photo_134.width = None
    complex_photo_134 = importer.save_or_locate(complex_photo_134)

    complex_photo_135 = Photo()
    complex_photo_135.height = None
    complex_photo_135.image_src = 'https://live.staticflickr.com/65535/51650969308_99788607cf_z.jpg'
    complex_photo_135.link = 'https://www.flickr.com/search/?lat=35.8046162&lon=139.102613&radius=0.1&has_geo=1&view_all=1'
    complex_photo_135.person = None
    complex_photo_135.title = 'Footbridge and Hikawa community'
    complex_photo_135.type_master = complex_type_master_23
    complex_photo_135.username = 'yhila'
    complex_photo_135.width = None
    complex_photo_135 = importer.save_or_locate(complex_photo_135)

    complex_photo_136 = Photo()
    complex_photo_136.height = None
    complex_photo_136.image_src = 'https://live.staticflickr.com/5822/21353452315_01849cdb2a_z.jpg'
    complex_photo_136.link = 'https://www.flickr.com/search/?lat=35.8057723&lon=139.1011388&radius=0.1&has_geo=1&view_all=1'
    complex_photo_136.person = None
    complex_photo_136.title = '蚊取り線香'
    complex_photo_136.type_master = complex_type_master_23
    complex_photo_136.username = 'Kentaro Ohno'
    complex_photo_136.width = None
    complex_photo_136 = importer.save_or_locate(complex_photo_136)

    complex_photo_137 = Photo()
    complex_photo_137.height = None
    complex_photo_137.image_src = 'https://live.staticflickr.com/65535/50578261153_5ec022a5a2_z.jpg'
    complex_photo_137.link = 'https://www.flickr.com/search/?lat=35.806077&lon=139.099594&radius=0.1&has_geo=1&view_all=1'
    complex_photo_137.person = None
    complex_photo_137.title = 'IMG_20201108_150634'
    complex_photo_137.type_master = complex_type_master_23
    complex_photo_137.username = 'tokotaha'
    complex_photo_137.width = None
    complex_photo_137 = importer.save_or_locate(complex_photo_137)

    complex_photo_138 = Photo()
    complex_photo_138.height = None
    complex_photo_138.image_src = 'https://live.staticflickr.com/65535/50579126647_616d09be0a_z.jpg'
    complex_photo_138.link = 'https://www.flickr.com/search/?lat=35.8048366&lon=139.0974752&radius=0.1&has_geo=1&view_all=1'
    complex_photo_138.person = None
    complex_photo_138.title = 'IMG_20201108_145530'
    complex_photo_138.type_master = complex_type_master_23
    complex_photo_138.username = 'tokotaha'
    complex_photo_138.width = None
    complex_photo_138 = importer.save_or_locate(complex_photo_138)

    complex_photo_139 = Photo()
    complex_photo_139.height = None
    complex_photo_139.image_src = 'https://live.staticflickr.com/3718/10379393606_6b2f0d524e_z.jpg'
    complex_photo_139.link = 'https://www.flickr.com/search/?lat=35.808468&lon=139.1135257&radius=0.1&has_geo=1&view_all=1'
    complex_photo_139.person = None
    complex_photo_139.title = 'October 20, 2013 at 12:17PM'
    complex_photo_139.type_master = complex_type_master_23
    complex_photo_139.username = 'Kimilee0317'
    complex_photo_139.width = None
    complex_photo_139 = importer.save_or_locate(complex_photo_139)

    complex_photo_140 = Photo()
    complex_photo_140.height = None
    complex_photo_140.image_src = 'https://live.staticflickr.com/65535/52112915167_dbb47714ff_z.jpg'
    complex_photo_140.link = 'https://www.flickr.com/search/?lat=35.6548755&lon=139.7911163&radius=0.1&has_geo=1&view_all=1'
    complex_photo_140.person = None
    complex_photo_140.title = '久しぶりの豊洲散策02'
    complex_photo_140.type_master = complex_type_master_23
    complex_photo_140.username = 'Norisa1'
    complex_photo_140.width = None
    complex_photo_140 = importer.save_or_locate(complex_photo_140)

    complex_photo_141 = Photo()
    complex_photo_141.height = None
    complex_photo_141.image_src = 'https://live.staticflickr.com/65535/52743896357_1c56d323c4_z.jpg'
    complex_photo_141.link = 'https://www.flickr.com/search/?lat=35.6767189&lon=139.7696552&radius=0.1&has_geo=1&view_all=1'
    complex_photo_141.person = None
    complex_photo_141.title = '前01'
    complex_photo_141.type_master = complex_type_master_23
    complex_photo_141.username = 'ソトノバ | sotonoba.place'
    complex_photo_141.width = None
    complex_photo_141 = importer.save_or_locate(complex_photo_141)

    complex_photo_142 = Photo()
    complex_photo_142.height = None
    complex_photo_142.image_src = 'https://live.staticflickr.com/65535/52738626857_aa1edffd87_z.jpg'
    complex_photo_142.link = 'https://www.flickr.com/search/?lat=35.675434&lon=139.7711133&radius=0.1&has_geo=1&view_all=1'
    complex_photo_142.person = None
    complex_photo_142.title = 'Spring sunshine gallery'
    complex_photo_142.type_master = complex_type_master_23
    complex_photo_142.username = 'sapphire_rouge'
    complex_photo_142.width = None
    complex_photo_142 = importer.save_or_locate(complex_photo_142)

    complex_photo_143 = Photo()
    complex_photo_143.height = None
    complex_photo_143.image_src = 'https://live.staticflickr.com/65535/52710240398_4987df2ec4_z.jpg'
    complex_photo_143.link = 'https://www.flickr.com/search/?lat=35.6717944&lon=139.7843753&radius=0.1&has_geo=1&view_all=1'
    complex_photo_143.person = None
    complex_photo_143.title = 'Tokyo Scapescape'
    complex_photo_143.type_master = complex_type_master_23
    complex_photo_143.username = 'Matthias Harbers'
    complex_photo_143.width = None
    complex_photo_143 = importer.save_or_locate(complex_photo_143)

    complex_photo_144 = Photo()
    complex_photo_144.height = None
    complex_photo_144.image_src = 'https://live.staticflickr.com/65535/52679552866_b3df95441d_z.jpg'
    complex_photo_144.link = 'https://www.flickr.com/search/?lat=35.6616846&lon=139.7787896&radius=0.1&has_geo=1&view_all=1'
    complex_photo_144.person = None
    complex_photo_144.title = 'Street, Tokyo, Japan'
    complex_photo_144.type_master = complex_type_master_23
    complex_photo_144.username = 'runslikethewind83'
    complex_photo_144.width = None
    complex_photo_144 = importer.save_or_locate(complex_photo_144)

    complex_photo_145 = Photo()
    complex_photo_145.height = None
    complex_photo_145.image_src = 'https://live.staticflickr.com/65535/52121708809_33a5bacd0f_z.jpg'
    complex_photo_145.link = 'https://www.flickr.com/search/?lat=35.6647554&lon=139.7833646&radius=0.1&has_geo=1&view_all=1'
    complex_photo_145.person = None
    complex_photo_145.title = 'by @yasuhiro.kuno'
    complex_photo_145.type_master = complex_type_master_23
    complex_photo_145.username = 'yasuhiro.kuno'
    complex_photo_145.width = None
    complex_photo_145 = importer.save_or_locate(complex_photo_145)

    complex_photo_146 = Photo()
    complex_photo_146.height = None
    complex_photo_146.image_src = 'https://live.staticflickr.com/65535/52121708799_24fe1a9c1b_z.jpg'
    complex_photo_146.link = 'https://www.flickr.com/search/?lat=35.6635775&lon=139.7813477&radius=0.1&has_geo=1&view_all=1'
    complex_photo_146.person = None
    complex_photo_146.title = 'by @yasuhiro.kuno'
    complex_photo_146.type_master = complex_type_master_23
    complex_photo_146.username = 'yasuhiro.kuno'
    complex_photo_146.width = None
    complex_photo_146 = importer.save_or_locate(complex_photo_146)

    complex_photo_147 = Photo()
    complex_photo_147.height = None
    complex_photo_147.image_src = 'https://live.staticflickr.com/65535/52767727250_295fb7038e_z.jpg'
    complex_photo_147.link = 'https://www.flickr.com/search/?lat=35.6584597&lon=139.7893269&radius=0.1&has_geo=1&view_all=1'
    complex_photo_147.person = None
    complex_photo_147.title = '豊洲の桜'
    complex_photo_147.type_master = complex_type_master_23
    complex_photo_147.username = 'Norisa1'
    complex_photo_147.width = None
    complex_photo_147 = importer.save_or_locate(complex_photo_147)

    complex_photo_148 = Photo()
    complex_photo_148.height = None
    complex_photo_148.image_src = 'https://live.staticflickr.com/65535/52742976447_5eeb8635f9_z.jpg'
    complex_photo_148.link = 'https://www.flickr.com/search/?lat=35.6533777&lon=139.793127&radius=0.1&has_geo=1&view_all=1'
    complex_photo_148.person = None
    complex_photo_148.title = '"Branz Tower Toyosu"'
    complex_photo_148.type_master = complex_type_master_23
    complex_photo_148.username = 'grain_frame'
    complex_photo_148.width = None
    complex_photo_148 = importer.save_or_locate(complex_photo_148)

    complex_photo_149 = Photo()
    complex_photo_149.height = None
    complex_photo_149.image_src = 'https://live.staticflickr.com/65535/51326188829_7f8ed2b205_z.jpg'
    complex_photo_149.link = 'https://www.flickr.com/search/?lat=35.6454136&lon=139.7862005&radius=0.1&has_geo=1&view_all=1'
    complex_photo_149.person = None
    complex_photo_149.title = 'IMG_5815'
    complex_photo_149.type_master = complex_type_master_23
    complex_photo_149.username = 'OOMYV'
    complex_photo_149.width = None
    complex_photo_149 = importer.save_or_locate(complex_photo_149)

    complex_photo_150 = Photo()
    complex_photo_150.height = None
    complex_photo_150.image_src = 'https://live.staticflickr.com/65535/51324728287_d2b7eac8df_z.jpg'
    complex_photo_150.link = 'https://www.flickr.com/search/?lat=35.6456235&lon=139.7862508&radius=0.1&has_geo=1&view_all=1'
    complex_photo_150.person = None
    complex_photo_150.title = 'IMG_5813'
    complex_photo_150.type_master = complex_type_master_23
    complex_photo_150.username = 'OOMYV'
    complex_photo_150.width = None
    complex_photo_150 = importer.save_or_locate(complex_photo_150)

    complex_photo_151 = Photo()
    complex_photo_151.height = None
    complex_photo_151.image_src = 'https://live.staticflickr.com/65535/51597016289_3307256434_z.jpg'
    complex_photo_151.link = 'https://www.flickr.com/search/?lat=35.6451738&lon=139.7815894&radius=0.1&has_geo=1&view_all=1'
    complex_photo_151.person = None
    complex_photo_151.title = 'Saturday Lunch'
    complex_photo_151.type_master = complex_type_master_23
    complex_photo_151.username = 'YUICHI38'
    complex_photo_151.width = None
    complex_photo_151 = importer.save_or_locate(complex_photo_151)

    complex_photo_152 = Photo()
    complex_photo_152.height = None
    complex_photo_152.image_src = 'https://live.staticflickr.com/65535/50336993523_e884f81620_z.jpg'
    complex_photo_152.link = 'https://www.flickr.com/search/?lat=35.6419028&lon=139.7818519&radius=0.1&has_geo=1&view_all=1'
    complex_photo_152.person = None
    complex_photo_152.title = 'IMG_9731.jpg'
    complex_photo_152.type_master = complex_type_master_23
    complex_photo_152.username = 'fasion'
    complex_photo_152.width = None
    complex_photo_152 = importer.save_or_locate(complex_photo_152)

    complex_photo_153 = Photo()
    complex_photo_153.height = None
    complex_photo_153.image_src = 'https://live.staticflickr.com/65535/52587203343_a0e34f3cb7_z.jpg'
    complex_photo_153.link = 'https://www.flickr.com/search/?lat=35.6405733&lon=139.8405881&radius=0.1&has_geo=1&view_all=1'
    complex_photo_153.person = None
    complex_photo_153.title = 'IMG_7839'
    complex_photo_153.type_master = complex_type_master_23
    complex_photo_153.username = 'OOMYV'
    complex_photo_153.width = None
    complex_photo_153 = importer.save_or_locate(complex_photo_153)

    complex_photo_154 = Photo()
    complex_photo_154.height = None
    complex_photo_154.image_src = 'https://live.staticflickr.com/65535/51500736002_7ed6b6fb95_z.jpg'
    complex_photo_154.link = 'https://www.flickr.com/search/?lat=35.61607&lon=139.7756369&radius=0.1&has_geo=1&view_all=1'
    complex_photo_154.person = None
    complex_photo_154.title = 'Emily'
    complex_photo_154.type_master = complex_type_master_23
    complex_photo_154.username = 'Kevin'
    complex_photo_154.width = None
    complex_photo_154 = importer.save_or_locate(complex_photo_154)

    complex_photo_155 = Photo()
    complex_photo_155.height = None
    complex_photo_155.image_src = 'https://live.staticflickr.com/65535/52717618048_c22807ab47_z.jpg'
    complex_photo_155.link = 'https://www.flickr.com/search/?lat=36.3746839&lon=140.4569096&radius=0.1&has_geo=1&view_all=1'
    complex_photo_155.person = None
    complex_photo_155.title = 'Mito'
    complex_photo_155.type_master = complex_type_master_23
    complex_photo_155.username = 'pantkiewicz'
    complex_photo_155.width = None
    complex_photo_155 = importer.save_or_locate(complex_photo_155)

    complex_photo_156 = Photo()
    complex_photo_156.height = None
    complex_photo_156.image_src = 'https://live.staticflickr.com/65535/52716610302_0fd0f05633_z.jpg'
    complex_photo_156.link = 'https://www.flickr.com/search/?lat=36.369809&lon=140.4758112&radius=0.1&has_geo=1&view_all=1'
    complex_photo_156.person = None
    complex_photo_156.title = 'Hotel Lake View'
    complex_photo_156.type_master = complex_type_master_23
    complex_photo_156.username = 'pantkiewicz'
    complex_photo_156.width = None
    complex_photo_156 = importer.save_or_locate(complex_photo_156)

    complex_photo_157 = Photo()
    complex_photo_157.height = None
    complex_photo_157.image_src = 'https://live.staticflickr.com/8247/8584638155_f528418c5e_z.jpg'
    complex_photo_157.link = 'https://www.flickr.com/search/?lat=36.5310286&lon=140.527941&radius=0.1&has_geo=1&view_all=1'
    complex_photo_157.person = None
    complex_photo_157.title = 'カメラロール-899'
    complex_photo_157.type_master = complex_type_master_23
    complex_photo_157.username = 'tottoko_8686'
    complex_photo_157.width = None
    complex_photo_157 = importer.save_or_locate(complex_photo_157)

    complex_photo_158 = Photo()
    complex_photo_158.height = None
    complex_photo_158.image_src = 'https://live.staticflickr.com/1503/24988603056_961339a3bd_z.jpg'
    complex_photo_158.link = 'https://www.flickr.com/search/?lat=36.5340318&lon=140.5259073&radius=0.1&has_geo=1&view_all=1'
    complex_photo_158.person = None
    complex_photo_158.title = 'DSC06282'
    complex_photo_158.type_master = complex_type_master_23
    complex_photo_158.username = 'szknbyk'
    complex_photo_158.width = None
    complex_photo_158 = importer.save_or_locate(complex_photo_158)

    complex_photo_159 = Photo()
    complex_photo_159.height = None
    complex_photo_159.image_src = 'https://live.staticflickr.com/65535/49278005281_68d5375921_z.jpg'
    complex_photo_159.link = 'https://www.flickr.com/search/?lat=36.5402389&lon=140.5224722&radius=0.1&has_geo=1&view_all=1'
    complex_photo_159.person = None
    complex_photo_159.title = 'Kujiragaoka'
    complex_photo_159.type_master = complex_type_master_23
    complex_photo_159.username = 'ubic from tokyo'
    complex_photo_159.width = None
    complex_photo_159 = importer.save_or_locate(complex_photo_159)

    complex_photo_160 = Photo()
    complex_photo_160.height = None
    complex_photo_160.image_src = 'https://live.staticflickr.com/65535/49277527958_2259b5ea8b_z.jpg'
    complex_photo_160.link = 'https://www.flickr.com/search/?lat=36.5407325&lon=140.5231782&radius=0.1&has_geo=1&view_all=1'
    complex_photo_160.person = None
    complex_photo_160.title = 'Kujiragaoka'
    complex_photo_160.type_master = complex_type_master_23
    complex_photo_160.username = 'ubic from tokyo'
    complex_photo_160.width = None
    complex_photo_160 = importer.save_or_locate(complex_photo_160)

    complex_photo_161 = Photo()
    complex_photo_161.height = None
    complex_photo_161.image_src = 'https://live.staticflickr.com/65535/49280957167_59ba13384b_z.jpg'
    complex_photo_161.link = 'https://www.flickr.com/search/?lat=36.541721&lon=140.523689&radius=0.1&has_geo=1&view_all=1'
    complex_photo_161.person = None
    complex_photo_161.title = 'Kujiragaoka'
    complex_photo_161.type_master = complex_type_master_23
    complex_photo_161.username = 'ubic from tokyo'
    complex_photo_161.width = None
    complex_photo_161 = importer.save_or_locate(complex_photo_161)

    complex_photo_162 = Photo()
    complex_photo_162.height = None
    complex_photo_162.image_src = 'https://live.staticflickr.com/7013/6700869925_c64629fc7c_z.jpg'
    complex_photo_162.link = 'https://www.flickr.com/search/?lat=36.542962&lon=140.5207&radius=0.1&has_geo=1&view_all=1'
    complex_photo_162.person = None
    complex_photo_162.title = 'IMG_0437'
    complex_photo_162.type_master = complex_type_master_23
    complex_photo_162.username = 'strngwrld'
    complex_photo_162.width = None
    complex_photo_162 = importer.save_or_locate(complex_photo_162)

    complex_photo_163 = Photo()
    complex_photo_163.height = None
    complex_photo_163.image_src = 'https://live.staticflickr.com/8084/29670060761_32e55ba854_z.jpg'
    complex_photo_163.link = 'https://www.flickr.com/search/?lat=36.5492822&lon=140.5235532&radius=0.1&has_geo=1&view_all=1'
    complex_photo_163.person = None
    complex_photo_163.title = 'image'
    complex_photo_163.type_master = complex_type_master_23
    complex_photo_163.username = 'mhrs.jp'
    complex_photo_163.width = None
    complex_photo_163 = importer.save_or_locate(complex_photo_163)

    complex_photo_164 = Photo()
    complex_photo_164.height = None
    complex_photo_164.image_src = 'https://live.staticflickr.com/65535/49278009171_ab772649e9_z.jpg'
    complex_photo_164.link = 'https://www.flickr.com/search/?lat=36.538385&lon=140.523225&radius=0.1&has_geo=1&view_all=1'
    complex_photo_164.person = None
    complex_photo_164.title = 'Kujiragaoka'
    complex_photo_164.type_master = complex_type_master_23
    complex_photo_164.username = 'ubic from tokyo'
    complex_photo_164.width = None
    complex_photo_164 = importer.save_or_locate(complex_photo_164)

    complex_photo_165 = Photo()
    complex_photo_165.height = None
    complex_photo_165.image_src = 'https://live.staticflickr.com/1977/45200850641_eeb121a874_z.jpg'
    complex_photo_165.link = 'https://www.flickr.com/search/?lat=36.6338743&lon=140.587316&radius=0.1&has_geo=1&view_all=1'
    complex_photo_165.person = None
    complex_photo_165.title = '20181008-105017-51'
    complex_photo_165.type_master = complex_type_master_23
    complex_photo_165.username = 'giu205'
    complex_photo_165.width = None
    complex_photo_165 = importer.save_or_locate(complex_photo_165)

    complex_photo_166 = Photo()
    complex_photo_166.height = None
    complex_photo_166.image_src = 'https://live.staticflickr.com/1903/31326270958_ccb17041be_z.jpg'
    complex_photo_166.link = 'https://www.flickr.com/search/?lat=36.6360807&lon=140.5855581&radius=0.1&has_geo=1&view_all=1'
    complex_photo_166.person = None
    complex_photo_166.title = '20181008-084906-40'
    complex_photo_166.type_master = complex_type_master_23
    complex_photo_166.username = 'giu205'
    complex_photo_166.width = None
    complex_photo_166 = importer.save_or_locate(complex_photo_166)

    complex_photo_167 = Photo()
    complex_photo_167.height = None
    complex_photo_167.image_src = 'https://live.staticflickr.com/1937/44288874835_15616258c1_z.jpg'
    complex_photo_167.link = 'https://www.flickr.com/search/?lat=36.6319654&lon=140.5907626&radius=0.1&has_geo=1&view_all=1'
    complex_photo_167.person = None
    complex_photo_167.title = '20181008-091903-46'
    complex_photo_167.type_master = complex_type_master_23
    complex_photo_167.username = 'giu205'
    complex_photo_167.width = None
    complex_photo_167 = importer.save_or_locate(complex_photo_167)

    complex_photo_168 = Photo()
    complex_photo_168.height = None
    complex_photo_168.image_src = 'https://live.staticflickr.com/3782/14264191244_f6d3a176a9_z.jpg'
    complex_photo_168.link = 'https://www.flickr.com/search/?lat=36.5873526&lon=140.6616108&radius=0.1&has_geo=1&view_all=1'
    complex_photo_168.person = None
    complex_photo_168.title = 'WP_20140517_08_25_51_Raw'
    complex_photo_168.type_master = complex_type_master_23
    complex_photo_168.username = 'rinproject'
    complex_photo_168.width = None
    complex_photo_168 = importer.save_or_locate(complex_photo_168)

    complex_photo_169 = Photo()
    complex_photo_169.height = None
    complex_photo_169.image_src = 'https://live.staticflickr.com/3956/15501150157_220386f221_z.jpg'
    complex_photo_169.link = 'https://www.flickr.com/search/?lat=36.5809219&lon=140.6617725&radius=0.1&has_geo=1&view_all=1'
    complex_photo_169.person = None
    complex_photo_169.title = '#sea #shore'
    complex_photo_169.type_master = complex_type_master_23
    complex_photo_169.username = 'culturalphenomenon27'
    complex_photo_169.width = None
    complex_photo_169 = importer.save_or_locate(complex_photo_169)

    complex_photo_170 = Photo()
    complex_photo_170.height = None
    complex_photo_170.image_src = 'https://live.staticflickr.com/65535/52650194693_3d5bd121c5_z.jpg'
    complex_photo_170.link = 'https://www.flickr.com/search/?lat=33.887012&lon=130.884924&radius=0.1&has_geo=1&view_all=1'
    complex_photo_170.person = None
    complex_photo_170.title = 'IMG_7668'
    complex_photo_170.type_master = complex_type_master_23
    complex_photo_170.username = 'Lewis Lai'
    complex_photo_170.width = None
    complex_photo_170 = importer.save_or_locate(complex_photo_170)

    complex_photo_171 = Photo()
    complex_photo_171.height = None
    complex_photo_171.image_src = 'https://live.staticflickr.com/65535/49256380933_28a3515052_z.jpg'
    complex_photo_171.link = 'https://www.flickr.com/search/?lat=33.5001247&lon=131.1717971&radius=0.1&has_geo=1&view_all=1'
    complex_photo_171.person = None
    complex_photo_171.title = '20191121_Kyushu_220'
    complex_photo_171.type_master = complex_type_master_23
    complex_photo_171.username = 'jinmsk'
    complex_photo_171.width = None
    complex_photo_171 = importer.save_or_locate(complex_photo_171)

    complex_photo_172 = Photo()
    complex_photo_172.height = None
    complex_photo_172.image_src = 'https://live.staticflickr.com/349/19351704725_a39aa65422_z.jpg'
    complex_photo_172.link = 'https://www.flickr.com/search/?lat=33.3744345&lon=131.2675881&radius=0.1&has_geo=1&view_all=1'
    complex_photo_172.person = None
    complex_photo_172.title = 'Usa no Machu Picchu'
    complex_photo_172.type_master = complex_type_master_23
    complex_photo_172.username = 'parsons service'
    complex_photo_172.width = None
    complex_photo_172 = importer.save_or_locate(complex_photo_172)

    complex_photo_173 = Photo()
    complex_photo_173.height = None
    complex_photo_173.image_src = 'https://live.staticflickr.com/65535/49257060537_cb7d87c5e1_z.jpg'
    complex_photo_173.link = 'https://www.flickr.com/search/?lat=33.3718603&lon=131.1651069&radius=0.1&has_geo=1&view_all=1'
    complex_photo_173.person = None
    complex_photo_173.title = '20191121_Kyushu_231'
    complex_photo_173.type_master = complex_type_master_23
    complex_photo_173.username = 'jinmsk'
    complex_photo_173.width = None
    complex_photo_173 = importer.save_or_locate(complex_photo_173)

    complex_photo_174 = Photo()
    complex_photo_174.height = None
    complex_photo_174.image_src = 'https://live.staticflickr.com/65535/52595305013_441af710de_z.jpg'
    complex_photo_174.link = 'https://www.flickr.com/search/?lat=33.5728799&lon=131.6046218&radius=0.1&has_geo=1&view_all=1'
    complex_photo_174.person = None
    complex_photo_174.title = 'Futagoji temple, Kyushu, Japan'
    complex_photo_174.type_master = complex_type_master_23
    complex_photo_174.username = 'Christian Kaden'
    complex_photo_174.width = None
    complex_photo_174 = importer.save_or_locate(complex_photo_174)

    complex_photo_175 = Photo()
    complex_photo_175.height = None
    complex_photo_175.image_src = 'https://live.staticflickr.com/65535/51982037700_732c5d8ca3_z.jpg'
    complex_photo_175.link = 'https://www.flickr.com/search/?lat=33.5740013&lon=131.603241&radius=0.1&has_geo=1&view_all=1'
    complex_photo_175.person = None
    complex_photo_175.title = 'oku-no-inn'
    complex_photo_175.type_master = complex_type_master_23
    complex_photo_175.username = 'MURATAGAWA Kei'
    complex_photo_175.width = None
    complex_photo_175 = importer.save_or_locate(complex_photo_175)

    complex_photo_176 = Photo()
    complex_photo_176.height = None
    complex_photo_176.image_src = 'https://live.staticflickr.com/65535/52595301148_e30fbfc2ee_z.jpg'
    complex_photo_176.link = 'https://www.flickr.com/search/?lat=33.5260019&lon=131.3746381&radius=0.1&has_geo=1&view_all=1'
    complex_photo_176.person = None
    complex_photo_176.title = 'Usa Jingu Shrine, Kyushu'
    complex_photo_176.type_master = complex_type_master_23
    complex_photo_176.username = 'Christian Kaden'
    complex_photo_176.width = None
    complex_photo_176 = importer.save_or_locate(complex_photo_176)

    complex_photo_177 = Photo()
    complex_photo_177.height = None
    complex_photo_177.image_src = 'https://live.staticflickr.com/4883/45923259842_da2f04d260_z.jpg'
    complex_photo_177.link = 'https://www.flickr.com/search/?lat=33.5279086&lon=131.3750797&radius=0.1&has_geo=1&view_all=1'
    complex_photo_177.person = None
    complex_photo_177.title = 'Looking Up'
    complex_photo_177.type_master = complex_type_master_23
    complex_photo_177.username = 'Martin Smith - Having the Time of my Life'
    complex_photo_177.width = None
    complex_photo_177 = importer.save_or_locate(complex_photo_177)

    complex_photo_178 = Photo()
    complex_photo_178.height = None
    complex_photo_178.image_src = 'https://live.staticflickr.com/65535/52761655133_409ca17669_z.jpg'
    complex_photo_178.link = 'https://www.flickr.com/search/?lat=35.6784667&lon=139.7442197&radius=0.1&has_geo=1&view_all=1'
    complex_photo_178.person = None
    complex_photo_178.title = 'IMG20230321123712'
    complex_photo_178.type_master = complex_type_master_23
    complex_photo_178.username = 'tokotaha'
    complex_photo_178.width = None
    complex_photo_178 = importer.save_or_locate(complex_photo_178)

    complex_photo_179 = Photo()
    complex_photo_179.height = None
    complex_photo_179.image_src = 'https://live.staticflickr.com/65535/52759355997_f5ab776e2f_z.jpg'
    complex_photo_179.link = 'https://www.flickr.com/search/?lat=35.6779568&lon=139.7365574&radius=0.1&has_geo=1&view_all=1'
    complex_photo_179.person = None
    complex_photo_179.title = 'Harry Potter'
    complex_photo_179.type_master = complex_type_master_23
    complex_photo_179.username = 'Chad Davis.'
    complex_photo_179.width = None
    complex_photo_179 = importer.save_or_locate(complex_photo_179)

    complex_photo_180 = Photo()
    complex_photo_180.height = None
    complex_photo_180.image_src = 'https://live.staticflickr.com/65535/52615354247_c2b0f0e9f0_z.jpg'
    complex_photo_180.link = 'https://www.flickr.com/search/?lat=35.6791113&lon=139.694663&radius=0.1&has_geo=1&view_all=1'
    complex_photo_180.person = None
    complex_photo_180.title = 'a food stand on a night'
    complex_photo_180.type_master = complex_type_master_23
    complex_photo_180.username = 'cat_in_136'
    complex_photo_180.width = None
    complex_photo_180 = importer.save_or_locate(complex_photo_180)

    complex_photo_181 = Photo()
    complex_photo_181.height = None
    complex_photo_181.image_src = 'https://live.staticflickr.com/65535/52244916083_0637b009f6_z.jpg'
    complex_photo_181.link = 'https://www.flickr.com/search/?lat=35.6839315&lon=139.690806&radius=0.1&has_geo=1&view_all=1'
    complex_photo_181.person = None
    complex_photo_181.title = 'E.T.A. II'
    complex_photo_181.type_master = complex_type_master_23
    complex_photo_181.username = 'Willem van den Hoed'
    complex_photo_181.width = None
    complex_photo_181 = importer.save_or_locate(complex_photo_181)

    complex_photo_182 = Photo()
    complex_photo_182.height = None
    complex_photo_182.image_src = 'https://live.staticflickr.com/65535/52750968046_5214d47bb6_z.jpg'
    complex_photo_182.link = 'https://www.flickr.com/search/?lat=35.6886568&lon=139.6915634&radius=0.1&has_geo=1&view_all=1'
    complex_photo_182.person = None
    complex_photo_182.title = 'TUI Sports DN TYO2023-DLN157'
    complex_photo_182.type_master = complex_type_master_23
    complex_photo_182.username = 'TUI Sports'
    complex_photo_182.width = None
    complex_photo_182 = importer.save_or_locate(complex_photo_182)

    complex_photo_183 = Photo()
    complex_photo_183.height = None
    complex_photo_183.image_src = 'https://live.staticflickr.com/65535/52082069740_98b272decc_z.jpg'
    complex_photo_183.link = 'https://www.flickr.com/search/?lat=35.6891142&lon=139.6830083&radius=0.1&has_geo=1&view_all=1'
    complex_photo_183.person = None
    complex_photo_183.title = 'PXL_20220518_020139857'
    complex_photo_183.type_master = complex_type_master_23
    complex_photo_183.username = 'nobusato'
    complex_photo_183.width = None
    complex_photo_183 = importer.save_or_locate(complex_photo_183)

    complex_photo_184 = Photo()
    complex_photo_184.height = None
    complex_photo_184.image_src = 'https://live.staticflickr.com/65535/51204598608_4534d514d2_z.jpg'
    complex_photo_184.link = 'https://www.flickr.com/search/?lat=35.6879053&lon=139.6810693&radius=0.1&has_geo=1&view_all=1'
    complex_photo_184.person = None
    complex_photo_184.title = '清水橋跡'
    complex_photo_184.type_master = complex_type_master_23
    complex_photo_184.username = 'いしだなおと'
    complex_photo_184.width = None
    complex_photo_184 = importer.save_or_locate(complex_photo_184)

    complex_photo_185 = Photo()
    complex_photo_185.height = None
    complex_photo_185.image_src = 'https://live.staticflickr.com/65535/49845619347_e12c126761_z.jpg'
    complex_photo_185.link = 'https://www.flickr.com/search/?lat=35.6713219&lon=139.651149&radius=0.1&has_geo=1&view_all=1'
    complex_photo_185.person = None
    complex_photo_185.title = 'SDIM0639'
    complex_photo_185.type_master = complex_type_master_23
    complex_photo_185.username = 'beve4'
    complex_photo_185.width = None
    complex_photo_185 = importer.save_or_locate(complex_photo_185)

    complex_photo_186 = Photo()
    complex_photo_186.height = None
    complex_photo_186.image_src = 'https://live.staticflickr.com/7309/27486755916_5b1cc3b3fe_z.jpg'
    complex_photo_186.link = 'https://www.flickr.com/search/?lat=35.6731172&lon=139.6478716&radius=0.1&has_geo=1&view_all=1'
    complex_photo_186.person = None
    complex_photo_186.title = 'Construction Platform over the Kanda River'
    complex_photo_186.type_master = complex_type_master_23
    complex_photo_186.username = 'ykanazawa1999'
    complex_photo_186.width = None
    complex_photo_186 = importer.save_or_locate(complex_photo_186)

    complex_photo_187 = Photo()
    complex_photo_187.height = None
    complex_photo_187.image_src = 'https://live.staticflickr.com/65535/52648532835_c2e0e5ac10_z.jpg'
    complex_photo_187.link = 'https://www.flickr.com/search/?lat=35.6218588&lon=139.7199399&radius=0.1&has_geo=1&view_all=1'
    complex_photo_187.person = None
    complex_photo_187.title = 'JAL B737 Flying above Nishi-gotanda Itchome Crossing'
    complex_photo_187.type_master = complex_type_master_23
    complex_photo_187.username = 'ykanazawa1999'
    complex_photo_187.width = None
    complex_photo_187 = importer.save_or_locate(complex_photo_187)

    complex_photo_188 = Photo()
    complex_photo_188.height = None
    complex_photo_188.image_src = 'https://live.staticflickr.com/65535/52602389165_dba333926c_z.jpg'
    complex_photo_188.link = 'https://www.flickr.com/search/?lat=35.6674381&lon=139.7392918&radius=0.1&has_geo=1&view_all=1'
    complex_photo_188.person = None
    complex_photo_188.title = '160602 Tokyo.jpg'
    complex_photo_188.type_master = complex_type_master_23
    complex_photo_188.username = 'Bruce Batten'
    complex_photo_188.width = None
    complex_photo_188 = importer.save_or_locate(complex_photo_188)

    complex_photo_189 = Photo()
    complex_photo_189.height = None
    complex_photo_189.image_src = 'https://live.staticflickr.com/65535/52767567336_4e988bae42_z.jpg'
    complex_photo_189.link = 'https://www.flickr.com/search/?lat=35.6774878&lon=139.7519827&radius=0.1&has_geo=1&view_all=1'
    complex_photo_189.person = None
    complex_photo_189.title = 'IMG20230324132954'
    complex_photo_189.type_master = complex_type_master_23
    complex_photo_189.username = 'tokotaha'
    complex_photo_189.width = None
    complex_photo_189 = importer.save_or_locate(complex_photo_189)

    complex_photo_190 = Photo()
    complex_photo_190.height = None
    complex_photo_190.image_src = 'https://live.staticflickr.com/65535/52516545636_f5659f9122_z.jpg'
    complex_photo_190.link = 'https://www.flickr.com/search/?lat=35.6956387&lon=139.7741829&radius=0.1&has_geo=1&view_all=1'
    complex_photo_190.person = None
    complex_photo_190.title = 'PXL_20221122_095337032.NIGHT~2'
    complex_photo_190.type_master = complex_type_master_23
    complex_photo_190.username = 'taitan-no'
    complex_photo_190.width = None
    complex_photo_190 = importer.save_or_locate(complex_photo_190)

    complex_photo_191 = Photo()
    complex_photo_191.height = None
    complex_photo_191.image_src = 'https://live.staticflickr.com/65535/52767704248_9728dea0c2_z.jpg'
    complex_photo_191.link = 'https://www.flickr.com/search/?lat=35.7519289&lon=139.7364344&radius=0.1&has_geo=1&view_all=1'
    complex_photo_191.person = None
    complex_photo_191.title = 'Cherry Blossoms 2023 by PxK-1_27.jpg'
    complex_photo_191.type_master = complex_type_master_23
    complex_photo_191.username = "h_nissy's Photography"
    complex_photo_191.width = None
    complex_photo_191 = importer.save_or_locate(complex_photo_191)

    complex_photo_192 = Photo()
    complex_photo_192.height = None
    complex_photo_192.image_src = 'https://live.staticflickr.com/65535/52441569088_bc0c85b863_z.jpg'
    complex_photo_192.link = 'https://www.flickr.com/search/?lat=35.7940375&lon=139.7260453&radius=0.1&has_geo=1&view_all=1'
    complex_photo_192.person = None
    complex_photo_192.title = '20221020_151212'
    complex_photo_192.type_master = complex_type_master_23
    complex_photo_192.username = 'tokotaha'
    complex_photo_192.width = None
    complex_photo_192 = importer.save_or_locate(complex_photo_192)

    complex_photo_193 = Photo()
    complex_photo_193.height = None
    complex_photo_193.image_src = 'https://live.staticflickr.com/1680/26268843192_d153e671a6_z.jpg'
    complex_photo_193.link = 'https://www.flickr.com/search/?lat=36.5717451&lon=139.0596769&radius=0.1&has_geo=1&view_all=1'
    complex_photo_193.person = None
    complex_photo_193.title = '26-P1000255'
    complex_photo_193.type_master = complex_type_master_23
    complex_photo_193.username = 'TZR6063'
    complex_photo_193.width = None
    complex_photo_193 = importer.save_or_locate(complex_photo_193)

    complex_photo_194 = Photo()
    complex_photo_194.height = None
    complex_photo_194.image_src = 'https://live.staticflickr.com/4665/27853362789_220ff1b401_z.jpg'
    complex_photo_194.link = 'https://www.flickr.com/search/?lat=36.5749053&lon=139.053134&radius=0.1&has_geo=1&view_all=1'
    complex_photo_194.person = None
    complex_photo_194.title = '18a1121'
    complex_photo_194.type_master = complex_type_master_23
    complex_photo_194.username = 'kimagurenote'
    complex_photo_194.width = None
    complex_photo_194 = importer.save_or_locate(complex_photo_194)

    complex_photo_195 = Photo()
    complex_photo_195.height = None
    complex_photo_195.image_src = 'https://live.staticflickr.com/2289/1756553017_8e9a5f2ebd_z.jpg'
    complex_photo_195.link = 'https://www.flickr.com/search/?lat=36.5814415&lon=139.0495015&radius=0.1&has_geo=1&view_all=1'
    complex_photo_195.person = None
    complex_photo_195.title = 'Blocked!'
    complex_photo_195.type_master = complex_type_master_23
    complex_photo_195.username = 'Katakanadian'
    complex_photo_195.width = None
    complex_photo_195 = importer.save_or_locate(complex_photo_195)

    complex_photo_196 = Photo()
    complex_photo_196.height = None
    complex_photo_196.image_src = 'https://live.staticflickr.com/4717/24762554287_dedf56efed_z.jpg'
    complex_photo_196.link = 'https://www.flickr.com/search/?lat=36.7810089&lon=138.9697672&radius=0.1&has_geo=1&view_all=1'
    complex_photo_196.person = None
    complex_photo_196.title = '18l3204'
    complex_photo_196.type_master = complex_type_master_23
    complex_photo_196.username = 'kimagurenote'
    complex_photo_196.width = None
    complex_photo_196 = importer.save_or_locate(complex_photo_196)

    complex_photo_197 = Photo()
    complex_photo_197.height = None
    complex_photo_197.image_src = 'https://live.staticflickr.com/65535/49682492822_67262b0264_z.jpg'
    complex_photo_197.link = 'https://www.flickr.com/search/?lat=36.7641343&lon=138.968798&radius=0.1&has_geo=1&view_all=1'
    complex_photo_197.person = None
    complex_photo_197.title = 'DSC07770'
    complex_photo_197.type_master = complex_type_master_23
    complex_photo_197.username = 'OOMYV'
    complex_photo_197.width = None
    complex_photo_197 = importer.save_or_locate(complex_photo_197)

    complex_photo_198 = Photo()
    complex_photo_198.height = None
    complex_photo_198.image_src = 'https://live.staticflickr.com/65535/49844880672_539a7d01db_z.jpg'
    complex_photo_198.link = 'https://www.flickr.com/search/?lat=33.5788333&lon=133.6458189&radius=0.1&has_geo=1&view_all=1'
    complex_photo_198.person = None
    complex_photo_198.title = 'nankoku_20190905111300'
    complex_photo_198.type_master = complex_type_master_23
    complex_photo_198.username = 'inunami'
    complex_photo_198.width = None
    complex_photo_198 = importer.save_or_locate(complex_photo_198)

    complex_photo_199 = Photo()
    complex_photo_199.height = None
    complex_photo_199.image_src = 'https://live.staticflickr.com/65535/49844880412_6cbf656155_z.jpg'
    complex_photo_199.link = 'https://www.flickr.com/search/?lat=33.578697&lon=133.6453861&radius=0.1&has_geo=1&view_all=1'
    complex_photo_199.person = None
    complex_photo_199.title = 'nankoku_20190905111603'
    complex_photo_199.type_master = complex_type_master_23
    complex_photo_199.username = 'inunami'
    complex_photo_199.width = None
    complex_photo_199 = importer.save_or_locate(complex_photo_199)

    complex_photo_200 = Photo()
    complex_photo_200.height = None
    complex_photo_200.image_src = 'https://live.staticflickr.com/65535/48685102857_1e704d90f3_z.jpg'
    complex_photo_200.link = 'https://www.flickr.com/search/?lat=33.5404756&lon=133.5527511&radius=0.1&has_geo=1&view_all=1'
    complex_photo_200.person = None
    complex_photo_200.title = 'Kōchi'
    complex_photo_200.type_master = complex_type_master_23
    complex_photo_200.username = 'Jan Dreesen'
    complex_photo_200.width = None
    complex_photo_200 = importer.save_or_locate(complex_photo_200)

    complex_photo_201 = Photo()
    complex_photo_201.height = None
    complex_photo_201.image_src = 'https://live.staticflickr.com/417/31638786993_de6a43f139_z.jpg'
    complex_photo_201.link = 'https://www.flickr.com/search/?lat=33.5373806&lon=133.5505423&radius=0.1&has_geo=1&view_all=1'
    complex_photo_201.person = None
    complex_photo_201.title = 'IMG_0337'
    complex_photo_201.type_master = complex_type_master_23
    complex_photo_201.username = 'hiromori'
    complex_photo_201.width = None
    complex_photo_201 = importer.save_or_locate(complex_photo_201)

    complex_photo_202 = Photo()
    complex_photo_202.height = None
    complex_photo_202.image_src = 'https://live.staticflickr.com/65535/50943993261_b4f4cff336_z.jpg'
    complex_photo_202.link = 'https://www.flickr.com/search/?lat=33.521597&lon=133.545798&radius=0.1&has_geo=1&view_all=1'
    complex_photo_202.person = None
    complex_photo_202.title = '温肉ぶっかけ\u3000よがなうどん'
    complex_photo_202.type_master = complex_type_master_23
    complex_photo_202.username = 'yajiro'
    complex_photo_202.width = None
    complex_photo_202 = importer.save_or_locate(complex_photo_202)

    complex_photo_203 = Photo()
    complex_photo_203.height = None
    complex_photo_203.image_src = 'https://live.staticflickr.com/2950/15192990680_73d48b430c_z.jpg'
    complex_photo_203.link = 'https://www.flickr.com/search/?lat=33.4924347&lon=133.5464292&radius=0.1&has_geo=1&view_all=1'
    complex_photo_203.person = None
    complex_photo_203.title = 'Motochika Chosokabe'
    complex_photo_203.type_master = complex_type_master_23
    complex_photo_203.username = 'fjt1986'
    complex_photo_203.width = None
    complex_photo_203 = importer.save_or_locate(complex_photo_203)

    complex_photo_204 = Photo()
    complex_photo_204.height = None
    complex_photo_204.image_src = 'https://live.staticflickr.com/6013/6016875198_40d0ea07d0_z.jpg'
    complex_photo_204.link = 'https://www.flickr.com/search/?lat=33.4930629&lon=133.5462907&radius=0.1&has_geo=1&view_all=1'
    complex_photo_204.person = None
    complex_photo_204.title = '姫若子'
    complex_photo_204.type_master = complex_type_master_23
    complex_photo_204.username = 'jour13'
    complex_photo_204.width = None
    complex_photo_204 = importer.save_or_locate(complex_photo_204)

    complex_photo_205 = Photo()
    complex_photo_205.height = None
    complex_photo_205.image_src = 'https://live.staticflickr.com/65535/51869995174_01855d0574_z.jpg'
    complex_photo_205.link = 'https://www.flickr.com/search/?lat=33.4887778&lon=133.5488726&radius=0.1&has_geo=1&view_all=1'
    complex_photo_205.person = None
    complex_photo_205.title = '20220208 12:00 Nagahama kochi'
    complex_photo_205.type_master = complex_type_master_23
    complex_photo_205.username = 'ichigosugawara'
    complex_photo_205.width = None
    complex_photo_205 = importer.save_or_locate(complex_photo_205)

    complex_photo_206 = Photo()
    complex_photo_206.height = None
    complex_photo_206.image_src = 'https://live.staticflickr.com/65535/52068951434_4fef6054c5_z.jpg'
    complex_photo_206.link = 'https://www.flickr.com/search/?lat=33.4991881&lon=133.5721656&radius=0.1&has_geo=1&view_all=1'
    complex_photo_206.person = None
    complex_photo_206.title = 'Urado Castle ruins (浦戸城跡)'
    complex_photo_206.type_master = complex_type_master_23
    complex_photo_206.username = 'pantkiewicz'
    complex_photo_206.width = None
    complex_photo_206 = importer.save_or_locate(complex_photo_206)

    complex_photo_207 = Photo()
    complex_photo_207.height = None
    complex_photo_207.image_src = 'https://live.staticflickr.com/65535/52068952264_27f3e0e513_z.jpg'
    complex_photo_207.link = 'https://www.flickr.com/search/?lat=33.4969444&lon=133.5736111&radius=0.1&has_geo=1&view_all=1'
    complex_photo_207.person = None
    complex_photo_207.title = 'Urado Castle ruins (浦戸城跡)'
    complex_photo_207.type_master = complex_type_master_23
    complex_photo_207.username = 'pantkiewicz'
    complex_photo_207.width = None
    complex_photo_207 = importer.save_or_locate(complex_photo_207)

    complex_photo_208 = Photo()
    complex_photo_208.height = None
    complex_photo_208.image_src = 'https://live.staticflickr.com/65535/52068937229_51497753c5_z.jpg'
    complex_photo_208.link = 'https://www.flickr.com/search/?lat=33.4956281&lon=133.5746555&radius=0.1&has_geo=1&view_all=1'
    complex_photo_208.person = None
    complex_photo_208.title = 'Ryuo-gu (龍王宮 海津見神社)'
    complex_photo_208.type_master = complex_type_master_23
    complex_photo_208.username = 'pantkiewicz'
    complex_photo_208.width = None
    complex_photo_208 = importer.save_or_locate(complex_photo_208)

    complex_photo_209 = Photo()
    complex_photo_209.height = None
    complex_photo_209.image_src = 'https://live.staticflickr.com/65535/52629856714_a47f9fdb91_z.jpg'
    complex_photo_209.link = 'https://www.flickr.com/search/?lat=33.5664177&lon=133.5430255&radius=0.1&has_geo=1&view_all=1'
    complex_photo_209.person = None
    complex_photo_209.title = 'Tosaden Kochi-Ekimae Station'
    complex_photo_209.type_master = complex_type_master_23
    complex_photo_209.username = 'Kzaral'
    complex_photo_209.width = None
    complex_photo_209 = importer.save_or_locate(complex_photo_209)

    complex_photo_210 = Photo()
    complex_photo_210.height = None
    complex_photo_210.image_src = 'https://live.staticflickr.com/65535/49844540966_ae50115601_z.jpg'
    complex_photo_210.link = 'https://www.flickr.com/search/?lat=33.4250302&lon=134.0180808&radius=0.1&has_geo=1&view_all=1'
    complex_photo_210.person = None
    complex_photo_210.title = 'nahari_20190905093608'
    complex_photo_210.type_master = complex_type_master_23
    complex_photo_210.username = 'inunami'
    complex_photo_210.width = None
    complex_photo_210 = importer.save_or_locate(complex_photo_210)

    complex_photo_211 = Photo()
    complex_photo_211.height = None
    complex_photo_211.image_src = 'https://live.staticflickr.com/65535/52068716838_377865f237_z.jpg'
    complex_photo_211.link = 'https://www.flickr.com/search/?lat=33.4955899&lon=133.5743881&radius=0.1&has_geo=1&view_all=1'
    complex_photo_211.person = None
    complex_photo_211.title = 'Ryuo-gu (龍王宮 海津見神社)'
    complex_photo_211.type_master = complex_type_master_23
    complex_photo_211.username = 'pantkiewicz'
    complex_photo_211.width = None
    complex_photo_211 = importer.save_or_locate(complex_photo_211)

    complex_photo_212 = Photo()
    complex_photo_212.height = None
    complex_photo_212.image_src = 'https://live.staticflickr.com/539/31675873315_f0af2045e2_z.jpg'
    complex_photo_212.link = 'https://www.flickr.com/search/?lat=41.9024872&lon=140.6523709&radius=0.1&has_geo=1&view_all=1'
    complex_photo_212.person = None
    complex_photo_212.title = 'P_20160827_100914'
    complex_photo_212.type_master = complex_type_master_23
    complex_photo_212.username = 'laylamorita'
    complex_photo_212.width = None
    complex_photo_212 = importer.save_or_locate(complex_photo_212)

    complex_photo_213 = Photo()
    complex_photo_213.height = None
    complex_photo_213.image_src = 'https://live.staticflickr.com/65535/52591074063_1b14693a9d_z.jpg'
    complex_photo_213.link = 'https://www.flickr.com/search/?lat=41.77272&lon=140.7255235&radius=0.1&has_geo=1&view_all=1'
    complex_photo_213.person = None
    complex_photo_213.title = '59'
    complex_photo_213.type_master = complex_type_master_23
    complex_photo_213.username = 'Otis Yang'
    complex_photo_213.width = None
    complex_photo_213 = importer.save_or_locate(complex_photo_213)

    complex_photo_214 = Photo()
    complex_photo_214.height = None
    complex_photo_214.image_src = 'https://live.staticflickr.com/65535/52590822239_1628895faa_z.jpg'
    complex_photo_214.link = 'https://www.flickr.com/search/?lat=41.7726202&lon=140.7258098&radius=0.1&has_geo=1&view_all=1'
    complex_photo_214.person = None
    complex_photo_214.title = '60'
    complex_photo_214.type_master = complex_type_master_23
    complex_photo_214.username = 'Otis Yang'
    complex_photo_214.width = None
    complex_photo_214 = importer.save_or_locate(complex_photo_214)

    complex_photo_215 = Photo()
    complex_photo_215.height = None
    complex_photo_215.image_src = 'https://live.staticflickr.com/65535/52608194414_c1ed74f450_z.jpg'
    complex_photo_215.link = 'https://www.flickr.com/search/?lat=41.7673531&lon=140.7176349&radius=0.1&has_geo=1&view_all=1'
    complex_photo_215.person = None
    complex_photo_215.title = 'by @Jean Wu 2013'
    complex_photo_215.type_master = complex_type_master_23
    complex_photo_215.username = 'Jean Wu 2013'
    complex_photo_215.width = None
    complex_photo_215 = importer.save_or_locate(complex_photo_215)

    complex_photo_216 = Photo()
    complex_photo_216.height = None
    complex_photo_216.image_src = 'https://live.staticflickr.com/65535/52590069227_cf56337fc8_z.jpg'
    complex_photo_216.link = 'https://www.flickr.com/search/?lat=41.7659929&lon=140.7146335&radius=0.1&has_geo=1&view_all=1'
    complex_photo_216.person = None
    complex_photo_216.title = '75a'
    complex_photo_216.type_master = complex_type_master_23
    complex_photo_216.username = 'Otis Yang'
    complex_photo_216.width = None
    complex_photo_216 = importer.save_or_locate(complex_photo_216)

    complex_photo_217 = Photo()
    complex_photo_217.height = None
    complex_photo_217.image_src = 'https://live.staticflickr.com/65535/51373178361_b4102b2024_z.jpg'
    complex_photo_217.link = 'https://www.flickr.com/search/?lat=41.7643549&lon=140.7161274&radius=0.1&has_geo=1&view_all=1'
    complex_photo_217.person = None
    complex_photo_217.title = 'DSC_0504'
    complex_photo_217.type_master = complex_type_master_23
    complex_photo_217.username = 'ylefou2004'
    complex_photo_217.width = None
    complex_photo_217 = importer.save_or_locate(complex_photo_217)

    complex_photo_218 = Photo()
    complex_photo_218.height = None
    complex_photo_218.image_src = 'https://live.staticflickr.com/65535/52694122083_432a577397_z.jpg'
    complex_photo_218.link = 'https://www.flickr.com/search/?lat=41.7629356&lon=140.7140386&radius=0.1&has_geo=1&view_all=1'
    complex_photo_218.person = None
    complex_photo_218.title = '633highland, St Johns Church (CC-BY-SA-3.0-migrated), Hakodate, Hokkaido, Japan'
    complex_photo_218.type_master = complex_type_master_23
    complex_photo_218.username = 'ali eminov'
    complex_photo_218.width = None
    complex_photo_218 = importer.save_or_locate(complex_photo_218)

    complex_photo_219 = Photo()
    complex_photo_219.height = None
    complex_photo_219.image_src = 'https://live.staticflickr.com/65535/51568966396_d672f1c502_z.jpg'
    complex_photo_219.link = 'https://www.flickr.com/search/?lat=41.7609078&lon=140.7143007&radius=0.1&has_geo=1&view_all=1'
    complex_photo_219.person = None
    complex_photo_219.title = '_DSC2833'
    complex_photo_219.type_master = complex_type_master_23
    complex_photo_219.username = 'de98lip'
    complex_photo_219.width = None
    complex_photo_219 = importer.save_or_locate(complex_photo_219)

    complex_photo_220 = Photo()
    complex_photo_220.height = None
    complex_photo_220.image_src = 'https://live.staticflickr.com/65535/52019963846_1ac751f20f_z.jpg'
    complex_photo_220.link = 'https://www.flickr.com/search/?lat=41.7757667&lon=140.7856914&radius=0.1&has_geo=1&view_all=1'
    complex_photo_220.person = None
    complex_photo_220.title = 'IMAG6415'
    complex_photo_220.type_master = complex_type_master_23
    complex_photo_220.username = '形影believe'
    complex_photo_220.width = None
    complex_photo_220 = importer.save_or_locate(complex_photo_220)

    complex_photo_221 = Photo()
    complex_photo_221.height = None
    complex_photo_221.image_src = 'https://live.staticflickr.com/3696/11099078126_61d9432550_z.jpg'
    complex_photo_221.link = 'https://www.flickr.com/search/?lat=41.7815466&lon=140.7909432&radius=0.1&has_geo=1&view_all=1'
    complex_photo_221.person = None
    complex_photo_221.title = 'IMG_2794'
    complex_photo_221.type_master = complex_type_master_23
    complex_photo_221.username = 'keizo_t'
    complex_photo_221.width = None
    complex_photo_221 = importer.save_or_locate(complex_photo_221)

    complex_photo_222 = Photo()
    complex_photo_222.height = None
    complex_photo_222.image_src = 'https://live.staticflickr.com/4901/45700351845_db3f442f05_z.jpg'
    complex_photo_222.link = 'https://www.flickr.com/search/?lat=41.7723579&lon=140.7536031&radius=0.1&has_geo=1&view_all=1'
    complex_photo_222.person = None
    complex_photo_222.title = 'Quick stop at Takubokusho Park'
    complex_photo_222.type_master = complex_type_master_23
    complex_photo_222.username = 'Stinkee Beek'
    complex_photo_222.width = None
    complex_photo_222 = importer.save_or_locate(complex_photo_222)

    complex_photo_223 = Photo()
    complex_photo_223.height = None
    complex_photo_223.image_src = 'https://live.staticflickr.com/65535/52020214979_3cba6da620_z.jpg'
    complex_photo_223.link = 'https://www.flickr.com/search/?lat=41.7776852&lon=140.7931866&radius=0.1&has_geo=1&view_all=1'
    complex_photo_223.person = None
    complex_photo_223.title = 'IMAG6430'
    complex_photo_223.type_master = complex_type_master_23
    complex_photo_223.username = '形影believe'
    complex_photo_223.width = None
    complex_photo_223 = importer.save_or_locate(complex_photo_223)

    complex_photo_224 = Photo()
    complex_photo_224.height = None
    complex_photo_224.image_src = 'https://live.staticflickr.com/65535/52018925572_cb93c68cb2_z.jpg'
    complex_photo_224.link = 'https://www.flickr.com/search/?lat=41.7770914&lon=140.7929599&radius=0.1&has_geo=1&view_all=1'
    complex_photo_224.person = None
    complex_photo_224.title = 'IMAG6432'
    complex_photo_224.type_master = complex_type_master_23
    complex_photo_224.username = '形影believe'
    complex_photo_224.width = None
    complex_photo_224 = importer.save_or_locate(complex_photo_224)

    complex_photo_225 = Photo()
    complex_photo_225.height = None
    complex_photo_225.image_src = 'https://live.staticflickr.com/65535/50987897093_9e724a25ea_z.jpg'
    complex_photo_225.link = 'https://www.flickr.com/search/?lat=41.7741951&lon=140.7883462&radius=0.1&has_geo=1&view_all=1'
    complex_photo_225.person = None
    complex_photo_225.title = 'サル'
    complex_photo_225.type_master = complex_type_master_23
    complex_photo_225.username = 'Chitaka Chou'
    complex_photo_225.width = None
    complex_photo_225 = importer.save_or_locate(complex_photo_225)

    complex_photo_226 = Photo()
    complex_photo_226.height = None
    complex_photo_226.image_src = 'https://live.staticflickr.com/1958/44915848902_f4cfc34975_z.jpg'
    complex_photo_226.link = 'https://www.flickr.com/search/?lat=41.7731667&lon=140.7874485&radius=0.1&has_geo=1&view_all=1'
    complex_photo_226.person = None
    complex_photo_226.title = 'IMG20180204113532'
    complex_photo_226.type_master = complex_type_master_23
    complex_photo_226.username = 'redice0112'
    complex_photo_226.width = None
    complex_photo_226 = importer.save_or_locate(complex_photo_226)

    complex_photo_227 = Photo()
    complex_photo_227.height = None
    complex_photo_227.image_src = 'https://live.staticflickr.com/65535/52020215794_f2e0e31d2e_z.jpg'
    complex_photo_227.link = 'https://www.flickr.com/search/?lat=41.7748933&lon=140.7878883&radius=0.1&has_geo=1&view_all=1'
    complex_photo_227.person = None
    complex_photo_227.title = 'IMAG6411'
    complex_photo_227.type_master = complex_type_master_23
    complex_photo_227.username = '形影believe'
    complex_photo_227.width = None
    complex_photo_227 = importer.save_or_locate(complex_photo_227)

    complex_photo_228 = Photo()
    complex_photo_228.height = None
    complex_photo_228.image_src = 'https://live.staticflickr.com/7005/27302570501_2c87ae78e7_z.jpg'
    complex_photo_228.link = 'https://www.flickr.com/search/?lat=41.7736848&lon=140.7572748&radius=0.1&has_geo=1&view_all=1'
    complex_photo_228.person = None
    complex_photo_228.title = 'DSC01096'
    complex_photo_228.type_master = complex_type_master_23
    complex_photo_228.username = '騰子'
    complex_photo_228.width = None
    complex_photo_228 = importer.save_or_locate(complex_photo_228)

    complex_photo_229 = Photo()
    complex_photo_229.height = None
    complex_photo_229.image_src = 'https://live.staticflickr.com/4916/31785169657_bdee66b579_z.jpg'
    complex_photo_229.link = 'https://www.flickr.com/search/?lat=41.7727805&lon=140.7530528&radius=0.1&has_geo=1&view_all=1'
    complex_photo_229.person = None
    complex_photo_229.title = 'Ishikawa Takuboku in Hakodate / 函館の啄木'
    complex_photo_229.type_master = complex_type_master_23
    complex_photo_229.username = 'yanoks48'
    complex_photo_229.width = None
    complex_photo_229 = importer.save_or_locate(complex_photo_229)

    complex_photo_230 = Photo()
    complex_photo_230.height = None
    complex_photo_230.image_src = 'https://live.staticflickr.com/7839/46614820461_09cfe120ba_z.jpg'
    complex_photo_230.link = 'https://www.flickr.com/search/?lat=41.7725071&lon=140.754053&radius=0.1&has_geo=1&view_all=1'
    complex_photo_230.person = None
    complex_photo_230.title = 'Quick stop at Takubokusho Park'
    complex_photo_230.type_master = complex_type_master_23
    complex_photo_230.username = 'Stinkee Beek'
    complex_photo_230.width = None
    complex_photo_230 = importer.save_or_locate(complex_photo_230)

    complex_photo_231 = Photo()
    complex_photo_231.height = None
    complex_photo_231.image_src = 'https://live.staticflickr.com/1925/44915848522_386c0ce707_z.jpg'
    complex_photo_231.link = 'https://www.flickr.com/search/?lat=41.770788&lon=140.745451&radius=0.1&has_geo=1&view_all=1'
    complex_photo_231.person = None
    complex_photo_231.title = 'IMG20180204135907'
    complex_photo_231.type_master = complex_type_master_23
    complex_photo_231.username = 'redice0112'
    complex_photo_231.width = None
    complex_photo_231 = importer.save_or_locate(complex_photo_231)

    complex_photo_232 = Photo()
    complex_photo_232.height = None
    complex_photo_232.image_src = 'https://live.staticflickr.com/65535/50074882542_30b0baceb7_z.jpg'
    complex_photo_232.link = 'https://www.flickr.com/search/?lat=41.7697786&lon=140.7404156&radius=0.1&has_geo=1&view_all=1'
    complex_photo_232.person = None
    complex_photo_232.title = '函館市電 39 ハイカラ号の絵'
    complex_photo_232.type_master = complex_type_master_23
    complex_photo_232.username = 'OOMYV'
    complex_photo_232.width = None
    complex_photo_232 = importer.save_or_locate(complex_photo_232)

    complex_photo_233 = Photo()
    complex_photo_233.height = None
    complex_photo_233.image_src = 'https://live.staticflickr.com/4536/26468861439_b0ba4e45e2_z.jpg'
    complex_photo_233.link = 'https://www.flickr.com/search/?lat=41.7474858&lon=140.7194496&radius=0.1&has_geo=1&view_all=1'
    complex_photo_233.person = None
    complex_photo_233.title = '北海道 函館 Hakodate, Hokkaido, Japan'
    complex_photo_233.type_master = complex_type_master_23
    complex_photo_233.username = 'スーパーサイヤ人Ⅳ'
    complex_photo_233.width = None
    complex_photo_233 = importer.save_or_locate(complex_photo_233)

    complex_photo_234 = Photo()
    complex_photo_234.height = None
    complex_photo_234.image_src = 'https://live.staticflickr.com/65535/51971873627_603eac0afc_z.jpg'
    complex_photo_234.link = 'https://www.flickr.com/search/?lat=41.7450354&lon=140.7212027&radius=0.1&has_geo=1&view_all=1'
    complex_photo_234.person = None
    complex_photo_234.title = 'Tsugaru Strait'
    complex_photo_234.type_master = complex_type_master_23
    complex_photo_234.username = '雷太'
    complex_photo_234.width = None
    complex_photo_234 = importer.save_or_locate(complex_photo_234)

    complex_photo_235 = Photo()
    complex_photo_235.height = None
    complex_photo_235.image_src = 'https://live.staticflickr.com/2836/33854197531_0cd60ea893_z.jpg'
    complex_photo_235.link = 'https://www.flickr.com/search/?lat=42.063333&lon=140.677222&radius=0.1&has_geo=1&view_all=1'
    complex_photo_235.person = None
    complex_photo_235.title = 'こまがたけ'
    complex_photo_235.type_master = complex_type_master_23
    complex_photo_235.username = 'fox_kawai'
    complex_photo_235.width = None
    complex_photo_235 = importer.save_or_locate(complex_photo_235)

    complex_photo_236 = Photo()
    complex_photo_236.height = None
    complex_photo_236.image_src = 'https://live.staticflickr.com/65535/50659827081_9b647d4562_z.jpg'
    complex_photo_236.link = 'https://www.flickr.com/search/?lat=41.9889583&lon=140.6668324&radius=0.1&has_geo=1&view_all=1'
    complex_photo_236.person = None
    complex_photo_236.title = 'Running along the raod.'
    complex_photo_236.type_master = complex_type_master_23
    complex_photo_236.username = 'Matt-The Mechanic'
    complex_photo_236.width = None
    complex_photo_236 = importer.save_or_locate(complex_photo_236)

    complex_photo_237 = Photo()
    complex_photo_237.height = None
    complex_photo_237.image_src = 'https://live.staticflickr.com/65535/50848642138_75718ccdbd_z.jpg'
    complex_photo_237.link = 'https://www.flickr.com/search/?lat=44.3067562&lon=143.4067317&radius=0.1&has_geo=1&view_all=1'
    complex_photo_237.person = None
    complex_photo_237.title = 'monbetsu_20201008122441'
    complex_photo_237.type_master = complex_type_master_23
    complex_photo_237.username = 'inunami'
    complex_photo_237.width = None
    complex_photo_237 = importer.save_or_locate(complex_photo_237)

    complex_photo_238 = Photo()
    complex_photo_238.height = None
    complex_photo_238.image_src = 'https://live.staticflickr.com/65535/51430924232_96879b9a13_z.jpg'
    complex_photo_238.link = 'https://www.flickr.com/search/?lat=35.6978467&lon=139.7442465&radius=0.1&has_geo=1&view_all=1'
    complex_photo_238.person = None
    complex_photo_238.title = 'JP029 Awajicho'
    complex_photo_238.type_master = complex_type_master_23
    complex_photo_238.username = '@oyajimbo'
    complex_photo_238.width = None
    complex_photo_238 = importer.save_or_locate(complex_photo_238)

    complex_photo_239 = Photo()
    complex_photo_239.height = None
    complex_photo_239.image_src = 'https://live.staticflickr.com/1897/43515868224_95bb4c0496_z.jpg'
    complex_photo_239.link = 'https://www.flickr.com/search/?lat=44.1106685&lon=144.2473548&radius=0.1&has_geo=1&view_all=1'
    complex_photo_239.person = None
    complex_photo_239.title = 'L1009111'
    complex_photo_239.type_master = complex_type_master_23
    complex_photo_239.username = 'bluepointchen'
    complex_photo_239.width = None
    complex_photo_239 = importer.save_or_locate(complex_photo_239)

    complex_photo_240 = Photo()
    complex_photo_240.height = None
    complex_photo_240.image_src = 'https://live.staticflickr.com/65535/52774550021_c43cc990e7_z.jpg'
    complex_photo_240.link = 'https://www.flickr.com/search/?lat=44.0124153&lon=144.1156977&radius=0.1&has_geo=1&view_all=1'
    complex_photo_240.person = None
    complex_photo_240.title = 'Black Eared Kite - Milvus migrans'
    complex_photo_240.type_master = complex_type_master_23
    complex_photo_240.username = 'adn_no'
    complex_photo_240.width = None
    complex_photo_240 = importer.save_or_locate(complex_photo_240)

    complex_photo_241 = Photo()
    complex_photo_241.height = None
    complex_photo_241.image_src = 'https://live.staticflickr.com/65535/51755152460_dcb21bb5c4_z.jpg'
    complex_photo_241.link = 'https://www.flickr.com/search/?lat=44.013852&lon=144.1167037&radius=0.1&has_geo=1&view_all=1'
    complex_photo_241.person = None
    complex_photo_241.title = 'Common glasswort around Lake Notoro,Abashiri city,Hokkaido 2021/09 No.5.'
    complex_photo_241.type_master = complex_type_master_23
    complex_photo_241.username = 'HIDE@Verdad'
    complex_photo_241.width = None
    complex_photo_241 = importer.save_or_locate(complex_photo_241)

    complex_photo_242 = Photo()
    complex_photo_242.height = None
    complex_photo_242.image_src = 'https://live.staticflickr.com/65535/50897590677_e80e2d3764_z.jpg'
    complex_photo_242.link = 'https://www.flickr.com/search/?lat=44.1133485&lon=144.2434854&radius=0.1&has_geo=1&view_all=1'
    complex_photo_242.person = None
    complex_photo_242.title = '20210201 15:01 Abashiri Hokkaido'
    complex_photo_242.type_master = complex_type_master_23
    complex_photo_242.username = 'ichigosugawara'
    complex_photo_242.width = None
    complex_photo_242 = importer.save_or_locate(complex_photo_242)

    complex_photo_243 = Photo()
    complex_photo_243.height = None
    complex_photo_243.image_src = 'https://live.staticflickr.com/65535/51373902734_fa09d51cd3_z.jpg'
    complex_photo_243.link = 'https://www.flickr.com/search/?lat=44.1121076&lon=144.2432936&radius=0.1&has_geo=1&view_all=1'
    complex_photo_243.person = None
    complex_photo_243.title = 'DSC_0222'
    complex_photo_243.type_master = complex_type_master_23
    complex_photo_243.username = 'ylefou2004'
    complex_photo_243.width = None
    complex_photo_243 = importer.save_or_locate(complex_photo_243)

    complex_photo_244 = Photo()
    complex_photo_244.height = None
    complex_photo_244.image_src = 'https://live.staticflickr.com/65535/50387289793_30abd477db_z.jpg'
    complex_photo_244.link = 'https://www.flickr.com/search/?lat=44.069034&lon=144.990695&radius=0.1&has_geo=1&view_all=1'
    complex_photo_244.person = None
    complex_photo_244.title = 'ウトロ港'
    complex_photo_244.type_master = complex_type_master_23
    complex_photo_244.username = 'Chitaka Chou'
    complex_photo_244.width = None
    complex_photo_244 = importer.save_or_locate(complex_photo_244)

    complex_photo_245 = Photo()
    complex_photo_245.height = None
    complex_photo_245.image_src = 'https://live.staticflickr.com/65535/49140018113_177eedfa74_z.jpg'
    complex_photo_245.link = 'https://www.flickr.com/search/?lat=44.0916901&lon=145.0251744&radius=0.1&has_geo=1&view_all=1'
    complex_photo_245.person = None
    complex_photo_245.title = '36261-Shiretoko'
    complex_photo_245.type_master = complex_type_master_23
    complex_photo_245.username = 'xiquinhosilva'
    complex_photo_245.width = None
    complex_photo_245 = importer.save_or_locate(complex_photo_245)

    complex_photo_246 = Photo()
    complex_photo_246.height = None
    complex_photo_246.image_src = 'https://live.staticflickr.com/65535/50103164102_ea594a813c_z.jpg'
    complex_photo_246.link = 'https://www.flickr.com/search/?lat=44.0757686&lon=145.1221149&radius=0.1&has_geo=1&view_all=1'
    complex_photo_246.person = None
    complex_photo_246.title = 'Sunset over Mt. Rausu'
    complex_photo_246.type_master = complex_type_master_23
    complex_photo_246.username = 'hermitvoita'
    complex_photo_246.width = None
    complex_photo_246 = importer.save_or_locate(complex_photo_246)

    complex_photo_247 = Photo()
    complex_photo_247.height = None
    complex_photo_247.image_src = 'https://live.staticflickr.com/65535/52021648039_38f4e134fb_z.jpg'
    complex_photo_247.link = 'https://www.flickr.com/search/?lat=44.0852361&lon=145.0108433&radius=0.1&has_geo=1&view_all=1'
    complex_photo_247.person = None
    complex_photo_247.title = '知床'
    complex_photo_247.type_master = complex_type_master_23
    complex_photo_247.username = 'Chitaka Chou'
    complex_photo_247.width = None
    complex_photo_247 = importer.save_or_locate(complex_photo_247)

    complex_photo_248 = Photo()
    complex_photo_248.height = None
    complex_photo_248.image_src = 'https://live.staticflickr.com/704/22071845355_6cfcfd6ac2_z.jpg'
    complex_photo_248.link = 'https://www.flickr.com/search/?lat=43.7597063&lon=143.5082092&radius=0.1&has_geo=1&view_all=1'
    complex_photo_248.person = None
    complex_photo_248.title = 'by @lovelva416'
    complex_photo_248.type_master = complex_type_master_23
    complex_photo_248.username = 'lovelva416'
    complex_photo_248.width = None
    complex_photo_248 = importer.save_or_locate(complex_photo_248)

    complex_photo_249 = Photo()
    complex_photo_249.height = None
    complex_photo_249.image_src = 'https://live.staticflickr.com/7042/14058398356_c15ba22f7f_z.jpg'
    complex_photo_249.link = 'https://www.flickr.com/search/?lat=35.5857414&lon=139.69341&radius=0.1&has_geo=1&view_all=1'
    complex_photo_249.person = None
    complex_photo_249.title = 'IMG_1961'
    complex_photo_249.type_master = complex_type_master_23
    complex_photo_249.username = 'smallcake1982'
    complex_photo_249.width = None
    complex_photo_249 = importer.save_or_locate(complex_photo_249)

    complex_photo_250 = Photo()
    complex_photo_250.height = None
    complex_photo_250.image_src = 'https://live.staticflickr.com/65535/52614588130_90a7031bc2_z.jpg'
    complex_photo_250.link = 'https://www.flickr.com/search/?lat=34.9025647&lon=139.8876262&radius=0.1&has_geo=1&view_all=1'
    complex_photo_250.person = None
    complex_photo_250.title = '野島崎灯台'
    complex_photo_250.type_master = complex_type_master_23
    complex_photo_250.username = 'BlueSky_s'
    complex_photo_250.width = None
    complex_photo_250 = importer.save_or_locate(complex_photo_250)

    complex_photo_251 = Photo()
    complex_photo_251.height = None
    complex_photo_251.image_src = 'https://live.staticflickr.com/959/27431164097_3d5c00b51b_z.jpg'
    complex_photo_251.link = 'https://www.flickr.com/search/?lat=34.9767087&lon=139.9547124&radius=0.1&has_geo=1&view_all=1'
    complex_photo_251.person = None
    complex_photo_251.title = 'DSCF5060'
    complex_photo_251.type_master = complex_type_master_23
    complex_photo_251.username = 'yugo.sakai'
    complex_photo_251.width = None
    complex_photo_251 = importer.save_or_locate(complex_photo_251)

    complex_photo_252 = Photo()
    complex_photo_252.height = None
    complex_photo_252.image_src = 'https://live.staticflickr.com/5066/5674612095_9c5fabc6ac_z.jpg'
    complex_photo_252.link = 'https://www.flickr.com/search/?lat=34.973351&lon=139.962721&radius=0.1&has_geo=1&view_all=1'
    complex_photo_252.person = None
    complex_photo_252.title = 'by @y_orima'
    complex_photo_252.type_master = complex_type_master_23
    complex_photo_252.username = 'y_orima'
    complex_photo_252.width = None
    complex_photo_252 = importer.save_or_locate(complex_photo_252)

    complex_photo_253 = Photo()
    complex_photo_253.height = None
    complex_photo_253.image_src = 'https://live.staticflickr.com/65535/52437208629_d5e5f155bd_z.jpg'
    complex_photo_253.link = 'https://www.flickr.com/search/?lat=34.9638919&lon=139.9596901&radius=0.1&has_geo=1&view_all=1'
    complex_photo_253.person = None
    complex_photo_253.title = 'כי הארץ מלאה באלימות דרכם'
    complex_photo_253.type_master = complex_type_master_23
    complex_photo_253.username = 'feeblefolk'
    complex_photo_253.width = None
    complex_photo_253 = importer.save_or_locate(complex_photo_253)

    complex_photo_254 = Photo()
    complex_photo_254.height = None
    complex_photo_254.image_src = 'https://live.staticflickr.com/903/28427314358_c36f1116c7_z.jpg'
    complex_photo_254.link = 'https://www.flickr.com/search/?lat=34.976704&lon=139.9545765&radius=0.1&has_geo=1&view_all=1'
    complex_photo_254.person = None
    complex_photo_254.title = 'IMG_9259'
    complex_photo_254.type_master = complex_type_master_23
    complex_photo_254.username = 'yugo.sakai'
    complex_photo_254.width = None
    complex_photo_254 = importer.save_or_locate(complex_photo_254)

    complex_photo_255 = Photo()
    complex_photo_255.height = None
    complex_photo_255.image_src = 'https://live.staticflickr.com/65535/52669758952_598664eba6_z.jpg'
    complex_photo_255.link = 'https://www.flickr.com/search/?lat=34.9602825&lon=139.9593564&radius=0.1&has_geo=1&view_all=1'
    complex_photo_255.person = None
    complex_photo_255.title = '230103_126'
    complex_photo_255.type_master = complex_type_master_23
    complex_photo_255.username = 'Matsui Hiroyuki'
    complex_photo_255.width = None
    complex_photo_255 = importer.save_or_locate(complex_photo_255)

    complex_photo_256 = Photo()
    complex_photo_256.height = None
    complex_photo_256.image_src = 'https://live.staticflickr.com/65535/52670759198_6f274bec66_z.jpg'
    complex_photo_256.link = 'https://www.flickr.com/search/?lat=34.95936&lon=139.9592&radius=0.1&has_geo=1&view_all=1'
    complex_photo_256.person = None
    complex_photo_256.title = '230103_149'
    complex_photo_256.type_master = complex_type_master_23
    complex_photo_256.username = 'Matsui Hiroyuki'
    complex_photo_256.width = None
    complex_photo_256 = importer.save_or_locate(complex_photo_256)

    complex_photo_257 = Photo()
    complex_photo_257.height = None
    complex_photo_257.image_src = 'https://live.staticflickr.com/65535/52669758662_f7e0311d2d_z.jpg'
    complex_photo_257.link = 'https://www.flickr.com/search/?lat=34.9578678&lon=139.9590959&radius=0.1&has_geo=1&view_all=1'
    complex_photo_257.person = None
    complex_photo_257.title = '230103_141'
    complex_photo_257.type_master = complex_type_master_23
    complex_photo_257.username = 'Matsui Hiroyuki'
    complex_photo_257.width = None
    complex_photo_257 = importer.save_or_locate(complex_photo_257)

    complex_photo_258 = Photo()
    complex_photo_258.height = None
    complex_photo_258.image_src = 'https://live.staticflickr.com/65535/52614419439_1461bfca62_z.jpg'
    complex_photo_258.link = 'https://www.flickr.com/search/?lat=34.9003949&lon=139.8880755&radius=0.1&has_geo=1&view_all=1'
    complex_photo_258.person = None
    complex_photo_258.title = '野島崎'
    complex_photo_258.type_master = complex_type_master_23
    complex_photo_258.username = 'BlueSky_s'
    complex_photo_258.width = None
    complex_photo_258 = importer.save_or_locate(complex_photo_258)

    complex_photo_259 = Photo()
    complex_photo_259.height = None
    complex_photo_259.image_src = 'https://live.staticflickr.com/65535/51735519668_e63f7b58e3_z.jpg'
    complex_photo_259.link = 'https://www.flickr.com/search/?lat=35.1681316&lon=139.8222539&radius=0.1&has_geo=1&view_all=1'
    complex_photo_259.person = None
    complex_photo_259.title = 'Kanaya#3'
    complex_photo_259.type_master = complex_type_master_23
    complex_photo_259.username = 'tetsuo5'
    complex_photo_259.width = None
    complex_photo_259 = importer.save_or_locate(complex_photo_259)

    complex_photo_260 = Photo()
    complex_photo_260.height = None
    complex_photo_260.image_src = 'https://live.staticflickr.com/65535/50527211156_2c46ed6036_z.jpg'
    complex_photo_260.link = 'https://www.flickr.com/search/?lat=35.1622171&lon=139.8230802&radius=0.1&has_geo=1&view_all=1'
    complex_photo_260.person = None
    complex_photo_260.title = 'R0010323_xmp'
    complex_photo_260.type_master = complex_type_master_23
    complex_photo_260.username = 'few0010'
    complex_photo_260.width = None
    complex_photo_260 = importer.save_or_locate(complex_photo_260)

    complex_photo_261 = Photo()
    complex_photo_261.height = None
    complex_photo_261.image_src = 'https://live.staticflickr.com/65535/51771699776_a51bf3b83d_z.jpg'
    complex_photo_261.link = 'https://www.flickr.com/search/?lat=35.1584928&lon=139.8284768&radius=0.1&has_geo=1&view_all=1'
    complex_photo_261.person = None
    complex_photo_261.title = 'View from Mount Nokogiri (Futtsu/Kyonan, Chiba, Japan)'
    complex_photo_261.type_master = complex_type_master_23
    complex_photo_261.username = 't-mizo'
    complex_photo_261.width = None
    complex_photo_261 = importer.save_or_locate(complex_photo_261)

    complex_photo_262 = Photo()
    complex_photo_262.height = None
    complex_photo_262.image_src = 'https://live.staticflickr.com/65535/51771714521_05cfa26a92_z.jpg'
    complex_photo_262.link = 'https://www.flickr.com/search/?lat=35.1582302&lon=139.8308355&radius=0.1&has_geo=1&view_all=1'
    complex_photo_262.person = None
    complex_photo_262.title = 'Nihon-ji on Mount Nokogiri (Futtsu/Kyonan, Chiba, Japan)'
    complex_photo_262.type_master = complex_type_master_23
    complex_photo_262.username = 't-mizo'
    complex_photo_262.width = None
    complex_photo_262 = importer.save_or_locate(complex_photo_262)

    complex_photo_263 = Photo()
    complex_photo_263.height = None
    complex_photo_263.image_src = 'https://live.staticflickr.com/65535/52725142574_a6eb489c72_z.jpg'
    complex_photo_263.link = 'https://www.flickr.com/search/?lat=35.1591666&lon=139.8326737&radius=0.1&has_geo=1&view_all=1'
    complex_photo_263.person = None
    complex_photo_263.title = '鋸山 地獄覗き'
    complex_photo_263.type_master = complex_type_master_23
    complex_photo_263.username = 'BlueSky_s'
    complex_photo_263.width = None
    complex_photo_263 = importer.save_or_locate(complex_photo_263)

    complex_photo_264 = Photo()
    complex_photo_264.height = None
    complex_photo_264.image_src = 'https://live.staticflickr.com/65535/52725365908_c6742123b9_z.jpg'
    complex_photo_264.link = 'https://www.flickr.com/search/?lat=35.1590417&lon=139.8329306&radius=0.1&has_geo=1&view_all=1'
    complex_photo_264.person = None
    complex_photo_264.title = '鋸山 岩舞台'
    complex_photo_264.type_master = complex_type_master_23
    complex_photo_264.username = 'BlueSky_s'
    complex_photo_264.width = None
    complex_photo_264 = importer.save_or_locate(complex_photo_264)

    complex_photo_265 = Photo()
    complex_photo_265.height = None
    complex_photo_265.image_src = 'https://live.staticflickr.com/65535/52724888081_2f147df3c5_z.jpg'
    complex_photo_265.link = 'https://www.flickr.com/search/?lat=35.1592647&lon=139.8331931&radius=0.1&has_geo=1&view_all=1'
    complex_photo_265.person = None
    complex_photo_265.title = '鋸山 観音洞窟'
    complex_photo_265.type_master = complex_type_master_23
    complex_photo_265.username = 'BlueSky_s'
    complex_photo_265.width = None
    complex_photo_265 = importer.save_or_locate(complex_photo_265)

    complex_photo_266 = Photo()
    complex_photo_266.height = None
    complex_photo_266.image_src = 'https://live.staticflickr.com/65535/52285002229_d2d7d8ce62_z.jpg'
    complex_photo_266.link = 'https://www.flickr.com/search/?lat=35.1581159&lon=139.8328907&radius=0.1&has_geo=1&view_all=1'
    complex_photo_266.person = None
    complex_photo_266.title = 'Mt. Nokogiriyama, Chiba, JAPAN'
    complex_photo_266.type_master = complex_type_master_23
    complex_photo_266.username = 'oisaki'
    complex_photo_266.width = None
    complex_photo_266 = importer.save_or_locate(complex_photo_266)

    complex_photo_267 = Photo()
    complex_photo_267.height = None
    complex_photo_267.image_src = 'https://live.staticflickr.com/65535/52726032041_3c60e38872_z.jpg'
    complex_photo_267.link = 'https://www.flickr.com/search/?lat=35.1588017&lon=139.8344269&radius=0.1&has_geo=1&view_all=1'
    complex_photo_267.person = None
    complex_photo_267.title = '鋸山 切り通し跡'
    complex_photo_267.type_master = complex_type_master_23
    complex_photo_267.username = 'BlueSky_s'
    complex_photo_267.width = None
    complex_photo_267 = importer.save_or_locate(complex_photo_267)

    complex_photo_268 = Photo()
    complex_photo_268.height = None
    complex_photo_268.image_src = 'https://live.staticflickr.com/65535/51782939679_b8036cfcd3_z.jpg'
    complex_photo_268.link = 'https://www.flickr.com/search/?lat=35.1576699&lon=139.8346891&radius=0.1&has_geo=1&view_all=1'
    complex_photo_268.person = None
    complex_photo_268.title = 'B/W #1769'
    complex_photo_268.type_master = complex_type_master_23
    complex_photo_268.username = 'Ville Misaki'
    complex_photo_268.width = None
    complex_photo_268 = importer.save_or_locate(complex_photo_268)

    complex_photo_269 = Photo()
    complex_photo_269.height = None
    complex_photo_269.image_src = 'https://live.staticflickr.com/65535/50618657233_68eacd1bdc_z.jpg'
    complex_photo_269.link = 'https://www.flickr.com/search/?lat=34.9002208&lon=139.8882015&radius=0.1&has_geo=1&view_all=1'
    complex_photo_269.person = None
    complex_photo_269.title = 'R0011417 パノラマ'
    complex_photo_269.type_master = complex_type_master_23
    complex_photo_269.username = 'TAKUMA KIMURA'
    complex_photo_269.width = None
    complex_photo_269 = importer.save_or_locate(complex_photo_269)

    complex_photo_270 = Photo()
    complex_photo_270.height = None
    complex_photo_270.image_src = 'https://live.staticflickr.com/65535/52257400724_a719e7f067_z.jpg'
    complex_photo_270.link = 'https://www.flickr.com/search/?lat=35.6687078&lon=138.5193729&radius=0.1&has_geo=1&view_all=1'
    complex_photo_270.person = None
    complex_photo_270.title = 'Today’s dinner - Jul. 30, 2022'
    complex_photo_270.type_master = complex_type_master_23
    complex_photo_270.username = 'miko0219'
    complex_photo_270.width = None
    complex_photo_270 = importer.save_or_locate(complex_photo_270)

    complex_photo_271 = Photo()
    complex_photo_271.height = None
    complex_photo_271.image_src = 'https://live.staticflickr.com/6040/6263141869_2fd6ff0071_z.jpg'
    complex_photo_271.link = 'https://www.flickr.com/search/?lat=35.6684556&lon=138.5022428&radius=0.1&has_geo=1&view_all=1'
    complex_photo_271.person = None
    complex_photo_271.title = 'Two'
    complex_photo_271.type_master = complex_type_master_23
    complex_photo_271.username = 'asksomeoneelse'
    complex_photo_271.width = None
    complex_photo_271 = importer.save_or_locate(complex_photo_271)

    complex_photo_272 = Photo()
    complex_photo_272.height = None
    complex_photo_272.image_src = 'https://live.staticflickr.com/65535/52439343938_3a10557436_z.jpg'
    complex_photo_272.link = 'https://www.flickr.com/search/?lat=35.6667113&lon=138.5180877&radius=0.1&has_geo=1&view_all=1'
    complex_photo_272.person = None
    complex_photo_272.title = '甲州道中(甲府柳町宿〜韮崎宿)'
    complex_photo_272.type_master = complex_type_master_23
    complex_photo_272.username = 'cyberwonk'
    complex_photo_272.width = None
    complex_photo_272 = importer.save_or_locate(complex_photo_272)

    complex_photo_273 = Photo()
    complex_photo_273.height = None
    complex_photo_273.image_src = 'https://live.staticflickr.com/2440/3540651804_82cc689bbc_z.jpg'
    complex_photo_273.link = 'https://www.flickr.com/search/?lat=35.6678647&lon=138.5078418&radius=0.1&has_geo=1&view_all=1'
    complex_photo_273.person = None
    complex_photo_273.title = 'Mount Fuji viewed from the train'
    complex_photo_273.type_master = complex_type_master_23
    complex_photo_273.username = 'mutantlog'
    complex_photo_273.width = None
    complex_photo_273 = importer.save_or_locate(complex_photo_273)

    complex_photo_274 = Photo()
    complex_photo_274.height = None
    complex_photo_274.image_src = 'https://live.staticflickr.com/5099/5491783662_eee49301b7_z.jpg'
    complex_photo_274.link = 'https://www.flickr.com/search/?lat=35.6677185&lon=138.5043247&radius=0.1&has_geo=1&view_all=1'
    complex_photo_274.person = None
    complex_photo_274.title = 'Store that tractor'
    complex_photo_274.type_master = complex_type_master_23
    complex_photo_274.username = 'asksomeoneelse'
    complex_photo_274.width = None
    complex_photo_274 = importer.save_or_locate(complex_photo_274)

    complex_photo_275 = Photo()
    complex_photo_275.height = None
    complex_photo_275.image_src = 'https://live.staticflickr.com/8431/7872839364_a3c3f05032_z.jpg'
    complex_photo_275.link = 'https://www.flickr.com/search/?lat=35.6641283&lon=138.502834&radius=0.1&has_geo=1&view_all=1'
    complex_photo_275.person = None
    complex_photo_275.title = 'IMG_3449.JPG'
    complex_photo_275.type_master = complex_type_master_23
    complex_photo_275.username = 'drillhidea'
    complex_photo_275.width = None
    complex_photo_275 = importer.save_or_locate(complex_photo_275)

    complex_photo_276 = Photo()
    complex_photo_276.height = None
    complex_photo_276.image_src = 'https://live.staticflickr.com/3781/12876991584_d45f163206_z.jpg'
    complex_photo_276.link = 'https://www.flickr.com/search/?lat=35.6581298&lon=138.4410014&radius=0.1&has_geo=1&view_all=1'
    complex_photo_276.person = None
    complex_photo_276.title = 'IMG_0001'
    complex_photo_276.type_master = complex_type_master_23
    complex_photo_276.username = 'K,Nakamura'
    complex_photo_276.width = None
    complex_photo_276 = importer.save_or_locate(complex_photo_276)

    complex_photo_277 = Photo()
    complex_photo_277.height = None
    complex_photo_277.image_src = 'https://live.staticflickr.com/65535/52652539975_e7f96efbd4_z.jpg'
    complex_photo_277.link = 'https://www.flickr.com/search/?lat=35.6668252&lon=138.5680188&radius=0.1&has_geo=1&view_all=1'
    complex_photo_277.person = None
    complex_photo_277.title = 'minobu_line_20220903153011'
    complex_photo_277.type_master = complex_type_master_23
    complex_photo_277.username = 'inunami'
    complex_photo_277.width = None
    complex_photo_277 = importer.save_or_locate(complex_photo_277)

    complex_photo_278 = Photo()
    complex_photo_278.height = None
    complex_photo_278.image_src = 'https://live.staticflickr.com/4753/39732007272_050f1228c6_z.jpg'
    complex_photo_278.link = 'https://www.flickr.com/search/?lat=31.5570611&lon=130.7033157&radius=0.1&has_geo=1&view_all=1'
    complex_photo_278.person = None
    complex_photo_278.title = '20120220-_DSC6318'
    complex_photo_278.type_master = complex_type_master_23
    complex_photo_278.username = 'Fomal Haut'
    complex_photo_278.width = None
    complex_photo_278 = importer.save_or_locate(complex_photo_278)

    complex_photo_279 = Photo()
    complex_photo_279.height = None
    complex_photo_279.image_src = 'https://live.staticflickr.com/65535/50793380102_8822e6275a_z.jpg'
    complex_photo_279.link = 'https://www.flickr.com/search/?lat=31.586563&lon=130.5461068&radius=0.1&has_geo=1&view_all=1'
    complex_photo_279.person = None
    complex_photo_279.title = '鹿児島路面電車'
    complex_photo_279.type_master = complex_type_master_23
    complex_photo_279.username = 'Chitaka Chou'
    complex_photo_279.width = None
    complex_photo_279 = importer.save_or_locate(complex_photo_279)

    complex_photo_280 = Photo()
    complex_photo_280.height = None
    complex_photo_280.image_src = 'https://live.staticflickr.com/65535/50188804221_aa97551593_z.jpg'
    complex_photo_280.link = 'https://www.flickr.com/search/?lat=31.5869927&lon=130.5472233&radius=0.1&has_geo=1&view_all=1'
    complex_photo_280.person = None
    complex_photo_280.title = 'Memorial on bridge'
    complex_photo_280.type_master = complex_type_master_23
    complex_photo_280.username = 'JohnSeb'
    complex_photo_280.width = None
    complex_photo_280 = importer.save_or_locate(complex_photo_280)

    complex_photo_281 = Photo()
    complex_photo_281.height = None
    complex_photo_281.image_src = 'https://live.staticflickr.com/65535/52616691953_aae7e7364a_z.jpg'
    complex_photo_281.link = 'https://www.flickr.com/search/?lat=31.5889911&lon=130.5510241&radius=0.1&has_geo=1&view_all=1'
    complex_photo_281.person = None
    complex_photo_281.title = 'Kagoshima Tram, Kyushu, Japan'
    complex_photo_281.type_master = complex_type_master_23
    complex_photo_281.username = 'globetrekimages'
    complex_photo_281.width = None
    complex_photo_281 = importer.save_or_locate(complex_photo_281)

    complex_photo_282 = Photo()
    complex_photo_282.height = None
    complex_photo_282.image_src = 'https://live.staticflickr.com/65535/52574453901_e4d0369f54_z.jpg'
    complex_photo_282.link = 'https://www.flickr.com/search/?lat=31.5914029&lon=130.553828&radius=0.1&has_geo=1&view_all=1'
    complex_photo_282.person = None
    complex_photo_282.title = 'Kagoshima Tram, Kyushu, Japan'
    complex_photo_282.type_master = complex_type_master_23
    complex_photo_282.username = 'globetrekimages'
    complex_photo_282.width = None
    complex_photo_282 = importer.save_or_locate(complex_photo_282)

    complex_photo_283 = Photo()
    complex_photo_283.height = None
    complex_photo_283.image_src = 'https://live.staticflickr.com/65535/52568189566_237243df57_z.jpg'
    complex_photo_283.link = 'https://www.flickr.com/search/?lat=31.589238&lon=130.555969&radius=0.1&has_geo=1&view_all=1'
    complex_photo_283.person = None
    complex_photo_283.title = 'Kagoshima Tenmonkan Shopping Arcade, Japan'
    complex_photo_283.type_master = complex_type_master_23
    complex_photo_283.username = 'globetrekimages'
    complex_photo_283.width = None
    complex_photo_283 = importer.save_or_locate(complex_photo_283)

    complex_photo_284 = Photo()
    complex_photo_284.height = None
    complex_photo_284.image_src = 'https://live.staticflickr.com/65535/51316887333_c153b6c170_z.jpg'
    complex_photo_284.link = 'https://www.flickr.com/search/?lat=31.5932664&lon=130.5570647&radius=0.1&has_geo=1&view_all=1'
    complex_photo_284.person = None
    complex_photo_284.title = 'IMG_2096'
    complex_photo_284.type_master = complex_type_master_23
    complex_photo_284.username = 'OOMYV'
    complex_photo_284.width = None
    complex_photo_284 = importer.save_or_locate(complex_photo_284)

    complex_photo_285 = Photo()
    complex_photo_285.height = None
    complex_photo_285.image_src = 'https://live.staticflickr.com/65535/50170708487_4dfa2239f2_z.jpg'
    complex_photo_285.link = 'https://www.flickr.com/search/?lat=31.5935195&lon=130.5631033&radius=0.1&has_geo=1&view_all=1'
    complex_photo_285.person = None
    complex_photo_285.title = '_DSC7224'
    complex_photo_285.type_master = complex_type_master_23
    complex_photo_285.username = 'de98lip'
    complex_photo_285.width = None
    complex_photo_285 = importer.save_or_locate(complex_photo_285)

    complex_photo_286 = Photo()
    complex_photo_286.height = None
    complex_photo_286.image_src = 'https://live.staticflickr.com/65535/51015897816_2161965f60_z.jpg'
    complex_photo_286.link = 'https://www.flickr.com/search/?lat=31.5964541&lon=130.5628203&radius=0.1&has_geo=1&view_all=1'
    complex_photo_286.person = None
    complex_photo_286.title = 'Kagoshima-58'
    complex_photo_286.type_master = complex_type_master_23
    complex_photo_286.username = 'Art Dekimpe'
    complex_photo_286.width = None
    complex_photo_286 = importer.save_or_locate(complex_photo_286)

    complex_photo_287 = Photo()
    complex_photo_287.height = None
    complex_photo_287.image_src = 'https://live.staticflickr.com/4752/38864868195_0d1ddf20f0_z.jpg'
    complex_photo_287.link = 'https://www.flickr.com/search/?lat=31.5521501&lon=130.6587304&radius=0.1&has_geo=1&view_all=1'
    complex_photo_287.person = None
    complex_photo_287.title = '20120220-_DSC6444'
    complex_photo_287.type_master = complex_type_master_23
    complex_photo_287.username = 'Fomal Haut'
    complex_photo_287.width = None
    complex_photo_287 = importer.save_or_locate(complex_photo_287)

    complex_photo_288 = Photo()
    complex_photo_288.height = None
    complex_photo_288.image_src = 'https://live.staticflickr.com/65535/50840431221_7fa46e0c13_z.jpg'
    complex_photo_288.link = 'https://www.flickr.com/search/?lat=31.5847772&lon=130.7064773&radius=0.1&has_geo=1&view_all=1'
    complex_photo_288.person = None
    complex_photo_288.title = '黒神埋沒鳥居'
    complex_photo_288.type_master = complex_type_master_23
    complex_photo_288.username = 'Chitaka Chou'
    complex_photo_288.width = None
    complex_photo_288 = importer.save_or_locate(complex_photo_288)

    complex_photo_289 = Photo()
    complex_photo_289.height = None
    complex_photo_289.image_src = 'https://live.staticflickr.com/4653/39054166074_efcb9ac51a_z.jpg'
    complex_photo_289.link = 'https://www.flickr.com/search/?lat=31.5530478&lon=130.6611474&radius=0.1&has_geo=1&view_all=1'
    complex_photo_289.person = None
    complex_photo_289.title = '20120220-_DSC6441'
    complex_photo_289.type_master = complex_type_master_23
    complex_photo_289.username = 'Fomal Haut'
    complex_photo_289.width = None
    complex_photo_289 = importer.save_or_locate(complex_photo_289)

    complex_photo_290 = Photo()
    complex_photo_290.height = None
    complex_photo_290.image_src = 'https://live.staticflickr.com/65535/52629608516_250ae611f5_z.jpg'
    complex_photo_290.link = 'https://www.flickr.com/search/?lat=33.437806&lon=135.7613677&radius=0.1&has_geo=1&view_all=1'
    complex_photo_290.person = None
    complex_photo_290.title = 'Cape Shionomisaki, Wakayama'
    complex_photo_290.type_master = complex_type_master_23
    complex_photo_290.username = 'Kzaral'
    complex_photo_290.width = None
    complex_photo_290 = importer.save_or_locate(complex_photo_290)

    complex_photo_291 = Photo()
    complex_photo_291.height = None
    complex_photo_291.image_src = 'https://live.staticflickr.com/65535/52613207584_09510cdf4b_z.jpg'
    complex_photo_291.link = 'https://www.flickr.com/search/?lat=35.6276803&lon=139.7888626&radius=0.1&has_geo=1&view_all=1'
    complex_photo_291.person = None
    complex_photo_291.title = 'Tokyo - Octagonal Monument in Ariake'
    complex_photo_291.type_master = complex_type_master_23
    complex_photo_291.username = 'Claudia L aus B'
    complex_photo_291.width = None
    complex_photo_291 = importer.save_or_locate(complex_photo_291)

    complex_photo_292 = Photo()
    complex_photo_292.height = None
    complex_photo_292.image_src = 'https://live.staticflickr.com/65535/48584799312_84cdceaeb8_z.jpg'
    complex_photo_292.link = 'https://www.flickr.com/search/?lat=35.6174045&lon=139.7957527&radius=0.1&has_geo=1&view_all=1'
    complex_photo_292.person = None
    complex_photo_292.title = '190813_101_EOSR1122'
    complex_photo_292.type_master = complex_type_master_23
    complex_photo_292.username = 'oda.shinsuke'
    complex_photo_292.width = None
    complex_photo_292 = importer.save_or_locate(complex_photo_292)

    complex_photo_293 = Photo()
    complex_photo_293.height = None
    complex_photo_293.image_src = 'https://live.staticflickr.com/1912/43405050030_c561f5ffaa_z.jpg'
    complex_photo_293.link = 'https://www.flickr.com/search/?lat=35.6122153&lon=139.8288838&radius=0.1&has_geo=1&view_all=1'
    complex_photo_293.person = None
    complex_photo_293.title = 'IMG_0463'
    complex_photo_293.type_master = complex_type_master_23
    complex_photo_293.username = 'tnoma'
    complex_photo_293.width = None
    complex_photo_293 = importer.save_or_locate(complex_photo_293)

    complex_photo_294 = Photo()
    complex_photo_294.height = None
    complex_photo_294.image_src = 'https://live.staticflickr.com/1944/45594546621_640e7afc17_z.jpg'
    complex_photo_294.link = 'https://www.flickr.com/search/?lat=34.0540334&lon=134.5966435&radius=0.1&has_geo=1&view_all=1'
    complex_photo_294.person = None
    complex_photo_294.title = 'IMG_0965'
    complex_photo_294.type_master = complex_type_master_23
    complex_photo_294.username = 'tnoma'
    complex_photo_294.width = None
    complex_photo_294 = importer.save_or_locate(complex_photo_294)

    complex_photo_295 = Photo()
    complex_photo_295.height = None
    complex_photo_295.image_src = 'https://live.staticflickr.com/65535/50869270052_1d66412aea_z.jpg'
    complex_photo_295.link = 'https://www.flickr.com/search/?lat=34.0686278&lon=134.5490887&radius=0.1&has_geo=1&view_all=1'
    complex_photo_295.person = None
    complex_photo_295.title = 'DSC_0922'
    complex_photo_295.type_master = complex_type_master_23
    complex_photo_295.username = 'Kuruman'
    complex_photo_295.width = None
    complex_photo_295 = importer.save_or_locate(complex_photo_295)

    complex_photo_296 = Photo()
    complex_photo_296.height = None
    complex_photo_296.image_src = 'https://live.staticflickr.com/8345/8152184698_125218a7a4_z.jpg'
    complex_photo_296.link = 'https://www.flickr.com/search/?lat=34.0536339&lon=134.5872961&radius=0.1&has_geo=1&view_all=1'
    complex_photo_296.person = None
    complex_photo_296.title = 'IMG_1840'
    complex_photo_296.type_master = complex_type_master_23
    complex_photo_296.username = 'rurinoshima'
    complex_photo_296.width = None
    complex_photo_296 = importer.save_or_locate(complex_photo_296)

    complex_photo_297 = Photo()
    complex_photo_297.height = None
    complex_photo_297.image_src = 'https://live.staticflickr.com/907/27201418887_e7396a031d_z.jpg'
    complex_photo_297.link = 'https://www.flickr.com/search/?lat=34.058427&lon=134.5862744&radius=0.1&has_geo=1&view_all=1'
    complex_photo_297.person = None
    complex_photo_297.title = '20180504-DSCF8882.jpg'
    complex_photo_297.type_master = complex_type_master_23
    complex_photo_297.username = 'kato_masashi'
    complex_photo_297.width = None
    complex_photo_297 = importer.save_or_locate(complex_photo_297)

    complex_photo_298 = Photo()
    complex_photo_298.height = None
    complex_photo_298.image_src = 'https://live.staticflickr.com/65535/52629089697_04aeda0e08_z.jpg'
    complex_photo_298.link = 'https://www.flickr.com/search/?lat=34.0744574&lon=134.5513574&radius=0.1&has_geo=1&view_all=1'
    complex_photo_298.person = None
    complex_photo_298.title = 'JR Tokushima Station'
    complex_photo_298.type_master = complex_type_master_23
    complex_photo_298.username = 'Kzaral'
    complex_photo_298.width = None
    complex_photo_298 = importer.save_or_locate(complex_photo_298)

    complex_photo_299 = Photo()
    complex_photo_299.height = None
    complex_photo_299.image_src = 'https://live.staticflickr.com/65535/52629089672_3a45ae0be8_z.jpg'
    complex_photo_299.link = 'https://www.flickr.com/search/?lat=34.0741023&lon=134.5502762&radius=0.1&has_geo=1&view_all=1'
    complex_photo_299.person = None
    complex_photo_299.title = 'JR Tokushima Station'
    complex_photo_299.type_master = complex_type_master_23
    complex_photo_299.username = 'Kzaral'
    complex_photo_299.width = None
    complex_photo_299 = importer.save_or_locate(complex_photo_299)

    complex_photo_300 = Photo()
    complex_photo_300.height = None
    complex_photo_300.image_src = 'https://live.staticflickr.com/65535/50869270292_856806fa59_z.jpg'
    complex_photo_300.link = 'https://www.flickr.com/search/?lat=34.0715266&lon=134.5486315&radius=0.1&has_geo=1&view_all=1'
    complex_photo_300.person = None
    complex_photo_300.title = 'DSC02553'
    complex_photo_300.type_master = complex_type_master_23
    complex_photo_300.username = 'Kuruman'
    complex_photo_300.width = None
    complex_photo_300 = importer.save_or_locate(complex_photo_300)

    complex_photo_301 = Photo()
    complex_photo_301.height = None
    complex_photo_301.image_src = 'https://live.staticflickr.com/65535/50869272632_b56ca0e765_z.jpg'
    complex_photo_301.link = 'https://www.flickr.com/search/?lat=34.0711498&lon=134.548539&radius=0.1&has_geo=1&view_all=1'
    complex_photo_301.person = None
    complex_photo_301.title = 'DSC_0940'
    complex_photo_301.type_master = complex_type_master_23
    complex_photo_301.username = 'Kuruman'
    complex_photo_301.width = None
    complex_photo_301 = importer.save_or_locate(complex_photo_301)

    complex_photo_302 = Photo()
    complex_photo_302.height = None
    complex_photo_302.image_src = 'https://live.staticflickr.com/65535/50869272587_d97c416e74_z.jpg'
    complex_photo_302.link = 'https://www.flickr.com/search/?lat=34.068563&lon=134.5496149&radius=0.1&has_geo=1&view_all=1'
    complex_photo_302.person = None
    complex_photo_302.title = 'DSC_0939'
    complex_photo_302.type_master = complex_type_master_23
    complex_photo_302.username = 'Kuruman'
    complex_photo_302.width = None
    complex_photo_302 = importer.save_or_locate(complex_photo_302)

    complex_photo_303 = Photo()
    complex_photo_303.height = None
    complex_photo_303.image_src = 'https://live.staticflickr.com/3679/33442218031_46e5299288_z.jpg'
    complex_photo_303.link = 'https://www.flickr.com/search/?lat=33.9740109&lon=134.3701509&radius=0.1&has_geo=1&view_all=1'
    complex_photo_303.person = None
    complex_photo_303.title = 'if_p_036'
    complex_photo_303.type_master = complex_type_master_23
    complex_photo_303.username = 'Kamiyama Archive Project'
    complex_photo_303.width = None
    complex_photo_303 = importer.save_or_locate(complex_photo_303)

    complex_photo_304 = Photo()
    complex_photo_304.height = None
    complex_photo_304.image_src = 'https://live.staticflickr.com/4257/35260792672_a87e049c54_z.jpg'
    complex_photo_304.link = 'https://www.flickr.com/search/?lat=33.9718748&lon=134.3699952&radius=0.1&has_geo=1&view_all=1'
    complex_photo_304.person = None
    complex_photo_304.title = 'DSC_3211'
    complex_photo_304.type_master = complex_type_master_23
    complex_photo_304.username = 'neruodokodemo'
    complex_photo_304.width = None
    complex_photo_304 = importer.save_or_locate(complex_photo_304)

    complex_photo_305 = Photo()
    complex_photo_305.height = None
    complex_photo_305.image_src = 'https://live.staticflickr.com/8547/15826602595_b10f5573bb_z.jpg'
    complex_photo_305.link = 'https://www.flickr.com/search/?lat=33.9708999&lon=134.3668724&radius=0.1&has_geo=1&view_all=1'
    complex_photo_305.person = None
    complex_photo_305.title = 'by @takeshi.kakeda'
    complex_photo_305.type_master = complex_type_master_23
    complex_photo_305.username = 'takeshi.kakeda'
    complex_photo_305.width = None
    complex_photo_305 = importer.save_or_locate(complex_photo_305)

    complex_photo_306 = Photo()
    complex_photo_306.height = None
    complex_photo_306.image_src = 'https://live.staticflickr.com/65535/50059125781_bab75afb06_z.jpg'
    complex_photo_306.link = 'https://www.flickr.com/search/?lat=34.0380181&lon=134.4628565&radius=0.1&has_geo=1&view_all=1'
    complex_photo_306.person = None
    complex_photo_306.title = '13'
    complex_photo_306.type_master = complex_type_master_23
    complex_photo_306.username = 'aldoschwartz01'
    complex_photo_306.width = None
    complex_photo_306 = importer.save_or_locate(complex_photo_306)

    complex_photo_307 = Photo()
    complex_photo_307.height = None
    complex_photo_307.image_src = 'https://live.staticflickr.com/65535/50099303767_f0feb326dc_z.jpg'
    complex_photo_307.link = 'https://www.flickr.com/search/?lat=34.0502992&lon=134.4757069&radius=0.1&has_geo=1&view_all=1'
    complex_photo_307.person = None
    complex_photo_307.title = '十四番札所 常楽寺'
    complex_photo_307.type_master = complex_type_master_23
    complex_photo_307.username = 'JH1FJP'
    complex_photo_307.width = None
    complex_photo_307 = importer.save_or_locate(complex_photo_307)

    complex_photo_308 = Photo()
    complex_photo_308.height = None
    complex_photo_308.image_src = 'https://live.staticflickr.com/65535/50099359547_c7666bf2cd_z.jpg'
    complex_photo_308.link = 'https://www.flickr.com/search/?lat=34.0556179&lon=134.4736354&radius=0.1&has_geo=1&view_all=1'
    complex_photo_308.person = None
    complex_photo_308.title = '十五番札所 国分寺'
    complex_photo_308.type_master = complex_type_master_23
    complex_photo_308.username = 'JH1FJP'
    complex_photo_308.width = None
    complex_photo_308 = importer.save_or_locate(complex_photo_308)

    complex_photo_309 = Photo()
    complex_photo_309.height = None
    complex_photo_309.image_src = 'https://live.staticflickr.com/65535/50099446932_9a76652ec8_z.jpg'
    complex_photo_309.link = 'https://www.flickr.com/search/?lat=34.0685003&lon=134.4743836&radius=0.1&has_geo=1&view_all=1'
    complex_photo_309.person = None
    complex_photo_309.title = '十六番札所 観音寺'
    complex_photo_309.type_master = complex_type_master_23
    complex_photo_309.username = 'JH1FJP'
    complex_photo_309.width = None
    complex_photo_309 = importer.save_or_locate(complex_photo_309)

    complex_photo_310 = Photo()
    complex_photo_310.height = None
    complex_photo_310.image_src = 'https://live.staticflickr.com/65535/51308597481_4a5a7ea708_z.jpg'
    complex_photo_310.link = 'https://www.flickr.com/search/?lat=34.2341614&lon=134.6403296&radius=0.1&has_geo=1&view_all=1'
    complex_photo_310.person = None
    complex_photo_310.title = 'by @perioanajou'
    complex_photo_310.type_master = complex_type_master_23
    complex_photo_310.username = 'perioanajou'
    complex_photo_310.width = None
    complex_photo_310 = importer.save_or_locate(complex_photo_310)

    complex_photo_311 = Photo()
    complex_photo_311.height = None
    complex_photo_311.image_src = 'https://live.staticflickr.com/65535/52619432070_a67e92471d_z.jpg'
    complex_photo_311.link = 'https://www.flickr.com/search/?lat=34.23617&lon=134.6419817&radius=0.1&has_geo=1&view_all=1'
    complex_photo_311.person = None
    complex_photo_311.title = '20221223-M10R8532 copy'
    complex_photo_311.type_master = complex_type_master_23
    complex_photo_311.username = '@pigstagram'
    complex_photo_311.width = None
    complex_photo_311 = importer.save_or_locate(complex_photo_311)

    complex_photo_312 = Photo()
    complex_photo_312.height = None
    complex_photo_312.image_src = 'https://live.staticflickr.com/65535/52619483858_c1175114e4_z.jpg'
    complex_photo_312.link = 'https://www.flickr.com/search/?lat=34.2369194&lon=134.6423874&radius=0.1&has_geo=1&view_all=1'
    complex_photo_312.person = None
    complex_photo_312.title = '20221223-M10R8533 copy'
    complex_photo_312.type_master = complex_type_master_23
    complex_photo_312.username = '@pigstagram'
    complex_photo_312.width = None
    complex_photo_312 = importer.save_or_locate(complex_photo_312)

    complex_photo_313 = Photo()
    complex_photo_313.height = None
    complex_photo_313.image_src = 'https://live.staticflickr.com/65535/52077775570_1430497406_z.jpg'
    complex_photo_313.link = 'https://www.flickr.com/search/?lat=34.1112386&lon=132.9759503&radius=0.1&has_geo=1&view_all=1'
    complex_photo_313.person = None
    complex_photo_313.title = 'Shimanami Kaido (しまなみ海道)'
    complex_photo_313.type_master = complex_type_master_23
    complex_photo_313.username = 'pantkiewicz'
    complex_photo_313.width = None
    complex_photo_313 = importer.save_or_locate(complex_photo_313)

    complex_photo_314 = Photo()
    complex_photo_314.height = None
    complex_photo_314.image_src = 'https://live.staticflickr.com/65535/52076208297_f6257062d7_z.jpg'
    complex_photo_314.link = 'https://www.flickr.com/search/?lat=34.0642051&lon=132.9936355&radius=0.1&has_geo=1&view_all=1'
    complex_photo_314.person = None
    complex_photo_314.title = 'バリィさん'
    complex_photo_314.type_master = complex_type_master_23
    complex_photo_314.username = 'pantkiewicz'
    complex_photo_314.width = None
    complex_photo_314 = importer.save_or_locate(complex_photo_314)

    complex_photo_315 = Photo()
    complex_photo_315.height = None
    complex_photo_315.image_src = 'https://live.staticflickr.com/65535/52077250206_4a33367549_z.jpg'
    complex_photo_315.link = 'https://www.flickr.com/search/?lat=34.0642515&lon=132.9947761&radius=0.1&has_geo=1&view_all=1'
    complex_photo_315.person = None
    complex_photo_315.title = 'バリィさん Mikan Juice'
    complex_photo_315.type_master = complex_type_master_23
    complex_photo_315.username = 'pantkiewicz'
    complex_photo_315.width = None
    complex_photo_315 = importer.save_or_locate(complex_photo_315)

    complex_photo_316 = Photo()
    complex_photo_316.height = None
    complex_photo_316.image_src = 'https://live.staticflickr.com/65535/51638469164_f8600edbff_z.jpg'
    complex_photo_316.link = 'https://www.flickr.com/search/?lat=34.0643481&lon=132.9987001&radius=0.1&has_geo=1&view_all=1'
    complex_photo_316.person = None
    complex_photo_316.title = '焼豚玉子飯'
    complex_photo_316.type_master = complex_type_master_23
    complex_photo_316.username = 'Chitaka Chou'
    complex_photo_316.width = None
    complex_photo_316 = importer.save_or_locate(complex_photo_316)

    complex_photo_317 = Photo()
    complex_photo_317.height = None
    complex_photo_317.image_src = 'https://live.staticflickr.com/4734/39553612811_76223874f6_z.jpg'
    complex_photo_317.link = 'https://www.flickr.com/search/?lat=34.064831&lon=133.000015&radius=0.1&has_geo=1&view_all=1'
    complex_photo_317.person = None
    complex_photo_317.title = 'IMG_1183'
    complex_photo_317.type_master = complex_type_master_23
    complex_photo_317.username = 'athena07_20'
    complex_photo_317.width = None
    complex_photo_317 = importer.save_or_locate(complex_photo_317)

    complex_photo_318 = Photo()
    complex_photo_318.height = None
    complex_photo_318.image_src = 'https://live.staticflickr.com/1971/30812424067_c3433697a1_z.jpg'
    complex_photo_318.link = 'https://www.flickr.com/search/?lat=34.0620614&lon=133.0005845&radius=0.1&has_geo=1&view_all=1'
    complex_photo_318.person = None
    complex_photo_318.title = 'Imabari-Ehime-30'
    complex_photo_318.type_master = complex_type_master_23
    complex_photo_318.username = 'luisete'
    complex_photo_318.width = None
    complex_photo_318 = importer.save_or_locate(complex_photo_318)

    complex_photo_319 = Photo()
    complex_photo_319.height = None
    complex_photo_319.image_src = 'https://live.staticflickr.com/65535/52077250101_a16bcb49cd_z.jpg'
    complex_photo_319.link = 'https://www.flickr.com/search/?lat=34.0633708&lon=133.0067794&radius=0.1&has_geo=1&view_all=1'
    complex_photo_319.person = None
    complex_photo_319.title = 'Imabari manhole'
    complex_photo_319.type_master = complex_type_master_23
    complex_photo_319.username = 'pantkiewicz'
    complex_photo_319.width = None
    complex_photo_319 = importer.save_or_locate(complex_photo_319)

    complex_photo_320 = Photo()
    complex_photo_320.height = None
    complex_photo_320.image_src = 'https://live.staticflickr.com/65535/52076243002_6c11985038_z.jpg'
    complex_photo_320.link = 'https://www.flickr.com/search/?lat=34.1185335&lon=132.9926989&radius=0.1&has_geo=1&view_all=1'
    complex_photo_320.person = None
    complex_photo_320.title = 'Shimanami Kaido (しまなみ海道)'
    complex_photo_320.type_master = complex_type_master_23
    complex_photo_320.username = 'pantkiewicz'
    complex_photo_320.width = None
    complex_photo_320 = importer.save_or_locate(complex_photo_320)

    complex_photo_321 = Photo()
    complex_photo_321.height = None
    complex_photo_321.image_src = 'https://live.staticflickr.com/65535/52077207751_c160d608f5_z.jpg'
    complex_photo_321.link = 'https://www.flickr.com/search/?lat=34.0653655&lon=133.0074369&radius=0.1&has_geo=1&view_all=1'
    complex_photo_321.person = None
    complex_photo_321.title = 'Imabari Castle (今治城)'
    complex_photo_321.type_master = complex_type_master_23
    complex_photo_321.username = 'pantkiewicz'
    complex_photo_321.width = None
    complex_photo_321 = importer.save_or_locate(complex_photo_321)

    complex_photo_322 = Photo()
    complex_photo_322.height = None
    complex_photo_322.image_src = 'https://live.staticflickr.com/65535/52077438159_e0a29333b9_z.jpg'
    complex_photo_322.link = 'https://www.flickr.com/search/?lat=34.0665969&lon=133.0080714&radius=0.1&has_geo=1&view_all=1'
    complex_photo_322.person = None
    complex_photo_322.title = 'Imabari Castle (今治城)'
    complex_photo_322.type_master = complex_type_master_23
    complex_photo_322.username = 'pantkiewicz'
    complex_photo_322.width = None
    complex_photo_322 = importer.save_or_locate(complex_photo_322)

    complex_photo_323 = Photo()
    complex_photo_323.height = None
    complex_photo_323.image_src = 'https://live.staticflickr.com/65535/52438545487_e666d2c0b6_z.jpg'
    complex_photo_323.link = 'https://www.flickr.com/search/?lat=34.0698411&lon=133.004898&radius=0.1&has_geo=1&view_all=1'
    complex_photo_323.person = None
    complex_photo_323.title = 'Food Truck'
    complex_photo_323.type_master = complex_type_master_23
    complex_photo_323.username = 'Hiro_A'
    complex_photo_323.width = None
    complex_photo_323 = importer.save_or_locate(complex_photo_323)

    complex_photo_324 = Photo()
    complex_photo_324.height = None
    complex_photo_324.image_src = 'https://live.staticflickr.com/65535/51108855204_e35612b4cf_z.jpg'
    complex_photo_324.link = 'https://www.flickr.com/search/?lat=34.1088928&lon=132.9759003&radius=0.1&has_geo=1&view_all=1'
    complex_photo_324.person = None
    complex_photo_324.title = 'IMG20210411114425'
    complex_photo_324.type_master = complex_type_master_23
    complex_photo_324.username = 'isao-net'
    complex_photo_324.width = None
    complex_photo_324 = importer.save_or_locate(complex_photo_324)

    complex_photo_325 = Photo()
    complex_photo_325.height = None
    complex_photo_325.image_src = 'https://live.staticflickr.com/65535/52476576694_38d45151ac_z.jpg'
    complex_photo_325.link = 'https://www.flickr.com/search/?lat=34.1114089&lon=132.9764984&radius=0.1&has_geo=1&view_all=1'
    complex_photo_325.person = None
    complex_photo_325.title = 'The long suspension bridge over the Seto inland sea'
    complex_photo_325.type_master = complex_type_master_23
    complex_photo_325.username = 'Teruhide Tomori'
    complex_photo_325.width = None
    complex_photo_325 = importer.save_or_locate(complex_photo_325)

    complex_photo_326 = Photo()
    complex_photo_326.height = None
    complex_photo_326.image_src = 'https://live.staticflickr.com/65535/52469216866_4d06af3d3b_z.jpg'
    complex_photo_326.link = 'https://www.flickr.com/search/?lat=34.1117368&lon=132.976139&radius=0.1&has_geo=1&view_all=1'
    complex_photo_326.person = None
    complex_photo_326.title = 'Light streams'
    complex_photo_326.type_master = complex_type_master_23
    complex_photo_326.username = 'Teruhide Tomori'
    complex_photo_326.width = None
    complex_photo_326 = importer.save_or_locate(complex_photo_326)

    complex_photo_327 = Photo()
    complex_photo_327.height = None
    complex_photo_327.image_src = 'https://live.staticflickr.com/65535/52211261288_b0c29f7c6d_z.jpg'
    complex_photo_327.link = 'https://www.flickr.com/search/?lat=34.1140186&lon=132.9778337&radius=0.1&has_geo=1&view_all=1'
    complex_photo_327.person = None
    complex_photo_327.title = 'IMGP7375'
    complex_photo_327.type_master = complex_type_master_23
    complex_photo_327.username = 'shinnnnn0619'
    complex_photo_327.width = None
    complex_photo_327 = importer.save_or_locate(complex_photo_327)

    complex_photo_328 = Photo()
    complex_photo_328.height = None
    complex_photo_328.image_src = 'https://live.staticflickr.com/65535/52038100948_da7cfcf3fc_z.jpg'
    complex_photo_328.link = 'https://www.flickr.com/search/?lat=34.1154406&lon=132.9849079&radius=0.1&has_geo=1&view_all=1'
    complex_photo_328.person = None
    complex_photo_328.title = '1B590DFD-4AB9-4FBA-9C85-B0D2946D1CCB'
    complex_photo_328.type_master = complex_type_master_23
    complex_photo_328.username = 'myuguchi'
    complex_photo_328.width = None
    complex_photo_328 = importer.save_or_locate(complex_photo_328)

    complex_photo_329 = Photo()
    complex_photo_329.height = None
    complex_photo_329.image_src = 'https://live.staticflickr.com/65535/52076258457_bc5b9be09e_z.jpg'
    complex_photo_329.link = 'https://www.flickr.com/search/?lat=34.1274537&lon=133.0220408&radius=0.1&has_geo=1&view_all=1'
    complex_photo_329.person = None
    complex_photo_329.title = 'Shimanami Kaido (しまなみ海道)'
    complex_photo_329.type_master = complex_type_master_23
    complex_photo_329.username = 'pantkiewicz'
    complex_photo_329.width = None
    complex_photo_329 = importer.save_or_locate(complex_photo_329)

    complex_photo_330 = Photo()
    complex_photo_330.height = None
    complex_photo_330.image_src = 'https://live.staticflickr.com/65535/50579679517_3dfb000951_z.jpg'
    complex_photo_330.link = 'https://www.flickr.com/search/?lat=34.1271124&lon=133.0239936&radius=0.1&has_geo=1&view_all=1'
    complex_photo_330.person = None
    complex_photo_330.title = 'IMG20201108113713'
    complex_photo_330.type_master = complex_type_master_23
    complex_photo_330.username = 'isao-net'
    complex_photo_330.width = None
    complex_photo_330 = importer.save_or_locate(complex_photo_330)

    complex_photo_331 = Photo()
    complex_photo_331.height = None
    complex_photo_331.image_src = 'https://live.staticflickr.com/65535/47947310413_bfd454a54d_z.jpg'
    complex_photo_331.link = 'https://www.flickr.com/search/?lat=36.071984&lon=138.0850612&radius=0.1&has_geo=1&view_all=1'
    complex_photo_331.person = None
    complex_photo_331.title = "Waving delegation, and we didn't even stop here"
    complex_photo_331.type_master = complex_type_master_23
    complex_photo_331.username = 'hawkstersf'
    complex_photo_331.width = None
    complex_photo_331 = importer.save_or_locate(complex_photo_331)

    complex_photo_332 = Photo()
    complex_photo_332.height = None
    complex_photo_332.image_src = 'https://live.staticflickr.com/8057/8189583591_d18ec24fb0_z.jpg'
    complex_photo_332.link = 'https://www.flickr.com/search/?lat=36.0810377&lon=138.0841048&radius=0.1&has_geo=1&view_all=1'
    complex_photo_332.person = None
    complex_photo_332.title = "Suwa, Nagano '12 #8"
    complex_photo_332.type_master = complex_type_master_23
    complex_photo_332.username = 'tt64jp'
    complex_photo_332.width = None
    complex_photo_332 = importer.save_or_locate(complex_photo_332)

    complex_photo_333 = Photo()
    complex_photo_333.height = None
    complex_photo_333.image_src = 'https://live.staticflickr.com/4686/38469283394_851f850c57_z.jpg'
    complex_photo_333.link = 'https://www.flickr.com/search/?lat=36.074517&lon=138.0849625&radius=0.1&has_geo=1&view_all=1'
    complex_photo_333.person = None
    complex_photo_333.title = 'Suwa#32'
    complex_photo_333.type_master = complex_type_master_23
    complex_photo_333.username = 'tetsuo5'
    complex_photo_333.width = None
    complex_photo_333 = importer.save_or_locate(complex_photo_333)

    complex_photo_334 = Photo()
    complex_photo_334.height = None
    complex_photo_334.image_src = 'https://live.staticflickr.com/4732/39168577352_bbb7b0dd71_z.jpg'
    complex_photo_334.link = 'https://www.flickr.com/search/?lat=36.0743681&lon=138.0833581&radius=0.1&has_geo=1&view_all=1'
    complex_photo_334.person = None
    complex_photo_334.title = 'Suwa#33'
    complex_photo_334.type_master = complex_type_master_23
    complex_photo_334.username = 'tetsuo5'
    complex_photo_334.width = None
    complex_photo_334 = importer.save_or_locate(complex_photo_334)

    complex_photo_335 = Photo()
    complex_photo_335.height = None
    complex_photo_335.image_src = 'https://live.staticflickr.com/7399/14156465213_3edf9d4fef_z.jpg'
    complex_photo_335.link = 'https://www.flickr.com/search/?lat=36.0742642&lon=138.0828459&radius=0.1&has_geo=1&view_all=1'
    complex_photo_335.person = None
    complex_photo_335.title = 'by @randombutsowhat'
    complex_photo_335.type_master = complex_type_master_23
    complex_photo_335.username = 'randombutsowhat'
    complex_photo_335.width = None
    complex_photo_335 = importer.save_or_locate(complex_photo_335)

    complex_photo_336 = Photo()
    complex_photo_336.height = None
    complex_photo_336.image_src = 'https://live.staticflickr.com/2815/8947685714_28e111ec88_z.jpg'
    complex_photo_336.link = 'https://www.flickr.com/search/?lat=36.0744486&lon=138.0810091&radius=0.1&has_geo=1&view_all=1'
    complex_photo_336.person = None
    complex_photo_336.title = '下諏訪'
    complex_photo_336.type_master = complex_type_master_23
    complex_photo_336.username = 'nmnr'
    complex_photo_336.width = None
    complex_photo_336 = importer.save_or_locate(complex_photo_336)

    complex_photo_337 = Photo()
    complex_photo_337.height = None
    complex_photo_337.image_src = 'https://live.staticflickr.com/5328/7155464342_0ca03500e8_z.jpg'
    complex_photo_337.link = 'https://www.flickr.com/search/?lat=36.0749816&lon=138.0811826&radius=0.1&has_geo=1&view_all=1'
    complex_photo_337.person = None
    complex_photo_337.title = 'IMG_4182'
    complex_photo_337.type_master = complex_type_master_23
    complex_photo_337.username = 'Take.I'
    complex_photo_337.width = None
    complex_photo_337 = importer.save_or_locate(complex_photo_337)

    complex_photo_338 = Photo()
    complex_photo_338.height = None
    complex_photo_338.image_src = 'https://live.staticflickr.com/6231/6222233663_2c2d2b1463_z.jpg'
    complex_photo_338.link = 'https://www.flickr.com/search/?lat=36.0775605&lon=138.0813264&radius=0.1&has_geo=1&view_all=1'
    complex_photo_338.person = None
    complex_photo_338.title = 'Antique Clock'
    complex_photo_338.type_master = complex_type_master_23
    complex_photo_338.username = 'mainichinatto'
    complex_photo_338.width = None
    complex_photo_338 = importer.save_or_locate(complex_photo_338)

    complex_photo_339 = Photo()
    complex_photo_339.height = None
    complex_photo_339.image_src = 'https://live.staticflickr.com/1904/43451563650_8862d0f258_z.jpg'
    complex_photo_339.link = 'https://www.flickr.com/search/?lat=36.0802859&lon=138.0818667&radius=0.1&has_geo=1&view_all=1'
    complex_photo_339.person = None
    complex_photo_339.title = 'by @digital_studio_japan'
    complex_photo_339.type_master = complex_type_master_23
    complex_photo_339.username = 'digital_studio_japan'
    complex_photo_339.width = None
    complex_photo_339 = importer.save_or_locate(complex_photo_339)

    complex_photo_340 = Photo()
    complex_photo_340.height = None
    complex_photo_340.image_src = 'https://live.staticflickr.com/65535/47720802241_7612b5d799_z.jpg'
    complex_photo_340.link = 'https://www.flickr.com/search/?lat=36.0813523&lon=138.0820146&radius=0.1&has_geo=1&view_all=1'
    complex_photo_340.person = None
    complex_photo_340.title = 'Suwa Grand Shrine (Suwa-taisha) 諏訪大社下社春宮'
    complex_photo_340.type_master = complex_type_master_23
    complex_photo_340.username = 'sugar4684'
    complex_photo_340.width = None
    complex_photo_340 = importer.save_or_locate(complex_photo_340)

    complex_photo_341 = Photo()
    complex_photo_341.height = None
    complex_photo_341.image_src = 'https://live.staticflickr.com/65535/32777646097_37e48d9812_z.jpg'
    complex_photo_341.link = 'https://www.flickr.com/search/?lat=36.0812502&lon=138.0820466&radius=0.1&has_geo=1&view_all=1'
    complex_photo_341.person = None
    complex_photo_341.title = 'Suwa Grand Shrine (Suwa-taisha) 諏訪大社下社春宮'
    complex_photo_341.type_master = complex_type_master_23
    complex_photo_341.username = 'sugar4684'
    complex_photo_341.width = None
    complex_photo_341 = importer.save_or_locate(complex_photo_341)

    complex_photo_342 = Photo()
    complex_photo_342.height = None
    complex_photo_342.image_src = 'https://live.staticflickr.com/65535/47668002312_8a1fd32fdf_z.jpg'
    complex_photo_342.link = 'https://www.flickr.com/search/?lat=36.0820837&lon=138.0821082&radius=0.1&has_geo=1&view_all=1'
    complex_photo_342.person = None
    complex_photo_342.title = 'Suwa Grand Shrine (Suwa-taisha) 諏訪大社下社春宮'
    complex_photo_342.type_master = complex_type_master_23
    complex_photo_342.username = 'sugar4684'
    complex_photo_342.width = None
    complex_photo_342 = importer.save_or_locate(complex_photo_342)

    complex_photo_343 = Photo()
    complex_photo_343.height = None
    complex_photo_343.image_src = 'https://live.staticflickr.com/65535/47720801711_bf18822955_z.jpg'
    complex_photo_343.link = 'https://www.flickr.com/search/?lat=36.0819986&lon=138.0819134&radius=0.1&has_geo=1&view_all=1'
    complex_photo_343.person = None
    complex_photo_343.title = 'Suwa Grand Shrine (Suwa-taisha) 諏訪大社下社春宮'
    complex_photo_343.type_master = complex_type_master_23
    complex_photo_343.username = 'sugar4684'
    complex_photo_343.width = None
    complex_photo_343 = importer.save_or_locate(complex_photo_343)

    complex_photo_344 = Photo()
    complex_photo_344.height = None
    complex_photo_344.image_src = 'https://live.staticflickr.com/65535/47668002062_3c86bc8051_z.jpg'
    complex_photo_344.link = 'https://www.flickr.com/search/?lat=36.0810907&lon=138.0832405&radius=0.1&has_geo=1&view_all=1'
    complex_photo_344.person = None
    complex_photo_344.title = 'Suwa Grand Shrine (Suwa-taisha) 諏訪大社下社春宮'
    complex_photo_344.type_master = complex_type_master_23
    complex_photo_344.username = 'sugar4684'
    complex_photo_344.width = None
    complex_photo_344 = importer.save_or_locate(complex_photo_344)

    complex_photo_345 = Photo()
    complex_photo_345.height = None
    complex_photo_345.image_src = 'https://live.staticflickr.com/1743/41826655655_ea46dba63f_z.jpg'
    complex_photo_345.link = 'https://www.flickr.com/search/?lat=36.0761953&lon=138.0884701&radius=0.1&has_geo=1&view_all=1'
    complex_photo_345.person = None
    complex_photo_345.title = 'DSCN5376'
    complex_photo_345.type_master = complex_type_master_23
    complex_photo_345.username = 'tomkichige'
    complex_photo_345.width = None
    complex_photo_345 = importer.save_or_locate(complex_photo_345)

    complex_photo_346 = Photo()
    complex_photo_346.height = None
    complex_photo_346.image_src = 'https://live.staticflickr.com/65535/50348136216_ba75fa9449_z.jpg'
    complex_photo_346.link = 'https://www.flickr.com/search/?lat=36.0759143&lon=138.0902028&radius=0.1&has_geo=1&view_all=1'
    complex_photo_346.person = None
    complex_photo_346.title = '諏訪大社\u3000下社秋宮'
    complex_photo_346.type_master = complex_type_master_23
    complex_photo_346.username = 'Ton_4777'
    complex_photo_346.width = None
    complex_photo_346 = importer.save_or_locate(complex_photo_346)

    complex_photo_347 = Photo()
    complex_photo_347.height = None
    complex_photo_347.image_src = 'https://live.staticflickr.com/65535/49435243447_57efee0f39_z.jpg'
    complex_photo_347.link = 'https://www.flickr.com/search/?lat=36.0748867&lon=138.0903172&radius=0.1&has_geo=1&view_all=1'
    complex_photo_347.person = None
    complex_photo_347.title = '長野 Nagano｜諏訪大社 Suwa Shrine - 01'
    complex_photo_347.type_master = complex_type_master_23
    complex_photo_347.username = 'mhhung0807'
    complex_photo_347.width = None
    complex_photo_347 = importer.save_or_locate(complex_photo_347)

    complex_photo_348 = Photo()
    complex_photo_348.height = None
    complex_photo_348.image_src = 'https://live.staticflickr.com/65535/49434544913_1e463e6e18_z.jpg'
    complex_photo_348.link = 'https://www.flickr.com/search/?lat=36.0753487&lon=138.0912391&radius=0.1&has_geo=1&view_all=1'
    complex_photo_348.person = None
    complex_photo_348.title = '長野 Nagano｜諏訪大社 Suwa Shrine - 02'
    complex_photo_348.type_master = complex_type_master_23
    complex_photo_348.username = 'mhhung0807'
    complex_photo_348.width = None
    complex_photo_348 = importer.save_or_locate(complex_photo_348)

    complex_photo_349 = Photo()
    complex_photo_349.height = None
    complex_photo_349.image_src = 'https://live.staticflickr.com/65535/49435018851_42b4e639fb_z.jpg'
    complex_photo_349.link = 'https://www.flickr.com/search/?lat=36.0752022&lon=138.090985&radius=0.1&has_geo=1&view_all=1'
    complex_photo_349.person = None
    complex_photo_349.title = '長野 Nagano｜諏訪湖 Lake Suwa - 04'
    complex_photo_349.type_master = complex_type_master_23
    complex_photo_349.username = 'mhhung0807'
    complex_photo_349.width = None
    complex_photo_349 = importer.save_or_locate(complex_photo_349)

    complex_photo_350 = Photo()
    complex_photo_350.height = None
    complex_photo_350.image_src = 'https://live.staticflickr.com/65535/32777650927_d3a11cd043_z.jpg'
    complex_photo_350.link = 'https://www.flickr.com/search/?lat=36.0748088&lon=138.0907196&radius=0.1&has_geo=1&view_all=1'
    complex_photo_350.person = None
    complex_photo_350.title = '万治の石仏'
    complex_photo_350.type_master = complex_type_master_23
    complex_photo_350.username = 'sugar4684'
    complex_photo_350.width = None
    complex_photo_350 = importer.save_or_locate(complex_photo_350)

    complex_photo_351 = Photo()
    complex_photo_351.height = None
    complex_photo_351.image_src = 'https://live.staticflickr.com/2556/5695650450_f47f3de8c7_z.jpg'
    complex_photo_351.link = 'https://www.flickr.com/search/?lat=36.0657698&lon=138.1022627&radius=0.1&has_geo=1&view_all=1'
    complex_photo_351.person = None
    complex_photo_351.title = 'The Dinosaurs come again... 大人の悲鳴シリーズ2 #tarotaro3'
    complex_photo_351.type_master = complex_type_master_23
    complex_photo_351.username = 'tarotaro-san'
    complex_photo_351.width = None
    complex_photo_351 = importer.save_or_locate(complex_photo_351)

    complex_photo_352 = Photo()
    complex_photo_352.height = None
    complex_photo_352.image_src = 'https://live.staticflickr.com/65535/50859553272_0526444458_z.jpg'
    complex_photo_352.link = 'https://www.flickr.com/search/?lat=36.0620891&lon=138.1061045&radius=0.1&has_geo=1&view_all=1'
    complex_photo_352.person = None
    complex_photo_352.title = 'Signs of Lake Suwa omiwatari'
    complex_photo_352.type_master = complex_type_master_23
    complex_photo_352.username = 'masahiro miyasaka'
    complex_photo_352.width = None
    complex_photo_352 = importer.save_or_locate(complex_photo_352)

    complex_photo_353 = Photo()
    complex_photo_353.height = None
    complex_photo_353.image_src = 'https://live.staticflickr.com/560/32066845671_1fb2466b5f_z.jpg'
    complex_photo_353.link = 'https://www.flickr.com/search/?lat=36.1153249&lon=137.9458606&radius=0.1&has_geo=1&view_all=1'
    complex_photo_353.person = None
    complex_photo_353.title = '20090718-100621-shine09-mike-nikon'
    complex_photo_353.type_master = complex_type_master_23
    complex_photo_353.username = 'halffastcycling'
    complex_photo_353.width = None
    complex_photo_353 = importer.save_or_locate(complex_photo_353)

    # Processing model: complex.models.Tweet

    from complex.models import Tweet

    complex_tweet_1 = Tweet()
    complex_tweet_1.description = None
    complex_tweet_1.person = None
    complex_tweet_1.tweet_id = '1639460905850372097'
    complex_tweet_1.type_master = complex_type_master_52
    complex_tweet_1.url = None
    complex_tweet_1.username = None
    complex_tweet_1 = importer.save_or_locate(complex_tweet_1)

    complex_tweet_2 = Tweet()
    complex_tweet_2.description = None
    complex_tweet_2.person = None
    complex_tweet_2.tweet_id = '1639470356921741313'
    complex_tweet_2.type_master = complex_type_master_52
    complex_tweet_2.url = None
    complex_tweet_2.username = None
    complex_tweet_2 = importer.save_or_locate(complex_tweet_2)

    complex_tweet_3 = Tweet()
    complex_tweet_3.description = None
    complex_tweet_3.person = None
    complex_tweet_3.tweet_id = '1639483777666920448'
    complex_tweet_3.type_master = complex_type_master_52
    complex_tweet_3.url = None
    complex_tweet_3.username = None
    complex_tweet_3 = importer.save_or_locate(complex_tweet_3)

    complex_tweet_4 = Tweet()
    complex_tweet_4.description = None
    complex_tweet_4.person = None
    complex_tweet_4.tweet_id = '1641001458479902722'
    complex_tweet_4.type_master = complex_type_master_52
    complex_tweet_4.url = None
    complex_tweet_4.username = None
    complex_tweet_4 = importer.save_or_locate(complex_tweet_4)

    complex_tweet_5 = Tweet()
    complex_tweet_5.description = None
    complex_tweet_5.person = None
    complex_tweet_5.tweet_id = '1639451463079559174'
    complex_tweet_5.type_master = complex_type_master_52
    complex_tweet_5.url = None
    complex_tweet_5.username = None
    complex_tweet_5 = importer.save_or_locate(complex_tweet_5)

    complex_tweet_6 = Tweet()
    complex_tweet_6.description = None
    complex_tweet_6.person = None
    complex_tweet_6.tweet_id = '1641272835208347649'
    complex_tweet_6.type_master = complex_type_master_52
    complex_tweet_6.url = None
    complex_tweet_6.username = None
    complex_tweet_6 = importer.save_or_locate(complex_tweet_6)

    complex_tweet_7 = Tweet()
    complex_tweet_7.description = None
    complex_tweet_7.person = None
    complex_tweet_7.tweet_id = '1641244280890224640'
    complex_tweet_7.type_master = complex_type_master_52
    complex_tweet_7.url = None
    complex_tweet_7.username = None
    complex_tweet_7 = importer.save_or_locate(complex_tweet_7)

    complex_tweet_8 = Tweet()
    complex_tweet_8.description = None
    complex_tweet_8.person = None
    complex_tweet_8.tweet_id = '1641270532942225415'
    complex_tweet_8.type_master = complex_type_master_52
    complex_tweet_8.url = None
    complex_tweet_8.username = None
    complex_tweet_8 = importer.save_or_locate(complex_tweet_8)

    complex_tweet_9 = Tweet()
    complex_tweet_9.description = None
    complex_tweet_9.person = None
    complex_tweet_9.tweet_id = '1640896990698672128'
    complex_tweet_9.type_master = complex_type_master_52
    complex_tweet_9.url = None
    complex_tweet_9.username = None
    complex_tweet_9 = importer.save_or_locate(complex_tweet_9)

    complex_tweet_10 = Tweet()
    complex_tweet_10.description = None
    complex_tweet_10.person = None
    complex_tweet_10.tweet_id = '1639761318986260480'
    complex_tweet_10.type_master = complex_type_master_52
    complex_tweet_10.url = None
    complex_tweet_10.username = None
    complex_tweet_10 = importer.save_or_locate(complex_tweet_10)

    complex_tweet_11 = Tweet()
    complex_tweet_11.description = None
    complex_tweet_11.person = None
    complex_tweet_11.tweet_id = '1639781852746596352'
    complex_tweet_11.type_master = complex_type_master_52
    complex_tweet_11.url = None
    complex_tweet_11.username = None
    complex_tweet_11 = importer.save_or_locate(complex_tweet_11)

    complex_tweet_12 = Tweet()
    complex_tweet_12.description = None
    complex_tweet_12.person = None
    complex_tweet_12.tweet_id = '1639083337716498433'
    complex_tweet_12.type_master = complex_type_master_52
    complex_tweet_12.url = None
    complex_tweet_12.username = None
    complex_tweet_12 = importer.save_or_locate(complex_tweet_12)

    complex_tweet_13 = Tweet()
    complex_tweet_13.description = None
    complex_tweet_13.person = None
    complex_tweet_13.tweet_id = '1639114747244318721'
    complex_tweet_13.type_master = complex_type_master_52
    complex_tweet_13.url = None
    complex_tweet_13.username = None
    complex_tweet_13 = importer.save_or_locate(complex_tweet_13)

    complex_tweet_14 = Tweet()
    complex_tweet_14.description = None
    complex_tweet_14.person = None
    complex_tweet_14.tweet_id = '1640623246327394305'
    complex_tweet_14.type_master = complex_type_master_52
    complex_tweet_14.url = None
    complex_tweet_14.username = None
    complex_tweet_14 = importer.save_or_locate(complex_tweet_14)

    complex_tweet_15 = Tweet()
    complex_tweet_15.description = None
    complex_tweet_15.person = None
    complex_tweet_15.tweet_id = '1640506439847276545'
    complex_tweet_15.type_master = complex_type_master_52
    complex_tweet_15.url = None
    complex_tweet_15.username = None
    complex_tweet_15 = importer.save_or_locate(complex_tweet_15)

    complex_tweet_16 = Tweet()
    complex_tweet_16.description = None
    complex_tweet_16.person = None
    complex_tweet_16.tweet_id = '1641276032257863686'
    complex_tweet_16.type_master = complex_type_master_52
    complex_tweet_16.url = None
    complex_tweet_16.username = None
    complex_tweet_16 = importer.save_or_locate(complex_tweet_16)

    complex_tweet_17 = Tweet()
    complex_tweet_17.description = None
    complex_tweet_17.person = None
    complex_tweet_17.tweet_id = '1639887220663529473'
    complex_tweet_17.type_master = complex_type_master_52
    complex_tweet_17.url = None
    complex_tweet_17.username = None
    complex_tweet_17 = importer.save_or_locate(complex_tweet_17)

    complex_tweet_18 = Tweet()
    complex_tweet_18.description = None
    complex_tweet_18.person = None
    complex_tweet_18.tweet_id = '1640144938754007040'
    complex_tweet_18.type_master = complex_type_master_52
    complex_tweet_18.url = None
    complex_tweet_18.username = None
    complex_tweet_18 = importer.save_or_locate(complex_tweet_18)

    complex_tweet_19 = Tweet()
    complex_tweet_19.description = None
    complex_tweet_19.person = None
    complex_tweet_19.tweet_id = '1638369260534657024'
    complex_tweet_19.type_master = complex_type_master_52
    complex_tweet_19.url = None
    complex_tweet_19.username = None
    complex_tweet_19 = importer.save_or_locate(complex_tweet_19)

    complex_tweet_20 = Tweet()
    complex_tweet_20.description = None
    complex_tweet_20.person = None
    complex_tweet_20.tweet_id = '1638354318754566144'
    complex_tweet_20.type_master = complex_type_master_52
    complex_tweet_20.url = None
    complex_tweet_20.username = None
    complex_tweet_20 = importer.save_or_locate(complex_tweet_20)

    complex_tweet_21 = Tweet()
    complex_tweet_21.description = None
    complex_tweet_21.person = None
    complex_tweet_21.tweet_id = '1640583879827283969'
    complex_tweet_21.type_master = complex_type_master_52
    complex_tweet_21.url = None
    complex_tweet_21.username = None
    complex_tweet_21 = importer.save_or_locate(complex_tweet_21)

    complex_tweet_22 = Tweet()
    complex_tweet_22.description = None
    complex_tweet_22.person = None
    complex_tweet_22.tweet_id = '1641266771024814083'
    complex_tweet_22.type_master = complex_type_master_52
    complex_tweet_22.url = None
    complex_tweet_22.username = None
    complex_tweet_22 = importer.save_or_locate(complex_tweet_22)

    complex_tweet_23 = Tweet()
    complex_tweet_23.description = None
    complex_tweet_23.person = None
    complex_tweet_23.tweet_id = '1638769038527705088'
    complex_tweet_23.type_master = complex_type_master_52
    complex_tweet_23.url = None
    complex_tweet_23.username = None
    complex_tweet_23 = importer.save_or_locate(complex_tweet_23)

    complex_tweet_24 = Tweet()
    complex_tweet_24.description = None
    complex_tweet_24.person = None
    complex_tweet_24.tweet_id = '1641153547827056643'
    complex_tweet_24.type_master = complex_type_master_52
    complex_tweet_24.url = None
    complex_tweet_24.username = None
    complex_tweet_24 = importer.save_or_locate(complex_tweet_24)

    complex_tweet_25 = Tweet()
    complex_tweet_25.description = None
    complex_tweet_25.person = None
    complex_tweet_25.tweet_id = '1639590275034284034'
    complex_tweet_25.type_master = complex_type_master_52
    complex_tweet_25.url = None
    complex_tweet_25.username = None
    complex_tweet_25 = importer.save_or_locate(complex_tweet_25)

    complex_tweet_26 = Tweet()
    complex_tweet_26.description = None
    complex_tweet_26.person = None
    complex_tweet_26.tweet_id = '1641275859960045569'
    complex_tweet_26.type_master = complex_type_master_52
    complex_tweet_26.url = None
    complex_tweet_26.username = None
    complex_tweet_26 = importer.save_or_locate(complex_tweet_26)

    complex_tweet_27 = Tweet()
    complex_tweet_27.description = None
    complex_tweet_27.person = None
    complex_tweet_27.tweet_id = '1641259868320350209'
    complex_tweet_27.type_master = complex_type_master_52
    complex_tweet_27.url = None
    complex_tweet_27.username = None
    complex_tweet_27 = importer.save_or_locate(complex_tweet_27)

    complex_tweet_28 = Tweet()
    complex_tweet_28.description = None
    complex_tweet_28.person = None
    complex_tweet_28.tweet_id = '1639803395203555330'
    complex_tweet_28.type_master = complex_type_master_52
    complex_tweet_28.url = None
    complex_tweet_28.username = None
    complex_tweet_28 = importer.save_or_locate(complex_tweet_28)

    complex_tweet_29 = Tweet()
    complex_tweet_29.description = None
    complex_tweet_29.person = None
    complex_tweet_29.tweet_id = '1638434686828527618'
    complex_tweet_29.type_master = complex_type_master_52
    complex_tweet_29.url = None
    complex_tweet_29.username = None
    complex_tweet_29 = importer.save_or_locate(complex_tweet_29)

    complex_tweet_30 = Tweet()
    complex_tweet_30.description = None
    complex_tweet_30.person = None
    complex_tweet_30.tweet_id = '1640624741105954823'
    complex_tweet_30.type_master = complex_type_master_52
    complex_tweet_30.url = None
    complex_tweet_30.username = None
    complex_tweet_30 = importer.save_or_locate(complex_tweet_30)

    complex_tweet_31 = Tweet()
    complex_tweet_31.description = None
    complex_tweet_31.person = None
    complex_tweet_31.tweet_id = '1640571786197712899'
    complex_tweet_31.type_master = complex_type_master_52
    complex_tweet_31.url = None
    complex_tweet_31.username = None
    complex_tweet_31 = importer.save_or_locate(complex_tweet_31)

    complex_tweet_32 = Tweet()
    complex_tweet_32.description = None
    complex_tweet_32.person = None
    complex_tweet_32.tweet_id = '1639483462972502016'
    complex_tweet_32.type_master = complex_type_master_52
    complex_tweet_32.url = None
    complex_tweet_32.username = None
    complex_tweet_32 = importer.save_or_locate(complex_tweet_32)

    complex_tweet_33 = Tweet()
    complex_tweet_33.description = None
    complex_tweet_33.person = None
    complex_tweet_33.tweet_id = '1641064723276759041'
    complex_tweet_33.type_master = complex_type_master_52
    complex_tweet_33.url = None
    complex_tweet_33.username = None
    complex_tweet_33 = importer.save_or_locate(complex_tweet_33)

    complex_tweet_34 = Tweet()
    complex_tweet_34.description = None
    complex_tweet_34.person = None
    complex_tweet_34.tweet_id = '1639494892085993474'
    complex_tweet_34.type_master = complex_type_master_52
    complex_tweet_34.url = None
    complex_tweet_34.username = None
    complex_tweet_34 = importer.save_or_locate(complex_tweet_34)

    complex_tweet_35 = Tweet()
    complex_tweet_35.description = None
    complex_tweet_35.person = None
    complex_tweet_35.tweet_id = '1640334170491592704'
    complex_tweet_35.type_master = complex_type_master_52
    complex_tweet_35.url = None
    complex_tweet_35.username = None
    complex_tweet_35 = importer.save_or_locate(complex_tweet_35)

    complex_tweet_36 = Tweet()
    complex_tweet_36.description = None
    complex_tweet_36.person = None
    complex_tweet_36.tweet_id = '1641232944730902529'
    complex_tweet_36.type_master = complex_type_master_52
    complex_tweet_36.url = None
    complex_tweet_36.username = None
    complex_tweet_36 = importer.save_or_locate(complex_tweet_36)

    complex_tweet_37 = Tweet()
    complex_tweet_37.description = None
    complex_tweet_37.person = None
    complex_tweet_37.tweet_id = '1638157502591426560'
    complex_tweet_37.type_master = complex_type_master_52
    complex_tweet_37.url = None
    complex_tweet_37.username = None
    complex_tweet_37 = importer.save_or_locate(complex_tweet_37)

    complex_tweet_38 = Tweet()
    complex_tweet_38.description = None
    complex_tweet_38.person = None
    complex_tweet_38.tweet_id = '1638291166864068612'
    complex_tweet_38.type_master = complex_type_master_52
    complex_tweet_38.url = None
    complex_tweet_38.username = None
    complex_tweet_38 = importer.save_or_locate(complex_tweet_38)

    complex_tweet_39 = Tweet()
    complex_tweet_39.description = None
    complex_tweet_39.person = None
    complex_tweet_39.tweet_id = '1641243776642433026'
    complex_tweet_39.type_master = complex_type_master_52
    complex_tweet_39.url = None
    complex_tweet_39.username = None
    complex_tweet_39 = importer.save_or_locate(complex_tweet_39)

    complex_tweet_40 = Tweet()
    complex_tweet_40.description = None
    complex_tweet_40.person = None
    complex_tweet_40.tweet_id = '1638418859794354178'
    complex_tweet_40.type_master = complex_type_master_52
    complex_tweet_40.url = None
    complex_tweet_40.username = None
    complex_tweet_40 = importer.save_or_locate(complex_tweet_40)

    complex_tweet_41 = Tweet()
    complex_tweet_41.description = None
    complex_tweet_41.person = None
    complex_tweet_41.tweet_id = '1639867120958808064'
    complex_tweet_41.type_master = complex_type_master_52
    complex_tweet_41.url = None
    complex_tweet_41.username = None
    complex_tweet_41 = importer.save_or_locate(complex_tweet_41)

    complex_tweet_42 = Tweet()
    complex_tweet_42.description = None
    complex_tweet_42.person = None
    complex_tweet_42.tweet_id = '1640497375453257728'
    complex_tweet_42.type_master = complex_type_master_52
    complex_tweet_42.url = None
    complex_tweet_42.username = None
    complex_tweet_42 = importer.save_or_locate(complex_tweet_42)

    complex_tweet_43 = Tweet()
    complex_tweet_43.description = None
    complex_tweet_43.person = None
    complex_tweet_43.tweet_id = '1638803606236459009'
    complex_tweet_43.type_master = complex_type_master_52
    complex_tweet_43.url = None
    complex_tweet_43.username = None
    complex_tweet_43 = importer.save_or_locate(complex_tweet_43)

    complex_tweet_44 = Tweet()
    complex_tweet_44.description = None
    complex_tweet_44.person = None
    complex_tweet_44.tweet_id = '1638431890213580802'
    complex_tweet_44.type_master = complex_type_master_52
    complex_tweet_44.url = None
    complex_tweet_44.username = None
    complex_tweet_44 = importer.save_or_locate(complex_tweet_44)

    complex_tweet_45 = Tweet()
    complex_tweet_45.description = None
    complex_tweet_45.person = None
    complex_tweet_45.tweet_id = '1639769172015022080'
    complex_tweet_45.type_master = complex_type_master_52
    complex_tweet_45.url = None
    complex_tweet_45.username = None
    complex_tweet_45 = importer.save_or_locate(complex_tweet_45)

    complex_tweet_46 = Tweet()
    complex_tweet_46.description = None
    complex_tweet_46.person = None
    complex_tweet_46.tweet_id = '1641016574235623424'
    complex_tweet_46.type_master = complex_type_master_52
    complex_tweet_46.url = None
    complex_tweet_46.username = None
    complex_tweet_46 = importer.save_or_locate(complex_tweet_46)

    complex_tweet_47 = Tweet()
    complex_tweet_47.description = None
    complex_tweet_47.person = None
    complex_tweet_47.tweet_id = '1638748833214771200'
    complex_tweet_47.type_master = complex_type_master_52
    complex_tweet_47.url = None
    complex_tweet_47.username = None
    complex_tweet_47 = importer.save_or_locate(complex_tweet_47)

    complex_tweet_48 = Tweet()
    complex_tweet_48.description = None
    complex_tweet_48.person = None
    complex_tweet_48.tweet_id = '1639842267820179456'
    complex_tweet_48.type_master = complex_type_master_52
    complex_tweet_48.url = None
    complex_tweet_48.username = None
    complex_tweet_48 = importer.save_or_locate(complex_tweet_48)

    complex_tweet_49 = Tweet()
    complex_tweet_49.description = None
    complex_tweet_49.person = None
    complex_tweet_49.tweet_id = '1639799720682954754'
    complex_tweet_49.type_master = complex_type_master_52
    complex_tweet_49.url = None
    complex_tweet_49.username = None
    complex_tweet_49 = importer.save_or_locate(complex_tweet_49)

    complex_tweet_50 = Tweet()
    complex_tweet_50.description = None
    complex_tweet_50.person = None
    complex_tweet_50.tweet_id = '1641333771986440197'
    complex_tweet_50.type_master = complex_type_master_52
    complex_tweet_50.url = None
    complex_tweet_50.username = None
    complex_tweet_50 = importer.save_or_locate(complex_tweet_50)

    complex_tweet_51 = Tweet()
    complex_tweet_51.description = None
    complex_tweet_51.person = None
    complex_tweet_51.tweet_id = '1638744631755313152'
    complex_tweet_51.type_master = complex_type_master_52
    complex_tweet_51.url = None
    complex_tweet_51.username = None
    complex_tweet_51 = importer.save_or_locate(complex_tweet_51)

    complex_tweet_52 = Tweet()
    complex_tweet_52.description = None
    complex_tweet_52.person = None
    complex_tweet_52.tweet_id = '1638661124240605185'
    complex_tweet_52.type_master = complex_type_master_52
    complex_tweet_52.url = None
    complex_tweet_52.username = None
    complex_tweet_52 = importer.save_or_locate(complex_tweet_52)

    complex_tweet_53 = Tweet()
    complex_tweet_53.description = None
    complex_tweet_53.person = None
    complex_tweet_53.tweet_id = '1640549132480675841'
    complex_tweet_53.type_master = complex_type_master_52
    complex_tweet_53.url = None
    complex_tweet_53.username = None
    complex_tweet_53 = importer.save_or_locate(complex_tweet_53)

    complex_tweet_54 = Tweet()
    complex_tweet_54.description = None
    complex_tweet_54.person = None
    complex_tweet_54.tweet_id = '1640534522402942977'
    complex_tweet_54.type_master = complex_type_master_52
    complex_tweet_54.url = None
    complex_tweet_54.username = None
    complex_tweet_54 = importer.save_or_locate(complex_tweet_54)

    complex_tweet_55 = Tweet()
    complex_tweet_55.description = None
    complex_tweet_55.person = None
    complex_tweet_55.tweet_id = '1641252382733647872'
    complex_tweet_55.type_master = complex_type_master_52
    complex_tweet_55.url = None
    complex_tweet_55.username = None
    complex_tweet_55 = importer.save_or_locate(complex_tweet_55)

    complex_tweet_56 = Tweet()
    complex_tweet_56.description = None
    complex_tweet_56.person = None
    complex_tweet_56.tweet_id = '1639949483025768449'
    complex_tweet_56.type_master = complex_type_master_52
    complex_tweet_56.url = None
    complex_tweet_56.username = None
    complex_tweet_56 = importer.save_or_locate(complex_tweet_56)

    complex_tweet_57 = Tweet()
    complex_tweet_57.description = None
    complex_tweet_57.person = None
    complex_tweet_57.tweet_id = '1356727800854536194'
    complex_tweet_57.type_master = complex_type_master_52
    complex_tweet_57.url = None
    complex_tweet_57.username = None
    complex_tweet_57 = importer.save_or_locate(complex_tweet_57)

    complex_tweet_58 = Tweet()
    complex_tweet_58.description = None
    complex_tweet_58.person = None
    complex_tweet_58.tweet_id = '1356728289205780482'
    complex_tweet_58.type_master = complex_type_master_52
    complex_tweet_58.url = None
    complex_tweet_58.username = None
    complex_tweet_58 = importer.save_or_locate(complex_tweet_58)

    complex_tweet_59 = Tweet()
    complex_tweet_59.description = None
    complex_tweet_59.person = None
    complex_tweet_59.tweet_id = '1356728690164436993'
    complex_tweet_59.type_master = complex_type_master_52
    complex_tweet_59.url = None
    complex_tweet_59.username = None
    complex_tweet_59 = importer.save_or_locate(complex_tweet_59)

    complex_tweet_60 = Tweet()
    complex_tweet_60.description = None
    complex_tweet_60.person = None
    complex_tweet_60.tweet_id = '1356731407851130882'
    complex_tweet_60.type_master = complex_type_master_52
    complex_tweet_60.url = None
    complex_tweet_60.username = None
    complex_tweet_60 = importer.save_or_locate(complex_tweet_60)

    complex_tweet_61 = Tweet()
    complex_tweet_61.description = None
    complex_tweet_61.person = None
    complex_tweet_61.tweet_id = '1356734621682032641'
    complex_tweet_61.type_master = complex_type_master_52
    complex_tweet_61.url = None
    complex_tweet_61.username = None
    complex_tweet_61 = importer.save_or_locate(complex_tweet_61)

    complex_tweet_62 = Tweet()
    complex_tweet_62.description = None
    complex_tweet_62.person = None
    complex_tweet_62.tweet_id = '1356737001681113089'
    complex_tweet_62.type_master = complex_type_master_52
    complex_tweet_62.url = None
    complex_tweet_62.username = None
    complex_tweet_62 = importer.save_or_locate(complex_tweet_62)

    complex_tweet_63 = Tweet()
    complex_tweet_63.description = None
    complex_tweet_63.person = None
    complex_tweet_63.tweet_id = '1356738652378816515'
    complex_tweet_63.type_master = complex_type_master_52
    complex_tweet_63.url = None
    complex_tweet_63.username = None
    complex_tweet_63 = importer.save_or_locate(complex_tweet_63)

    complex_tweet_64 = Tweet()
    complex_tweet_64.description = None
    complex_tweet_64.person = None
    complex_tweet_64.tweet_id = '1356740048192823297'
    complex_tweet_64.type_master = complex_type_master_52
    complex_tweet_64.url = None
    complex_tweet_64.username = None
    complex_tweet_64 = importer.save_or_locate(complex_tweet_64)

    complex_tweet_65 = Tweet()
    complex_tweet_65.description = None
    complex_tweet_65.person = None
    complex_tweet_65.tweet_id = '1356743717240020998'
    complex_tweet_65.type_master = complex_type_master_52
    complex_tweet_65.url = None
    complex_tweet_65.username = None
    complex_tweet_65 = importer.save_or_locate(complex_tweet_65)

    complex_tweet_66 = Tweet()
    complex_tweet_66.description = None
    complex_tweet_66.person = None
    complex_tweet_66.tweet_id = '1640277958349791232'
    complex_tweet_66.type_master = complex_type_master_52
    complex_tweet_66.url = None
    complex_tweet_66.username = None
    complex_tweet_66 = importer.save_or_locate(complex_tweet_66)

    complex_tweet_67 = Tweet()
    complex_tweet_67.description = None
    complex_tweet_67.person = None
    complex_tweet_67.tweet_id = '1356783562016522241'
    complex_tweet_67.type_master = complex_type_master_52
    complex_tweet_67.url = None
    complex_tweet_67.username = None
    complex_tweet_67 = importer.save_or_locate(complex_tweet_67)

    complex_tweet_68 = Tweet()
    complex_tweet_68.description = None
    complex_tweet_68.person = None
    complex_tweet_68.tweet_id = '1356789878155956225'
    complex_tweet_68.type_master = complex_type_master_52
    complex_tweet_68.url = None
    complex_tweet_68.username = None
    complex_tweet_68 = importer.save_or_locate(complex_tweet_68)

    complex_tweet_69 = Tweet()
    complex_tweet_69.description = None
    complex_tweet_69.person = None
    complex_tweet_69.tweet_id = '1356796933445046274'
    complex_tweet_69.type_master = complex_type_master_52
    complex_tweet_69.url = None
    complex_tweet_69.username = None
    complex_tweet_69 = importer.save_or_locate(complex_tweet_69)

    complex_tweet_70 = Tweet()
    complex_tweet_70.description = None
    complex_tweet_70.person = None
    complex_tweet_70.tweet_id = '1356813548194648066'
    complex_tweet_70.type_master = complex_type_master_52
    complex_tweet_70.url = None
    complex_tweet_70.username = None
    complex_tweet_70 = importer.save_or_locate(complex_tweet_70)

    complex_tweet_71 = Tweet()
    complex_tweet_71.description = None
    complex_tweet_71.person = None
    complex_tweet_71.tweet_id = '1356821219480281089'
    complex_tweet_71.type_master = complex_type_master_52
    complex_tweet_71.url = None
    complex_tweet_71.username = None
    complex_tweet_71 = importer.save_or_locate(complex_tweet_71)

    complex_tweet_72 = Tweet()
    complex_tweet_72.description = None
    complex_tweet_72.person = None
    complex_tweet_72.tweet_id = '1356823217529184258'
    complex_tweet_72.type_master = complex_type_master_52
    complex_tweet_72.url = None
    complex_tweet_72.username = None
    complex_tweet_72 = importer.save_or_locate(complex_tweet_72)

    complex_tweet_73 = Tweet()
    complex_tweet_73.description = None
    complex_tweet_73.person = None
    complex_tweet_73.tweet_id = '1356891816268754950'
    complex_tweet_73.type_master = complex_type_master_52
    complex_tweet_73.url = None
    complex_tweet_73.username = None
    complex_tweet_73 = importer.save_or_locate(complex_tweet_73)

    complex_tweet_74 = Tweet()
    complex_tweet_74.description = None
    complex_tweet_74.person = None
    complex_tweet_74.tweet_id = '1356850055135731712'
    complex_tweet_74.type_master = complex_type_master_52
    complex_tweet_74.url = None
    complex_tweet_74.username = None
    complex_tweet_74 = importer.save_or_locate(complex_tweet_74)

    complex_tweet_75 = Tweet()
    complex_tweet_75.description = None
    complex_tweet_75.person = None
    complex_tweet_75.tweet_id = '1640926245432233986'
    complex_tweet_75.type_master = complex_type_master_52
    complex_tweet_75.url = None
    complex_tweet_75.username = None
    complex_tweet_75 = importer.save_or_locate(complex_tweet_75)

    complex_tweet_76 = Tweet()
    complex_tweet_76.description = None
    complex_tweet_76.person = None
    complex_tweet_76.tweet_id = '1641401583396339714'
    complex_tweet_76.type_master = complex_type_master_52
    complex_tweet_76.url = None
    complex_tweet_76.username = None
    complex_tweet_76 = importer.save_or_locate(complex_tweet_76)

    complex_tweet_77 = Tweet()
    complex_tweet_77.description = None
    complex_tweet_77.person = None
    complex_tweet_77.tweet_id = '1640919679484022784'
    complex_tweet_77.type_master = complex_type_master_52
    complex_tweet_77.url = None
    complex_tweet_77.username = None
    complex_tweet_77 = importer.save_or_locate(complex_tweet_77)

    complex_tweet_78 = Tweet()
    complex_tweet_78.description = None
    complex_tweet_78.person = None
    complex_tweet_78.tweet_id = '1640568832522690562'
    complex_tweet_78.type_master = complex_type_master_52
    complex_tweet_78.url = None
    complex_tweet_78.username = None
    complex_tweet_78 = importer.save_or_locate(complex_tweet_78)

    complex_tweet_79 = Tweet()
    complex_tweet_79.description = None
    complex_tweet_79.person = None
    complex_tweet_79.tweet_id = '1638698132061188096'
    complex_tweet_79.type_master = complex_type_master_52
    complex_tweet_79.url = None
    complex_tweet_79.username = None
    complex_tweet_79 = importer.save_or_locate(complex_tweet_79)

    complex_tweet_80 = Tweet()
    complex_tweet_80.description = None
    complex_tweet_80.person = None
    complex_tweet_80.tweet_id = '1638553488371113987'
    complex_tweet_80.type_master = complex_type_master_52
    complex_tweet_80.url = None
    complex_tweet_80.username = None
    complex_tweet_80 = importer.save_or_locate(complex_tweet_80)

    complex_tweet_81 = Tweet()
    complex_tweet_81.description = None
    complex_tweet_81.person = None
    complex_tweet_81.tweet_id = '1640595402893455360'
    complex_tweet_81.type_master = complex_type_master_52
    complex_tweet_81.url = None
    complex_tweet_81.username = None
    complex_tweet_81 = importer.save_or_locate(complex_tweet_81)

    complex_tweet_82 = Tweet()
    complex_tweet_82.description = None
    complex_tweet_82.person = None
    complex_tweet_82.tweet_id = '1638669282547740673'
    complex_tweet_82.type_master = complex_type_master_52
    complex_tweet_82.url = None
    complex_tweet_82.username = None
    complex_tweet_82 = importer.save_or_locate(complex_tweet_82)

    complex_tweet_83 = Tweet()
    complex_tweet_83.description = None
    complex_tweet_83.person = None
    complex_tweet_83.tweet_id = '1638670166925144064'
    complex_tweet_83.type_master = complex_type_master_52
    complex_tweet_83.url = None
    complex_tweet_83.username = None
    complex_tweet_83 = importer.save_or_locate(complex_tweet_83)

    complex_tweet_84 = Tweet()
    complex_tweet_84.description = None
    complex_tweet_84.person = None
    complex_tweet_84.tweet_id = '1638695673343393793'
    complex_tweet_84.type_master = complex_type_master_52
    complex_tweet_84.url = None
    complex_tweet_84.username = None
    complex_tweet_84 = importer.save_or_locate(complex_tweet_84)

    complex_tweet_85 = Tweet()
    complex_tweet_85.description = None
    complex_tweet_85.person = None
    complex_tweet_85.tweet_id = '1640843649335402497'
    complex_tweet_85.type_master = complex_type_master_52
    complex_tweet_85.url = None
    complex_tweet_85.username = None
    complex_tweet_85 = importer.save_or_locate(complex_tweet_85)

    complex_tweet_86 = Tweet()
    complex_tweet_86.description = None
    complex_tweet_86.person = None
    complex_tweet_86.tweet_id = '1640199377976262658'
    complex_tweet_86.type_master = complex_type_master_52
    complex_tweet_86.url = None
    complex_tweet_86.username = None
    complex_tweet_86 = importer.save_or_locate(complex_tweet_86)

    complex_tweet_87 = Tweet()
    complex_tweet_87.description = None
    complex_tweet_87.person = None
    complex_tweet_87.tweet_id = '1639782642026414081'
    complex_tweet_87.type_master = complex_type_master_52
    complex_tweet_87.url = None
    complex_tweet_87.username = None
    complex_tweet_87 = importer.save_or_locate(complex_tweet_87)

    complex_tweet_88 = Tweet()
    complex_tweet_88.description = None
    complex_tweet_88.person = None
    complex_tweet_88.tweet_id = '1639906488771567617'
    complex_tweet_88.type_master = complex_type_master_52
    complex_tweet_88.url = None
    complex_tweet_88.username = None
    complex_tweet_88 = importer.save_or_locate(complex_tweet_88)

    complex_tweet_89 = Tweet()
    complex_tweet_89.description = None
    complex_tweet_89.person = None
    complex_tweet_89.tweet_id = '1639536126376673280'
    complex_tweet_89.type_master = complex_type_master_52
    complex_tweet_89.url = None
    complex_tweet_89.username = None
    complex_tweet_89 = importer.save_or_locate(complex_tweet_89)

    complex_tweet_90 = Tweet()
    complex_tweet_90.description = None
    complex_tweet_90.person = None
    complex_tweet_90.tweet_id = '1640963334420807680'
    complex_tweet_90.type_master = complex_type_master_52
    complex_tweet_90.url = None
    complex_tweet_90.username = None
    complex_tweet_90 = importer.save_or_locate(complex_tweet_90)

    complex_tweet_91 = Tweet()
    complex_tweet_91.description = None
    complex_tweet_91.person = None
    complex_tweet_91.tweet_id = '1639562203442597888'
    complex_tweet_91.type_master = complex_type_master_52
    complex_tweet_91.url = None
    complex_tweet_91.username = None
    complex_tweet_91 = importer.save_or_locate(complex_tweet_91)

    complex_tweet_92 = Tweet()
    complex_tweet_92.description = None
    complex_tweet_92.person = None
    complex_tweet_92.tweet_id = '1639466510858199047'
    complex_tweet_92.type_master = complex_type_master_52
    complex_tweet_92.url = None
    complex_tweet_92.username = None
    complex_tweet_92 = importer.save_or_locate(complex_tweet_92)

    complex_tweet_93 = Tweet()
    complex_tweet_93.description = None
    complex_tweet_93.person = None
    complex_tweet_93.tweet_id = '1638423793805795329'
    complex_tweet_93.type_master = complex_type_master_52
    complex_tweet_93.url = None
    complex_tweet_93.username = None
    complex_tweet_93 = importer.save_or_locate(complex_tweet_93)

    complex_tweet_94 = Tweet()
    complex_tweet_94.description = None
    complex_tweet_94.person = None
    complex_tweet_94.tweet_id = '1640205489274335232'
    complex_tweet_94.type_master = complex_type_master_52
    complex_tweet_94.url = None
    complex_tweet_94.username = None
    complex_tweet_94 = importer.save_or_locate(complex_tweet_94)

    complex_tweet_95 = Tweet()
    complex_tweet_95.description = None
    complex_tweet_95.person = None
    complex_tweet_95.tweet_id = '1641342904701427712'
    complex_tweet_95.type_master = complex_type_master_52
    complex_tweet_95.url = None
    complex_tweet_95.username = None
    complex_tweet_95 = importer.save_or_locate(complex_tweet_95)

    complex_tweet_96 = Tweet()
    complex_tweet_96.description = None
    complex_tweet_96.person = None
    complex_tweet_96.tweet_id = '1639482736825212928'
    complex_tweet_96.type_master = complex_type_master_52
    complex_tweet_96.url = None
    complex_tweet_96.username = None
    complex_tweet_96 = importer.save_or_locate(complex_tweet_96)

    complex_tweet_97 = Tweet()
    complex_tweet_97.description = None
    complex_tweet_97.person = None
    complex_tweet_97.tweet_id = '1640221677450678274'
    complex_tweet_97.type_master = complex_type_master_52
    complex_tweet_97.url = None
    complex_tweet_97.username = None
    complex_tweet_97 = importer.save_or_locate(complex_tweet_97)

    complex_tweet_98 = Tweet()
    complex_tweet_98.description = None
    complex_tweet_98.person = None
    complex_tweet_98.tweet_id = '1640964879514324993'
    complex_tweet_98.type_master = complex_type_master_52
    complex_tweet_98.url = None
    complex_tweet_98.username = None
    complex_tweet_98 = importer.save_or_locate(complex_tweet_98)

    complex_tweet_99 = Tweet()
    complex_tweet_99.description = None
    complex_tweet_99.person = None
    complex_tweet_99.tweet_id = '1641236708426383366'
    complex_tweet_99.type_master = complex_type_master_52
    complex_tweet_99.url = None
    complex_tweet_99.username = None
    complex_tweet_99 = importer.save_or_locate(complex_tweet_99)

    complex_tweet_100 = Tweet()
    complex_tweet_100.description = None
    complex_tweet_100.person = None
    complex_tweet_100.tweet_id = '1639100927411109890'
    complex_tweet_100.type_master = complex_type_master_52
    complex_tweet_100.url = None
    complex_tweet_100.username = None
    complex_tweet_100 = importer.save_or_locate(complex_tweet_100)

    complex_tweet_101 = Tweet()
    complex_tweet_101.description = None
    complex_tweet_101.person = None
    complex_tweet_101.tweet_id = '1639837726424834050'
    complex_tweet_101.type_master = complex_type_master_52
    complex_tweet_101.url = None
    complex_tweet_101.username = None
    complex_tweet_101 = importer.save_or_locate(complex_tweet_101)

    complex_tweet_102 = Tweet()
    complex_tweet_102.description = None
    complex_tweet_102.person = None
    complex_tweet_102.tweet_id = '1639835686114148352'
    complex_tweet_102.type_master = complex_type_master_52
    complex_tweet_102.url = None
    complex_tweet_102.username = None
    complex_tweet_102 = importer.save_or_locate(complex_tweet_102)

    complex_tweet_103 = Tweet()
    complex_tweet_103.description = None
    complex_tweet_103.person = None
    complex_tweet_103.tweet_id = '1638733525758390274'
    complex_tweet_103.type_master = complex_type_master_52
    complex_tweet_103.url = None
    complex_tweet_103.username = None
    complex_tweet_103 = importer.save_or_locate(complex_tweet_103)

    complex_tweet_104 = Tweet()
    complex_tweet_104.description = None
    complex_tweet_104.person = None
    complex_tweet_104.tweet_id = '1640576403526524929'
    complex_tweet_104.type_master = complex_type_master_52
    complex_tweet_104.url = None
    complex_tweet_104.username = None
    complex_tweet_104 = importer.save_or_locate(complex_tweet_104)

    complex_tweet_105 = Tweet()
    complex_tweet_105.description = None
    complex_tweet_105.person = None
    complex_tweet_105.tweet_id = '1639761993283391489'
    complex_tweet_105.type_master = complex_type_master_52
    complex_tweet_105.url = None
    complex_tweet_105.username = None
    complex_tweet_105 = importer.save_or_locate(complex_tweet_105)

    complex_tweet_106 = Tweet()
    complex_tweet_106.description = None
    complex_tweet_106.person = None
    complex_tweet_106.tweet_id = '1639167173905244161'
    complex_tweet_106.type_master = complex_type_master_52
    complex_tweet_106.url = None
    complex_tweet_106.username = None
    complex_tweet_106 = importer.save_or_locate(complex_tweet_106)

    complex_tweet_107 = Tweet()
    complex_tweet_107.description = None
    complex_tweet_107.person = None
    complex_tweet_107.tweet_id = '1640617221788499968'
    complex_tweet_107.type_master = complex_type_master_52
    complex_tweet_107.url = None
    complex_tweet_107.username = None
    complex_tweet_107 = importer.save_or_locate(complex_tweet_107)

    complex_tweet_108 = Tweet()
    complex_tweet_108.description = None
    complex_tweet_108.person = None
    complex_tweet_108.tweet_id = '1639425741371879425'
    complex_tweet_108.type_master = complex_type_master_52
    complex_tweet_108.url = None
    complex_tweet_108.username = None
    complex_tweet_108 = importer.save_or_locate(complex_tweet_108)

    # Processing model: complex.models.Web_comic

    from complex.models import Web_comic


    # Processing model: complex.models.Fragment

    from complex.models import Fragment


    # Processing model: complex.models.Story

    from complex.models import Story

    complex_story_1 = Story()
    complex_story_1.camera_zoom_level = 10
    complex_story_1.comic = complex_comic_1
    complex_story_1.journey = complex_journey_1
    complex_story_1.magazine = complex_magazine_2
    complex_story_1.subtitle = 'はじめの1225段'
    complex_story_1.title = '第1旅 会津若松'
    complex_story_1.type_master = complex_type_master_40
    complex_story_1 = importer.save_or_locate(complex_story_1)

    complex_story_2 = Story()
    complex_story_2.camera_zoom_level = 11
    complex_story_2.comic = complex_comic_1
    complex_story_2.journey = complex_journey_2
    complex_story_2.magazine = complex_magazine_3
    complex_story_2.subtitle = '伊達じゃない伊達'
    complex_story_2.title = '第2旅 松島'
    complex_story_2.type_master = complex_type_master_40
    complex_story_2 = importer.save_or_locate(complex_story_2)

    complex_story_3 = Story()
    complex_story_3.camera_zoom_level = 11
    complex_story_3.comic = complex_comic_1
    complex_story_3.journey = complex_journey_3
    complex_story_3.magazine = complex_magazine_4
    complex_story_3.subtitle = 'きときとふたり旅'
    complex_story_3.title = '第3旅 黒部'
    complex_story_3.type_master = complex_type_master_40
    complex_story_3 = importer.save_or_locate(complex_story_3)

    complex_story_4 = Story()
    complex_story_4.camera_zoom_level = 10
    complex_story_4.comic = complex_comic_1
    complex_story_4.journey = complex_journey_4
    complex_story_4.magazine = complex_magazine_5
    complex_story_4.subtitle = 'そのままのコシで'
    complex_story_4.title = '第4旅 高松'
    complex_story_4.type_master = complex_type_master_40
    complex_story_4 = importer.save_or_locate(complex_story_4)

    complex_story_5 = Story()
    complex_story_5.camera_zoom_level = 9
    complex_story_5.comic = complex_comic_2
    complex_story_5.journey = complex_journey_5
    complex_story_5.magazine = complex_magazine_6
    complex_story_5.subtitle = 'ふ、ばいざしー'
    complex_story_5.title = '第5旅 京都'
    complex_story_5.type_master = complex_type_master_40
    complex_story_5 = importer.save_or_locate(complex_story_5)

    complex_story_6 = Story()
    complex_story_6.camera_zoom_level = 10
    complex_story_6.comic = complex_comic_2
    complex_story_6.journey = complex_journey_6
    complex_story_6.magazine = complex_magazine_7
    complex_story_6.subtitle = 'カラスと龍と蕎麦の先'
    complex_story_6.title = '第6旅 栃木'
    complex_story_6.type_master = complex_type_master_40
    complex_story_6 = importer.save_or_locate(complex_story_6)

    complex_story_7 = Story()
    complex_story_7.camera_zoom_level = 10
    complex_story_7.comic = complex_comic_2
    complex_story_7.journey = complex_journey_7
    complex_story_7.magazine = complex_magazine_8
    complex_story_7.subtitle = '初めての離島'
    complex_story_7.title = '第7旅 粟島'
    complex_story_7.type_master = complex_type_master_40
    complex_story_7 = importer.save_or_locate(complex_story_7)

    complex_story_8 = Story()
    complex_story_8.camera_zoom_level = 10
    complex_story_8.comic = complex_comic_2
    complex_story_8.journey = complex_journey_8
    complex_story_8.magazine = complex_magazine_9
    complex_story_8.subtitle = '神様と出会える街？'
    complex_story_8.title = '第8旅 伊勢'
    complex_story_8.type_master = complex_type_master_40
    complex_story_8 = importer.save_or_locate(complex_story_8)

    complex_story_9 = Story()
    complex_story_9.camera_zoom_level = 10
    complex_story_9.comic = complex_comic_2
    complex_story_9.journey = complex_journey_9
    complex_story_9.magazine = complex_magazine_10
    complex_story_9.subtitle = '三人よれば…バス？'
    complex_story_9.title = '第9旅 広島前編'
    complex_story_9.type_master = complex_type_master_40
    complex_story_9 = importer.save_or_locate(complex_story_9)

    complex_story_10 = Story()
    complex_story_10.camera_zoom_level = 9
    complex_story_10.comic = complex_comic_3
    complex_story_10.journey = complex_journey_9
    complex_story_10.magazine = complex_magazine_11
    complex_story_10.subtitle = '女子三人寄って睦まじい'
    complex_story_10.title = '第9旅 広島後編'
    complex_story_10.type_master = complex_type_master_40
    complex_story_10 = importer.save_or_locate(complex_story_10)

    complex_story_11 = Story()
    complex_story_11.camera_zoom_level = 9
    complex_story_11.comic = complex_comic_3
    complex_story_11.journey = complex_journey_10
    complex_story_11.magazine = complex_magazine_12
    complex_story_11.subtitle = '温泉で完成'
    complex_story_11.title = '第10旅 青森'
    complex_story_11.type_master = complex_type_master_40
    complex_story_11 = importer.save_or_locate(complex_story_11)

    complex_story_12 = Story()
    complex_story_12.camera_zoom_level = 9
    complex_story_12.comic = complex_comic_3
    complex_story_12.journey = complex_journey_11
    complex_story_12.magazine = complex_magazine_13
    complex_story_12.subtitle = '一年のおわりとはじまり'
    complex_story_12.title = '第11旅 和歌山'
    complex_story_12.type_master = complex_type_master_40
    complex_story_12 = importer.save_or_locate(complex_story_12)

    complex_story_13 = Story()
    complex_story_13.camera_zoom_level = 9
    complex_story_13.comic = complex_comic_3
    complex_story_13.journey = complex_journey_12
    complex_story_13.magazine = complex_magazine_14
    complex_story_13.subtitle = 'ココロのふるさと'
    complex_story_13.title = '第12旅 花巻'
    complex_story_13.type_master = complex_type_master_40
    complex_story_13 = importer.save_or_locate(complex_story_13)

    complex_story_14 = Story()
    complex_story_14.camera_zoom_level = 9
    complex_story_14.comic = complex_comic_3
    complex_story_14.journey = complex_journey_13
    complex_story_14.magazine = complex_magazine_15
    complex_story_14.subtitle = '師匠と片参り'
    complex_story_14.title = '第13旅 島根前編'
    complex_story_14.type_master = complex_type_master_40
    complex_story_14 = importer.save_or_locate(complex_story_14)

    complex_story_15 = Story()
    complex_story_15.camera_zoom_level = 9
    complex_story_15.comic = complex_comic_4
    complex_story_15.journey = complex_journey_13
    complex_story_15.magazine = complex_magazine_16
    complex_story_15.subtitle = '導かれて端っこ'
    complex_story_15.title = '第13旅 島根後編'
    complex_story_15.type_master = complex_type_master_40
    complex_story_15 = importer.save_or_locate(complex_story_15)

    complex_story_16 = Story()
    complex_story_16.camera_zoom_level = 10
    complex_story_16.comic = complex_comic_4
    complex_story_16.journey = complex_journey_14
    complex_story_16.magazine = complex_magazine_20
    complex_story_16.subtitle = 'ほんとうに都内'
    complex_story_16.title = '第14旅 奥多摩'
    complex_story_16.type_master = complex_type_master_40
    complex_story_16 = importer.save_or_locate(complex_story_16)

    complex_story_17 = Story()
    complex_story_17.camera_zoom_level = 12
    complex_story_17.comic = complex_comic_4
    complex_story_17.journey = complex_journey_15
    complex_story_17.magazine = complex_magazine_21
    complex_story_17.subtitle = 'それでも繋がってる'
    complex_story_17.title = '第15旅 都内'
    complex_story_17.type_master = complex_type_master_40
    complex_story_17 = importer.save_or_locate(complex_story_17)

    complex_story_18 = Story()
    complex_story_18.camera_zoom_level = 10
    complex_story_18.comic = complex_comic_5
    complex_story_18.journey = complex_journey_16
    complex_story_18.magazine = complex_magazine_22
    complex_story_18.subtitle = 'あたらしい旅'
    complex_story_18.title = '第16旅 茨城前編'
    complex_story_18.type_master = complex_type_master_40
    complex_story_18 = importer.save_or_locate(complex_story_18)

    complex_story_19 = Story()
    complex_story_19.camera_zoom_level = 10
    complex_story_19.comic = complex_comic_5
    complex_story_19.journey = complex_journey_16
    complex_story_19.magazine = complex_magazine_23
    complex_story_19.subtitle = '今日出来ることは！'
    complex_story_19.title = '第16旅 茨城後編'
    complex_story_19.type_master = complex_type_master_40
    complex_story_19 = importer.save_or_locate(complex_story_19)

    complex_story_20 = Story()
    complex_story_20.camera_zoom_level = 9
    complex_story_20.comic = complex_comic_5
    complex_story_20.journey = complex_journey_17
    complex_story_20.magazine = complex_magazine_24
    complex_story_20.subtitle = 'はじめての九州で'
    complex_story_20.title = '第17旅 九州前編'
    complex_story_20.type_master = complex_type_master_40
    complex_story_20 = importer.save_or_locate(complex_story_20)

    complex_story_21 = Story()
    complex_story_21.camera_zoom_level = 9
    complex_story_21.comic = complex_comic_5
    complex_story_21.journey = complex_journey_17
    complex_story_21.magazine = complex_magazine_25
    complex_story_21.subtitle = 'おうちに着くまで気ーをつけよう'
    complex_story_21.title = '第17旅 九州後編'
    complex_story_21.type_master = complex_type_master_40
    complex_story_21 = importer.save_or_locate(complex_story_21)

    complex_story_22 = Story()
    complex_story_22.camera_zoom_level = 11
    complex_story_22.comic = complex_comic_5
    complex_story_22.journey = complex_journey_18
    complex_story_22.magazine = complex_magazine_27
    complex_story_22.subtitle = '時にはあの番組のように'
    complex_story_22.title = '第18旅 都内Ⅲ'
    complex_story_22.type_master = complex_type_master_40
    complex_story_22 = importer.save_or_locate(complex_story_22)

    complex_story_23 = Story()
    complex_story_23.camera_zoom_level = 11
    complex_story_23.comic = complex_comic_6
    complex_story_23.journey = complex_journey_19
    complex_story_23.magazine = complex_magazine_28
    complex_story_23.subtitle = 'ツーリング旅始まる…？'
    complex_story_23.title = '第19旅 前編'
    complex_story_23.type_master = complex_type_master_40
    complex_story_23 = importer.save_or_locate(complex_story_23)

    complex_story_24 = Story()
    complex_story_24.camera_zoom_level = 8
    complex_story_24.comic = complex_comic_6
    complex_story_24.journey = complex_journey_19
    complex_story_24.magazine = complex_magazine_29
    complex_story_24.subtitle = '思い出して群馬'
    complex_story_24.title = '第19旅 群馬後編'
    complex_story_24.type_master = complex_type_master_40
    complex_story_24 = importer.save_or_locate(complex_story_24)

    complex_story_25 = Story()
    complex_story_25.camera_zoom_level = 12
    complex_story_25.comic = complex_comic_6
    complex_story_25.journey = complex_journey_20
    complex_story_25.magazine = complex_magazine_31
    complex_story_25.subtitle = 'そこに立つためには'
    complex_story_25.title = '第20旅 高知前編'
    complex_story_25.type_master = complex_type_master_40
    complex_story_25 = importer.save_or_locate(complex_story_25)

    complex_story_26 = Story()
    complex_story_26.camera_zoom_level = 10
    complex_story_26.comic = complex_comic_6
    complex_story_26.journey = complex_journey_20
    complex_story_26.magazine = complex_magazine_34
    complex_story_26.subtitle = 'そして次の場所へ'
    complex_story_26.title = '第20旅 高知後編'
    complex_story_26.type_master = complex_type_master_40
    complex_story_26 = importer.save_or_locate(complex_story_26)

    complex_story_27 = Story()
    complex_story_27.camera_zoom_level = 10
    complex_story_27.comic = complex_comic_7
    complex_story_27.journey = complex_journey_21
    complex_story_27.magazine = complex_magazine_36
    complex_story_27.subtitle = 'たどり着いたら北'
    complex_story_27.title = '第21旅 北海道・道南前編'
    complex_story_27.type_master = complex_type_master_40
    complex_story_27 = importer.save_or_locate(complex_story_27)

    complex_story_28 = Story()
    complex_story_28.camera_zoom_level = 10
    complex_story_28.comic = complex_comic_7
    complex_story_28.journey = complex_journey_21
    complex_story_28.magazine = complex_magazine_37
    complex_story_28.subtitle = 'またくるぞ北'
    complex_story_28.title = '第21旅 北海道・道南後編'
    complex_story_28.type_master = complex_type_master_40
    complex_story_28 = importer.save_or_locate(complex_story_28)

    complex_story_29 = Story()
    complex_story_29.camera_zoom_level = 10
    complex_story_29.comic = complex_comic_7
    complex_story_29.journey = complex_journey_22
    complex_story_29.magazine = complex_magazine_38
    complex_story_29.subtitle = '空からまたきた！'
    complex_story_29.title = '第22旅 北海道・道東前編'
    complex_story_29.type_master = complex_type_master_40
    complex_story_29 = importer.save_or_locate(complex_story_29)

    complex_story_30 = Story()
    complex_story_30.camera_zoom_level = 8
    complex_story_30.comic = complex_comic_7
    complex_story_30.journey = complex_journey_22
    complex_story_30.magazine = complex_magazine_40
    complex_story_30.subtitle = '無くたって良いどう'
    complex_story_30.title = '第22旅 北海道・道東後編'
    complex_story_30.type_master = complex_type_master_40
    complex_story_30 = importer.save_or_locate(complex_story_30)

    complex_story_31 = Story()
    complex_story_31.camera_zoom_level = 10
    complex_story_31.comic = complex_comic_8
    complex_story_31.journey = complex_journey_23
    complex_story_31.magazine = complex_magazine_41
    complex_story_31.subtitle = '激動せよ！2022年！'
    complex_story_31.title = '第23旅 千葉'
    complex_story_31.type_master = complex_type_master_40
    complex_story_31 = importer.save_or_locate(complex_story_31)

    complex_story_32 = Story()
    complex_story_32.camera_zoom_level = 12
    complex_story_32.comic = complex_comic_8
    complex_story_32.journey = complex_journey_24
    complex_story_32.magazine = complex_magazine_43
    complex_story_32.subtitle = '甲斐国での誓い'
    complex_story_32.title = '第24旅 山梨'
    complex_story_32.type_master = complex_type_master_40
    complex_story_32 = importer.save_or_locate(complex_story_32)

    complex_story_33 = Story()
    complex_story_33.camera_zoom_level = 12
    complex_story_33.comic = complex_comic_8
    complex_story_33.journey = complex_journey_25
    complex_story_33.magazine = complex_magazine_45
    complex_story_33.subtitle = '旅は自分に素直に'
    complex_story_33.title = '第25旅 鹿児島'
    complex_story_33.type_master = complex_type_master_40
    complex_story_33 = importer.save_or_locate(complex_story_33)

    complex_story_34 = Story()
    complex_story_34.camera_zoom_level = 11
    complex_story_34.comic = complex_comic_8
    complex_story_34.journey = complex_journey_26
    complex_story_34.magazine = complex_magazine_46
    complex_story_34.subtitle = 'そこにも路はある！'
    complex_story_34.title = '第26旅 徳島前編'
    complex_story_34.type_master = complex_type_master_40
    complex_story_34 = importer.save_or_locate(complex_story_34)

    complex_story_35 = Story()
    complex_story_35.camera_zoom_level = 11
    complex_story_35.comic = complex_comic_9
    complex_story_35.journey = complex_journey_26
    complex_story_35.magazine = complex_magazine_48
    complex_story_35.subtitle = 'ソノ場所ヘ至ル'
    complex_story_35.title = '第26旅 徳島後編'
    complex_story_35.type_master = complex_type_master_40
    complex_story_35 = importer.save_or_locate(complex_story_35)

    complex_story_36 = Story()
    complex_story_36.camera_zoom_level = 12
    complex_story_36.comic = complex_comic_9
    complex_story_36.journey = complex_journey_27
    complex_story_36.magazine = complex_magazine_49
    complex_story_36.subtitle = 'さあ歩こうまだ見ぬ地を'
    complex_story_36.title = '第27旅 愛媛'
    complex_story_36.type_master = complex_type_master_40
    complex_story_36 = importer.save_or_locate(complex_story_36)

    complex_story_37 = Story()
    complex_story_37.camera_zoom_level = 13
    complex_story_37.comic = complex_comic_9
    complex_story_37.journey = complex_journey_28
    complex_story_37.magazine = complex_magazine_50
    complex_story_37.subtitle = 'すわ！後輩三日会わざるば'
    complex_story_37.title = '第28旅 長野前編'
    complex_story_37.type_master = complex_type_master_40
    complex_story_37 = importer.save_or_locate(complex_story_37)

    complex_story_38 = Story()
    complex_story_38.camera_zoom_level = 11
    complex_story_38.comic = complex_comic_9
    complex_story_38.journey = complex_journey_28
    complex_story_38.magazine = complex_magazine_51
    complex_story_38.subtitle = '物語を紡ぐのはきっと'
    complex_story_38.title = '第28旅 長野後編'
    complex_story_38.type_master = complex_type_master_40
    complex_story_38 = importer.save_or_locate(complex_story_38)

    complex_story_39 = Story()
    complex_story_39.camera_center_place = None
    complex_story_39.camera_zoom_level = None
    complex_story_39.comic = complex_comic_4
    complex_story_39.journey = None
    complex_story_39.magazine = complex_magazine_17
    complex_story_39.subtitle = ''
    complex_story_39.title = '番外旅 うどんと後輩と'
    complex_story_39.type_master = complex_type_master_41
    complex_story_39 = importer.save_or_locate(complex_story_39)

    complex_story_40 = Story()
    complex_story_40.camera_center_place = None
    complex_story_40.camera_zoom_level = None
    complex_story_40.comic = complex_comic_4
    complex_story_40.journey = None
    complex_story_40.magazine = complex_magazine_18
    complex_story_40.subtitle = ''
    complex_story_40.title = '新しい挑戦！'
    complex_story_40.type_master = complex_type_master_44
    complex_story_40 = importer.save_or_locate(complex_story_40)

    complex_story_41 = Story()
    complex_story_41.camera_center_place = None
    complex_story_41.camera_zoom_level = None
    complex_story_41.comic = complex_comic_4
    complex_story_41.journey = None
    complex_story_41.magazine = complex_magazine_19
    complex_story_41.subtitle = ''
    complex_story_41.title = '番外旅 載った！そして…！'
    complex_story_41.type_master = complex_type_master_41
    complex_story_41 = importer.save_or_locate(complex_story_41)

    complex_story_42 = Story()
    complex_story_42.camera_center_place = None
    complex_story_42.camera_zoom_level = None
    complex_story_42.comic = complex_comic_5
    complex_story_42.journey = None
    complex_story_42.magazine = complex_magazine_26
    complex_story_42.subtitle = ''
    complex_story_42.title = '番外旅 さようなら2020年！'
    complex_story_42.type_master = complex_type_master_41
    complex_story_42 = importer.save_or_locate(complex_story_42)

    complex_story_43 = Story()
    complex_story_43.camera_center_place = None
    complex_story_43.camera_zoom_level = None
    complex_story_43.comic = complex_comic_6
    complex_story_43.journey = None
    complex_story_43.magazine = complex_magazine_30
    complex_story_43.subtitle = ''
    complex_story_43.title = '番外旅 思い出して旅'
    complex_story_43.type_master = complex_type_master_41
    complex_story_43 = importer.save_or_locate(complex_story_43)

    complex_story_44 = Story()
    complex_story_44.camera_center_place = None
    complex_story_44.camera_zoom_level = None
    complex_story_44.comic = complex_comic_6
    complex_story_44.journey = None
    complex_story_44.magazine = complex_magazine_32
    complex_story_44.subtitle = ''
    complex_story_44.title = '番外旅 この先のため…！'
    complex_story_44.type_master = complex_type_master_41
    complex_story_44 = importer.save_or_locate(complex_story_44)

    complex_story_45 = Story()
    complex_story_45.camera_center_place = None
    complex_story_45.camera_zoom_level = None
    complex_story_45.comic = complex_comic_7
    complex_story_45.journey = None
    complex_story_45.magazine = complex_magazine_33
    complex_story_45.subtitle = ''
    complex_story_45.title = '番外旅 でっかい空とごはん'
    complex_story_45.type_master = complex_type_master_41
    complex_story_45 = importer.save_or_locate(complex_story_45)

    complex_story_46 = Story()
    complex_story_46.camera_center_place = None
    complex_story_46.camera_zoom_level = None
    complex_story_46.comic = complex_comic_6
    complex_story_46.journey = None
    complex_story_46.magazine = complex_magazine_35
    complex_story_46.subtitle = ''
    complex_story_46.title = '番外旅 そして次の旅が…！'
    complex_story_46.type_master = complex_type_master_41
    complex_story_46 = importer.save_or_locate(complex_story_46)

    complex_story_47 = Story()
    complex_story_47.camera_center_place = None
    complex_story_47.camera_zoom_level = None
    complex_story_47.comic = None
    complex_story_47.journey = None
    complex_story_47.magazine = complex_magazine_39
    complex_story_47.subtitle = ''
    complex_story_47.title = '番外旅 描いた！出た！'
    complex_story_47.type_master = complex_type_master_41
    complex_story_47 = importer.save_or_locate(complex_story_47)

    complex_story_48 = Story()
    complex_story_48.camera_center_place = None
    complex_story_48.camera_zoom_level = None
    complex_story_48.comic = complex_comic_8
    complex_story_48.journey = None
    complex_story_48.magazine = complex_magazine_1
    complex_story_48.subtitle = ''
    complex_story_48.title = 'あのしゅん間'
    complex_story_48.type_master = complex_type_master_44
    complex_story_48 = importer.save_or_locate(complex_story_48)

    complex_story_49 = Story()
    complex_story_49.camera_center_place = None
    complex_story_49.camera_zoom_level = None
    complex_story_49.comic = complex_comic_8
    complex_story_49.journey = None
    complex_story_49.magazine = complex_magazine_42
    complex_story_49.subtitle = ''
    complex_story_49.title = '番外旅 新しい始まり'
    complex_story_49.type_master = complex_type_master_41
    complex_story_49 = importer.save_or_locate(complex_story_49)

    complex_story_50 = Story()
    complex_story_50.camera_center_place = None
    complex_story_50.camera_zoom_level = None
    complex_story_50.comic = complex_comic_8
    complex_story_50.journey = None
    complex_story_50.magazine = complex_magazine_44
    complex_story_50.subtitle = ''
    complex_story_50.title = '番外旅 それはきっと近い未来'
    complex_story_50.type_master = complex_type_master_41
    complex_story_50 = importer.save_or_locate(complex_story_50)

    complex_story_51 = Story()
    complex_story_51.camera_center_place = None
    complex_story_51.camera_zoom_level = None
    complex_story_51.comic = complex_comic_9
    complex_story_51.journey = None
    complex_story_51.magazine = complex_magazine_47
    complex_story_51.subtitle = None
    complex_story_51.title = '番外旅 日帰ろう二人旅'
    complex_story_51.type_master = complex_type_master_41
    complex_story_51 = importer.save_or_locate(complex_story_51)

    complex_story_52 = Story()
    complex_story_52.camera_center_place = None
    complex_story_52.camera_zoom_level = None
    complex_story_52.comic = None
    complex_story_52.journey = None
    complex_story_52.magazine = None
    complex_story_52.subtitle = ''
    complex_story_52.title = '18旅で有ったかもしれないNGシーン風'
    complex_story_52.type_master = complex_type_master_44
    complex_story_52 = importer.save_or_locate(complex_story_52)

    complex_story_53 = Story()
    complex_story_53.camera_center_place = None
    complex_story_53.camera_zoom_level = None
    complex_story_53.comic = complex_comic_6
    complex_story_53.journey = None
    complex_story_53.magazine = None
    complex_story_53.subtitle = ''
    complex_story_53.title = '次にくるマンガ大賞2021ノミネートされました！'
    complex_story_53.type_master = complex_type_master_44
    complex_story_53 = importer.save_or_locate(complex_story_53)

    complex_story_54 = Story()
    complex_story_54.camera_center_place = None
    complex_story_54.camera_zoom_level = None
    complex_story_54.comic = complex_comic_6
    complex_story_54.journey = None
    complex_story_54.magazine = None
    complex_story_54.subtitle = ''
    complex_story_54.title = 'コミックス6巻発売告知'
    complex_story_54.type_master = complex_type_master_44
    complex_story_54 = importer.save_or_locate(complex_story_54)

    complex_story_55 = Story()
    complex_story_55.camera_center_place = None
    complex_story_55.camera_zoom_level = None
    complex_story_55.comic = complex_comic_9
    complex_story_55.journey = complex_journey_29
    complex_story_55.magazine = complex_magazine_52
    complex_story_55.subtitle = '無事帰る、それこそが良い旅'
    complex_story_55.title = '第29旅 山口'
    complex_story_55.type_master = complex_type_master_40
    complex_story_55 = importer.save_or_locate(complex_story_55)

    complex_story_56 = Story()
    complex_story_56.camera_center_place = None
    complex_story_56.camera_zoom_level = None
    complex_story_56.comic = None
    complex_story_56.journey = complex_journey_30
    complex_story_56.magazine = complex_magazine_53
    complex_story_56.subtitle = '3人、だから楽しい'
    complex_story_56.title = '第30旅 福岡'
    complex_story_56.type_master = complex_type_master_40
    complex_story_56 = importer.save_or_locate(complex_story_56)

    complex_story_57 = Story()
    complex_story_57.camera_center_place = None
    complex_story_57.camera_zoom_level = None
    complex_story_57.comic = None
    complex_story_57.journey = complex_journey_31
    complex_story_57.magazine = complex_magazine_54
    complex_story_57.subtitle = 'こうして2人は進んで行く'
    complex_story_57.title = '第31旅 秋田'
    complex_story_57.type_master = complex_type_master_40
    complex_story_57 = importer.save_or_locate(complex_story_57)

    complex_story_58 = Story()
    complex_story_58.camera_center_place = None
    complex_story_58.camera_zoom_level = None
    complex_story_58.comic = None
    complex_story_58.journey = None
    complex_story_58.magazine = complex_magazine_55
    complex_story_58.subtitle = '出版社の壁には耳有り'
    complex_story_58.title = '番外旅'
    complex_story_58.type_master = complex_type_master_41
    complex_story_58 = importer.save_or_locate(complex_story_58)

    # Processing model: complex.models.Route

    from complex.models import Route

    complex_route_1 = Route()
    complex_route_1.memo = None
    complex_route_1.name = '第1旅 会津若松 (default)'
    complex_route_1.type_master = complex_type_master_31
    complex_route_1 = importer.save_or_locate(complex_route_1)

    complex_route_1.story.add(complex_story_1)

    complex_route_2 = Route()
    complex_route_2.memo = None
    complex_route_2.name = '第2旅 松島 (default)'
    complex_route_2.type_master = complex_type_master_31
    complex_route_2 = importer.save_or_locate(complex_route_2)

    complex_route_2.story.add(complex_story_2)

    complex_route_3 = Route()
    complex_route_3.memo = None
    complex_route_3.name = '第3旅 黒部 (default)'
    complex_route_3.type_master = complex_type_master_31
    complex_route_3 = importer.save_or_locate(complex_route_3)

    complex_route_3.story.add(complex_story_3)

    complex_route_4 = Route()
    complex_route_4.memo = None
    complex_route_4.name = '第4旅 高松 (default)'
    complex_route_4.type_master = complex_type_master_31
    complex_route_4 = importer.save_or_locate(complex_route_4)

    complex_route_4.story.add(complex_story_4)

    complex_route_5 = Route()
    complex_route_5.memo = None
    complex_route_5.name = '第5旅 京都 (default)'
    complex_route_5.type_master = complex_type_master_31
    complex_route_5 = importer.save_or_locate(complex_route_5)

    complex_route_5.story.add(complex_story_5)

    complex_route_6 = Route()
    complex_route_6.memo = None
    complex_route_6.name = '第6旅 栃木 (default)'
    complex_route_6.type_master = complex_type_master_31
    complex_route_6 = importer.save_or_locate(complex_route_6)

    complex_route_6.story.add(complex_story_6)

    complex_route_7 = Route()
    complex_route_7.memo = None
    complex_route_7.name = '第7旅 粟島 (default)'
    complex_route_7.type_master = complex_type_master_31
    complex_route_7 = importer.save_or_locate(complex_route_7)

    complex_route_7.story.add(complex_story_7)

    complex_route_8 = Route()
    complex_route_8.memo = None
    complex_route_8.name = '第8旅 伊勢 (default)'
    complex_route_8.type_master = complex_type_master_31
    complex_route_8 = importer.save_or_locate(complex_route_8)

    complex_route_8.story.add(complex_story_8)

    complex_route_9 = Route()
    complex_route_9.memo = None
    complex_route_9.name = '第9旅 広島前編 (default)'
    complex_route_9.type_master = complex_type_master_31
    complex_route_9 = importer.save_or_locate(complex_route_9)

    complex_route_9.story.add(complex_story_9)

    complex_route_10 = Route()
    complex_route_10.memo = None
    complex_route_10.name = '第9旅 広島後編 (default)'
    complex_route_10.type_master = complex_type_master_31
    complex_route_10 = importer.save_or_locate(complex_route_10)

    complex_route_10.story.add(complex_story_10)

    complex_route_11 = Route()
    complex_route_11.memo = None
    complex_route_11.name = '第10旅 青森 (default)'
    complex_route_11.type_master = complex_type_master_31
    complex_route_11 = importer.save_or_locate(complex_route_11)

    complex_route_11.story.add(complex_story_11)

    complex_route_12 = Route()
    complex_route_12.memo = None
    complex_route_12.name = '第11旅 和歌山 (default)'
    complex_route_12.type_master = complex_type_master_31
    complex_route_12 = importer.save_or_locate(complex_route_12)

    complex_route_12.story.add(complex_story_12)

    complex_route_13 = Route()
    complex_route_13.memo = None
    complex_route_13.name = '第12旅 花巻 (default)'
    complex_route_13.type_master = complex_type_master_31
    complex_route_13 = importer.save_or_locate(complex_route_13)

    complex_route_13.story.add(complex_story_13)

    complex_route_14 = Route()
    complex_route_14.memo = None
    complex_route_14.name = '第13旅 島根前編 (default)'
    complex_route_14.type_master = complex_type_master_31
    complex_route_14 = importer.save_or_locate(complex_route_14)

    complex_route_14.story.add(complex_story_14)

    complex_route_15 = Route()
    complex_route_15.memo = None
    complex_route_15.name = '第13旅 島根後編 (default)'
    complex_route_15.type_master = complex_type_master_31
    complex_route_15 = importer.save_or_locate(complex_route_15)

    complex_route_15.story.add(complex_story_15)

    complex_route_16 = Route()
    complex_route_16.memo = None
    complex_route_16.name = '第14旅 奥多摩 (default)'
    complex_route_16.type_master = complex_type_master_31
    complex_route_16 = importer.save_or_locate(complex_route_16)

    complex_route_16.story.add(complex_story_16)

    complex_route_17 = Route()
    complex_route_17.memo = None
    complex_route_17.name = '第15旅 都内 (default)'
    complex_route_17.type_master = complex_type_master_31
    complex_route_17 = importer.save_or_locate(complex_route_17)

    complex_route_17.story.add(complex_story_17)

    complex_route_18 = Route()
    complex_route_18.memo = None
    complex_route_18.name = '第16旅 茨城前編 (default)'
    complex_route_18.type_master = complex_type_master_31
    complex_route_18 = importer.save_or_locate(complex_route_18)

    complex_route_18.story.add(complex_story_18)

    complex_route_19 = Route()
    complex_route_19.memo = None
    complex_route_19.name = '第16旅 茨城後編 (default)'
    complex_route_19.type_master = complex_type_master_31
    complex_route_19 = importer.save_or_locate(complex_route_19)

    complex_route_19.story.add(complex_story_19)

    complex_route_20 = Route()
    complex_route_20.memo = None
    complex_route_20.name = '第17旅 九州前編 (default)'
    complex_route_20.type_master = complex_type_master_31
    complex_route_20 = importer.save_or_locate(complex_route_20)

    complex_route_20.story.add(complex_story_20)

    complex_route_21 = Route()
    complex_route_21.memo = None
    complex_route_21.name = '第17旅 九州後編 (default)'
    complex_route_21.type_master = complex_type_master_31
    complex_route_21 = importer.save_or_locate(complex_route_21)

    complex_route_21.story.add(complex_story_21)

    complex_route_22 = Route()
    complex_route_22.memo = None
    complex_route_22.name = '第18旅 都内Ⅲ (default)'
    complex_route_22.type_master = complex_type_master_31
    complex_route_22 = importer.save_or_locate(complex_route_22)

    complex_route_22.story.add(complex_story_22)

    complex_route_23 = Route()
    complex_route_23.memo = None
    complex_route_23.name = '第19旅 前編 (default)'
    complex_route_23.type_master = complex_type_master_31
    complex_route_23 = importer.save_or_locate(complex_route_23)

    complex_route_23.story.add(complex_story_23)

    complex_route_24 = Route()
    complex_route_24.memo = None
    complex_route_24.name = '第19旅 群馬後編 (default)'
    complex_route_24.type_master = complex_type_master_31
    complex_route_24 = importer.save_or_locate(complex_route_24)

    complex_route_24.story.add(complex_story_24)

    complex_route_25 = Route()
    complex_route_25.memo = None
    complex_route_25.name = '第20旅 高知前編 (default)'
    complex_route_25.type_master = complex_type_master_31
    complex_route_25 = importer.save_or_locate(complex_route_25)

    complex_route_25.story.add(complex_story_25)

    complex_route_26 = Route()
    complex_route_26.memo = None
    complex_route_26.name = '第20旅 高知後編 (default)'
    complex_route_26.type_master = complex_type_master_31
    complex_route_26 = importer.save_or_locate(complex_route_26)

    complex_route_26.story.add(complex_story_26)

    complex_route_27 = Route()
    complex_route_27.memo = None
    complex_route_27.name = '第21旅 北海道・道南前編 (default)'
    complex_route_27.type_master = complex_type_master_31
    complex_route_27 = importer.save_or_locate(complex_route_27)

    complex_route_27.story.add(complex_story_27)

    complex_route_28 = Route()
    complex_route_28.memo = None
    complex_route_28.name = '第21旅 北海道・道南後編 (default)'
    complex_route_28.type_master = complex_type_master_31
    complex_route_28 = importer.save_or_locate(complex_route_28)

    complex_route_28.story.add(complex_story_28)

    complex_route_29 = Route()
    complex_route_29.memo = None
    complex_route_29.name = '第22旅 北海道・道東前編 (default)'
    complex_route_29.type_master = complex_type_master_31
    complex_route_29 = importer.save_or_locate(complex_route_29)

    complex_route_29.story.add(complex_story_29)

    complex_route_30 = Route()
    complex_route_30.memo = None
    complex_route_30.name = '第22旅 北海道・道東後編 (default)'
    complex_route_30.type_master = complex_type_master_31
    complex_route_30 = importer.save_or_locate(complex_route_30)

    complex_route_30.story.add(complex_story_30)

    complex_route_31 = Route()
    complex_route_31.memo = None
    complex_route_31.name = '第23旅 千葉 (default)'
    complex_route_31.type_master = complex_type_master_31
    complex_route_31 = importer.save_or_locate(complex_route_31)

    complex_route_31.story.add(complex_story_31)

    complex_route_32 = Route()
    complex_route_32.memo = None
    complex_route_32.name = '第24旅 山梨 (default)'
    complex_route_32.type_master = complex_type_master_31
    complex_route_32 = importer.save_or_locate(complex_route_32)

    complex_route_32.story.add(complex_story_32)

    complex_route_33 = Route()
    complex_route_33.memo = None
    complex_route_33.name = '第25旅 鹿児島 (default)'
    complex_route_33.type_master = complex_type_master_31
    complex_route_33 = importer.save_or_locate(complex_route_33)

    complex_route_33.story.add(complex_story_33)

    complex_route_34 = Route()
    complex_route_34.memo = None
    complex_route_34.name = '第26旅 徳島前編 (default)'
    complex_route_34.type_master = complex_type_master_31
    complex_route_34 = importer.save_or_locate(complex_route_34)

    complex_route_34.story.add(complex_story_34)

    complex_route_35 = Route()
    complex_route_35.memo = None
    complex_route_35.name = '第26旅 徳島後編 (default)'
    complex_route_35.type_master = complex_type_master_31
    complex_route_35 = importer.save_or_locate(complex_route_35)

    complex_route_35.story.add(complex_story_35)

    complex_route_36 = Route()
    complex_route_36.memo = None
    complex_route_36.name = '第27旅 愛媛 (default)'
    complex_route_36.type_master = complex_type_master_31
    complex_route_36 = importer.save_or_locate(complex_route_36)

    complex_route_36.story.add(complex_story_36)

    complex_route_37 = Route()
    complex_route_37.memo = None
    complex_route_37.name = '第28旅 長野前編 (default)'
    complex_route_37.type_master = complex_type_master_31
    complex_route_37 = importer.save_or_locate(complex_route_37)

    complex_route_37.story.add(complex_story_37)

    complex_route_38 = Route()
    complex_route_38.memo = None
    complex_route_38.name = '第28旅 長野後編 (default)'
    complex_route_38.type_master = complex_type_master_31
    complex_route_38 = importer.save_or_locate(complex_route_38)

    complex_route_38.story.add(complex_story_38)

    complex_route_39 = Route()
    complex_route_39.memo = None
    complex_route_39.name = '番外旅 うどんと後輩と (default)'
    complex_route_39.type_master = complex_type_master_31
    complex_route_39 = importer.save_or_locate(complex_route_39)

    complex_route_39.story.add(complex_story_39)

    complex_route_40 = Route()
    complex_route_40.memo = None
    complex_route_40.name = '新しい挑戦！ (default)'
    complex_route_40.type_master = complex_type_master_31
    complex_route_40 = importer.save_or_locate(complex_route_40)

    complex_route_40.story.add(complex_story_40)

    complex_route_41 = Route()
    complex_route_41.memo = None
    complex_route_41.name = '番外旅 載った！そして…！ (default)'
    complex_route_41.type_master = complex_type_master_31
    complex_route_41 = importer.save_or_locate(complex_route_41)

    complex_route_41.story.add(complex_story_41)

    complex_route_42 = Route()
    complex_route_42.memo = None
    complex_route_42.name = '番外旅 さようなら2020年！ (default)'
    complex_route_42.type_master = complex_type_master_31
    complex_route_42 = importer.save_or_locate(complex_route_42)

    complex_route_42.story.add(complex_story_42)

    complex_route_43 = Route()
    complex_route_43.memo = None
    complex_route_43.name = '番外旅 思い出して旅 (default)'
    complex_route_43.type_master = complex_type_master_31
    complex_route_43 = importer.save_or_locate(complex_route_43)

    complex_route_43.story.add(complex_story_43)

    complex_route_44 = Route()
    complex_route_44.memo = None
    complex_route_44.name = '番外旅 この先のため…！ (default)'
    complex_route_44.type_master = complex_type_master_31
    complex_route_44 = importer.save_or_locate(complex_route_44)

    complex_route_44.story.add(complex_story_44)

    complex_route_45 = Route()
    complex_route_45.memo = None
    complex_route_45.name = '番外旅 でっかい空とごはん (default)'
    complex_route_45.type_master = complex_type_master_31
    complex_route_45 = importer.save_or_locate(complex_route_45)

    complex_route_45.story.add(complex_story_45)

    complex_route_46 = Route()
    complex_route_46.memo = None
    complex_route_46.name = '番外旅 そして次の旅が…！ (default)'
    complex_route_46.type_master = complex_type_master_31
    complex_route_46 = importer.save_or_locate(complex_route_46)

    complex_route_46.story.add(complex_story_46)

    complex_route_47 = Route()
    complex_route_47.memo = None
    complex_route_47.name = '番外旅 描いた！出た！ (default)'
    complex_route_47.type_master = complex_type_master_31
    complex_route_47 = importer.save_or_locate(complex_route_47)

    complex_route_47.story.add(complex_story_47)

    complex_route_48 = Route()
    complex_route_48.memo = None
    complex_route_48.name = 'あのしゅん間 (default)'
    complex_route_48.type_master = complex_type_master_31
    complex_route_48 = importer.save_or_locate(complex_route_48)

    complex_route_48.story.add(complex_story_48)

    complex_route_49 = Route()
    complex_route_49.memo = None
    complex_route_49.name = '番外旅 新しい始まり (default)'
    complex_route_49.type_master = complex_type_master_31
    complex_route_49 = importer.save_or_locate(complex_route_49)

    complex_route_49.story.add(complex_story_49)

    complex_route_50 = Route()
    complex_route_50.memo = None
    complex_route_50.name = '番外旅 それはきっと近い未来 (default)'
    complex_route_50.type_master = complex_type_master_31
    complex_route_50 = importer.save_or_locate(complex_route_50)

    complex_route_50.story.add(complex_story_50)

    complex_route_51 = Route()
    complex_route_51.memo = None
    complex_route_51.name = '番外旅 日帰ろう二人旅 (default)'
    complex_route_51.type_master = complex_type_master_31
    complex_route_51 = importer.save_or_locate(complex_route_51)

    complex_route_51.story.add(complex_story_51)

    complex_route_52 = Route()
    complex_route_52.memo = None
    complex_route_52.name = '18旅で有ったかもしれないNGシーン風 (default)'
    complex_route_52.type_master = complex_type_master_31
    complex_route_52 = importer.save_or_locate(complex_route_52)

    complex_route_52.story.add(complex_story_52)

    complex_route_53 = Route()
    complex_route_53.memo = None
    complex_route_53.name = '次にくるマンガ大賞2021ノミネートされました！ (default)'
    complex_route_53.type_master = complex_type_master_31
    complex_route_53 = importer.save_or_locate(complex_route_53)

    complex_route_53.story.add(complex_story_53)

    complex_route_54 = Route()
    complex_route_54.memo = None
    complex_route_54.name = 'コミックス6巻発売告知 (default)'
    complex_route_54.type_master = complex_type_master_31
    complex_route_54 = importer.save_or_locate(complex_route_54)

    complex_route_54.story.add(complex_story_54)

    # Processing model: complex.models.Venue

    from complex.models import Venue

    complex_venue_1 = Venue()
    complex_venue_1.name = 'むつ市'
    complex_venue_1.type_master = complex_type_master_56
    complex_venue_1 = importer.save_or_locate(complex_venue_1)

    complex_venue_1.story.add(complex_story_11)

    complex_venue_2 = Venue()
    complex_venue_2.name = '三鷹市'
    complex_venue_2.type_master = complex_type_master_56
    complex_venue_2 = importer.save_or_locate(complex_venue_2)

    complex_venue_2.story.add(complex_story_22)

    complex_venue_3 = Venue()
    complex_venue_3.name = '中央区'
    complex_venue_3.type_master = complex_type_master_56
    complex_venue_3 = importer.save_or_locate(complex_venue_3)

    complex_venue_3.story.add(complex_story_17)

    complex_venue_4 = Venue()
    complex_venue_4.name = '中津市'
    complex_venue_4.type_master = complex_type_master_56
    complex_venue_4 = importer.save_or_locate(complex_venue_4)

    complex_venue_4.story.add(complex_story_20)
    complex_venue_4.story.add(complex_story_21)

    complex_venue_5 = Venue()
    complex_venue_5.name = '亀田郡七飯町'
    complex_venue_5.type_master = complex_type_master_56
    complex_venue_5 = importer.save_or_locate(complex_venue_5)

    complex_venue_5.story.add(complex_story_27)
    complex_venue_5.story.add(complex_story_28)

    complex_venue_6 = Venue()
    complex_venue_6.name = '京都市下京区'
    complex_venue_6.type_master = complex_type_master_56
    complex_venue_6 = importer.save_or_locate(complex_venue_6)

    complex_venue_6.story.add(complex_story_5)

    complex_venue_7 = Venue()
    complex_venue_7.name = '京都市伏見区'
    complex_venue_7.type_master = complex_type_master_56
    complex_venue_7 = importer.save_or_locate(complex_venue_7)

    complex_venue_7.story.add(complex_story_5)

    complex_venue_8 = Venue()
    complex_venue_8.name = '今治市'
    complex_venue_8.type_master = complex_type_master_56
    complex_venue_8 = importer.save_or_locate(complex_venue_8)

    complex_venue_8.story.add(complex_story_36)

    complex_venue_9 = Venue()
    complex_venue_9.name = '仙台市青葉区'
    complex_venue_9.type_master = complex_type_master_56
    complex_venue_9 = importer.save_or_locate(complex_venue_9)

    complex_venue_9.story.add(complex_story_2)

    complex_venue_10 = Venue()
    complex_venue_10.name = '伊勢市'
    complex_venue_10.type_master = complex_type_master_56
    complex_venue_10 = importer.save_or_locate(complex_venue_10)

    complex_venue_10.story.add(complex_story_8)

    complex_venue_11 = Venue()
    complex_venue_11.name = '会津若松市'
    complex_venue_11.type_master = complex_type_master_56
    complex_venue_11 = importer.save_or_locate(complex_venue_11)

    complex_venue_11.story.add(complex_story_1)

    complex_venue_12 = Venue()
    complex_venue_12.name = '出雲市'
    complex_venue_12.type_master = complex_type_master_56
    complex_venue_12 = importer.save_or_locate(complex_venue_12)

    complex_venue_12.story.add(complex_story_14)

    complex_venue_13 = Venue()
    complex_venue_13.name = '函館市'
    complex_venue_13.type_master = complex_type_master_56
    complex_venue_13 = importer.save_or_locate(complex_venue_13)

    complex_venue_13.story.add(complex_story_27)
    complex_venue_13.story.add(complex_story_28)

    complex_venue_14 = Venue()
    complex_venue_14.name = '利根郡みなかみ町'
    complex_venue_14.type_master = complex_type_master_56
    complex_venue_14 = importer.save_or_locate(complex_venue_14)

    complex_venue_14.story.add(complex_story_24)

    complex_venue_15 = Venue()
    complex_venue_15.name = '北上市'
    complex_venue_15.type_master = complex_type_master_56
    complex_venue_15 = importer.save_or_locate(complex_venue_15)

    complex_venue_15.story.add(complex_story_13)

    complex_venue_16 = Venue()
    complex_venue_16.name = '北九州市小倉北区'
    complex_venue_16.type_master = complex_type_master_56
    complex_venue_16 = importer.save_or_locate(complex_venue_16)

    complex_venue_16.story.add(complex_story_20)

    complex_venue_17 = Venue()
    complex_venue_17.name = '北区'
    complex_venue_17.type_master = complex_type_master_56
    complex_venue_17 = importer.save_or_locate(complex_venue_17)

    complex_venue_17.story.add(complex_story_24)

    complex_venue_18 = Venue()
    complex_venue_18.name = '北斗市'
    complex_venue_18.type_master = complex_type_master_56
    complex_venue_18 = importer.save_or_locate(complex_venue_18)

    complex_venue_18.story.add(complex_story_27)

    complex_venue_19 = Venue()
    complex_venue_19.name = '北群馬郡吉岡町'
    complex_venue_19.type_master = complex_type_master_56
    complex_venue_19 = importer.save_or_locate(complex_venue_19)

    complex_venue_19.story.add(complex_story_24)

    complex_venue_20 = Venue()
    complex_venue_20.name = '北見市'
    complex_venue_20.type_master = complex_type_master_56
    complex_venue_20 = importer.save_or_locate(complex_venue_20)

    complex_venue_20.story.add(complex_story_29)
    complex_venue_20.story.add(complex_story_30)

    complex_venue_21 = Venue()
    complex_venue_21.name = '北都留郡丹波山村'
    complex_venue_21.type_master = complex_type_master_56
    complex_venue_21 = importer.save_or_locate(complex_venue_21)

    complex_venue_21.story.add(complex_story_51)

    complex_venue_22 = Venue()
    complex_venue_22.name = '十和田市'
    complex_venue_22.type_master = complex_type_master_56
    complex_venue_22 = importer.save_or_locate(complex_venue_22)

    complex_venue_22.story.add(complex_story_11)

    complex_venue_23 = Venue()
    complex_venue_23.name = '千代田区'
    complex_venue_23.type_master = complex_type_master_56
    complex_venue_23 = importer.save_or_locate(complex_venue_23)

    complex_venue_23.story.add(complex_story_3)
    complex_venue_23.story.add(complex_story_4)
    complex_venue_23.story.add(complex_story_16)
    complex_venue_23.story.add(complex_story_17)
    complex_venue_23.story.add(complex_story_18)
    complex_venue_23.story.add(complex_story_20)
    complex_venue_23.story.add(complex_story_22)
    complex_venue_23.story.add(complex_story_23)
    complex_venue_23.story.add(complex_story_24)
    complex_venue_23.story.add(complex_story_26)
    complex_venue_23.story.add(complex_story_30)
    complex_venue_23.story.add(complex_story_52)

    complex_venue_24 = Venue()
    complex_venue_24.name = '南アルプス市'
    complex_venue_24.type_master = complex_type_master_56
    complex_venue_24 = importer.save_or_locate(complex_venue_24)

    complex_venue_24.story.add(complex_story_32)

    complex_venue_25 = Venue()
    complex_venue_25.name = '南国市'
    complex_venue_25.type_master = complex_type_master_56
    complex_venue_25 = importer.save_or_locate(complex_venue_25)

    complex_venue_25.story.add(complex_story_25)

    complex_venue_26 = Venue()
    complex_venue_26.name = '南房総市'
    complex_venue_26.type_master = complex_type_master_56
    complex_venue_26 = importer.save_or_locate(complex_venue_26)

    complex_venue_26.story.add(complex_story_31)

    complex_venue_27 = Venue()
    complex_venue_27.name = '南魚沼市'
    complex_venue_27.type_master = complex_type_master_56
    complex_venue_27 = importer.save_or_locate(complex_venue_27)

    complex_venue_27.story.add(complex_story_45)

    complex_venue_28 = Venue()
    complex_venue_28.name = '名西郡神山町'
    complex_venue_28.type_master = complex_type_master_56
    complex_venue_28 = importer.save_or_locate(complex_venue_28)

    complex_venue_28.story.add(complex_story_35)

    complex_venue_29 = Venue()
    complex_venue_29.name = '呉市'
    complex_venue_29.type_master = complex_type_master_56
    complex_venue_29 = importer.save_or_locate(complex_venue_29)

    complex_venue_29.story.add(complex_story_10)

    complex_venue_30 = Venue()
    complex_venue_30.name = '品川区'
    complex_venue_30.type_master = complex_type_master_56
    complex_venue_30 = importer.save_or_locate(complex_venue_30)

    complex_venue_30.story.add(complex_story_23)

    complex_venue_31 = Venue()
    complex_venue_31.name = '国東市'
    complex_venue_31.type_master = complex_type_master_56
    complex_venue_31 = importer.save_or_locate(complex_venue_31)

    complex_venue_31.story.add(complex_story_21)

    complex_venue_32 = Venue()
    complex_venue_32.name = '大田区'
    complex_venue_32.type_master = complex_type_master_56
    complex_venue_32 = importer.save_or_locate(complex_venue_32)

    complex_venue_32.story.add(complex_story_23)
    complex_venue_32.story.add(complex_story_29)

    complex_venue_33 = Venue()
    complex_venue_33.name = '太田市'
    complex_venue_33.type_master = complex_type_master_56
    complex_venue_33 = importer.save_or_locate(complex_venue_33)

    complex_venue_33.story.add(complex_story_24)

    complex_venue_34 = Venue()
    complex_venue_34.name = '宇佐市'
    complex_venue_34.type_master = complex_type_master_56
    complex_venue_34 = importer.save_or_locate(complex_venue_34)

    complex_venue_34.story.add(complex_story_20)
    complex_venue_34.story.add(complex_story_21)

    complex_venue_35 = Venue()
    complex_venue_35.name = '宇都宮市'
    complex_venue_35.type_master = complex_type_master_56
    complex_venue_35 = importer.save_or_locate(complex_venue_35)

    complex_venue_35.story.add(complex_story_6)

    complex_venue_36 = Venue()
    complex_venue_36.name = '安房郡鋸南町'
    complex_venue_36.type_master = complex_type_master_56
    complex_venue_36 = importer.save_or_locate(complex_venue_36)

    complex_venue_36.story.add(complex_story_31)

    complex_venue_37 = Venue()
    complex_venue_37.name = '安芸郡奈半利町'
    complex_venue_37.type_master = complex_type_master_56
    complex_venue_37 = importer.save_or_locate(complex_venue_37)

    complex_venue_37.story.add(complex_story_26)

    complex_venue_38 = Venue()
    complex_venue_38.name = '安芸郡田野町'
    complex_venue_38.type_master = complex_type_master_56
    complex_venue_38 = importer.save_or_locate(complex_venue_38)

    complex_venue_38.story.add(complex_story_26)

    complex_venue_39 = Venue()
    complex_venue_39.name = '宮城郡松島町'
    complex_venue_39.type_master = complex_type_master_56
    complex_venue_39 = importer.save_or_locate(complex_venue_39)

    complex_venue_39.story.add(complex_story_2)

    complex_venue_40 = Venue()
    complex_venue_40.name = '宮津市'
    complex_venue_40.type_master = complex_type_master_56
    complex_venue_40 = importer.save_or_locate(complex_venue_40)

    complex_venue_40.story.add(complex_story_5)

    complex_venue_41 = Venue()
    complex_venue_41.name = '富津市'
    complex_venue_41.type_master = complex_type_master_56
    complex_venue_41 = importer.save_or_locate(complex_venue_41)

    complex_venue_41.story.add(complex_story_31)

    complex_venue_42 = Venue()
    complex_venue_42.name = '尾道市'
    complex_venue_42.type_master = complex_type_master_56
    complex_venue_42 = importer.save_or_locate(complex_venue_42)

    complex_venue_42.story.add(complex_story_10)

    complex_venue_43 = Venue()
    complex_venue_43.name = '岡山市北区'
    complex_venue_43.type_master = complex_type_master_56
    complex_venue_43 = importer.save_or_locate(complex_venue_43)

    complex_venue_43.story.add(complex_story_4)

    complex_venue_44 = Venue()
    complex_venue_44.name = '岩船郡粟島浦村'
    complex_venue_44.type_master = complex_type_master_56
    complex_venue_44 = importer.save_or_locate(complex_venue_44)

    complex_venue_44.story.add(complex_story_7)

    complex_venue_45 = Venue()
    complex_venue_45.name = '川口市'
    complex_venue_45.type_master = complex_type_master_56
    complex_venue_45 = importer.save_or_locate(complex_venue_45)

    complex_venue_45.story.add(complex_story_24)

    complex_venue_46 = Venue()
    complex_venue_46.name = '常陸太田市'
    complex_venue_46.type_master = complex_type_master_56
    complex_venue_46 = importer.save_or_locate(complex_venue_46)

    complex_venue_46.story.add(complex_story_18)

    complex_venue_47 = Venue()
    complex_venue_47.name = '広島市南区'
    complex_venue_47.type_master = complex_type_master_56
    complex_venue_47 = importer.save_or_locate(complex_venue_47)

    complex_venue_47.story.add(complex_story_9)

    complex_venue_48 = Venue()
    complex_venue_48.name = '広島市東区'
    complex_venue_48.type_master = complex_type_master_56
    complex_venue_48 = importer.save_or_locate(complex_venue_48)

    complex_venue_48.story.add(complex_story_9)

    complex_venue_49 = Venue()
    complex_venue_49.name = '廿日市市'
    complex_venue_49.type_master = complex_type_master_56
    complex_venue_49 = importer.save_or_locate(complex_venue_49)

    complex_venue_49.story.add(complex_story_9)
    complex_venue_49.story.add(complex_story_10)

    complex_venue_50 = Venue()
    complex_venue_50.name = '徳島市'
    complex_venue_50.type_master = complex_type_master_56
    complex_venue_50 = importer.save_or_locate(complex_venue_50)

    complex_venue_50.story.add(complex_story_34)
    complex_venue_50.story.add(complex_story_35)

    complex_venue_51 = Venue()
    complex_venue_51.name = '文京区'
    complex_venue_51.type_master = complex_type_master_56
    complex_venue_51 = importer.save_or_locate(complex_venue_51)

    complex_venue_51.story.add(complex_story_9)

    complex_venue_52 = Venue()
    complex_venue_52.name = '斜里郡斜里町'
    complex_venue_52.type_master = complex_type_master_56
    complex_venue_52 = importer.save_or_locate(complex_venue_52)

    complex_venue_52.story.add(complex_story_30)

    complex_venue_53 = Venue()
    complex_venue_53.name = '新宮市'
    complex_venue_53.type_master = complex_type_master_56
    complex_venue_53 = importer.save_or_locate(complex_venue_53)

    complex_venue_53.story.add(complex_story_12)

    complex_venue_54 = Venue()
    complex_venue_54.name = '新宿区'
    complex_venue_54.type_master = complex_type_master_56
    complex_venue_54 = importer.save_or_locate(complex_venue_54)

    complex_venue_54.story.add(complex_story_22)

    complex_venue_55 = Venue()
    complex_venue_55.name = '日立市'
    complex_venue_55.type_master = complex_type_master_56
    complex_venue_55 = importer.save_or_locate(complex_venue_55)

    complex_venue_55.story.add(complex_story_18)
    complex_venue_55.story.add(complex_story_19)

    complex_venue_56 = Venue()
    complex_venue_56.name = '杉並区'
    complex_venue_56.type_master = complex_type_master_56
    complex_venue_56 = importer.save_or_locate(complex_venue_56)

    complex_venue_56.story.add(complex_story_22)

    complex_venue_57 = Venue()
    complex_venue_57.name = '東牟婁郡串本町'
    complex_venue_57.type_master = complex_type_master_56
    complex_venue_57 = importer.save_or_locate(complex_venue_57)

    complex_venue_57.story.add(complex_story_12)

    complex_venue_58 = Venue()
    complex_venue_58.name = '松江市'
    complex_venue_58.type_master = complex_type_master_56
    complex_venue_58 = importer.save_or_locate(complex_venue_58)

    complex_venue_58.story.add(complex_story_14)
    complex_venue_58.story.add(complex_story_15)

    complex_venue_59 = Venue()
    complex_venue_59.name = '水戸市'
    complex_venue_59.type_master = complex_type_master_56
    complex_venue_59 = importer.save_or_locate(complex_venue_59)

    complex_venue_59.story.add(complex_story_18)

    complex_venue_60 = Venue()
    complex_venue_60.name = '江東区'
    complex_venue_60.type_master = complex_type_master_56
    complex_venue_60 = importer.save_or_locate(complex_venue_60)

    complex_venue_60.story.add(complex_story_17)
    complex_venue_60.story.add(complex_story_34)

    complex_venue_61 = Venue()
    complex_venue_61.name = '海老名市'
    complex_venue_61.type_master = complex_type_master_56
    complex_venue_61 = importer.save_or_locate(complex_venue_61)

    complex_venue_61.story.add(complex_story_9)

    complex_venue_62 = Venue()
    complex_venue_62.name = '渋川市'
    complex_venue_62.type_master = complex_type_master_56
    complex_venue_62 = importer.save_or_locate(complex_venue_62)

    complex_venue_62.story.add(complex_story_24)
    complex_venue_62.story.add(complex_story_53)

    complex_venue_63 = Venue()
    complex_venue_63.name = '渋谷区'
    complex_venue_63.type_master = complex_type_master_56
    complex_venue_63 = importer.save_or_locate(complex_venue_63)

    complex_venue_63.story.add(complex_story_22)

    complex_venue_64 = Venue()
    complex_venue_64.name = '港区'
    complex_venue_64.type_master = complex_type_master_56
    complex_venue_64 = importer.save_or_locate(complex_venue_64)

    complex_venue_64.story.add(complex_story_22)
    complex_venue_64.story.add(complex_story_23)
    complex_venue_64.story.add(complex_story_29)

    complex_venue_65 = Venue()
    complex_venue_65.name = '玖珠郡玖珠町'
    complex_venue_65.type_master = complex_type_master_56
    complex_venue_65 = importer.save_or_locate(complex_venue_65)

    complex_venue_65.story.add(complex_story_20)

    complex_venue_66 = Venue()
    complex_venue_66.name = '田辺市'
    complex_venue_66.type_master = complex_type_master_56
    complex_venue_66 = importer.save_or_locate(complex_venue_66)

    complex_venue_66.story.add(complex_story_12)

    complex_venue_67 = Venue()
    complex_venue_67.name = '甲府市'
    complex_venue_67.type_master = complex_type_master_56
    complex_venue_67 = importer.save_or_locate(complex_venue_67)

    complex_venue_67.story.add(complex_story_32)

    complex_venue_68 = Venue()
    complex_venue_68.name = '甲斐市'
    complex_venue_68.type_master = complex_type_master_56
    complex_venue_68 = importer.save_or_locate(complex_venue_68)

    complex_venue_68.story.add(complex_story_32)

    complex_venue_69 = Venue()
    complex_venue_69.name = '立川市'
    complex_venue_69.type_master = complex_type_master_56
    complex_venue_69 = importer.save_or_locate(complex_venue_69)

    complex_venue_69.story.add(complex_story_16)

    complex_venue_70 = Venue()
    complex_venue_70.name = '紋別市'
    complex_venue_70.type_master = complex_type_master_56
    complex_venue_70 = importer.save_or_locate(complex_venue_70)

    complex_venue_70.story.add(complex_story_29)

    complex_venue_71 = Venue()
    complex_venue_71.name = '網走市'
    complex_venue_71.type_master = complex_type_master_56
    complex_venue_71 = importer.save_or_locate(complex_venue_71)

    complex_venue_71.story.add(complex_story_30)

    complex_venue_72 = Venue()
    complex_venue_72.name = '花巻市'
    complex_venue_72.type_master = complex_type_master_56
    complex_venue_72 = importer.save_or_locate(complex_venue_72)

    complex_venue_72.story.add(complex_story_13)

    complex_venue_73 = Venue()
    complex_venue_73.name = '茅部郡森町'
    complex_venue_73.type_master = complex_type_master_56
    complex_venue_73 = importer.save_or_locate(complex_venue_73)

    complex_venue_73.story.add(complex_story_28)

    complex_venue_74 = Venue()
    complex_venue_74.name = '西多摩郡奥多摩町'
    complex_venue_74.type_master = complex_type_master_56
    complex_venue_74 = importer.save_or_locate(complex_venue_74)

    complex_venue_74.story.add(complex_story_16)
    complex_venue_74.story.add(complex_story_51)

    complex_venue_75 = Venue()
    complex_venue_75.name = '西磐井郡平泉町'
    complex_venue_75.type_master = complex_type_master_56
    complex_venue_75 = importer.save_or_locate(complex_venue_75)

    complex_venue_75.story.add(complex_story_13)

    complex_venue_76 = Venue()
    complex_venue_76.name = '諏訪郡下諏訪町'
    complex_venue_76.type_master = complex_type_master_56
    complex_venue_76 = importer.save_or_locate(complex_venue_76)

    complex_venue_76.story.add(complex_story_37)

    complex_venue_77 = Venue()
    complex_venue_77.name = '那須烏山市'
    complex_venue_77.type_master = complex_type_master_56
    complex_venue_77 = importer.save_or_locate(complex_venue_77)

    complex_venue_77.story.add(complex_story_6)

    complex_venue_78 = Venue()
    complex_venue_78.name = '郡山市'
    complex_venue_78.type_master = complex_type_master_56
    complex_venue_78 = importer.save_or_locate(complex_venue_78)

    complex_venue_78.story.add(complex_story_1)

    complex_venue_79 = Venue()
    complex_venue_79.name = '鈴鹿市'
    complex_venue_79.type_master = complex_type_master_56
    complex_venue_79 = importer.save_or_locate(complex_venue_79)

    complex_venue_79.story.add(complex_story_8)

    complex_venue_80 = Venue()
    complex_venue_80.name = '青梅市'
    complex_venue_80.type_master = complex_type_master_56
    complex_venue_80 = importer.save_or_locate(complex_venue_80)

    complex_venue_80.story.add(complex_story_16)

    complex_venue_81 = Venue()
    complex_venue_81.name = '青森市'
    complex_venue_81.type_master = complex_type_master_56
    complex_venue_81 = importer.save_or_locate(complex_venue_81)

    complex_venue_81.story.add(complex_story_11)

    complex_venue_82 = Venue()
    complex_venue_82.name = '館山市'
    complex_venue_82.type_master = complex_type_master_56
    complex_venue_82 = importer.save_or_locate(complex_venue_82)

    complex_venue_82.story.add(complex_story_31)

    complex_venue_83 = Venue()
    complex_venue_83.name = '高松市'
    complex_venue_83.type_master = complex_type_master_56
    complex_venue_83 = importer.save_or_locate(complex_venue_83)

    complex_venue_83.story.add(complex_story_4)

    complex_venue_84 = Venue()
    complex_venue_84.name = '高知市'
    complex_venue_84.type_master = complex_type_master_56
    complex_venue_84 = importer.save_or_locate(complex_venue_84)

    complex_venue_84.story.add(complex_story_25)
    complex_venue_84.story.add(complex_story_26)
    complex_venue_84.story.add(complex_story_54)

    complex_venue_85 = Venue()
    complex_venue_85.name = '魚沼市'
    complex_venue_85.type_master = complex_type_master_56
    complex_venue_85 = importer.save_or_locate(complex_venue_85)

    complex_venue_85.story.add(complex_story_45)

    complex_venue_86 = Venue()
    complex_venue_86.name = '鳥羽市'
    complex_venue_86.type_master = complex_type_master_56
    complex_venue_86 = importer.save_or_locate(complex_venue_86)

    complex_venue_86.story.add(complex_story_8)

    complex_venue_87 = Venue()
    complex_venue_87.name = '鳴門市'
    complex_venue_87.type_master = complex_type_master_56
    complex_venue_87 = importer.save_or_locate(complex_venue_87)

    complex_venue_87.story.add(complex_story_35)

    complex_venue_88 = Venue()
    complex_venue_88.name = '鹿児島市'
    complex_venue_88.type_master = complex_type_master_56
    complex_venue_88 = importer.save_or_locate(complex_venue_88)

    complex_venue_88.story.add(complex_story_33)

    complex_venue_89 = Venue()
    complex_venue_89.name = '黒部市'
    complex_venue_89.type_master = complex_type_master_56
    complex_venue_89 = importer.save_or_locate(complex_venue_89)

    complex_venue_89.story.add(complex_story_3)

    complex_venue_90 = Venue()
    complex_venue_90.name = 'その他'
    complex_venue_90.type_master = complex_type_master_73
    complex_venue_90 = importer.save_or_locate(complex_venue_90)

    complex_venue_90.story.add(complex_story_43)

    complex_venue_91 = Venue()
    complex_venue_91.name = 'レインボーブリッジ'
    complex_venue_91.type_master = complex_type_master_73
    complex_venue_91 = importer.save_or_locate(complex_venue_91)

    complex_venue_91.story.add(complex_story_44)

    complex_venue_92 = Venue()
    complex_venue_92.name = '教習所'
    complex_venue_92.type_master = complex_type_master_73
    complex_venue_92 = importer.save_or_locate(complex_venue_92)

    complex_venue_92.story.add(complex_story_40)

    complex_venue_93 = Venue()
    complex_venue_93.name = '歌舞伎座'
    complex_venue_93.type_master = complex_type_master_73
    complex_venue_93 = importer.save_or_locate(complex_venue_93)

    complex_venue_93.story.add(complex_story_44)

    complex_venue_94 = Venue()
    complex_venue_94.name = '特急あずさ'
    complex_venue_94.type_master = complex_type_master_73
    complex_venue_94 = importer.save_or_locate(complex_venue_94)

    complex_venue_94.story.add(complex_story_50)

    complex_venue_95 = Venue()
    complex_venue_95.name = '甲府駅'
    complex_venue_95.type_master = complex_type_master_73
    complex_venue_95 = importer.save_or_locate(complex_venue_95)

    complex_venue_95.story.add(complex_story_50)

    complex_venue_96 = Venue()
    complex_venue_96.name = '自宅'
    complex_venue_96.type_master = complex_type_master_73
    complex_venue_96 = importer.save_or_locate(complex_venue_96)

    complex_venue_96.story.add(complex_story_39)
    complex_venue_96.story.add(complex_story_40)
    complex_venue_96.story.add(complex_story_41)
    complex_venue_96.story.add(complex_story_42)
    complex_venue_96.story.add(complex_story_43)
    complex_venue_96.story.add(complex_story_44)
    complex_venue_96.story.add(complex_story_46)
    complex_venue_96.story.add(complex_story_47)
    complex_venue_96.story.add(complex_story_49)
    complex_venue_96.story.add(complex_story_50)
    complex_venue_96.story.add(complex_story_51)

    complex_venue_97 = Venue()
    complex_venue_97.name = '蓮沼宅前'
    complex_venue_97.type_master = complex_type_master_73
    complex_venue_97 = importer.save_or_locate(complex_venue_97)

    complex_venue_97.story.add(complex_story_46)

    complex_venue_98 = Venue()
    complex_venue_98.name = '角川第2本社ビル(千代田区富士見)'
    complex_venue_98.type_master = complex_type_master_73
    complex_venue_98 = importer.save_or_locate(complex_venue_98)

    complex_venue_98.story.add(complex_story_49)

    complex_venue_99 = Venue()
    complex_venue_99.name = '鵜木宅'
    complex_venue_99.type_master = complex_type_master_73
    complex_venue_99 = importer.save_or_locate(complex_venue_99)

    complex_venue_99.story.add(complex_story_48)

    # Processing model: complex.models.Place

    from complex.models import Place

    complex_place_1 = Place()
    complex_place_1.address = '北海道紋別市 真砂町五丁目3 '
    complex_place_1.altitude = Decimal('0.000000')
    complex_place_1.latitude = Decimal('44.363727')
    complex_place_1.longitude = Decimal('143.353108')
    complex_place_1.memo = None
    complex_place_1.name = 'ワンズレンタカー紋別店'
    complex_place_1.venue = None
    complex_place_1 = importer.save_or_locate(complex_place_1)

    complex_place_2 = Place()
    complex_place_2.address = '北海道紋別市  '
    complex_place_2.altitude = Decimal('0.000000')
    complex_place_2.latitude = Decimal('44.311595')
    complex_place_2.longitude = Decimal('143.402507')
    complex_place_2.memo = None
    complex_place_2.name = 'クロスカントリーコース'
    complex_place_2.venue = None
    complex_place_2 = importer.save_or_locate(complex_place_2)

    complex_place_3 = Place()
    complex_place_3.address = '北海道紋別市  '
    complex_place_3.altitude = Decimal('0.000000')
    complex_place_3.latitude = Decimal('44.308991')
    complex_place_3.longitude = Decimal('143.406739')
    complex_place_3.memo = None
    complex_place_3.name = '海のゲート'
    complex_place_3.venue = None
    complex_place_3 = importer.save_or_locate(complex_place_3)

    complex_place_4 = Place()
    complex_place_4.address = '北海道紋別市  '
    complex_place_4.altitude = Decimal('0.000000')
    complex_place_4.latitude = Decimal('44.306756')
    complex_place_4.longitude = Decimal('143.406732')
    complex_place_4.memo = None
    complex_place_4.name = 'トヨタレンタリース北見 紋別空港カウンター'
    complex_place_4.venue = None
    complex_place_4 = importer.save_or_locate(complex_place_4)

    complex_place_5 = Place()
    complex_place_5.address = '北海道紋別市  '
    complex_place_5.altitude = Decimal('0.000000')
    complex_place_5.latitude = Decimal('44.306398')
    complex_place_5.longitude = Decimal('143.406836')
    complex_place_5.memo = None
    complex_place_5.name = '紋別空港（オホーツク紋別空港）'
    complex_place_5.venue = None
    complex_place_5 = importer.save_or_locate(complex_place_5)

    complex_place_6 = Place()
    complex_place_6.address = '北海道紋別郡 湧別町 錦町'
    complex_place_6.altitude = Decimal('0.000000')
    complex_place_6.latitude = Decimal('44.215784')
    complex_place_6.longitude = Decimal('143.597097')
    complex_place_6.memo = None
    complex_place_6.name = '湧別大橋'
    complex_place_6.venue = None
    complex_place_6 = importer.save_or_locate(complex_place_6)

    complex_place_7 = Place()
    complex_place_7.address = None
    complex_place_7.altitude = Decimal('0.000000')
    complex_place_7.latitude = Decimal('44.200000')
    complex_place_7.longitude = Decimal('143.704357')
    complex_place_7.memo = None
    complex_place_7.name = '第22旅 北海道・道東前編 (camera)'
    complex_place_7.venue = None
    complex_place_7 = importer.save_or_locate(complex_place_7)

    complex_place_8 = Place()
    complex_place_8.address = '北海道紋別郡 湧別町 中湧別南町'
    complex_place_8.altitude = Decimal('0.000000')
    complex_place_8.latitude = Decimal('44.185355')
    complex_place_8.longitude = Decimal('143.595783')
    complex_place_8.memo = None
    complex_place_8.name = '中湧別駅跡'
    complex_place_8.venue = None
    complex_place_8 = importer.save_or_locate(complex_place_8)

    complex_place_9 = Place()
    complex_place_9.address = '北海道北見市  '
    complex_place_9.altitude = Decimal('0.000000')
    complex_place_9.latitude = Decimal('44.121295')
    complex_place_9.longitude = Decimal('144.070824')
    complex_place_9.memo = None
    complex_place_9.name = '松寿し'
    complex_place_9.venue = None
    complex_place_9 = importer.save_or_locate(complex_place_9)

    complex_place_10 = Place()
    complex_place_10.address = None
    complex_place_10.altitude = Decimal('0.000000')
    complex_place_10.latitude = Decimal('44.114228')
    complex_place_10.longitude = Decimal('144.245963')
    complex_place_10.memo = None
    complex_place_10.name = '第22旅 北海道・道東後編 (camera)'
    complex_place_10.venue = None
    complex_place_10 = importer.save_or_locate(complex_place_10)

    complex_place_11 = Place()
    complex_place_11.address = '北海道網走市  '
    complex_place_11.altitude = Decimal('0.000000')
    complex_place_11.latitude = Decimal('44.113349')
    complex_place_11.longitude = Decimal('144.243485')
    complex_place_11.memo = None
    complex_place_11.name = '能取岬'
    complex_place_11.venue = None
    complex_place_11 = importer.save_or_locate(complex_place_11)

    complex_place_12 = Place()
    complex_place_12.address = '北海道網走市  '
    complex_place_12.altitude = Decimal('0.000000')
    complex_place_12.latitude = Decimal('44.112108')
    complex_place_12.longitude = Decimal('144.243294')
    complex_place_12.memo = None
    complex_place_12.name = '能取岬灯台'
    complex_place_12.venue = None
    complex_place_12 = importer.save_or_locate(complex_place_12)

    complex_place_13 = Place()
    complex_place_13.address = '北海道網走市  '
    complex_place_13.altitude = Decimal('0.000000')
    complex_place_13.latitude = Decimal('44.110669')
    complex_place_13.longitude = Decimal('144.247355')
    complex_place_13.memo = None
    complex_place_13.name = 'オホーツクの塔'
    complex_place_13.venue = None
    complex_place_13 = importer.save_or_locate(complex_place_13)

    complex_place_14 = Place()
    complex_place_14.address = '北海道斜里郡 斜里町 '
    complex_place_14.altitude = Decimal('0.000000')
    complex_place_14.latitude = Decimal('44.091690')
    complex_place_14.longitude = Decimal('145.025174')
    complex_place_14.memo = None
    complex_place_14.name = '知床横断道路通行止め'
    complex_place_14.venue = None
    complex_place_14 = importer.save_or_locate(complex_place_14)

    complex_place_15 = Place()
    complex_place_15.address = '北海道斜里郡 斜里町 '
    complex_place_15.altitude = Decimal('0.000000')
    complex_place_15.latitude = Decimal('44.091488')
    complex_place_15.longitude = Decimal('145.022962')
    complex_place_15.memo = None
    complex_place_15.name = '知床自然センター'
    complex_place_15.venue = None
    complex_place_15 = importer.save_or_locate(complex_place_15)

    complex_place_16 = Place()
    complex_place_16.address = '北海道斜里郡 斜里町 ウトロ東'
    complex_place_16.altitude = Decimal('0.000000')
    complex_place_16.latitude = Decimal('44.085236')
    complex_place_16.longitude = Decimal('145.010843')
    complex_place_16.memo = None
    complex_place_16.name = '幌別橋'
    complex_place_16.venue = None
    complex_place_16 = importer.save_or_locate(complex_place_16)

    complex_place_17 = Place()
    complex_place_17.address = '北海道斜里郡 斜里町 '
    complex_place_17.altitude = Decimal('0.000000')
    complex_place_17.latitude = Decimal('44.075769')
    complex_place_17.longitude = Decimal('145.122115')
    complex_place_17.memo = None
    complex_place_17.name = '羅臼岳'
    complex_place_17.venue = None
    complex_place_17 = importer.save_or_locate(complex_place_17)

    complex_place_18 = Place()
    complex_place_18.address = '北海道斜里郡 斜里町 '
    complex_place_18.altitude = Decimal('0.000000')
    complex_place_18.latitude = Decimal('44.069034')
    complex_place_18.longitude = Decimal('144.990695')
    complex_place_18.memo = None
    complex_place_18.name = '道の駅 うとろ・シリエトク'
    complex_place_18.venue = None
    complex_place_18 = importer.save_or_locate(complex_place_18)

    complex_place_19 = Place()
    complex_place_19.address = '北海道斜里郡 斜里町 '
    complex_place_19.altitude = Decimal('0.000000')
    complex_place_19.latitude = Decimal('44.038424')
    complex_place_19.longitude = Decimal('144.938058')
    complex_place_19.memo = None
    complex_place_19.name = 'オシンコシン展望台'
    complex_place_19.venue = None
    complex_place_19 = importer.save_or_locate(complex_place_19)

    complex_place_20 = Place()
    complex_place_20.address = '北海道網走市  '
    complex_place_20.altitude = Decimal('0.000000')
    complex_place_20.latitude = Decimal('44.013852')
    complex_place_20.longitude = Decimal('144.116704')
    complex_place_20.memo = None
    complex_place_20.name = '卯原内サンゴ草群落地'
    complex_place_20.venue = None
    complex_place_20 = importer.save_or_locate(complex_place_20)

    complex_place_21 = Place()
    complex_place_21.address = '北海道網走市  '
    complex_place_21.altitude = Decimal('0.000000')
    complex_place_21.latitude = Decimal('44.012415')
    complex_place_21.longitude = Decimal('144.115698')
    complex_place_21.memo = None
    complex_place_21.name = '能取の荘 かがり屋'
    complex_place_21.venue = None
    complex_place_21 = importer.save_or_locate(complex_place_21)

    complex_place_22 = Place()
    complex_place_22.address = '北海道斜里郡 斜里町 '
    complex_place_22.altitude = Decimal('0.000000')
    complex_place_22.latitude = Decimal('43.906771')
    complex_place_22.longitude = Decimal('144.798707')
    complex_place_22.memo = None
    complex_place_22.name = '天に続く道スタート地点'
    complex_place_22.venue = None
    complex_place_22 = importer.save_or_locate(complex_place_22)

    complex_place_23 = Place()
    complex_place_23.address = '北海道北見市 留辺蘂町温根湯温泉一区453 '
    complex_place_23.altitude = Decimal('0.000000')
    complex_place_23.latitude = Decimal('43.759706')
    complex_place_23.longitude = Decimal('143.508209')
    complex_place_23.memo = None
    complex_place_23.name = '美白の湯宿 大江本家'
    complex_place_23.venue = None
    complex_place_23 = importer.save_or_locate(complex_place_23)

    complex_place_24 = Place()
    complex_place_24.address = '北海道茅部郡 森町 字本町131'
    complex_place_24.altitude = Decimal('0.000000')
    complex_place_24.latitude = Decimal('42.108930')
    complex_place_24.longitude = Decimal('140.573914')
    complex_place_24.memo = None
    complex_place_24.name = '森駅'
    complex_place_24.venue = None
    complex_place_24 = importer.save_or_locate(complex_place_24)

    complex_place_25 = Place()
    complex_place_25.address = '北海道茅部郡 森町 字駒ケ岳'
    complex_place_25.altitude = Decimal('0.000000')
    complex_place_25.latitude = Decimal('42.063333')
    complex_place_25.longitude = Decimal('140.677222')
    complex_place_25.memo = None
    complex_place_25.name = '北海道駒ヶ岳'
    complex_place_25.venue = None
    complex_place_25 = importer.save_or_locate(complex_place_25)

    complex_place_26 = Place()
    complex_place_26.address = '北海道亀田郡 七飯町 '
    complex_place_26.altitude = Decimal('0.000000')
    complex_place_26.latitude = Decimal('41.988958')
    complex_place_26.longitude = Decimal('140.666832')
    complex_place_26.memo = None
    complex_place_26.name = '月見橋'
    complex_place_26.venue = None
    complex_place_26 = importer.save_or_locate(complex_place_26)

    complex_place_27 = Place()
    complex_place_27.address = '北海道亀田郡 七飯町 '
    complex_place_27.altitude = Decimal('0.000000')
    complex_place_27.latitude = Decimal('41.983889')
    complex_place_27.longitude = Decimal('140.672908')
    complex_place_27.memo = None
    complex_place_27.name = '大沼国定公園'
    complex_place_27.venue = None
    complex_place_27 = importer.save_or_locate(complex_place_27)

    complex_place_28 = Place()
    complex_place_28.address = '北海道北斗市 市渡一丁目1 '
    complex_place_28.altitude = Decimal('0.000000')
    complex_place_28.latitude = Decimal('41.904698')
    complex_place_28.longitude = Decimal('140.648376')
    complex_place_28.memo = None
    complex_place_28.name = '新函館北斗駅'
    complex_place_28.venue = None
    complex_place_28 = importer.save_or_locate(complex_place_28)

    complex_place_29 = Place()
    complex_place_29.address = '北海道北斗市 市渡723 '
    complex_place_29.altitude = Decimal('0.000000')
    complex_place_29.latitude = Decimal('41.902487')
    complex_place_29.longitude = Decimal('140.652371')
    complex_place_29.memo = None
    complex_place_29.name = 'この「↓」'
    complex_place_29.venue = None
    complex_place_29 = importer.save_or_locate(complex_place_29)

    complex_place_30 = Place()
    complex_place_30.address = '北海道亀田郡 七飯町 本町一丁目1'
    complex_place_30.altitude = Decimal('0.000000')
    complex_place_30.latitude = Decimal('41.887713')
    complex_place_30.longitude = Decimal('140.688198')
    complex_place_30.memo = None
    complex_place_30.name = '七飯駅'
    complex_place_30.venue = None
    complex_place_30 = importer.save_or_locate(complex_place_30)

    complex_place_31 = Place()
    complex_place_31.address = '北海道北斗市 白川241 '
    complex_place_31.altitude = Decimal('0.000000')
    complex_place_31.latitude = Decimal('41.887474')
    complex_place_31.longitude = Decimal('140.666636')
    complex_place_31.memo = None
    complex_place_31.name = '道道676号線'
    complex_place_31.venue = None
    complex_place_31 = importer.save_or_locate(complex_place_31)

    complex_place_32 = Place()
    complex_place_32.address = None
    complex_place_32.altitude = Decimal('0.000000')
    complex_place_32.latitude = Decimal('41.850000')
    complex_place_32.longitude = Decimal('140.745432')
    complex_place_32.memo = None
    complex_place_32.name = '第21旅 北海道・道南後編 (camera)'
    complex_place_32.venue = None
    complex_place_32 = importer.save_or_locate(complex_place_32)

    complex_place_33 = Place()
    complex_place_33.address = '北海道函館市 湯川町二丁目28 '
    complex_place_33.altitude = Decimal('0.000000')
    complex_place_33.latitude = Decimal('41.782105')
    complex_place_33.longitude = Decimal('140.791023')
    complex_place_33.memo = None
    complex_place_33.name = '湯倉神社'
    complex_place_33.venue = None
    complex_place_33 = importer.save_or_locate(complex_place_33)

    complex_place_34 = Place()
    complex_place_34.address = '北海道函館市 湯川町二丁目28 '
    complex_place_34.altitude = Decimal('0.000000')
    complex_place_34.latitude = Decimal('41.781547')
    complex_place_34.longitude = Decimal('140.790943')
    complex_place_34.memo = None
    complex_place_34.name = '湯倉神社 鳥居'
    complex_place_34.venue = None
    complex_place_34 = importer.save_or_locate(complex_place_34)

    complex_place_35 = Place()
    complex_place_35.address = '北海道函館市 湯川町三丁目13 '
    complex_place_35.altitude = Decimal('0.000000')
    complex_place_35.latitude = Decimal('41.777685')
    complex_place_35.longitude = Decimal('140.793187')
    complex_place_35.memo = None
    complex_place_35.name = 'コーヒールームきくち'
    complex_place_35.venue = None
    complex_place_35 = importer.save_or_locate(complex_place_35)

    complex_place_36 = Place()
    complex_place_36.address = '北海道函館市 湯川町三丁目12 '
    complex_place_36.altitude = Decimal('0.000000')
    complex_place_36.latitude = Decimal('41.777091')
    complex_place_36.longitude = Decimal('140.792960')
    complex_place_36.memo = None
    complex_place_36.name = '湯川第２街区公園'
    complex_place_36.venue = None
    complex_place_36 = importer.save_or_locate(complex_place_36)

    complex_place_37 = Place()
    complex_place_37.address = '北海道函館市 湯川町一丁目3 '
    complex_place_37.altitude = Decimal('0.000000')
    complex_place_37.latitude = Decimal('41.775767')
    complex_place_37.longitude = Decimal('140.785691')
    complex_place_37.memo = None
    complex_place_37.name = '旅館一乃松'
    complex_place_37.venue = None
    complex_place_37 = importer.save_or_locate(complex_place_37)

    complex_place_38 = Place()
    complex_place_38.address = '北海道函館市 湯川町二丁目1 '
    complex_place_38.altitude = Decimal('0.000000')
    complex_place_38.latitude = Decimal('41.774893')
    complex_place_38.longitude = Decimal('140.787888')
    complex_place_38.memo = None
    complex_place_38.name = '函館麺や 一文字 函館総本店'
    complex_place_38.venue = None
    complex_place_38 = importer.save_or_locate(complex_place_38)

    complex_place_39 = Place()
    complex_place_39.address = '北海道函館市 湯川町二丁目1 '
    complex_place_39.altitude = Decimal('0.000000')
    complex_place_39.latitude = Decimal('41.774195')
    complex_place_39.longitude = Decimal('140.788346')
    complex_place_39.memo = None
    complex_place_39.name = '函館市熱帯植物園駐車場'
    complex_place_39.venue = None
    complex_place_39 = importer.save_or_locate(complex_place_39)

    complex_place_40 = Place()
    complex_place_40.address = '北海道函館市 若松町12 '
    complex_place_40.altitude = Decimal('0.000000')
    complex_place_40.latitude = Decimal('41.773780')
    complex_place_40.longitude = Decimal('140.726474')
    complex_place_40.memo = None
    complex_place_40.name = '函館駅'
    complex_place_40.venue = None
    complex_place_40 = importer.save_or_locate(complex_place_40)

    complex_place_41 = Place()
    complex_place_41.address = '北海道函館市 金堀町2 '
    complex_place_41.altitude = Decimal('0.000000')
    complex_place_41.latitude = Decimal('41.773685')
    complex_place_41.longitude = Decimal('140.757275')
    complex_place_41.memo = None
    complex_place_41.name = '漁火通'
    complex_place_41.venue = None
    complex_place_41 = importer.save_or_locate(complex_place_41)

    complex_place_42 = Place()
    complex_place_42.address = '北海道函館市 湯川町三丁目1 '
    complex_place_42.altitude = Decimal('0.000000')
    complex_place_42.latitude = Decimal('41.773167')
    complex_place_42.longitude = Decimal('140.787449')
    complex_place_42.memo = None
    complex_place_42.name = '湯川堤防'
    complex_place_42.venue = None
    complex_place_42 = importer.save_or_locate(complex_place_42)

    complex_place_43 = Place()
    complex_place_43.address = '北海道函館市 日乃出町14 '
    complex_place_43.altitude = Decimal('0.000000')
    complex_place_43.latitude = Decimal('41.772781')
    complex_place_43.longitude = Decimal('140.753053')
    complex_place_43.memo = None
    complex_place_43.name = '日乃出ひまわり'
    complex_place_43.venue = None
    complex_place_43 = importer.save_or_locate(complex_place_43)

    complex_place_44 = Place()
    complex_place_44.address = '北海道函館市 若松町13 '
    complex_place_44.altitude = Decimal('0.000000')
    complex_place_44.latitude = Decimal('41.772720')
    complex_place_44.longitude = Decimal('140.725524')
    complex_place_44.memo = None
    complex_place_44.name = '函館朝市 どんぶり横丁市場'
    complex_place_44.venue = None
    complex_place_44 = importer.save_or_locate(complex_place_44)

    complex_place_45 = Place()
    complex_place_45.address = '北海道函館市 若松町13 '
    complex_place_45.altitude = Decimal('0.000000')
    complex_place_45.latitude = Decimal('41.772620')
    complex_place_45.longitude = Decimal('140.725810')
    complex_place_45.memo = None
    complex_place_45.name = '朝市お食事処 山三道下商店'
    complex_place_45.venue = None
    complex_place_45 = importer.save_or_locate(complex_place_45)

    complex_place_46 = Place()
    complex_place_46.address = '北海道函館市 日乃出町25 '
    complex_place_46.altitude = Decimal('0.000000')
    complex_place_46.latitude = Decimal('41.772507')
    complex_place_46.longitude = Decimal('140.754053')
    complex_place_46.memo = None
    complex_place_46.name = '東屋（四阿）'
    complex_place_46.venue = None
    complex_place_46 = importer.save_or_locate(complex_place_46)

    complex_place_47 = Place()
    complex_place_47.address = '北海道函館市 日乃出町25 '
    complex_place_47.altitude = Decimal('0.000000')
    complex_place_47.latitude = Decimal('41.772358')
    complex_place_47.longitude = Decimal('140.753603')
    complex_place_47.memo = None
    complex_place_47.name = '石川啄木像'
    complex_place_47.venue = None
    complex_place_47 = importer.save_or_locate(complex_place_47)

    complex_place_48 = Place()
    complex_place_48.address = '北海道函館市 宇賀浦町14 '
    complex_place_48.altitude = Decimal('0.000000')
    complex_place_48.latitude = Decimal('41.770788')
    complex_place_48.longitude = Decimal('140.745451')
    complex_place_48.memo = None
    complex_place_48.name = '函館グルメ回転ずし函太郎 宇賀浦本店'
    complex_place_48.venue = None
    complex_place_48 = importer.save_or_locate(complex_place_48)

    complex_place_49 = Place()
    complex_place_49.address = '北海道函館市 宇賀浦町1 '
    complex_place_49.altitude = Decimal('0.000000')
    complex_place_49.latitude = Decimal('41.769779')
    complex_place_49.longitude = Decimal('140.740416')
    complex_place_49.memo = None
    complex_place_49.name = '大森町'
    complex_place_49.venue = None
    complex_place_49 = importer.save_or_locate(complex_place_49)

    complex_place_50 = Place()
    complex_place_50.address = '北海道函館市 豊川町11 '
    complex_place_50.altitude = Decimal('0.000000')
    complex_place_50.latitude = Decimal('41.767353')
    complex_place_50.longitude = Decimal('140.717635')
    complex_place_50.memo = None
    complex_place_50.name = '金森赤レンガ倉庫'
    complex_place_50.venue = None
    complex_place_50 = importer.save_or_locate(complex_place_50)

    complex_place_51 = Place()
    complex_place_51.address = '北海道函館市 末広町23 '
    complex_place_51.altitude = Decimal('0.000000')
    complex_place_51.latitude = Decimal('41.765993')
    complex_place_51.longitude = Decimal('140.714633')
    complex_place_51.memo = None
    complex_place_51.name = 'カリフォルニアベイビー'
    complex_place_51.venue = None
    complex_place_51 = importer.save_or_locate(complex_place_51)

    complex_place_52 = Place()
    complex_place_52.address = '北海道函館市 末広町16 '
    complex_place_52.altitude = Decimal('0.000000')
    complex_place_52.latitude = Decimal('41.764355')
    complex_place_52.longitude = Decimal('140.716127')
    complex_place_52.memo = None
    complex_place_52.name = '二十間坂'
    complex_place_52.venue = None
    complex_place_52 = importer.save_or_locate(complex_place_52)

    complex_place_53 = Place()
    complex_place_53.address = '北海道函館市 元町16 '
    complex_place_53.altitude = Decimal('0.000000')
    complex_place_53.latitude = Decimal('41.762936')
    complex_place_53.longitude = Decimal('140.714039')
    complex_place_53.memo = None
    complex_place_53.name = '真宗大谷派 東本願寺 函館別院'
    complex_place_53.venue = None
    complex_place_53 = importer.save_or_locate(complex_place_53)

    complex_place_54 = Place()
    complex_place_54.address = '北海道函館市 元町19 '
    complex_place_54.altitude = Decimal('0.000000')
    complex_place_54.latitude = Decimal('41.760908')
    complex_place_54.longitude = Decimal('140.714301')
    complex_place_54.memo = None
    complex_place_54.name = '函館山ロープウェイ山麓駅'
    complex_place_54.venue = None
    complex_place_54 = importer.save_or_locate(complex_place_54)

    complex_place_55 = Place()
    complex_place_55.address = '北海道函館市 住吉町15 '
    complex_place_55.altitude = Decimal('0.000000')
    complex_place_55.latitude = Decimal('41.747486')
    complex_place_55.longitude = Decimal('140.719450')
    complex_place_55.memo = None
    complex_place_55.name = '石川啄木一族の墓'
    complex_place_55.venue = None
    complex_place_55 = importer.save_or_locate(complex_place_55)

    complex_place_56 = Place()
    complex_place_56.address = '北海道函館市 住吉町15 '
    complex_place_56.altitude = Decimal('0.000000')
    complex_place_56.latitude = Decimal('41.745035')
    complex_place_56.longitude = Decimal('140.721203')
    complex_place_56.memo = None
    complex_place_56.name = '立待岬'
    complex_place_56.venue = None
    complex_place_56 = importer.save_or_locate(complex_place_56)

    complex_place_57 = Place()
    complex_place_57.address = '青森県むつ市  '
    complex_place_57.altitude = Decimal('0.000000')
    complex_place_57.latitude = Decimal('41.328370')
    complex_place_57.longitude = Decimal('141.091705')
    complex_place_57.memo = None
    complex_place_57.name = '恐山 花染の湯'
    complex_place_57.venue = None
    complex_place_57 = importer.save_or_locate(complex_place_57)

    complex_place_58 = Place()
    complex_place_58.address = '青森県むつ市  '
    complex_place_58.altitude = Decimal('0.000000')
    complex_place_58.latitude = Decimal('41.327247')
    complex_place_58.longitude = Decimal('141.090762')
    complex_place_58.memo = None
    complex_place_58.name = '恐山菩提寺'
    complex_place_58.venue = None
    complex_place_58 = importer.save_or_locate(complex_place_58)

    complex_place_59 = Place()
    complex_place_59.address = '青森県むつ市  '
    complex_place_59.altitude = Decimal('0.000000')
    complex_place_59.latitude = Decimal('41.326497')
    complex_place_59.longitude = Decimal('141.086011')
    complex_place_59.memo = None
    complex_place_59.name = '宇曽利山湖 極楽浜'
    complex_place_59.venue = None
    complex_place_59 = importer.save_or_locate(complex_place_59)

    complex_place_60 = Place()
    complex_place_60.address = '青森県むつ市  '
    complex_place_60.altitude = Decimal('0.000000')
    complex_place_60.latitude = Decimal('41.326066')
    complex_place_60.longitude = Decimal('141.096227')
    complex_place_60.memo = None
    complex_place_60.name = '三途の川'
    complex_place_60.venue = None
    complex_place_60 = importer.save_or_locate(complex_place_60)

    complex_place_61 = Place()
    complex_place_61.address = '青森県むつ市  '
    complex_place_61.altitude = Decimal('0.000000')
    complex_place_61.latitude = Decimal('41.314566')
    complex_place_61.longitude = Decimal('141.126492')
    complex_place_61.memo = None
    complex_place_61.name = '恐山冷水'
    complex_place_61.venue = None
    complex_place_61 = importer.save_or_locate(complex_place_61)

    complex_place_62 = Place()
    complex_place_62.address = '青森県むつ市 下北町4 '
    complex_place_62.altitude = Decimal('0.000000')
    complex_place_62.latitude = Decimal('41.282743')
    complex_place_62.longitude = Decimal('141.189904')
    complex_place_62.memo = None
    complex_place_62.name = '下北駅'
    complex_place_62.venue = None
    complex_place_62 = importer.save_or_locate(complex_place_62)

    complex_place_63 = Place()
    complex_place_63.address = None
    complex_place_63.altitude = Decimal('0.000000')
    complex_place_63.latitude = Decimal('40.840000')
    complex_place_63.longitude = Decimal('140.846000')
    complex_place_63.memo = None
    complex_place_63.name = '第10旅 青森 (camera)'
    complex_place_63.venue = None
    complex_place_63 = importer.save_or_locate(complex_place_63)

    complex_place_64 = Place()
    complex_place_64.address = '青森県青森市 大字横内字八重菊62 '
    complex_place_64.altitude = Decimal('0.000000')
    complex_place_64.latitude = Decimal('40.705758')
    complex_place_64.longitude = Decimal('140.822305')
    complex_place_64.memo = None
    complex_place_64.name = '萱野茶屋'
    complex_place_64.venue = None
    complex_place_64 = importer.save_or_locate(complex_place_64)

    complex_place_65 = Place()
    complex_place_65.address = '青森県青森市  '
    complex_place_65.altitude = Decimal('0.000000')
    complex_place_65.latitude = Decimal('40.675822')
    complex_place_65.longitude = Decimal('140.858813')
    complex_place_65.memo = None
    complex_place_65.name = '八甲田ロープウェイ 山頂公園駅'
    complex_place_65.venue = None
    complex_place_65 = importer.save_or_locate(complex_place_65)

    complex_place_66 = Place()
    complex_place_66.address = '青森県青森市  '
    complex_place_66.altitude = Decimal('0.000000')
    complex_place_66.latitude = Decimal('40.675774')
    complex_place_66.longitude = Decimal('140.859212')
    complex_place_66.memo = None
    complex_place_66.name = '八甲田 山頂公園'
    complex_place_66.venue = None
    complex_place_66 = importer.save_or_locate(complex_place_66)

    complex_place_67 = Place()
    complex_place_67.address = '青森県十和田市  '
    complex_place_67.altitude = Decimal('0.000000')
    complex_place_67.latitude = Decimal('40.633018')
    complex_place_67.longitude = Decimal('140.924527')
    complex_place_67.memo = None
    complex_place_67.name = '谷地温泉'
    complex_place_67.venue = None
    complex_place_67 = importer.save_or_locate(complex_place_67)

    complex_place_68 = Place()
    complex_place_68.address = '岩手県花巻市 湯口字大沢171 '
    complex_place_68.altitude = Decimal('0.000000')
    complex_place_68.latitude = Decimal('39.436549')
    complex_place_68.longitude = Decimal('141.015962')
    complex_place_68.memo = None
    complex_place_68.name = '大沢温泉 湯治屋'
    complex_place_68.venue = None
    complex_place_68 = importer.save_or_locate(complex_place_68)

    complex_place_69 = Place()
    complex_place_69.address = '岩手県花巻市 湯口字渡り24 '
    complex_place_69.altitude = Decimal('0.000000')
    complex_place_69.latitude = Decimal('39.425692')
    complex_place_69.longitude = Decimal('141.015199')
    complex_place_69.memo = None
    complex_place_69.name = '渡り温泉 ホテルさつき・別邸楓'
    complex_place_69.venue = None
    complex_place_69 = importer.save_or_locate(complex_place_69)

    complex_place_70 = Place()
    complex_place_70.address = '岩手県花巻市 上似内126 '
    complex_place_70.altitude = Decimal('0.000000')
    complex_place_70.latitude = Decimal('39.412046')
    complex_place_70.longitude = Decimal('141.141406')
    complex_place_70.memo = None
    complex_place_70.name = '案山子'
    complex_place_70.venue = None
    complex_place_70 = importer.save_or_locate(complex_place_70)

    complex_place_71 = Place()
    complex_place_71.address = '岩手県花巻市 胡四王一丁目1 '
    complex_place_71.altitude = Decimal('0.000000')
    complex_place_71.latitude = Decimal('39.406450')
    complex_place_71.longitude = Decimal('141.173865')
    complex_place_71.memo = None
    complex_place_71.name = '新花巻駅'
    complex_place_71.venue = None
    complex_place_71 = importer.save_or_locate(complex_place_71)

    complex_place_72 = Place()
    complex_place_72.address = '岩手県花巻市 胡四王一丁目3 '
    complex_place_72.altitude = Decimal('0.000000')
    complex_place_72.latitude = Decimal('39.405893')
    complex_place_72.longitude = Decimal('141.172809')
    complex_place_72.memo = None
    complex_place_72.name = '今この辺をぶらついているよ！'
    complex_place_72.venue = None
    complex_place_72 = importer.save_or_locate(complex_place_72)

    complex_place_73 = Place()
    complex_place_73.address = '岩手県花巻市 矢沢3 '
    complex_place_73.altitude = Decimal('0.000000')
    complex_place_73.latitude = Decimal('39.401598')
    complex_place_73.longitude = Decimal('141.161020')
    complex_place_73.memo = None
    complex_place_73.name = '胡四王神社'
    complex_place_73.venue = None
    complex_place_73 = importer.save_or_locate(complex_place_73)

    complex_place_74 = Place()
    complex_place_74.address = '岩手県花巻市 高松第二十六地割8 '
    complex_place_74.altitude = Decimal('0.000000')
    complex_place_74.latitude = Decimal('39.399458')
    complex_place_74.longitude = Decimal('141.164588')
    complex_place_74.memo = None
    complex_place_74.name = '山猫軒'
    complex_place_74.venue = None
    complex_place_74 = importer.save_or_locate(complex_place_74)

    complex_place_75 = Place()
    complex_place_75.address = '岩手県花巻市 矢沢第一地割15 '
    complex_place_75.altitude = Decimal('0.000000')
    complex_place_75.latitude = Decimal('39.399207')
    complex_place_75.longitude = Decimal('141.162670')
    complex_place_75.memo = None
    complex_place_75.name = '宮沢賢治記念館'
    complex_place_75.venue = None
    complex_place_75 = importer.save_or_locate(complex_place_75)

    complex_place_76 = Place()
    complex_place_76.address = '岩手県花巻市 材木町3 '
    complex_place_76.altitude = Decimal('0.000000')
    complex_place_76.latitude = Decimal('39.389429')
    complex_place_76.longitude = Decimal('141.109114')
    complex_place_76.memo = None
    complex_place_76.name = '材木町公園'
    complex_place_76.venue = None
    complex_place_76 = importer.save_or_locate(complex_place_76)

    complex_place_77 = Place()
    complex_place_77.address = '岩手県花巻市 上町6 '
    complex_place_77.altitude = Decimal('0.000000')
    complex_place_77.latitude = Decimal('39.385894')
    complex_place_77.longitude = Decimal('141.117104')
    complex_place_77.memo = None
    complex_place_77.name = 'マルカン百貨店'
    complex_place_77.venue = None
    complex_place_77 = importer.save_or_locate(complex_place_77)

    complex_place_78 = Place()
    complex_place_78.address = '岩手県花巻市 上町6 '
    complex_place_78.altitude = Decimal('0.000000')
    complex_place_78.latitude = Decimal('39.385832')
    complex_place_78.longitude = Decimal('141.117110')
    complex_place_78.memo = None
    complex_place_78.name = 'マルカンビル大食堂'
    complex_place_78.venue = None
    complex_place_78 = importer.save_or_locate(complex_place_78)

    complex_place_79 = Place()
    complex_place_79.address = '岩手県花巻市 石神町201 '
    complex_place_79.altitude = Decimal('0.000000')
    complex_place_79.latitude = Decimal('39.383010')
    complex_place_79.longitude = Decimal('141.103901')
    complex_place_79.memo = None
    complex_place_79.name = '鼬幣稲荷神社'
    complex_place_79.venue = None
    complex_place_79 = importer.save_or_locate(complex_place_79)

    complex_place_80 = Place()
    complex_place_80.address = '岩手県花巻市 山の神1000 '
    complex_place_80.altitude = Decimal('0.000000')
    complex_place_80.latitude = Decimal('39.356792')
    complex_place_80.longitude = Decimal('141.109131')
    complex_place_80.memo = None
    complex_place_80.name = '元祖満州にらラーメンさかえや 本店'
    complex_place_80.venue = None
    complex_place_80 = importer.save_or_locate(complex_place_80)

    complex_place_81 = Place()
    complex_place_81.address = '岩手県北上市 村崎野十五地割148 '
    complex_place_81.altitude = Decimal('0.000000')
    complex_place_81.latitude = Decimal('39.322611')
    complex_place_81.longitude = Decimal('141.120402')
    complex_place_81.memo = None
    complex_place_81.name = '村崎野駅'
    complex_place_81.venue = None
    complex_place_81 = importer.save_or_locate(complex_place_81)

    complex_place_82 = Place()
    complex_place_82.address = None
    complex_place_82.altitude = Decimal('0.000000')
    complex_place_82.latitude = Decimal('39.300000')
    complex_place_82.longitude = Decimal('141.254200')
    complex_place_82.memo = None
    complex_place_82.name = '第12旅 花巻 (camera)'
    complex_place_82.venue = None
    complex_place_82 = importer.save_or_locate(complex_place_82)

    complex_place_83 = Place()
    complex_place_83.address = '岩手県西磐井郡 平泉町 平泉43'
    complex_place_83.altitude = Decimal('0.000000')
    complex_place_83.latitude = Decimal('39.001736')
    complex_place_83.longitude = Decimal('141.102596')
    complex_place_83.memo = None
    complex_place_83.name = '中尊寺'
    complex_place_83.venue = None
    complex_place_83 = importer.save_or_locate(complex_place_83)

    complex_place_84 = Place()
    complex_place_84.address = '新潟県岩船郡 粟島浦村 '
    complex_place_84.altitude = Decimal('0.000000')
    complex_place_84.latitude = Decimal('38.487600')
    complex_place_84.longitude = Decimal('139.263736')
    complex_place_84.memo = None
    complex_place_84.name = '鳥崎展望台'
    complex_place_84.venue = None
    complex_place_84 = importer.save_or_locate(complex_place_84)

    complex_place_85 = Place()
    complex_place_85.address = '新潟県岩船郡 粟島浦村 '
    complex_place_85.altitude = Decimal('0.000000')
    complex_place_85.latitude = Decimal('38.468752')
    complex_place_85.longitude = Decimal('139.254986')
    complex_place_85.memo = None
    complex_place_85.name = '漁火温泉 おと姫の湯'
    complex_place_85.venue = None
    complex_place_85 = importer.save_or_locate(complex_place_85)

    complex_place_86 = Place()
    complex_place_86.address = '新潟県岩船郡 粟島浦村 '
    complex_place_86.altitude = Decimal('0.000000')
    complex_place_86.latitude = Decimal('38.467443')
    complex_place_86.longitude = Decimal('139.254906')
    complex_place_86.memo = None
    complex_place_86.name = '粟島観光案内所'
    complex_place_86.venue = None
    complex_place_86 = importer.save_or_locate(complex_place_86)

    complex_place_87 = Place()
    complex_place_87.address = '新潟県岩船郡 粟島浦村 '
    complex_place_87.altitude = Decimal('0.000000')
    complex_place_87.latitude = Decimal('38.465077')
    complex_place_87.longitude = Decimal('139.253097')
    complex_place_87.memo = None
    complex_place_87.name = 'みやこや食堂'
    complex_place_87.venue = None
    complex_place_87 = importer.save_or_locate(complex_place_87)

    complex_place_88 = Place()
    complex_place_88.address = '新潟県岩船郡 粟島浦村 '
    complex_place_88.altitude = Decimal('0.000000')
    complex_place_88.latitude = Decimal('38.446990')
    complex_place_88.longitude = Decimal('139.223125')
    complex_place_88.memo = None
    complex_place_88.name = '源左エ門'
    complex_place_88.venue = None
    complex_place_88 = importer.save_or_locate(complex_place_88)

    complex_place_89 = Place()
    complex_place_89.address = '新潟県岩船郡 粟島浦村 '
    complex_place_89.altitude = Decimal('0.000000')
    complex_place_89.latitude = Decimal('38.437462')
    complex_place_89.longitude = Decimal('139.223981')
    complex_place_89.memo = None
    complex_place_89.name = '矢ヶ鼻展望台'
    complex_place_89.venue = None
    complex_place_89 = importer.save_or_locate(complex_place_89)

    complex_place_90 = Place()
    complex_place_90.address = None
    complex_place_90.altitude = Decimal('0.000000')
    complex_place_90.latitude = Decimal('38.400000')
    complex_place_90.longitude = Decimal('139.329600')
    complex_place_90.memo = None
    complex_place_90.name = '第7旅 粟島 (camera)'
    complex_place_90.venue = None
    complex_place_90 = importer.save_or_locate(complex_place_90)

    complex_place_91 = Place()
    complex_place_91.address = '宮城県宮城郡 松島町 松島字道珍浜'
    complex_place_91.altitude = Decimal('0.000000')
    complex_place_91.latitude = Decimal('38.376820')
    complex_place_91.longitude = Decimal('141.068558')
    complex_place_91.memo = None
    complex_place_91.name = '松島ホテル和楽'
    complex_place_91.venue = None
    complex_place_91 = importer.save_or_locate(complex_place_91)

    complex_place_92 = Place()
    complex_place_92.address = '宮城県宮城郡 松島町 松島字普賢堂'
    complex_place_92.altitude = Decimal('0.000000')
    complex_place_92.latitude = Decimal('38.371952')
    complex_place_92.longitude = Decimal('141.065172')
    complex_place_92.memo = None
    complex_place_92.name = '松島さかな市場'
    complex_place_92.venue = None
    complex_place_92 = importer.save_or_locate(complex_place_92)

    complex_place_93 = Place()
    complex_place_93.address = '宮城県宮城郡 松島町 松島字町内'
    complex_place_93.altitude = Decimal('0.000000')
    complex_place_93.latitude = Decimal('38.371873')
    complex_place_93.longitude = Decimal('141.060390')
    complex_place_93.memo = None
    complex_place_93.name = '瑞巌寺'
    complex_place_93.venue = None
    complex_place_93 = importer.save_or_locate(complex_place_93)

    complex_place_94 = Place()
    complex_place_94.address = '宮城県宮城郡 松島町 松島字仙隨'
    complex_place_94.altitude = Decimal('0.000000')
    complex_place_94.latitude = Decimal('38.370710')
    complex_place_94.longitude = Decimal('141.065417')
    complex_place_94.memo = None
    complex_place_94.name = 'うな真石田家'
    complex_place_94.venue = None
    complex_place_94 = importer.save_or_locate(complex_place_94)

    complex_place_95 = Place()
    complex_place_95.address = '  '
    complex_place_95.altitude = Decimal('0.000000')
    complex_place_95.latitude = Decimal('38.368956')
    complex_place_95.longitude = Decimal('141.062895')
    complex_place_95.memo = None
    complex_place_95.name = '松島巡り観光船 乗り場(松島觀光遊艇搭船場)'
    complex_place_95.venue = None
    complex_place_95 = importer.save_or_locate(complex_place_95)

    complex_place_96 = Place()
    complex_place_96.address = '宮城県宮城郡 松島町 松島字浪打浜'
    complex_place_96.altitude = Decimal('0.000000')
    complex_place_96.latitude = Decimal('38.368550')
    complex_place_96.longitude = Decimal('141.059362')
    complex_place_96.memo = None
    complex_place_96.name = 'かき松島 こうは「松島海岸駅前本店」１号店'
    complex_place_96.venue = None
    complex_place_96 = importer.save_or_locate(complex_place_96)

    complex_place_97 = Place()
    complex_place_97.address = '宮城県宮城郡 松島町 松島字浪打浜'
    complex_place_97.altitude = Decimal('0.000000')
    complex_place_97.latitude = Decimal('38.368520')
    complex_place_97.longitude = Decimal('141.059557')
    complex_place_97.memo = None
    complex_place_97.name = '三陸海鮮料理 たからや食堂'
    complex_place_97.venue = None
    complex_place_97 = importer.save_or_locate(complex_place_97)

    complex_place_98 = Place()
    complex_place_98.address = '宮城県宮城郡 松島町 松島字浪打浜'
    complex_place_98.altitude = Decimal('0.000000')
    complex_place_98.latitude = Decimal('38.368390')
    complex_place_98.longitude = Decimal('141.058891')
    complex_place_98.memo = None
    complex_place_98.name = '（閉店）笹かま販売所'
    complex_place_98.venue = None
    complex_place_98 = importer.save_or_locate(complex_place_98)

    complex_place_99 = Place()
    complex_place_99.address = '宮城県宮城郡 松島町 松島字浪打浜'
    complex_place_99.altitude = Decimal('0.000000')
    complex_place_99.latitude = Decimal('38.368053')
    complex_place_99.longitude = Decimal('141.058815')
    complex_place_99.memo = None
    complex_place_99.name = '松島海岸駅'
    complex_place_99.venue = None
    complex_place_99 = importer.save_or_locate(complex_place_99)

    complex_place_100 = Place()
    complex_place_100.address = '宮城県宮城郡 松島町 松島字霞ケ浦'
    complex_place_100.altitude = Decimal('0.000000')
    complex_place_100.latitude = Decimal('38.366173')
    complex_place_100.longitude = Decimal('141.061130')
    complex_place_100.memo = None
    complex_place_100.name = '松島公園'
    complex_place_100.venue = None
    complex_place_100 = importer.save_or_locate(complex_place_100)

    complex_place_101 = Place()
    complex_place_101.address = '宮城県宮城郡 松島町 松島字霞ケ浦'
    complex_place_101.altitude = Decimal('0.000000')
    complex_place_101.latitude = Decimal('38.365484')
    complex_place_101.longitude = Decimal('141.062256')
    complex_place_101.memo = None
    complex_place_101.name = '御嶋真珠稲荷大明神'
    complex_place_101.venue = None
    complex_place_101 = importer.save_or_locate(complex_place_101)

    complex_place_102 = Place()
    complex_place_102.address = '宮城県宮城郡 松島町 松島字霞ケ浦'
    complex_place_102.altitude = Decimal('0.000000')
    complex_place_102.latitude = Decimal('38.365350')
    complex_place_102.longitude = Decimal('141.062530')
    complex_place_102.memo = None
    complex_place_102.name = '雄島'
    complex_place_102.venue = None
    complex_place_102 = importer.save_or_locate(complex_place_102)

    complex_place_103 = Place()
    complex_place_103.address = None
    complex_place_103.altitude = Decimal('0.000000')
    complex_place_103.latitude = Decimal('38.332100')
    complex_place_103.longitude = Decimal('140.974700')
    complex_place_103.memo = None
    complex_place_103.name = '第2旅 松島 (camera)'
    complex_place_103.venue = None
    complex_place_103 = importer.save_or_locate(complex_place_103)

    complex_place_104 = Place()
    complex_place_104.address = '宮城県仙台市 青葉区 中央一丁目'
    complex_place_104.altitude = Decimal('0.000000')
    complex_place_104.latitude = Decimal('38.260132')
    complex_place_104.longitude = Decimal('140.882438')
    complex_place_104.memo = None
    complex_place_104.name = '仙台駅'
    complex_place_104.venue = None
    complex_place_104 = importer.save_or_locate(complex_place_104)

    complex_place_105 = Place()
    complex_place_105.address = '福島県会津若松市 駅前町1 '
    complex_place_105.altitude = Decimal('0.000000')
    complex_place_105.latitude = Decimal('37.507866')
    complex_place_105.longitude = Decimal('139.930326')
    complex_place_105.memo = None
    complex_place_105.name = '会津若松駅'
    complex_place_105.venue = None
    complex_place_105 = importer.save_or_locate(complex_place_105)

    complex_place_106 = Place()
    complex_place_106.address = '福島県会津若松市 駅前町6 '
    complex_place_106.altitude = Decimal('0.000000')
    complex_place_106.latitude = Decimal('37.506627')
    complex_place_106.longitude = Decimal('139.931417')
    complex_place_106.memo = None
    complex_place_106.name = 'ラーメン二郎 会津若松駅前店'
    complex_place_106.venue = None
    complex_place_106 = importer.save_or_locate(complex_place_106)

    complex_place_107 = Place()
    complex_place_107.address = '福島県会津若松市 蚕養町4 '
    complex_place_107.altitude = Decimal('0.000000')
    complex_place_107.latitude = Decimal('37.506019')
    complex_place_107.longitude = Decimal('139.937912')
    complex_place_107.memo = None
    complex_place_107.name = '子安観音と古峯神社'
    complex_place_107.venue = None
    complex_place_107 = importer.save_or_locate(complex_place_107)

    complex_place_108 = Place()
    complex_place_108.address = '福島県会津若松市 一箕町八幡弁天下33 '
    complex_place_108.altitude = Decimal('0.000000')
    complex_place_108.latitude = Decimal('37.504532')
    complex_place_108.longitude = Decimal('139.953970')
    complex_place_108.memo = None
    complex_place_108.name = '会津さざえ堂 (円通寺三匝堂)'
    complex_place_108.venue = None
    complex_place_108 = importer.save_or_locate(complex_place_108)

    complex_place_109 = Place()
    complex_place_109.address = '福島県会津若松市 一箕町八幡弁天下2 '
    complex_place_109.altitude = Decimal('0.000000')
    complex_place_109.latitude = Decimal('37.504477')
    complex_place_109.longitude = Decimal('139.952828')
    complex_place_109.memo = None
    complex_place_109.name = '小池菓子舗 飯盛山店'
    complex_place_109.venue = None
    complex_place_109 = importer.save_or_locate(complex_place_109)

    complex_place_110 = Place()
    complex_place_110.address = None
    complex_place_110.altitude = Decimal('0.000000')
    complex_place_110.latitude = Decimal('37.493400')
    complex_place_110.longitude = Decimal('140.159800')
    complex_place_110.memo = None
    complex_place_110.name = '第1旅 会津若松 (camera)'
    complex_place_110.venue = None
    complex_place_110 = importer.save_or_locate(complex_place_110)

    complex_place_111 = Place()
    complex_place_111.address = '福島県会津若松市 東山町湯本寺屋敷19 '
    complex_place_111.altitude = Decimal('0.000000')
    complex_place_111.latitude = Decimal('37.481876')
    complex_place_111.longitude = Decimal('139.965171')
    complex_place_111.memo = None
    complex_place_111.name = '羽黒山湯上神社本殿'
    complex_place_111.venue = None
    complex_place_111 = importer.save_or_locate(complex_place_111)

    complex_place_112 = Place()
    complex_place_112.address = '福島県郡山市 熱海町熱海一丁目109 '
    complex_place_112.altitude = Decimal('0.000000')
    complex_place_112.latitude = Decimal('37.480896')
    complex_place_112.longitude = Decimal('140.270869')
    complex_place_112.memo = None
    complex_place_112.name = '磐梯熱海駅'
    complex_place_112.venue = None
    complex_place_112 = importer.save_or_locate(complex_place_112)

    complex_place_113 = Place()
    complex_place_113.address = '福島県会津若松市 東山町湯本寺屋敷10 '
    complex_place_113.altitude = Decimal('0.000000')
    complex_place_113.latitude = Decimal('37.479700')
    complex_place_113.longitude = Decimal('139.962081')
    complex_place_113.memo = None
    complex_place_113.name = '羽黒山神社 神門'
    complex_place_113.venue = None
    complex_place_113 = importer.save_or_locate(complex_place_113)

    complex_place_114 = Place()
    complex_place_114.address = '福島県会津若松市 東山町湯本寺屋敷19 '
    complex_place_114.altitude = Decimal('0.000000')
    complex_place_114.latitude = Decimal('37.479336')
    complex_place_114.longitude = Decimal('139.962392')
    complex_place_114.memo = None
    complex_place_114.name = 'くつろぎ宿 千代滝'
    complex_place_114.venue = None
    complex_place_114 = importer.save_or_locate(complex_place_114)

    complex_place_115 = Place()
    complex_place_115.address = '福島県会津若松市 東山町湯本居平122 '
    complex_place_115.altitude = Decimal('0.000000')
    complex_place_115.latitude = Decimal('37.478147')
    complex_place_115.longitude = Decimal('139.963241')
    complex_place_115.memo = None
    complex_place_115.name = '射的場'
    complex_place_115.venue = None
    complex_place_115 = importer.save_or_locate(complex_place_115)

    complex_place_116 = Place()
    complex_place_116.address = '福島県会津若松市 東山町湯本居平41 '
    complex_place_116.altitude = Decimal('0.000000')
    complex_place_116.latitude = Decimal('37.478055')
    complex_place_116.longitude = Decimal('139.961089')
    complex_place_116.memo = None
    complex_place_116.name = '会津東山温泉 向瀧'
    complex_place_116.venue = None
    complex_place_116 = importer.save_or_locate(complex_place_116)

    complex_place_117 = Place()
    complex_place_117.address = '福島県郡山市 駅前二丁目4 '
    complex_place_117.altitude = Decimal('0.000000')
    complex_place_117.latitude = Decimal('37.398557')
    complex_place_117.longitude = Decimal('140.388402')
    complex_place_117.memo = None
    complex_place_117.name = '郡山駅'
    complex_place_117.venue = None
    complex_place_117 = importer.save_or_locate(complex_place_117)

    complex_place_118 = Place()
    complex_place_118.address = '富山県黒部市 生地中区265 '
    complex_place_118.altitude = Decimal('0.000000')
    complex_place_118.latitude = Decimal('36.891315')
    complex_place_118.longitude = Decimal('137.418478')
    complex_place_118.memo = None
    complex_place_118.name = '魚の駅生地 とれたて館'
    complex_place_118.venue = None
    complex_place_118 = importer.save_or_locate(complex_place_118)

    complex_place_119 = Place()
    complex_place_119.address = '富山県黒部市 生地中区265 '
    complex_place_119.altitude = Decimal('0.000000')
    complex_place_119.latitude = Decimal('36.891126')
    complex_place_119.longitude = Decimal('137.418853')
    complex_place_119.memo = None
    complex_place_119.name = '魚の駅生地 できたて館 航海灯'
    complex_place_119.venue = None
    complex_place_119 = importer.save_or_locate(complex_place_119)

    complex_place_120 = Place()
    complex_place_120.address = '富山県黒部市 生地292 '
    complex_place_120.altitude = Decimal('0.000000')
    complex_place_120.latitude = Decimal('36.890697')
    complex_place_120.longitude = Decimal('137.417061')
    complex_place_120.memo = None
    complex_place_120.name = '岩瀬家の清水'
    complex_place_120.venue = None
    complex_place_120 = importer.save_or_locate(complex_place_120)

    complex_place_121 = Place()
    complex_place_121.address = '富山県黒部市 若栗3203 '
    complex_place_121.altitude = Decimal('0.000000')
    complex_place_121.latitude = Decimal('36.874237')
    complex_place_121.longitude = Decimal('137.481415')
    complex_place_121.memo = None
    complex_place_121.name = '黒部宇奈月温泉駅'
    complex_place_121.venue = None
    complex_place_121 = importer.save_or_locate(complex_place_121)

    complex_place_122 = Place()
    complex_place_122.address = '富山県黒部市 山田新282 '
    complex_place_122.altitude = Decimal('0.000000')
    complex_place_122.latitude = Decimal('36.873683')
    complex_place_122.longitude = Decimal('137.465870')
    complex_place_122.memo = None
    complex_place_122.name = '吉祥寺'
    complex_place_122.venue = None
    complex_place_122 = importer.save_or_locate(complex_place_122)

    complex_place_123 = Place()
    complex_place_123.address = '富山県黒部市 若栗2762 '
    complex_place_123.altitude = Decimal('0.000000')
    complex_place_123.latitude = Decimal('36.873154')
    complex_place_123.longitude = Decimal('137.480916')
    complex_place_123.memo = None
    complex_place_123.name = '新黒部駅'
    complex_place_123.venue = None
    complex_place_123 = importer.save_or_locate(complex_place_123)

    complex_place_124 = Place()
    complex_place_124.address = None
    complex_place_124.altitude = Decimal('0.000000')
    complex_place_124.latitude = Decimal('36.834090')
    complex_place_124.longitude = Decimal('137.512720')
    complex_place_124.memo = None
    complex_place_124.name = '第3旅 黒部 (camera)'
    complex_place_124.venue = None
    complex_place_124 = importer.save_or_locate(complex_place_124)

    complex_place_125 = Place()
    complex_place_125.address = '富山県黒部市 宇奈月温泉7 '
    complex_place_125.altitude = Decimal('0.000000')
    complex_place_125.latitude = Decimal('36.815776')
    complex_place_125.longitude = Decimal('137.582676')
    complex_place_125.memo = None
    complex_place_125.name = '河鹿（かじか）'
    complex_place_125.venue = None
    complex_place_125 = importer.save_or_locate(complex_place_125)

    complex_place_126 = Place()
    complex_place_126.address = '富山県黒部市 宇奈月温泉243 '
    complex_place_126.altitude = Decimal('0.000000')
    complex_place_126.latitude = Decimal('36.815775')
    complex_place_126.longitude = Decimal('137.583631')
    complex_place_126.memo = None
    complex_place_126.name = '宇奈月温泉駅'
    complex_place_126.venue = None
    complex_place_126 = importer.save_or_locate(complex_place_126)

    complex_place_127 = Place()
    complex_place_127.address = '富山県黒部市 黒部峡谷口9 '
    complex_place_127.altitude = Decimal('0.000000')
    complex_place_127.latitude = Decimal('36.815025')
    complex_place_127.longitude = Decimal('137.585936')
    complex_place_127.memo = None
    complex_place_127.name = '宇奈月駅'
    complex_place_127.venue = None
    complex_place_127 = importer.save_or_locate(complex_place_127)

    complex_place_128 = Place()
    complex_place_128.address = '富山県黒部市 黒部峡谷口9 '
    complex_place_128.altitude = Decimal('0.000000')
    complex_place_128.latitude = Decimal('36.814287')
    complex_place_128.longitude = Decimal('137.588156')
    complex_place_128.memo = None
    complex_place_128.name = 'やまびこ展望台'
    complex_place_128.venue = None
    complex_place_128 = importer.save_or_locate(complex_place_128)

    complex_place_129 = Place()
    complex_place_129.address = '富山県黒部市 宇奈月温泉6 '
    complex_place_129.altitude = Decimal('0.000000')
    complex_place_129.latitude = Decimal('36.812619')
    complex_place_129.longitude = Decimal('137.590073')
    complex_place_129.memo = None
    complex_place_129.name = 'ホテル黒部'
    complex_place_129.venue = None
    complex_place_129 = importer.save_or_locate(complex_place_129)

    complex_place_130 = Place()
    complex_place_130.address = '群馬県利根郡 みなかみ町 鹿野沢326'
    complex_place_130.altitude = Decimal('0.000000')
    complex_place_130.latitude = Decimal('36.781009')
    complex_place_130.longitude = Decimal('138.969767')
    complex_place_130.memo = None
    complex_place_130.name = '水上駅SL転車台広場'
    complex_place_130.venue = None
    complex_place_130 = importer.save_or_locate(complex_place_130)

    complex_place_131 = Place()
    complex_place_131.address = '群馬県利根郡 みなかみ町 鹿野沢70'
    complex_place_131.altitude = Decimal('0.000000')
    complex_place_131.latitude = Decimal('36.778636')
    complex_place_131.longitude = Decimal('138.968840')
    complex_place_131.memo = None
    complex_place_131.name = '水上駅'
    complex_place_131.venue = None
    complex_place_131 = importer.save_or_locate(complex_place_131)

    complex_place_132 = Place()
    complex_place_132.address = '群馬県利根郡 みなかみ町 小日向416'
    complex_place_132.altitude = Decimal('0.000000')
    complex_place_132.latitude = Decimal('36.764134')
    complex_place_132.longitude = Decimal('138.968798')
    complex_place_132.memo = None
    complex_place_132.name = '足湯'
    complex_place_132.venue = None
    complex_place_132 = importer.save_or_locate(complex_place_132)

    complex_place_133 = Place()
    complex_place_133.address = '茨城県常陸太田市  '
    complex_place_133.altitude = Decimal('0.000000')
    complex_place_133.latitude = Decimal('36.724453')
    complex_place_133.longitude = Decimal('140.509003')
    complex_place_133.memo = None
    complex_place_133.name = '中野屋旅館'
    complex_place_133.venue = None
    complex_place_133 = importer.save_or_locate(complex_place_133)

    complex_place_134 = Place()
    complex_place_134.address = '栃木県那須烏山市 中央三丁目11 '
    complex_place_134.altitude = Decimal('0.000000')
    complex_place_134.latitude = Decimal('36.664258')
    complex_place_134.longitude = Decimal('140.147593')
    complex_place_134.memo = None
    complex_place_134.name = '烏山城跡'
    complex_place_134.venue = None
    complex_place_134 = importer.save_or_locate(complex_place_134)

    complex_place_135 = Place()
    complex_place_135.address = '栃木県那須烏山市 神長140 '
    complex_place_135.altitude = Decimal('0.000000')
    complex_place_135.latitude = Decimal('36.656870')
    complex_place_135.longitude = Decimal('140.138100')
    complex_place_135.memo = None
    complex_place_135.name = 'どうくつ酒造（島崎酒造）'
    complex_place_135.venue = None
    complex_place_135 = importer.save_or_locate(complex_place_135)

    complex_place_136 = Place()
    complex_place_136.address = '栃木県那須烏山市 中央二丁目1 '
    complex_place_136.altitude = Decimal('0.000000')
    complex_place_136.latitude = Decimal('36.655762')
    complex_place_136.longitude = Decimal('140.153683')
    complex_place_136.memo = None
    complex_place_136.name = '(株)島崎酒造'
    complex_place_136.venue = None
    complex_place_136 = importer.save_or_locate(complex_place_136)

    complex_place_137 = Place()
    complex_place_137.address = '栃木県那須烏山市 旭二丁目14 '
    complex_place_137.altitude = Decimal('0.000000')
    complex_place_137.latitude = Decimal('36.652717')
    complex_place_137.longitude = Decimal('140.168464')
    complex_place_137.memo = None
    complex_place_137.name = '烏山大橋'
    complex_place_137.venue = None
    complex_place_137 = importer.save_or_locate(complex_place_137)

    complex_place_138 = Place()
    complex_place_138.address = '栃木県那須烏山市 金井二丁目20 '
    complex_place_138.altitude = Decimal('0.000000')
    complex_place_138.latitude = Decimal('36.650852')
    complex_place_138.longitude = Decimal('140.154528')
    complex_place_138.memo = None
    complex_place_138.name = '福住旅館'
    complex_place_138.venue = None
    complex_place_138 = importer.save_or_locate(complex_place_138)

    complex_place_139 = Place()
    complex_place_139.address = '栃木県那須烏山市 南二丁目4 '
    complex_place_139.altitude = Decimal('0.000000')
    complex_place_139.latitude = Decimal('36.650446')
    complex_place_139.longitude = Decimal('140.155054')
    complex_place_139.memo = None
    complex_place_139.name = '烏山駅'
    complex_place_139.venue = None
    complex_place_139 = importer.save_or_locate(complex_place_139)

    complex_place_140 = Place()
    complex_place_140.address = '栃木県那須烏山市  '
    complex_place_140.altitude = Decimal('0.000000')
    complex_place_140.latitude = Decimal('36.649359')
    complex_place_140.longitude = Decimal('140.185293')
    complex_place_140.memo = None
    complex_place_140.name = 'もり食堂'
    complex_place_140.venue = None
    complex_place_140 = importer.save_or_locate(complex_place_140)

    complex_place_141 = Place()
    complex_place_141.address = '栃木県那須烏山市 滝233 '
    complex_place_141.altitude = Decimal('0.000000')
    complex_place_141.latitude = Decimal('36.648585')
    complex_place_141.longitude = Decimal('140.138194')
    complex_place_141.memo = None
    complex_place_141.name = '滝駅'
    complex_place_141.venue = None
    complex_place_141 = importer.save_or_locate(complex_place_141)

    complex_place_142 = Place()
    complex_place_142.address = '栃木県那須烏山市 滝20 '
    complex_place_142.altitude = Decimal('0.000000')
    complex_place_142.latitude = Decimal('36.645599')
    complex_place_142.longitude = Decimal('140.139814')
    complex_place_142.memo = None
    complex_place_142.name = '龍門の滝'
    complex_place_142.venue = None
    complex_place_142 = importer.save_or_locate(complex_place_142)

    complex_place_143 = Place()
    complex_place_143.address = '栃木県那須烏山市 滝20 '
    complex_place_143.altitude = Decimal('0.000000')
    complex_place_143.latitude = Decimal('36.645550')
    complex_place_143.longitude = Decimal('140.138925')
    complex_place_143.memo = None
    complex_place_143.name = '那須烏山市 龍門ふるさと民芸館'
    complex_place_143.venue = None
    complex_place_143 = importer.save_or_locate(complex_place_143)

    complex_place_144 = Place()
    complex_place_144.address = '茨城県日立市  '
    complex_place_144.altitude = Decimal('0.000000')
    complex_place_144.latitude = Decimal('36.636553')
    complex_place_144.longitude = Decimal('140.545687')
    complex_place_144.memo = None
    complex_place_144.name = 'セブン-イレブン 日立下深荻町店'
    complex_place_144.venue = None
    complex_place_144 = importer.save_or_locate(complex_place_144)

    complex_place_145 = Place()
    complex_place_145.address = '茨城県日立市  '
    complex_place_145.altitude = Decimal('0.000000')
    complex_place_145.latitude = Decimal('36.636081')
    complex_place_145.longitude = Decimal('140.585558')
    complex_place_145.memo = None
    complex_place_145.name = '御岩神社'
    complex_place_145.venue = None
    complex_place_145 = importer.save_or_locate(complex_place_145)

    complex_place_146 = Place()
    complex_place_146.address = '茨城県日立市  '
    complex_place_146.altitude = Decimal('0.000000')
    complex_place_146.latitude = Decimal('36.633874')
    complex_place_146.longitude = Decimal('140.587316')
    complex_place_146.memo = None
    complex_place_146.name = '薩都神社中宮'
    complex_place_146.venue = None
    complex_place_146 = importer.save_or_locate(complex_place_146)

    complex_place_147 = Place()
    complex_place_147.address = '茨城県日立市  '
    complex_place_147.altitude = Decimal('0.000000')
    complex_place_147.latitude = Decimal('36.632579')
    complex_place_147.longitude = Decimal('140.593467')
    complex_place_147.memo = None
    complex_place_147.name = '御岩山'
    complex_place_147.venue = None
    complex_place_147 = importer.save_or_locate(complex_place_147)

    complex_place_148 = Place()
    complex_place_148.address = '茨城県日立市  '
    complex_place_148.altitude = Decimal('0.000000')
    complex_place_148.latitude = Decimal('36.631965')
    complex_place_148.longitude = Decimal('140.590763')
    complex_place_148.memo = None
    complex_place_148.name = '賀毗禮神宮'
    complex_place_148.venue = None
    complex_place_148 = importer.save_or_locate(complex_place_148)

    complex_place_149 = Place()
    complex_place_149.address = '茨城県日立市 旭町一丁目3 '
    complex_place_149.altitude = Decimal('0.000000')
    complex_place_149.latitude = Decimal('36.590685')
    complex_place_149.longitude = Decimal('140.662102')
    complex_place_149.memo = None
    complex_place_149.name = '日立駅'
    complex_place_149.venue = None
    complex_place_149 = importer.save_or_locate(complex_place_149)

    complex_place_150 = Place()
    complex_place_150.address = '茨城県日立市 旭町二丁目3 '
    complex_place_150.altitude = Decimal('0.000000')
    complex_place_150.latitude = Decimal('36.587353')
    complex_place_150.longitude = Decimal('140.661611')
    complex_place_150.memo = None
    complex_place_150.name = '山文魚'
    complex_place_150.venue = None
    complex_place_150 = importer.save_or_locate(complex_place_150)

    complex_place_151 = Place()
    complex_place_151.address = None
    complex_place_151.altitude = Decimal('0.000000')
    complex_place_151.latitude = Decimal('36.584900')
    complex_place_151.longitude = Decimal('140.025900')
    complex_place_151.memo = None
    complex_place_151.name = '第6旅 栃木 (camera)'
    complex_place_151.venue = None
    complex_place_151 = importer.save_or_locate(complex_place_151)

    complex_place_152 = Place()
    complex_place_152.address = '群馬県渋川市  '
    complex_place_152.altitude = Decimal('0.000000')
    complex_place_152.latitude = Decimal('36.581441')
    complex_place_152.longitude = Decimal('139.049501')
    complex_place_152.memo = None
    complex_place_152.name = '綾戸橋'
    complex_place_152.venue = None
    complex_place_152 = importer.save_or_locate(complex_place_152)

    complex_place_153 = Place()
    complex_place_153.address = '茨城県日立市 相賀町14 '
    complex_place_153.altitude = Decimal('0.000000')
    complex_place_153.latitude = Decimal('36.580922')
    complex_place_153.longitude = Decimal('140.661773')
    complex_place_153.memo = None
    complex_place_153.name = '津神社'
    complex_place_153.venue = None
    complex_place_153 = importer.save_or_locate(complex_place_153)

    complex_place_154 = Place()
    complex_place_154.address = '群馬県渋川市 上白井400 '
    complex_place_154.altitude = Decimal('0.000000')
    complex_place_154.latitude = Decimal('36.574905')
    complex_place_154.longitude = Decimal('139.053134')
    complex_place_154.memo = None
    complex_place_154.name = 'ばーちゃん再会の地'
    complex_place_154.venue = None
    complex_place_154 = importer.save_or_locate(complex_place_154)

    complex_place_155 = Place()
    complex_place_155.address = '群馬県渋川市 赤城町棚下 '
    complex_place_155.altitude = Decimal('0.000000')
    complex_place_155.latitude = Decimal('36.571745')
    complex_place_155.longitude = Decimal('139.059677')
    complex_place_155.memo = None
    complex_place_155.name = '棚下不動の滝(雄滝)'
    complex_place_155.venue = None
    complex_place_155 = importer.save_or_locate(complex_place_155)

    complex_place_156 = Place()
    complex_place_156.address = '栃木県宇都宮市 駅前通り三丁目1 '
    complex_place_156.altitude = Decimal('0.000000')
    complex_place_156.latitude = Decimal('36.559023')
    complex_place_156.longitude = Decimal('139.898451')
    complex_place_156.memo = None
    complex_place_156.name = '宇都宮駅'
    complex_place_156.venue = None
    complex_place_156 = importer.save_or_locate(complex_place_156)

    complex_place_157 = Place()
    complex_place_157.address = '茨城県常陸太田市 馬場町90 '
    complex_place_157.altitude = Decimal('0.000000')
    complex_place_157.latitude = Decimal('36.551139')
    complex_place_157.longitude = Decimal('140.530521')
    complex_place_157.memo = None
    complex_place_157.name = 'セイコーマート まいづる店'
    complex_place_157.venue = None
    complex_place_157 = importer.save_or_locate(complex_place_157)

    complex_place_158 = Place()
    complex_place_158.address = '茨城県常陸太田市 馬場町506 '
    complex_place_158.altitude = Decimal('0.000000')
    complex_place_158.latitude = Decimal('36.549282')
    complex_place_158.longitude = Decimal('140.523553')
    complex_place_158.memo = None
    complex_place_158.name = 'いづみや本店'
    complex_place_158.venue = None
    complex_place_158 = importer.save_or_locate(complex_place_158)

    complex_place_159 = Place()
    complex_place_159.address = '茨城県常陸太田市 中城町西鯉沼2991 '
    complex_place_159.altitude = Decimal('0.000000')
    complex_place_159.latitude = Decimal('36.544472')
    complex_place_159.longitude = Decimal('140.530151')
    complex_place_159.memo = None
    complex_place_159.name = 'いづみや東バイパス店'
    complex_place_159.venue = None
    complex_place_159 = importer.save_or_locate(complex_place_159)

    complex_place_160 = Place()
    complex_place_160.address = '茨城県常陸太田市 宮本町288 '
    complex_place_160.altitude = Decimal('0.000000')
    complex_place_160.latitude = Decimal('36.542962')
    complex_place_160.longitude = Decimal('140.520700')
    complex_place_160.memo = None
    complex_place_160.name = '若宮八幡宮'
    complex_place_160.venue = None
    complex_place_160 = importer.save_or_locate(complex_place_160)

    complex_place_161 = Place()
    complex_place_161.address = '茨城県常陸太田市 東一町2283 '
    complex_place_161.altitude = Decimal('0.000000')
    complex_place_161.latitude = Decimal('36.541721')
    complex_place_161.longitude = Decimal('140.523689')
    complex_place_161.memo = None
    complex_place_161.name = '黒澤輪業'
    complex_place_161.venue = None
    complex_place_161 = importer.save_or_locate(complex_place_161)

    complex_place_162 = Place()
    complex_place_162.address = '群馬県渋川市 上白井2796 '
    complex_place_162.altitude = Decimal('0.000000')
    complex_place_162.latitude = Decimal('36.541417')
    complex_place_162.longitude = Decimal('139.033880')
    complex_place_162.memo = None
    complex_place_162.name = '福増寺屋'
    complex_place_162.venue = None
    complex_place_162 = importer.save_or_locate(complex_place_162)

    complex_place_163 = Place()
    complex_place_163.address = '茨城県常陸太田市 東一町2298 '
    complex_place_163.altitude = Decimal('0.000000')
    complex_place_163.latitude = Decimal('36.540732')
    complex_place_163.longitude = Decimal('140.523178')
    complex_place_163.memo = None
    complex_place_163.name = '東通り商店街'
    complex_place_163.venue = None
    complex_place_163 = importer.save_or_locate(complex_place_163)

    complex_place_164 = Place()
    complex_place_164.address = '茨城県常陸太田市 西二町2170 '
    complex_place_164.altitude = Decimal('0.000000')
    complex_place_164.latitude = Decimal('36.540239')
    complex_place_164.longitude = Decimal('140.522472')
    complex_place_164.memo = None
    complex_place_164.name = '常陸太田市郷土資料館'
    complex_place_164.venue = None
    complex_place_164 = importer.save_or_locate(complex_place_164)

    complex_place_165 = Place()
    complex_place_165.address = '茨城県常陸太田市 西三町2129 '
    complex_place_165.altitude = Decimal('0.000000')
    complex_place_165.latitude = Decimal('36.538385')
    complex_place_165.longitude = Decimal('140.523225')
    complex_place_165.memo = None
    complex_place_165.name = '釜平'
    complex_place_165.venue = None
    complex_place_165 = importer.save_or_locate(complex_place_165)

    complex_place_166 = Place()
    complex_place_166.address = '茨城県常陸太田市 木崎二町1949 '
    complex_place_166.altitude = Decimal('0.000000')
    complex_place_166.latitude = Decimal('36.534032')
    complex_place_166.longitude = Decimal('140.525907')
    complex_place_166.memo = None
    complex_place_166.name = '木崎坂'
    complex_place_166.venue = None
    complex_place_166 = importer.save_or_locate(complex_place_166)

    complex_place_167 = Place()
    complex_place_167.address = '茨城県常陸太田市 山下町954 '
    complex_place_167.altitude = Decimal('0.000000')
    complex_place_167.latitude = Decimal('36.531528')
    complex_place_167.longitude = Decimal('140.527906')
    complex_place_167.memo = None
    complex_place_167.name = '常陸太田駅'
    complex_place_167.venue = None
    complex_place_167 = importer.save_or_locate(complex_place_167)

    complex_place_168 = Place()
    complex_place_168.address = '茨城県常陸太田市 山下町977 '
    complex_place_168.altitude = Decimal('0.000000')
    complex_place_168.latitude = Decimal('36.531029')
    complex_place_168.longitude = Decimal('140.527941')
    complex_place_168.memo = None
    complex_place_168.name = '常陸太田市観光案内センター'
    complex_place_168.venue = None
    complex_place_168 = importer.save_or_locate(complex_place_168)

    complex_place_169 = Place()
    complex_place_169.address = None
    complex_place_169.altitude = Decimal('0.000000')
    complex_place_169.latitude = Decimal('36.513300')
    complex_place_169.longitude = Decimal('140.545400')
    complex_place_169.memo = None
    complex_place_169.name = '第16旅 茨城後編 (camera)'
    complex_place_169.venue = None
    complex_place_169 = importer.save_or_locate(complex_place_169)

    complex_place_170 = Place()
    complex_place_170.address = '群馬県渋川市 渋川1655 '
    complex_place_170.altitude = Decimal('0.000000')
    complex_place_170.latitude = Decimal('36.491322')
    complex_place_170.longitude = Decimal('139.008798')
    complex_place_170.memo = None
    complex_place_170.name = '渋川駅'
    complex_place_170.venue = None
    complex_place_170 = importer.save_or_locate(complex_place_170)

    complex_place_171 = Place()
    complex_place_171.address = None
    complex_place_171.altitude = Decimal('0.000000')
    complex_place_171.latitude = Decimal('36.491300')
    complex_place_171.longitude = Decimal('139.008800')
    complex_place_171.memo = None
    complex_place_171.name = '第19旅 群馬後編 (camera)'
    complex_place_171.venue = None
    complex_place_171 = importer.save_or_locate(complex_place_171)

    complex_place_172 = Place()
    complex_place_172.address = '群馬県北群馬郡 吉岡町 漆原2003'
    complex_place_172.altitude = Decimal('0.000000')
    complex_place_172.latitude = Decimal('36.440681')
    complex_place_172.longitude = Decimal('139.038650')
    complex_place_172.memo = None
    complex_place_172.name = '新坂東橋'
    complex_place_172.venue = None
    complex_place_172 = importer.save_or_locate(complex_place_172)

    complex_place_173 = Place()
    complex_place_173.address = '茨城県水戸市 常磐町二丁目8 '
    complex_place_173.altitude = Decimal('0.000000')
    complex_place_173.latitude = Decimal('36.374684')
    complex_place_173.longitude = Decimal('140.456910')
    complex_place_173.memo = None
    complex_place_173.name = '偕楽園・常磐神社前'
    complex_place_173.venue = None
    complex_place_173 = importer.save_or_locate(complex_place_173)

    complex_place_174 = Place()
    complex_place_174.address = '茨城県水戸市 常磐町6031 '
    complex_place_174.altitude = Decimal('0.000000')
    complex_place_174.latitude = Decimal('36.372626')
    complex_place_174.longitude = Decimal('140.452177')
    complex_place_174.memo = None
    complex_place_174.name = '偕楽園'
    complex_place_174.venue = None
    complex_place_174 = importer.save_or_locate(complex_place_174)

    complex_place_175 = Place()
    complex_place_175.address = '茨城県水戸市 宮町一丁目7 '
    complex_place_175.altitude = Decimal('0.000000')
    complex_place_175.latitude = Decimal('36.370733')
    complex_place_175.longitude = Decimal('140.476279')
    complex_place_175.memo = None
    complex_place_175.name = '水戸駅'
    complex_place_175.venue = None
    complex_place_175 = importer.save_or_locate(complex_place_175)

    complex_place_176 = Place()
    complex_place_176.address = '茨城県水戸市 宮町一丁目7 '
    complex_place_176.altitude = Decimal('0.000000')
    complex_place_176.latitude = Decimal('36.369809')
    complex_place_176.longitude = Decimal('140.475811')
    complex_place_176.memo = None
    complex_place_176.name = '水戸の納豆記念碑'
    complex_place_176.venue = None
    complex_place_176 = importer.save_or_locate(complex_place_176)

    complex_place_177 = Place()
    complex_place_177.address = '群馬県太田市 飯塚町1695 '
    complex_place_177.altitude = Decimal('0.000000')
    complex_place_177.latitude = Decimal('36.279206')
    complex_place_177.longitude = Decimal('139.377876')
    complex_place_177.memo = None
    complex_place_177.name = 'ホテルルートイン太田南-国道407号-'
    complex_place_177.venue = None
    complex_place_177 = importer.save_or_locate(complex_place_177)

    complex_place_178 = Place()
    complex_place_178.address = '群馬県太田市 粕川町701 '
    complex_place_178.altitude = Decimal('0.000000')
    complex_place_178.latitude = Decimal('36.264522')
    complex_place_178.longitude = Decimal('139.295997')
    complex_place_178.memo = None
    complex_place_178.name = '道の駅 おおた'
    complex_place_178.venue = None
    complex_place_178 = importer.save_or_locate(complex_place_178)

    complex_place_179 = Place()
    complex_place_179.address = None
    complex_place_179.altitude = Decimal('0.000000')
    complex_place_179.latitude = Decimal('36.120000')
    complex_place_179.longitude = Decimal('138.020000')
    complex_place_179.memo = None
    complex_place_179.name = '第28旅 長野後編 (camera)'
    complex_place_179.venue = None
    complex_place_179 = importer.save_or_locate(complex_place_179)

    complex_place_180 = Place()
    complex_place_180.address = ''
    complex_place_180.altitude = Decimal('0.000000')
    complex_place_180.latitude = Decimal('36.115325')
    complex_place_180.longitude = Decimal('137.945861')
    complex_place_180.memo = None
    complex_place_180.name = 'そば処 桔梗 塩尻駅'
    complex_place_180.venue = None
    complex_place_180 = importer.save_or_locate(complex_place_180)

    complex_place_181 = Place()
    complex_place_181.address = ''
    complex_place_181.altitude = Decimal('0.000000')
    complex_place_181.latitude = Decimal('36.082084')
    complex_place_181.longitude = Decimal('138.082108')
    complex_place_181.memo = None
    complex_place_181.name = '諏訪大社 下社 春宮'
    complex_place_181.venue = None
    complex_place_181 = importer.save_or_locate(complex_place_181)

    complex_place_182 = Place()
    complex_place_182.address = ''
    complex_place_182.altitude = Decimal('0.000000')
    complex_place_182.latitude = Decimal('36.081999')
    complex_place_182.longitude = Decimal('138.081913')
    complex_place_182.memo = None
    complex_place_182.name = '諏訪大社 下社春宮 二之御柱'
    complex_place_182.venue = None
    complex_place_182 = importer.save_or_locate(complex_place_182)

    complex_place_183 = Place()
    complex_place_183.address = ''
    complex_place_183.altitude = Decimal('0.000000')
    complex_place_183.latitude = Decimal('36.081352')
    complex_place_183.longitude = Decimal('138.082015')
    complex_place_183.memo = None
    complex_place_183.name = '諏訪大社 下社春宮 二之鳥居'
    complex_place_183.venue = None
    complex_place_183 = importer.save_or_locate(complex_place_183)

    complex_place_184 = Place()
    complex_place_184.address = ''
    complex_place_184.altitude = Decimal('0.000000')
    complex_place_184.latitude = Decimal('36.081250')
    complex_place_184.longitude = Decimal('138.082047')
    complex_place_184.memo = None
    complex_place_184.name = '打ち込み接ぎの石垣'
    complex_place_184.venue = None
    complex_place_184 = importer.save_or_locate(complex_place_184)

    complex_place_185 = Place()
    complex_place_185.address = ''
    complex_place_185.altitude = Decimal('0.000000')
    complex_place_185.latitude = Decimal('36.081091')
    complex_place_185.longitude = Decimal('138.083240')
    complex_place_185.memo = None
    complex_place_185.name = '今日のお宿はどうします？'
    complex_place_185.venue = None
    complex_place_185 = importer.save_or_locate(complex_place_185)

    complex_place_186 = Place()
    complex_place_186.address = ''
    complex_place_186.altitude = Decimal('0.000000')
    complex_place_186.latitude = Decimal('36.081038')
    complex_place_186.longitude = Decimal('138.084105')
    complex_place_186.memo = None
    complex_place_186.name = '稲荷大明神'
    complex_place_186.venue = None
    complex_place_186 = importer.save_or_locate(complex_place_186)

    complex_place_187 = Place()
    complex_place_187.address = ''
    complex_place_187.altitude = Decimal('0.000000')
    complex_place_187.latitude = Decimal('36.080902')
    complex_place_187.longitude = Decimal('138.083996')
    complex_place_187.memo = None
    complex_place_187.name = '信玄公ゆかりの地'
    complex_place_187.venue = None
    complex_place_187 = importer.save_or_locate(complex_place_187)

    complex_place_188 = Place()
    complex_place_188.address = ''
    complex_place_188.altitude = Decimal('0.000000')
    complex_place_188.latitude = Decimal('36.080286')
    complex_place_188.longitude = Decimal('138.081867')
    complex_place_188.memo = None
    complex_place_188.name = '下馬橋'
    complex_place_188.venue = None
    complex_place_188 = importer.save_or_locate(complex_place_188)

    complex_place_189 = Place()
    complex_place_189.address = ''
    complex_place_189.altitude = Decimal('0.000000')
    complex_place_189.latitude = Decimal('36.077560')
    complex_place_189.longitude = Decimal('138.081326')
    complex_place_189.memo = None
    complex_place_189.name = 'サンコーパン'
    complex_place_189.venue = None
    complex_place_189 = importer.save_or_locate(complex_place_189)

    complex_place_190 = Place()
    complex_place_190.address = None
    complex_place_190.altitude = Decimal('0.000000')
    complex_place_190.latitude = Decimal('36.077000')
    complex_place_190.longitude = Decimal('138.100000')
    complex_place_190.memo = None
    complex_place_190.name = '第28旅 長野前編 (camera)'
    complex_place_190.venue = None
    complex_place_190 = importer.save_or_locate(complex_place_190)

    complex_place_191 = Place()
    complex_place_191.address = ''
    complex_place_191.altitude = Decimal('0.000000')
    complex_place_191.latitude = Decimal('36.076195')
    complex_place_191.longitude = Decimal('138.088470')
    complex_place_191.memo = None
    complex_place_191.name = 'ぎん月'
    complex_place_191.venue = None
    complex_place_191 = importer.save_or_locate(complex_place_191)

    complex_place_192 = Place()
    complex_place_192.address = ''
    complex_place_192.altitude = Decimal('0.000000')
    complex_place_192.latitude = Decimal('36.075914')
    complex_place_192.longitude = Decimal('138.090203')
    complex_place_192.memo = None
    complex_place_192.name = '甲州道中・中山道合流之地'
    complex_place_192.venue = None
    complex_place_192 = importer.save_or_locate(complex_place_192)

    complex_place_193 = Place()
    complex_place_193.address = ''
    complex_place_193.altitude = Decimal('0.000000')
    complex_place_193.latitude = Decimal('36.075349')
    complex_place_193.longitude = Decimal('138.091239')
    complex_place_193.memo = None
    complex_place_193.name = '諏訪大社 下社 秋宮'
    complex_place_193.venue = None
    complex_place_193 = importer.save_or_locate(complex_place_193)

    complex_place_194 = Place()
    complex_place_194.address = ''
    complex_place_194.altitude = Decimal('0.000000')
    complex_place_194.latitude = Decimal('36.075202')
    complex_place_194.longitude = Decimal('138.090985')
    complex_place_194.memo = None
    complex_place_194.name = '吽像（狛犬）'
    complex_place_194.venue = None
    complex_place_194 = importer.save_or_locate(complex_place_194)

    complex_place_195 = Place()
    complex_place_195.address = ''
    complex_place_195.altitude = Decimal('0.000000')
    complex_place_195.latitude = Decimal('36.074982')
    complex_place_195.longitude = Decimal('138.081183')
    complex_place_195.memo = None
    complex_place_195.name = '諏訪大社 下社春宮 大門（一之鳥居）'
    complex_place_195.venue = None
    complex_place_195 = importer.save_or_locate(complex_place_195)

    complex_place_196 = Place()
    complex_place_196.address = ''
    complex_place_196.altitude = Decimal('0.000000')
    complex_place_196.latitude = Decimal('36.074887')
    complex_place_196.longitude = Decimal('138.090317')
    complex_place_196.memo = None
    complex_place_196.name = '鳥居'
    complex_place_196.venue = None
    complex_place_196 = importer.save_or_locate(complex_place_196)

    complex_place_197 = Place()
    complex_place_197.address = ''
    complex_place_197.altitude = Decimal('0.000000')
    complex_place_197.latitude = Decimal('36.074809')
    complex_place_197.longitude = Decimal('138.090720')
    complex_place_197.memo = None
    complex_place_197.name = '御神湯'
    complex_place_197.venue = None
    complex_place_197 = importer.save_or_locate(complex_place_197)

    complex_place_198 = Place()
    complex_place_198.address = ''
    complex_place_198.altitude = Decimal('0.000000')
    complex_place_198.latitude = Decimal('36.074517')
    complex_place_198.longitude = Decimal('138.084962')
    complex_place_198.memo = None
    complex_place_198.name = 'ほうほう'
    complex_place_198.venue = None
    complex_place_198 = importer.save_or_locate(complex_place_198)

    complex_place_199 = Place()
    complex_place_199.address = ''
    complex_place_199.altitude = Decimal('0.000000')
    complex_place_199.latitude = Decimal('36.074449')
    complex_place_199.longitude = Decimal('138.081009')
    complex_place_199.memo = None
    complex_place_199.name = '大石灯籠'
    complex_place_199.venue = None
    complex_place_199 = importer.save_or_locate(complex_place_199)

    complex_place_200 = Place()
    complex_place_200.address = ''
    complex_place_200.altitude = Decimal('0.000000')
    complex_place_200.latitude = Decimal('36.074368')
    complex_place_200.longitude = Decimal('138.083358')
    complex_place_200.memo = None
    complex_place_200.name = 'あと・・・'
    complex_place_200.venue = None
    complex_place_200 = importer.save_or_locate(complex_place_200)

    complex_place_201 = Place()
    complex_place_201.address = ''
    complex_place_201.altitude = Decimal('0.000000')
    complex_place_201.latitude = Decimal('36.074264')
    complex_place_201.longitude = Decimal('138.082846')
    complex_place_201.memo = None
    complex_place_201.name = '魁塚(相楽塚)'
    complex_place_201.venue = None
    complex_place_201 = importer.save_or_locate(complex_place_201)

    complex_place_202 = Place()
    complex_place_202.address = ''
    complex_place_202.altitude = Decimal('0.000000')
    complex_place_202.latitude = Decimal('36.071984')
    complex_place_202.longitude = Decimal('138.085061')
    complex_place_202.memo = None
    complex_place_202.name = '下諏訪駅'
    complex_place_202.venue = None
    complex_place_202 = importer.save_or_locate(complex_place_202)

    complex_place_203 = Place()
    complex_place_203.address = ''
    complex_place_203.altitude = Decimal('0.000000')
    complex_place_203.latitude = Decimal('36.065770')
    complex_place_203.longitude = Decimal('138.102263')
    complex_place_203.memo = None
    complex_place_203.name = '諏訪湖'
    complex_place_203.venue = None
    complex_place_203 = importer.save_or_locate(complex_place_203)

    complex_place_204 = Place()
    complex_place_204.address = ''
    complex_place_204.altitude = Decimal('0.000000')
    complex_place_204.latitude = Decimal('36.062089')
    complex_place_204.longitude = Decimal('138.106104')
    complex_place_204.memo = None
    complex_place_204.name = 'だから'
    complex_place_204.venue = None
    complex_place_204 = importer.save_or_locate(complex_place_204)

    complex_place_205 = Place()
    complex_place_205.address = '東京都西多摩郡 奥多摩町 '
    complex_place_205.altitude = Decimal('0.000000')
    complex_place_205.latitude = Decimal('35.814941')
    complex_place_205.longitude = Decimal('139.128745')
    complex_place_205.memo = None
    complex_place_205.name = '鳩ノ巣駅'
    complex_place_205.venue = None
    complex_place_205 = importer.save_or_locate(complex_place_205)

    complex_place_206 = Place()
    complex_place_206.address = '東京都西多摩郡 奥多摩町 白丸'
    complex_place_206.altitude = Decimal('0.000000')
    complex_place_206.latitude = Decimal('35.811076')
    complex_place_206.longitude = Decimal('139.123941')
    complex_place_206.memo = None
    complex_place_206.name = '白丸調整池ダム'
    complex_place_206.venue = None
    complex_place_206 = importer.save_or_locate(complex_place_206)

    complex_place_207 = Place()
    complex_place_207.address = '東京都西多摩郡 奥多摩町 '
    complex_place_207.altitude = Decimal('0.000000')
    complex_place_207.latitude = Decimal('35.809374')
    complex_place_207.longitude = Decimal('139.096929')
    complex_place_207.memo = None
    complex_place_207.name = '奥多摩駅'
    complex_place_207.venue = None
    complex_place_207 = importer.save_or_locate(complex_place_207)

    complex_place_208 = Place()
    complex_place_208.address = '東京都西多摩郡 奥多摩町 白丸'
    complex_place_208.altitude = Decimal('0.000000')
    complex_place_208.latitude = Decimal('35.808503')
    complex_place_208.longitude = Decimal('139.113890')
    complex_place_208.memo = None
    complex_place_208.name = '数馬隧道'
    complex_place_208.venue = None
    complex_place_208 = importer.save_or_locate(complex_place_208)

    complex_place_209 = Place()
    complex_place_209.address = '東京都西多摩郡 奥多摩町 白丸'
    complex_place_209.altitude = Decimal('0.000000')
    complex_place_209.latitude = Decimal('35.808468')
    complex_place_209.longitude = Decimal('139.113526')
    complex_place_209.memo = None
    complex_place_209.name = '数馬の切通し'
    complex_place_209.venue = None
    complex_place_209 = importer.save_or_locate(complex_place_209)

    complex_place_210 = Place()
    complex_place_210.address = '東京都西多摩郡 奥多摩町 '
    complex_place_210.altitude = Decimal('0.000000')
    complex_place_210.latitude = Decimal('35.806077')
    complex_place_210.longitude = Decimal('139.099594')
    complex_place_210.memo = None
    complex_place_210.name = '山城屋 奥多摩わさび本舗'
    complex_place_210.venue = None
    complex_place_210 = importer.save_or_locate(complex_place_210)

    complex_place_211 = Place()
    complex_place_211.address = '東京都西多摩郡 奥多摩町 '
    complex_place_211.altitude = Decimal('0.000000')
    complex_place_211.latitude = Decimal('35.805772')
    complex_place_211.longitude = Decimal('139.101139')
    complex_place_211.memo = None
    complex_place_211.name = 'もえぎ橋'
    complex_place_211.venue = None
    complex_place_211 = importer.save_or_locate(complex_place_211)

    complex_place_212 = Place()
    complex_place_212.address = '東京都西多摩郡 奥多摩町 '
    complex_place_212.altitude = Decimal('0.000000')
    complex_place_212.latitude = Decimal('35.804837')
    complex_place_212.longitude = Decimal('139.097475')
    complex_place_212.memo = None
    complex_place_212.name = '愛宕神社階段'
    complex_place_212.venue = None
    complex_place_212 = importer.save_or_locate(complex_place_212)

    complex_place_213 = Place()
    complex_place_213.address = '東京都西多摩郡 奥多摩町 '
    complex_place_213.altitude = Decimal('0.000000')
    complex_place_213.latitude = Decimal('35.804616')
    complex_place_213.longitude = Decimal('139.102613')
    complex_place_213.memo = None
    complex_place_213.name = '奥多摩温泉 もえぎの湯'
    complex_place_213.venue = None
    complex_place_213 = importer.save_or_locate(complex_place_213)

    complex_place_214 = Place()
    complex_place_214.address = '埼玉県川口市 本町一丁目9 '
    complex_place_214.altitude = Decimal('0.000000')
    complex_place_214.latitude = Decimal('35.794038')
    complex_place_214.longitude = Decimal('139.726045')
    complex_place_214.memo = None
    complex_place_214.name = '埼玉突入'
    complex_place_214.venue = None
    complex_place_214 = importer.save_or_locate(complex_place_214)

    complex_place_215 = Place()
    complex_place_215.address = '東京都青梅市 本町131 '
    complex_place_215.altitude = Decimal('0.000000')
    complex_place_215.latitude = Decimal('35.790497')
    complex_place_215.longitude = Decimal('139.258300')
    complex_place_215.memo = None
    complex_place_215.name = '青梅駅'
    complex_place_215.venue = None
    complex_place_215 = importer.save_or_locate(complex_place_215)

    complex_place_216 = Place()
    complex_place_216.address = '東京都西多摩郡 奥多摩町 境'
    complex_place_216.altitude = Decimal('0.000000')
    complex_place_216.latitude = Decimal('35.789492')
    complex_place_216.longitude = Decimal('139.052035')
    complex_place_216.memo = None
    complex_place_216.name = '小河内ダム'
    complex_place_216.venue = None
    complex_place_216 = importer.save_or_locate(complex_place_216)

    complex_place_217 = Place()
    complex_place_217.address = '東京都西多摩郡 奥多摩町 '
    complex_place_217.altitude = Decimal('0.000000')
    complex_place_217.latitude = Decimal('35.789486')
    complex_place_217.longitude = Decimal('139.047093')
    complex_place_217.memo = None
    complex_place_217.name = '奥多摩湖'
    complex_place_217.venue = None
    complex_place_217 = importer.save_or_locate(complex_place_217)

    complex_place_218 = Place()
    complex_place_218.address = None
    complex_place_218.altitude = Decimal('0.000000')
    complex_place_218.latitude = Decimal('35.777400')
    complex_place_218.longitude = Decimal('139.151000')
    complex_place_218.memo = None
    complex_place_218.name = '第14旅 奥多摩 (camera)'
    complex_place_218.venue = None
    complex_place_218 = importer.save_or_locate(complex_place_218)

    complex_place_219 = Place()
    complex_place_219.address = '東京都北区 滝野川二丁目4 '
    complex_place_219.altitude = Decimal('0.000000')
    complex_place_219.latitude = Decimal('35.751929')
    complex_place_219.longitude = Decimal('139.736434')
    complex_place_219.memo = None
    complex_place_219.name = '路面電車'
    complex_place_219.venue = None
    complex_place_219 = importer.save_or_locate(complex_place_219)

    complex_place_220 = Place()
    complex_place_220.address = '東京都文京区 後楽一丁目3 '
    complex_place_220.altitude = Decimal('0.000000')
    complex_place_220.latitude = Decimal('35.703667')
    complex_place_220.longitude = Decimal('139.753393')
    complex_place_220.memo = None
    complex_place_220.name = '東京ドームホテル'
    complex_place_220.venue = None
    complex_place_220 = importer.save_or_locate(complex_place_220)

    complex_place_221 = Place()
    complex_place_221.address = '東京都三鷹市 井の頭四丁目1 '
    complex_place_221.altitude = Decimal('0.000000')
    complex_place_221.latitude = Decimal('35.700108')
    complex_place_221.longitude = Decimal('139.576034')
    complex_place_221.memo = None
    complex_place_221.name = '井の頭恩賜公園'
    complex_place_221.venue = None
    complex_place_221 = importer.save_or_locate(complex_place_221)

    complex_place_222 = Place()
    complex_place_222.address = '東京都立川市 柴崎町三丁目1 '
    complex_place_222.altitude = Decimal('0.000000')
    complex_place_222.latitude = Decimal('35.697914')
    complex_place_222.longitude = Decimal('139.413741')
    complex_place_222.memo = None
    complex_place_222.name = '立川駅'
    complex_place_222.venue = None
    complex_place_222 = importer.save_or_locate(complex_place_222)

    complex_place_223 = Place()
    complex_place_223.address = '東京都千代田区 富士見二丁目13 '
    complex_place_223.altitude = Decimal('0.000000')
    complex_place_223.latitude = Decimal('35.697847')
    complex_place_223.longitude = Decimal('139.744247')
    complex_place_223.memo = None
    complex_place_223.name = '角川第2本社ビル'
    complex_place_223.venue = None
    complex_place_223 = importer.save_or_locate(complex_place_223)

    complex_place_224 = Place()
    complex_place_224.address = '東京都千代田区 神田須田町二丁目8 '
    complex_place_224.altitude = Decimal('0.000000')
    complex_place_224.latitude = Decimal('35.695639')
    complex_place_224.longitude = Decimal('139.774183')
    complex_place_224.memo = None
    complex_place_224.name = '矢印いっぱい'
    complex_place_224.venue = None
    complex_place_224 = importer.save_or_locate(complex_place_224)

    complex_place_225 = Place()
    complex_place_225.address = '東京都新宿区 西新宿二丁目8 '
    complex_place_225.altitude = Decimal('0.000000')
    complex_place_225.latitude = Decimal('35.689634')
    complex_place_225.longitude = Decimal('139.692101')
    complex_place_225.memo = None
    complex_place_225.name = '東京都庁'
    complex_place_225.venue = None
    complex_place_225 = importer.save_or_locate(complex_place_225)

    complex_place_226 = Place()
    complex_place_226.address = '東京都渋谷区 本町三丁目9 '
    complex_place_226.altitude = Decimal('0.000000')
    complex_place_226.latitude = Decimal('35.689114')
    complex_place_226.longitude = Decimal('139.683008')
    complex_place_226.memo = None
    complex_place_226.name = '都庁からさらに西へ・・・'
    complex_place_226.venue = None
    complex_place_226 = importer.save_or_locate(complex_place_226)

    complex_place_227 = Place()
    complex_place_227.address = '東京都渋谷区 本町三丁目11 '
    complex_place_227.altitude = Decimal('0.000000')
    complex_place_227.latitude = Decimal('35.688807')
    complex_place_227.longitude = Decimal('139.682698')
    complex_place_227.memo = None
    complex_place_227.name = '清水橋跡'
    complex_place_227.venue = None
    complex_place_227 = importer.save_or_locate(complex_place_227)

    complex_place_228 = Place()
    complex_place_228.address = '東京都新宿区 西新宿二丁目9 '
    complex_place_228.altitude = Decimal('0.000000')
    complex_place_228.latitude = Decimal('35.688657')
    complex_place_228.longitude = Decimal('139.691563')
    complex_place_228.memo = None
    complex_place_228.name = 'なんだこれ？'
    complex_place_228.venue = None
    complex_place_228 = importer.save_or_locate(complex_place_228)

    complex_place_229 = Place()
    complex_place_229.address = '東京都渋谷区 本町四丁目12 '
    complex_place_229.altitude = Decimal('0.000000')
    complex_place_229.latitude = Decimal('35.687905')
    complex_place_229.longitude = Decimal('139.681069')
    complex_place_229.memo = None
    complex_place_229.name = '二軒家橋跡'
    complex_place_229.venue = None
    complex_place_229 = importer.save_or_locate(complex_place_229)

    complex_place_230 = Place()
    complex_place_230.address = '東京都渋谷区 本町四丁目10 '
    complex_place_230.altitude = Decimal('0.000000')
    complex_place_230.latitude = Decimal('35.687014')
    complex_place_230.longitude = Decimal('139.680175')
    complex_place_230.memo = None
    complex_place_230.name = '村木橋跡'
    complex_place_230.venue = None
    complex_place_230 = importer.save_or_locate(complex_place_230)

    complex_place_231 = Place()
    complex_place_231.address = '東京都新宿区 西新宿三丁目15 '
    complex_place_231.altitude = Decimal('0.000000')
    complex_place_231.latitude = Decimal('35.683931')
    complex_place_231.longitude = Decimal('139.690806')
    complex_place_231.memo = None
    complex_place_231.name = '大都会味ある'
    complex_place_231.venue = None
    complex_place_231 = importer.save_or_locate(complex_place_231)

    complex_place_232 = Place()
    complex_place_232.address = '東京都千代田区 皇居外苑2 '
    complex_place_232.altitude = Decimal('0.000000')
    complex_place_232.latitude = Decimal('35.682744')
    complex_place_232.longitude = Decimal('139.757805')
    complex_place_232.memo = None
    complex_place_232.name = '皇居の石垣 その2'
    complex_place_232.venue = None
    complex_place_232 = importer.save_or_locate(complex_place_232)

    complex_place_233 = Place()
    complex_place_233.address = '東京都千代田区 丸の内一丁目5 '
    complex_place_233.altitude = Decimal('0.000000')
    complex_place_233.latitude = Decimal('35.682621')
    complex_place_233.longitude = Decimal('139.764244')
    complex_place_233.memo = None
    complex_place_233.name = '新丸の内ビルディング'
    complex_place_233.venue = None
    complex_place_233 = importer.save_or_locate(complex_place_233)

    complex_place_234 = Place()
    complex_place_234.address = '東京都千代田区 皇居外苑3 '
    complex_place_234.altitude = Decimal('0.000000')
    complex_place_234.latitude = Decimal('35.682064')
    complex_place_234.longitude = Decimal('139.761186')
    complex_place_234.memo = None
    complex_place_234.name = '皇居の石垣'
    complex_place_234.venue = None
    complex_place_234 = importer.save_or_locate(complex_place_234)

    complex_place_235 = Place()
    complex_place_235.address = '東京都千代田区 丸の内一丁目9 '
    complex_place_235.altitude = Decimal('0.000000')
    complex_place_235.latitude = Decimal('35.681236')
    complex_place_235.longitude = Decimal('139.767125')
    complex_place_235.memo = None
    complex_place_235.name = '東京駅'
    complex_place_235.venue = None
    complex_place_235 = importer.save_or_locate(complex_place_235)

    complex_place_236 = Place()
    complex_place_236.address = '東京都渋谷区 千駄ケ谷一丁目35 '
    complex_place_236.altitude = Decimal('0.000000')
    complex_place_236.latitude = Decimal('35.681100')
    complex_place_236.longitude = Decimal('139.711282')
    complex_place_236.memo = None
    complex_place_236.name = '千駄ヶ谷駅'
    complex_place_236.venue = None
    complex_place_236 = importer.save_or_locate(complex_place_236)

    complex_place_237 = Place()
    complex_place_237.address = '東京都千代田区 丸の内二丁目4 '
    complex_place_237.altitude = Decimal('0.000000')
    complex_place_237.latitude = Decimal('35.681040')
    complex_place_237.longitude = Decimal('139.763803')
    complex_place_237.memo = None
    complex_place_237.name = '丸の内ビルディング'
    complex_place_237.venue = None
    complex_place_237 = importer.save_or_locate(complex_place_237)

    complex_place_238 = Place()
    complex_place_238.address = None
    complex_place_238.altitude = Decimal('0.000000')
    complex_place_238.latitude = Decimal('35.680800')
    complex_place_238.longitude = Decimal('139.670300')
    complex_place_238.memo = None
    complex_place_238.name = '第19旅 前編 (camera)'
    complex_place_238.venue = None
    complex_place_238 = importer.save_or_locate(complex_place_238)

    complex_place_239 = Place()
    complex_place_239.address = '東京都千代田区 皇居外苑2 '
    complex_place_239.altitude = Decimal('0.000000')
    complex_place_239.latitude = Decimal('35.680215')
    complex_place_239.longitude = Decimal('139.753598')
    complex_place_239.memo = None
    complex_place_239.name = '二重橋'
    complex_place_239.venue = None
    complex_place_239 = importer.save_or_locate(complex_place_239)

    complex_place_240 = Place()
    complex_place_240.address = '東京都渋谷区 代々木神園町4 '
    complex_place_240.altitude = Decimal('0.000000')
    complex_place_240.latitude = Decimal('35.679111')
    complex_place_240.longitude = Decimal('139.694663')
    complex_place_240.memo = None
    complex_place_240.name = '東京乗馬倶楽部'
    complex_place_240.venue = None
    complex_place_240 = importer.save_or_locate(complex_place_240)

    complex_place_241 = Place()
    complex_place_241.address = '東京都渋谷区 代々木一丁目1 '
    complex_place_241.altitude = Decimal('0.000000')
    complex_place_241.latitude = Decimal('35.678982')
    complex_place_241.longitude = Decimal('139.702120')
    complex_place_241.memo = None
    complex_place_241.name = '北参道 鳥居'
    complex_place_241.venue = None
    complex_place_241 = importer.save_or_locate(complex_place_241)

    complex_place_242 = Place()
    complex_place_242.address = '東京都千代田区 紀尾井町1 '
    complex_place_242.altitude = Decimal('0.000000')
    complex_place_242.latitude = Decimal('35.678842')
    complex_place_242.longitude = Decimal('139.736270')
    complex_place_242.memo = None
    complex_place_242.name = '弁慶橋'
    complex_place_242.venue = None
    complex_place_242 = importer.save_or_locate(complex_place_242)

    complex_place_243 = Place()
    complex_place_243.address = '東京都千代田区 皇居外苑1 '
    complex_place_243.altitude = Decimal('0.000000')
    complex_place_243.latitude = Decimal('35.678503')
    complex_place_243.longitude = Decimal('139.753638')
    complex_place_243.memo = None
    complex_place_243.name = '桜田門'
    complex_place_243.venue = None
    complex_place_243 = importer.save_or_locate(complex_place_243)

    complex_place_244 = Place()
    complex_place_244.address = '東京都千代田区 永田町一丁目10 '
    complex_place_244.altitude = Decimal('0.000000')
    complex_place_244.latitude = Decimal('35.678467')
    complex_place_244.longitude = Decimal('139.744220')
    complex_place_244.memo = None
    complex_place_244.name = '国立国会図書館'
    complex_place_244.venue = None
    complex_place_244 = importer.save_or_locate(complex_place_244)

    complex_place_245 = Place()
    complex_place_245.address = '東京都港区 赤坂三丁目1 '
    complex_place_245.altitude = Decimal('0.000000')
    complex_place_245.latitude = Decimal('35.677957')
    complex_place_245.longitude = Decimal('139.736557')
    complex_place_245.memo = None
    complex_place_245.name = '都道405号線（外堀通り）'
    complex_place_245.venue = None
    complex_place_245 = importer.save_or_locate(complex_place_245)

    complex_place_246 = Place()
    complex_place_246.address = '東京都千代田区 霞が関一丁目1 '
    complex_place_246.altitude = Decimal('0.000000')
    complex_place_246.latitude = Decimal('35.677488')
    complex_place_246.longitude = Decimal('139.751983')
    complex_place_246.memo = None
    complex_place_246.name = 'い"い”い”い”っ'
    complex_place_246.venue = None
    complex_place_246 = importer.save_or_locate(complex_place_246)

    complex_place_247 = Place()
    complex_place_247.address = '東京都千代田区 霞が関一丁目1 '
    complex_place_247.altitude = Decimal('0.000000')
    complex_place_247.latitude = Decimal('35.677126')
    complex_place_247.longitude = Decimal('139.752463')
    complex_place_247.memo = None
    complex_place_247.name = '警視庁本部'
    complex_place_247.venue = None
    complex_place_247 = importer.save_or_locate(complex_place_247)

    complex_place_248 = Place()
    complex_place_248.address = '東京都中央区 京橋二丁目4 '
    complex_place_248.altitude = Decimal('0.000000')
    complex_place_248.latitude = Decimal('35.676719')
    complex_place_248.longitude = Decimal('139.769655')
    complex_place_248.memo = None
    complex_place_248.name = '京橋第一生命ビルディング'
    complex_place_248.venue = None
    complex_place_248 = importer.save_or_locate(complex_place_248)

    complex_place_249 = Place()
    complex_place_249.address = '東京都千代田区 永田町一丁目7 '
    complex_place_249.altitude = Decimal('0.000000')
    complex_place_249.latitude = Decimal('35.675888')
    complex_place_249.longitude = Decimal('139.744858')
    complex_place_249.memo = None
    complex_place_249.name = '国会議事堂'
    complex_place_249.venue = None
    complex_place_249 = importer.save_or_locate(complex_place_249)

    complex_place_250 = Place()
    complex_place_250.address = '東京都中央区 京橋三丁目8 '
    complex_place_250.altitude = Decimal('0.000000')
    complex_place_250.latitude = Decimal('35.675434')
    complex_place_250.longitude = Decimal('139.771113')
    complex_place_250.memo = None
    complex_place_250.name = '小原鐵五郎寿像'
    complex_place_250.venue = None
    complex_place_250 = importer.save_or_locate(complex_place_250)

    complex_place_251 = Place()
    complex_place_251.address = '東京都渋谷区 代々木神園町1 '
    complex_place_251.altitude = Decimal('0.000000')
    complex_place_251.latitude = Decimal('35.675414')
    complex_place_251.longitude = Decimal('139.699461')
    complex_place_251.memo = None
    complex_place_251.name = '南神門'
    complex_place_251.venue = None
    complex_place_251 = importer.save_or_locate(complex_place_251)

    complex_place_252 = Place()
    complex_place_252.address = '東京都杉並区 和泉二丁目14 '
    complex_place_252.altitude = Decimal('0.000000')
    complex_place_252.latitude = Decimal('35.673117')
    complex_place_252.longitude = Decimal('139.647872')
    complex_place_252.memo = None
    complex_place_252.name = '普通の街という感じ・・・'
    complex_place_252.venue = None
    complex_place_252 = importer.save_or_locate(complex_place_252)

    complex_place_253 = Place()
    complex_place_253.address = '山梨県韮崎市 龍岡町下條南割517 '
    complex_place_253.altitude = Decimal('0.000000')
    complex_place_253.latitude = Decimal('35.671853')
    complex_place_253.longitude = Decimal('138.456501')
    complex_place_253.memo = None
    complex_place_253.name = '竜岡将棋頭'
    complex_place_253.venue = None
    complex_place_253 = importer.save_or_locate(complex_place_253)

    complex_place_254 = Place()
    complex_place_254.address = '東京都中央区 新川二丁目32 '
    complex_place_254.altitude = Decimal('0.000000')
    complex_place_254.latitude = Decimal('35.671794')
    complex_place_254.longitude = Decimal('139.784375')
    complex_place_254.memo = None
    complex_place_254.name = '中央大橋'
    complex_place_254.venue = None
    complex_place_254 = importer.save_or_locate(complex_place_254)

    complex_place_255 = Place()
    complex_place_255.address = '東京都杉並区 和泉二丁目8 '
    complex_place_255.altitude = Decimal('0.000000')
    complex_place_255.latitude = Decimal('35.671322')
    complex_place_255.longitude = Decimal('139.651149')
    complex_place_255.memo = None
    complex_place_255.name = '杉並区立玉川上水公園'
    complex_place_255.venue = None
    complex_place_255 = importer.save_or_locate(complex_place_255)

    complex_place_256 = Place()
    complex_place_256.address = '東京都杉並区 和泉二丁目10 '
    complex_place_256.altitude = Decimal('0.000000')
    complex_place_256.latitude = Decimal('35.671208')
    complex_place_256.longitude = Decimal('139.649936')
    complex_place_256.memo = None
    complex_place_256.name = '東京山手急行電鉄跡'
    complex_place_256.venue = None
    complex_place_256 = importer.save_or_locate(complex_place_256)

    complex_place_257 = Place()
    complex_place_257.address = '山梨県南アルプス市 野牛島16 '
    complex_place_257.altitude = Decimal('0.000000')
    complex_place_257.latitude = Decimal('35.668991')
    complex_place_257.longitude = Decimal('138.479074')
    complex_place_257.memo = None
    complex_place_257.name = '南アルプス市 ふるさと文化伝承館'
    complex_place_257.venue = None
    complex_place_257 = importer.save_or_locate(complex_place_257)

    complex_place_258 = Place()
    complex_place_258.address = '山梨県甲斐市 竜王新町464 '
    complex_place_258.altitude = Decimal('0.000000')
    complex_place_258.latitude = Decimal('35.668708')
    complex_place_258.longitude = Decimal('138.519373')
    complex_place_258.memo = None
    complex_place_258.name = '竜王駅'
    complex_place_258.venue = None
    complex_place_258 = importer.save_or_locate(complex_place_258)

    complex_place_259 = Place()
    complex_place_259.address = '山梨県甲斐市 竜王1875 '
    complex_place_259.altitude = Decimal('0.000000')
    complex_place_259.latitude = Decimal('35.668456')
    complex_place_259.longitude = Decimal('138.502243')
    complex_place_259.memo = None
    complex_place_259.name = '三社神社石鳥居'
    complex_place_259.venue = None
    complex_place_259 = importer.save_or_locate(complex_place_259)

    complex_place_260 = Place()
    complex_place_260.address = '山梨県甲斐市 竜王86 '
    complex_place_260.altitude = Decimal('0.000000')
    complex_place_260.latitude = Decimal('35.668261')
    complex_place_260.longitude = Decimal('138.501376')
    complex_place_260.memo = None
    complex_place_260.name = '信玄堤'
    complex_place_260.venue = None
    complex_place_260 = importer.save_or_locate(complex_place_260)

    complex_place_261 = Place()
    complex_place_261.address = '山梨県甲斐市 竜王1047 '
    complex_place_261.altitude = Decimal('0.000000')
    complex_place_261.latitude = Decimal('35.667865')
    complex_place_261.longitude = Decimal('138.507842')
    complex_place_261.memo = None
    complex_place_261.name = '竜王北小学校前横断歩道橋'
    complex_place_261.venue = None
    complex_place_261 = importer.save_or_locate(complex_place_261)

    complex_place_262 = Place()
    complex_place_262.address = '山梨県甲斐市 竜王490 '
    complex_place_262.altitude = Decimal('0.000000')
    complex_place_262.latitude = Decimal('35.667718')
    complex_place_262.longitude = Decimal('138.504325')
    complex_place_262.memo = None
    complex_place_262.name = '信玄堤散策コース'
    complex_place_262.venue = None
    complex_place_262 = importer.save_or_locate(complex_place_262)

    complex_place_263 = Place()
    complex_place_263.address = '山梨県甲斐市 竜王1891 '
    complex_place_263.altitude = Decimal('0.000000')
    complex_place_263.latitude = Decimal('35.667445')
    complex_place_263.longitude = Decimal('138.501998')
    complex_place_263.memo = None
    complex_place_263.name = '信玄堤公園'
    complex_place_263.venue = None
    complex_place_263 = importer.save_or_locate(complex_place_263)

    complex_place_264 = Place()
    complex_place_264.address = '東京都港区 六本木二丁目2 '
    complex_place_264.altitude = Decimal('0.000000')
    complex_place_264.latitude = Decimal('35.667438')
    complex_place_264.longitude = Decimal('139.739292')
    complex_place_264.memo = None
    complex_place_264.name = '道路多いっ'
    complex_place_264.venue = None
    complex_place_264 = importer.save_or_locate(complex_place_264)

    complex_place_265 = Place()
    complex_place_265.address = '山梨県甲府市 丸の内一丁目3 '
    complex_place_265.altitude = Decimal('0.000000')
    complex_place_265.latitude = Decimal('35.667098')
    complex_place_265.longitude = Decimal('138.569063')
    complex_place_265.memo = None
    complex_place_265.name = '甲府駅'
    complex_place_265.venue = None
    complex_place_265 = importer.save_or_locate(complex_place_265)

    complex_place_266 = Place()
    complex_place_266.address = '山梨県甲府市 丸の内二丁目1 '
    complex_place_266.altitude = Decimal('0.000000')
    complex_place_266.latitude = Decimal('35.666825')
    complex_place_266.longitude = Decimal('138.568019')
    complex_place_266.memo = None
    complex_place_266.name = '武田信玄公之像'
    complex_place_266.venue = None
    complex_place_266 = importer.save_or_locate(complex_place_266)

    complex_place_267 = Place()
    complex_place_267.address = '山梨県甲斐市 竜王新町335 '
    complex_place_267.altitude = Decimal('0.000000')
    complex_place_267.latitude = Decimal('35.666711')
    complex_place_267.longitude = Decimal('138.518088')
    complex_place_267.memo = None
    complex_place_267.name = '新町下公民館'
    complex_place_267.venue = None
    complex_place_267 = importer.save_or_locate(complex_place_267)

    complex_place_268 = Place()
    complex_place_268.address = '山梨県甲斐市 竜王新町6 '
    complex_place_268.altitude = Decimal('0.000000')
    complex_place_268.latitude = Decimal('35.666654')
    complex_place_268.longitude = Decimal('138.517730')
    complex_place_268.memo = None
    complex_place_268.name = '道祖神'
    complex_place_268.venue = None
    complex_place_268 = importer.save_or_locate(complex_place_268)

    complex_place_269 = Place()
    complex_place_269.address = '東京都中央区 築地三丁目15 '
    complex_place_269.altitude = Decimal('0.000000')
    complex_place_269.latitude = Decimal('35.666486')
    complex_place_269.longitude = Decimal('139.772284')
    complex_place_269.memo = None
    complex_place_269.name = '築地本願寺'
    complex_place_269.venue = None
    complex_place_269 = importer.save_or_locate(complex_place_269)

    complex_place_270 = Place()
    complex_place_270.address = '東京都中央区 月島一丁目8 '
    complex_place_270.altitude = Decimal('0.000000')
    complex_place_270.latitude = Decimal('35.664755')
    complex_place_270.longitude = Decimal('139.783365')
    complex_place_270.memo = None
    complex_place_270.name = '月島もんじゃ振興会協同組合'
    complex_place_270.venue = None
    complex_place_270 = importer.save_or_locate(complex_place_270)

    complex_place_271 = Place()
    complex_place_271.address = '山梨県甲斐市 竜王2089 '
    complex_place_271.altitude = Decimal('0.000000')
    complex_place_271.latitude = Decimal('35.664128')
    complex_place_271.longitude = Decimal('138.502834')
    complex_place_271.memo = None
    complex_place_271.name = '信玄橋'
    complex_place_271.venue = None
    complex_place_271 = importer.save_or_locate(complex_place_271)

    complex_place_272 = Place()
    complex_place_272.address = '東京都中央区 月島三丁目4 '
    complex_place_272.altitude = Decimal('0.000000')
    complex_place_272.latitude = Decimal('35.663578')
    complex_place_272.longitude = Decimal('139.781348')
    complex_place_272.memo = None
    complex_place_272.name = '月島警察署 西仲通地域安全センター'
    complex_place_272.venue = None
    complex_place_272 = importer.save_or_locate(complex_place_272)

    complex_place_273 = Place()
    complex_place_273.address = None
    complex_place_273.altitude = Decimal('0.000000')
    complex_place_273.latitude = Decimal('35.662430')
    complex_place_273.longitude = Decimal('138.465081')
    complex_place_273.memo = None
    complex_place_273.name = '第24旅 山梨 (camera)'
    complex_place_273.venue = None
    complex_place_273 = importer.save_or_locate(complex_place_273)

    complex_place_274 = Place()
    complex_place_274.address = '山梨県南アルプス市 百々1821 '
    complex_place_274.altitude = Decimal('0.000000')
    complex_place_274.latitude = Decimal('35.662430')
    complex_place_274.longitude = Decimal('138.465081')
    complex_place_274.memo = None
    complex_place_274.name = '菓子処 松の屋'
    complex_place_274.venue = None
    complex_place_274 = importer.save_or_locate(complex_place_274)

    complex_place_275 = Place()
    complex_place_275.address = '東京都中央区 築地六丁目19 '
    complex_place_275.altitude = Decimal('0.000000')
    complex_place_275.latitude = Decimal('35.662403')
    complex_place_275.longitude = Decimal('139.774853')
    complex_place_275.memo = None
    complex_place_275.name = '勝鬨橋'
    complex_place_275.venue = None
    complex_place_275 = importer.save_or_locate(complex_place_275)

    complex_place_276 = Place()
    complex_place_276.address = '東京都中央区 月島三丁目27 '
    complex_place_276.altitude = Decimal('0.000000')
    complex_place_276.latitude = Decimal('35.661685')
    complex_place_276.longitude = Decimal('139.778790')
    complex_place_276.memo = None
    complex_place_276.name = '月島西仲通り商店街'
    complex_place_276.venue = None
    complex_place_276 = importer.save_or_locate(complex_place_276)

    complex_place_277 = Place()
    complex_place_277.address = '東京都中央区 晴海二丁目2 '
    complex_place_277.altitude = Decimal('0.000000')
    complex_place_277.latitude = Decimal('35.658460')
    complex_place_277.longitude = Decimal('139.789327')
    complex_place_277.memo = None
    complex_place_277.name = '晴海橋梁'
    complex_place_277.venue = None
    complex_place_277 = importer.save_or_locate(complex_place_277)

    complex_place_278 = Place()
    complex_place_278.address = '山梨県南アルプス市 有野1100 '
    complex_place_278.altitude = Decimal('0.000000')
    complex_place_278.latitude = Decimal('35.658130')
    complex_place_278.longitude = Decimal('138.441001')
    complex_place_278.memo = None
    complex_place_278.name = '晴れてよかった'
    complex_place_278.venue = None
    complex_place_278 = importer.save_or_locate(complex_place_278)

    complex_place_279 = Place()
    complex_place_279.address = '  '
    complex_place_279.altitude = Decimal('0.000000')
    complex_place_279.latitude = Decimal('35.654876')
    complex_place_279.longitude = Decimal('139.791116')
    complex_place_279.memo = None
    complex_place_279.name = 'アーバンゲートブリッジ'
    complex_place_279.venue = None
    complex_place_279 = importer.save_or_locate(complex_place_279)

    complex_place_280 = Place()
    complex_place_280.address = '東京都江東区 豊洲二丁目3 '
    complex_place_280.altitude = Decimal('0.000000')
    complex_place_280.latitude = Decimal('35.653378')
    complex_place_280.longitude = Decimal('139.793127')
    complex_place_280.memo = None
    complex_place_280.name = '豊洲公園'
    complex_place_280.venue = None
    complex_place_280 = importer.save_or_locate(complex_place_280)

    complex_place_281 = Place()
    complex_place_281.address = '山梨県南アルプス市 飯野新田658 '
    complex_place_281.altitude = Decimal('0.000000')
    complex_place_281.latitude = Decimal('35.649285')
    complex_place_281.longitude = Decimal('138.439334')
    complex_place_281.memo = None
    complex_place_281.name = '八重森理容本店'
    complex_place_281.venue = None
    complex_place_281 = importer.save_or_locate(complex_place_281)

    complex_place_282 = Place()
    complex_place_282.address = '東京都江東区 新木場一丁目2 '
    complex_place_282.altitude = Decimal('0.000000')
    complex_place_282.latitude = Decimal('35.645902')
    complex_place_282.longitude = Decimal('139.826695')
    complex_place_282.memo = None
    complex_place_282.name = '新木場駅'
    complex_place_282.venue = None
    complex_place_282 = importer.save_or_locate(complex_place_282)

    complex_place_283 = Place()
    complex_place_283.address = '東京都江東区 豊洲六丁目4 '
    complex_place_283.altitude = Decimal('0.000000')
    complex_place_283.latitude = Decimal('35.645623')
    complex_place_283.longitude = Decimal('139.786251')
    complex_place_283.memo = None
    complex_place_283.name = '鈴富'
    complex_place_283.venue = None
    complex_place_283 = importer.save_or_locate(complex_place_283)

    complex_place_284 = Place()
    complex_place_284.address = '東京都江東区 豊洲六丁目4 '
    complex_place_284.altitude = Decimal('0.000000')
    complex_place_284.latitude = Decimal('35.645414')
    complex_place_284.longitude = Decimal('139.786201')
    complex_place_284.memo = None
    complex_place_284.name = '江戸前場下町'
    complex_place_284.venue = None
    complex_place_284 = importer.save_or_locate(complex_place_284)

    complex_place_285 = Place()
    complex_place_285.address = '東京都江東区 豊洲六丁目5 '
    complex_place_285.altitude = Decimal('0.000000')
    complex_place_285.latitude = Decimal('35.645174')
    complex_place_285.longitude = Decimal('139.781589')
    complex_place_285.memo = None
    complex_place_285.name = '福せん'
    complex_place_285.venue = None
    complex_place_285 = importer.save_or_locate(complex_place_285)

    complex_place_286 = Place()
    complex_place_286.address = None
    complex_place_286.altitude = Decimal('0.000000')
    complex_place_286.latitude = Decimal('35.643170')
    complex_place_286.longitude = Decimal('139.800640')
    complex_place_286.memo = None
    complex_place_286.name = '第15旅 都内 (camera)'
    complex_place_286.venue = None
    complex_place_286 = importer.save_or_locate(complex_place_286)

    complex_place_287 = Place()
    complex_place_287.address = '東京都江東区 豊洲六丁目6 '
    complex_place_287.altitude = Decimal('0.000000')
    complex_place_287.latitude = Decimal('35.641903')
    complex_place_287.longitude = Decimal('139.781852')
    complex_place_287.memo = None
    complex_place_287.name = '東京都中央卸売市場 豊洲市場 水産卸売場棟'
    complex_place_287.venue = None
    complex_place_287 = importer.save_or_locate(complex_place_287)

    complex_place_288 = Place()
    complex_place_288.address = '東京都江東区 新木場四丁目4 '
    complex_place_288.altitude = Decimal('0.000000')
    complex_place_288.latitude = Decimal('35.640573')
    complex_place_288.longitude = Decimal('139.840588')
    complex_place_288.memo = None
    complex_place_288.name = '新木場緑道公園'
    complex_place_288.venue = None
    complex_place_288 = importer.save_or_locate(complex_place_288)

    complex_place_289 = Place()
    complex_place_289.address = '山梨県南アルプス市 上今諏訪433 '
    complex_place_289.altitude = Decimal('0.000000')
    complex_place_289.latitude = Decimal('35.637166')
    complex_place_289.longitude = Decimal('138.504673')
    complex_place_289.memo = None
    complex_place_289.name = '開国橋'
    complex_place_289.venue = None
    complex_place_289 = importer.save_or_locate(complex_place_289)

    complex_place_290 = Place()
    complex_place_290.address = '  '
    complex_place_290.altitude = Decimal('0.000000')
    complex_place_290.latitude = Decimal('35.636564')
    complex_place_290.longitude = Decimal('139.763144')
    complex_place_290.memo = None
    complex_place_290.name = 'レインボーブリッジ'
    complex_place_290.venue = None
    complex_place_290 = importer.save_or_locate(complex_place_290)

    complex_place_291 = Place()
    complex_place_291.address = '山梨県南アルプス市  '
    complex_place_291.altitude = Decimal('0.000000')
    complex_place_291.latitude = Decimal('35.635321')
    complex_place_291.longitude = Decimal('138.369719')
    complex_place_291.memo = None
    complex_place_291.name = '芦安温泉 岩園館'
    complex_place_291.venue = None
    complex_place_291 = importer.save_or_locate(complex_place_291)

    complex_place_292 = Place()
    complex_place_292.address = '東京都江東区 有明三丁目7 '
    complex_place_292.altitude = Decimal('0.000000')
    complex_place_292.latitude = Decimal('35.634435')
    complex_place_292.longitude = Decimal('139.791650')
    complex_place_292.memo = None
    complex_place_292.name = '国際展示場駅'
    complex_place_292.venue = None
    complex_place_292 = importer.save_or_locate(complex_place_292)

    complex_place_293 = Place()
    complex_place_293.address = ''
    complex_place_293.altitude = Decimal('0.000000')
    complex_place_293.latitude = Decimal('35.634435')
    complex_place_293.longitude = Decimal('139.791650')
    complex_place_293.memo = None
    complex_place_293.name = '国際展示場駅'
    complex_place_293.venue = None
    complex_place_293 = importer.save_or_locate(complex_place_293)

    complex_place_294 = Place()
    complex_place_294.address = '東京都江東区 有明三丁目11 '
    complex_place_294.altitude = Decimal('0.000000')
    complex_place_294.latitude = Decimal('35.629818')
    complex_place_294.longitude = Decimal('139.794287')
    complex_place_294.memo = None
    complex_place_294.name = '東京ビッグサイト'
    complex_place_294.venue = None
    complex_place_294 = importer.save_or_locate(complex_place_294)

    complex_place_295 = Place()
    complex_place_295.address = '東京都港区 高輪三丁目26 '
    complex_place_295.altitude = Decimal('0.000000')
    complex_place_295.latitude = Decimal('35.628471')
    complex_place_295.longitude = Decimal('139.738760')
    complex_place_295.memo = None
    complex_place_295.name = '品川駅'
    complex_place_295.venue = None
    complex_place_295 = importer.save_or_locate(complex_place_295)

    complex_place_296 = Place()
    complex_place_296.address = '  '
    complex_place_296.altitude = Decimal('0.000000')
    complex_place_296.latitude = Decimal('35.627680')
    complex_place_296.longitude = Decimal('139.788863')
    complex_place_296.memo = None
    complex_place_296.name = '有明埠頭橋'
    complex_place_296.venue = None
    complex_place_296 = importer.save_or_locate(complex_place_296)

    complex_place_297 = Place()
    complex_place_297.address = '山梨県南アルプス市 高尾 '
    complex_place_297.altitude = Decimal('0.000000')
    complex_place_297.latitude = Decimal('35.622008')
    complex_place_297.longitude = Decimal('138.405122')
    complex_place_297.memo = None
    complex_place_297.name = '高尾穂見神社'
    complex_place_297.venue = None
    complex_place_297 = importer.save_or_locate(complex_place_297)

    complex_place_298 = Place()
    complex_place_298.address = '東京都品川区 西五反田七丁目13 '
    complex_place_298.altitude = Decimal('0.000000')
    complex_place_298.latitude = Decimal('35.621859')
    complex_place_298.longitude = Decimal('139.719940')
    complex_place_298.memo = None
    complex_place_298.name = 'さくらだもんっ'
    complex_place_298.venue = None
    complex_place_298 = importer.save_or_locate(complex_place_298)

    complex_place_299 = Place()
    complex_place_299.address = '  '
    complex_place_299.altitude = Decimal('0.000000')
    complex_place_299.latitude = Decimal('35.619110')
    complex_place_299.longitude = Decimal('139.773843')
    complex_place_299.memo = None
    complex_place_299.name = '南極観測船『宗谷』'
    complex_place_299.venue = None
    complex_place_299 = importer.save_or_locate(complex_place_299)

    complex_place_300 = Place()
    complex_place_300.address = '東京都江東区 有明四丁目8 '
    complex_place_300.altitude = Decimal('0.000000')
    complex_place_300.latitude = Decimal('35.617404')
    complex_place_300.longitude = Decimal('139.795753')
    complex_place_300.memo = None
    complex_place_300.name = '東京港フェリーターミナル'
    complex_place_300.venue = None
    complex_place_300 = importer.save_or_locate(complex_place_300)

    complex_place_301 = Place()
    complex_place_301.address = '東京都江東区 青海二丁目8 '
    complex_place_301.altitude = Decimal('0.000000')
    complex_place_301.latitude = Decimal('35.616070')
    complex_place_301.longitude = Decimal('139.775637')
    complex_place_301.memo = None
    complex_place_301.name = '青海南ふ頭公園'
    complex_place_301.venue = None
    complex_place_301 = importer.save_or_locate(complex_place_301)

    complex_place_302 = Place()
    complex_place_302.address = '  '
    complex_place_302.altitude = Decimal('0.000000')
    complex_place_302.latitude = Decimal('35.612215')
    complex_place_302.longitude = Decimal('139.828884')
    complex_place_302.memo = None
    complex_place_302.name = '東京ゲートブリッジ'
    complex_place_302.venue = None
    complex_place_302 = importer.save_or_locate(complex_place_302)

    complex_place_303 = Place()
    complex_place_303.address = '東京都大田区 久が原一丁目7 '
    complex_place_303.altitude = Decimal('0.000000')
    complex_place_303.latitude = Decimal('35.585741')
    complex_place_303.longitude = Decimal('139.693410')
    complex_place_303.memo = None
    complex_place_303.name = '道々橋八幡神社'
    complex_place_303.venue = None
    complex_place_303 = importer.save_or_locate(complex_place_303)

    complex_place_304 = Place()
    complex_place_304.address = '京都府宮津市 江尻430 '
    complex_place_304.altitude = Decimal('0.000000')
    complex_place_304.latitude = Decimal('35.582784')
    complex_place_304.longitude = Decimal('135.196701')
    complex_place_304.memo = None
    complex_place_304.name = '丹後國一之宮 元伊勢 籠神社'
    complex_place_304.venue = None
    complex_place_304 = importer.save_or_locate(complex_place_304)

    complex_place_305 = Place()
    complex_place_305.address = '〒146-0082 東京都大田区池上２丁目６−１２'
    complex_place_305.altitude = Decimal('0.000000')
    complex_place_305.latitude = Decimal('35.579625')
    complex_place_305.longitude = Decimal('139.682701')
    complex_place_305.memo = '📕電撃マオウJUL.2021-P15 下右\r\n🗯いいかも スーパーカブ！'
    complex_place_305.name = "McDonald's マクドナルド １号線池上店"
    complex_place_305.venue = complex_venue_32
    complex_place_305 = importer.save_or_locate(complex_place_305)

    complex_place_306 = Place()
    complex_place_306.address = '京都府宮津市 字江尻927 '
    complex_place_306.altitude = Decimal('0.000000')
    complex_place_306.latitude = Decimal('35.569802')
    complex_place_306.longitude = Decimal('135.191820')
    complex_place_306.memo = None
    complex_place_306.name = '天橋立'
    complex_place_306.venue = None
    complex_place_306 = importer.save_or_locate(complex_place_306)

    complex_place_307 = Place()
    complex_place_307.address = '島根県松江市  '
    complex_place_307.altitude = Decimal('0.000000')
    complex_place_307.latitude = Decimal('35.567298')
    complex_place_307.longitude = Decimal('133.325446')
    complex_place_307.memo = None
    complex_place_307.name = '美保関灯台'
    complex_place_307.venue = None
    complex_place_307 = importer.save_or_locate(complex_place_307)

    complex_place_308 = Place()
    complex_place_308.address = '島根県松江市  '
    complex_place_308.altitude = Decimal('0.000000')
    complex_place_308.latitude = Decimal('35.567285')
    complex_place_308.longitude = Decimal('133.325638')
    complex_place_308.memo = None
    complex_place_308.name = '沖之御前地之御前遥拝所'
    complex_place_308.venue = None
    complex_place_308 = importer.save_or_locate(complex_place_308)

    complex_place_309 = Place()
    complex_place_309.address = '島根県松江市  '
    complex_place_309.altitude = Decimal('0.000000')
    complex_place_309.latitude = Decimal('35.567249')
    complex_place_309.longitude = Decimal('133.325048')
    complex_place_309.memo = None
    complex_place_309.name = '美保関灯台ビュッフェ'
    complex_place_309.venue = None
    complex_place_309 = importer.save_or_locate(complex_place_309)

    complex_place_310 = Place()
    complex_place_310.address = '〒146-0095 東京都大田区多摩川１丁目１６−１６'
    complex_place_310.altitude = Decimal('0.000000')
    complex_place_310.latitude = Decimal('35.564476')
    complex_place_310.longitude = Decimal('139.678398')
    complex_place_310.memo = '📕電撃マオウJUL.2021-P14 上右\r\n🗯教習所のバイクと全然違う！'
    complex_place_310.name = 'シトロエン大田 東邦自動車㈱'
    complex_place_310.venue = complex_venue_32
    complex_place_310 = importer.save_or_locate(complex_place_310)

    complex_place_311 = Place()
    complex_place_311.address = '島根県松江市  '
    complex_place_311.altitude = Decimal('0.000000')
    complex_place_311.latitude = Decimal('35.564208')
    complex_place_311.longitude = Decimal('133.319861')
    complex_place_311.memo = None
    complex_place_311.name = '恵美須社'
    complex_place_311.venue = None
    complex_place_311 = importer.save_or_locate(complex_place_311)

    complex_place_312 = Place()
    complex_place_312.address = '京都府宮津市 字文珠 '
    complex_place_312.altitude = Decimal('0.000000')
    complex_place_312.latitude = Decimal('35.563407')
    complex_place_312.longitude = Decimal('135.187916')
    complex_place_312.memo = None
    complex_place_312.name = '天橋立神社'
    complex_place_312.venue = None
    complex_place_312 = importer.save_or_locate(complex_place_312)

    complex_place_313 = Place()
    complex_place_313.address = '京都府宮津市 字文珠 '
    complex_place_313.altitude = Decimal('0.000000')
    complex_place_313.latitude = Decimal('35.562872')
    complex_place_313.longitude = Decimal('135.188148')
    complex_place_313.memo = None
    complex_place_313.name = '岩見重太郎 仇討ちの場'
    complex_place_313.venue = None
    complex_place_313 = importer.save_or_locate(complex_place_313)

    complex_place_314 = Place()
    complex_place_314.address = '島根県松江市 美保関町美保関 '
    complex_place_314.altitude = Decimal('0.000000')
    complex_place_314.latitude = Decimal('35.562510')
    complex_place_314.longitude = Decimal('133.307680')
    complex_place_314.memo = None
    complex_place_314.name = '青石畳通り'
    complex_place_314.venue = None
    complex_place_314 = importer.save_or_locate(complex_place_314)

    complex_place_315 = Place()
    complex_place_315.address = '島根県松江市 美保関町美保関 '
    complex_place_315.altitude = Decimal('0.000000')
    complex_place_315.latitude = Decimal('35.562318')
    complex_place_315.longitude = Decimal('133.306222')
    complex_place_315.memo = None
    complex_place_315.name = '美保神社'
    complex_place_315.venue = None
    complex_place_315 = importer.save_or_locate(complex_place_315)

    complex_place_316 = Place()
    complex_place_316.address = '島根県松江市 美保関町美保関 '
    complex_place_316.altitude = Decimal('0.000000')
    complex_place_316.latitude = Decimal('35.562302')
    complex_place_316.longitude = Decimal('133.307495')
    complex_place_316.memo = None
    complex_place_316.name = '廻船御用水'
    complex_place_316.venue = None
    complex_place_316 = importer.save_or_locate(complex_place_316)

    complex_place_317 = Place()
    complex_place_317.address = '島根県松江市 美保関町美保関 '
    complex_place_317.altitude = Decimal('0.000000')
    complex_place_317.latitude = Decimal('35.560334')
    complex_place_317.longitude = Decimal('133.310951')
    complex_place_317.memo = None
    complex_place_317.name = '美保関漁港'
    complex_place_317.venue = None
    complex_place_317 = importer.save_or_locate(complex_place_317)

    complex_place_318 = Place()
    complex_place_318.address = '〒146-0095 東京都大田区多摩川２丁目１６−７'
    complex_place_318.altitude = Decimal('0.000000')
    complex_place_318.latitude = Decimal('35.557735')
    complex_place_318.longitude = Decimal('139.678790')
    complex_place_318.memo = '📕電撃マオウJUL.2021-P14 上左\r\n※交差点の特徴が似ている？'
    complex_place_318.name = 'グランベルミューネス多摩川'
    complex_place_318.venue = complex_venue_32
    complex_place_318 = importer.save_or_locate(complex_place_318)

    complex_place_319 = Place()
    complex_place_319.address = '京都府宮津市 字文珠190 '
    complex_place_319.altitude = Decimal('0.000000')
    complex_place_319.latitude = Decimal('35.555720')
    complex_place_319.longitude = Decimal('135.183929')
    complex_place_319.memo = None
    complex_place_319.name = '天橋立ビューランド リフト・モノレールのりば'
    complex_place_319.venue = None
    complex_place_319 = importer.save_or_locate(complex_place_319)

    complex_place_320 = Place()
    complex_place_320.address = '京都府宮津市 文珠1 '
    complex_place_320.altitude = Decimal('0.000000')
    complex_place_320.latitude = Decimal('35.552778')
    complex_place_320.longitude = Decimal('135.182117')
    complex_place_320.memo = None
    complex_place_320.name = '天橋立ビューランド'
    complex_place_320.venue = None
    complex_place_320 = importer.save_or_locate(complex_place_320)

    complex_place_321 = Place()
    complex_place_321.address = '東京都大田区 羽田空港三丁目4 '
    complex_place_321.altitude = Decimal('0.000000')
    complex_place_321.latitude = Decimal('35.549971')
    complex_place_321.longitude = Decimal('139.786427')
    complex_place_321.memo = None
    complex_place_321.name = '羽田空港第１・第２ターミナル駅'
    complex_place_321.venue = None
    complex_place_321 = importer.save_or_locate(complex_place_321)

    complex_place_322 = Place()
    complex_place_322.address = '東京都大田区 羽田空港三丁目3 '
    complex_place_322.altitude = Decimal('0.000000')
    complex_place_322.latitude = Decimal('35.549393')
    complex_place_322.longitude = Decimal('139.779839')
    complex_place_322.memo = None
    complex_place_322.name = '羽田空港'
    complex_place_322.venue = None
    complex_place_322 = importer.save_or_locate(complex_place_322)

    complex_place_323 = Place()
    complex_place_323.address = '〒144-0056 東京都大田区西六郷２丁目５７'
    complex_place_323.altitude = Decimal('0.000000')
    complex_place_323.latitude = Decimal('35.548631')
    complex_place_323.longitude = Decimal('139.685846')
    complex_place_323.memo = '📕電撃マオウJUL.2021-P14 中\r\n※多摩川沿いの堤防上の道路'
    complex_place_323.name = '大田区道主要第102号線'
    complex_place_323.venue = complex_venue_32
    complex_place_323 = importer.save_or_locate(complex_place_323)

    complex_place_324 = Place()
    complex_place_324.address = '〒144-0056 東京都大田区西六郷２丁目５８'
    complex_place_324.altitude = Decimal('0.000000')
    complex_place_324.latitude = Decimal('35.548189')
    complex_place_324.longitude = Decimal('139.685834')
    complex_place_324.memo = '📕電撃マオウJUL.2021-P14 中\r\n※建物の形の特徴が一致する'
    complex_place_324.name = 'ルミエール ミヤモト'
    complex_place_324.venue = complex_venue_32
    complex_place_324 = importer.save_or_locate(complex_place_324)

    complex_place_325 = Place()
    complex_place_325.address = '〒144-0055 東京都大田区仲六郷４丁目３４−１０'
    complex_place_325.altitude = Decimal('0.000000')
    complex_place_325.latitude = Decimal('35.543548')
    complex_place_325.longitude = Decimal('139.692286')
    complex_place_325.memo = '📕電撃マオウJUL.2021-P25\r\n🗯古いバイクなので'
    complex_place_325.name = 'レッドバロン東京大田'
    complex_place_325.venue = complex_venue_32
    complex_place_325 = importer.save_or_locate(complex_place_325)

    complex_place_326 = Place()
    complex_place_326.address = '京都府宮津市 字本町842 '
    complex_place_326.altitude = Decimal('0.000000')
    complex_place_326.latitude = Decimal('35.536840')
    complex_place_326.longitude = Decimal('135.191831')
    complex_place_326.memo = None
    complex_place_326.name = '茶六本館'
    complex_place_326.venue = None
    complex_place_326 = importer.save_or_locate(complex_place_326)

    complex_place_327 = Place()
    complex_place_327.address = '京都府宮津市 字鶴賀2066 '
    complex_place_327.altitude = Decimal('0.000000')
    complex_place_327.latitude = Decimal('35.534848')
    complex_place_327.longitude = Decimal('135.199261')
    complex_place_327.memo = None
    complex_place_327.name = '富田屋'
    complex_place_327.venue = None
    complex_place_327 = importer.save_or_locate(complex_place_327)

    complex_place_328 = Place()
    complex_place_328.address = '島根県松江市  '
    complex_place_328.altitude = Decimal('0.000000')
    complex_place_328.latitude = Decimal('35.534707')
    complex_place_328.longitude = Decimal('133.164644')
    complex_place_328.memo = None
    complex_place_328.name = '美保関バスターミナル'
    complex_place_328.venue = None
    complex_place_328 = importer.save_or_locate(complex_place_328)

    complex_place_329 = Place()
    complex_place_329.address = '京都府宮津市 字鶴賀2099 '
    complex_place_329.altitude = Decimal('0.000000')
    complex_place_329.latitude = Decimal('35.534419')
    complex_place_329.longitude = Decimal('135.199751')
    complex_place_329.memo = None
    complex_place_329.name = '宮津駅'
    complex_place_329.venue = None
    complex_place_329 = importer.save_or_locate(complex_place_329)

    complex_place_330 = Place()
    complex_place_330.address = None
    complex_place_330.altitude = Decimal('0.000000')
    complex_place_330.latitude = Decimal('35.483400')
    complex_place_330.longitude = Decimal('133.048300')
    complex_place_330.memo = None
    complex_place_330.name = '第13旅 島根後編 (camera)'
    complex_place_330.venue = None
    complex_place_330 = importer.save_or_locate(complex_place_330)

    complex_place_331 = Place()
    complex_place_331.address = '島根県松江市 殿町1 '
    complex_place_331.altitude = Decimal('0.000000')
    complex_place_331.latitude = Decimal('35.475133')
    complex_place_331.longitude = Decimal('133.050678')
    complex_place_331.memo = None
    complex_place_331.name = '松江城'
    complex_place_331.venue = None
    complex_place_331 = importer.save_or_locate(complex_place_331)

    complex_place_332 = Place()
    complex_place_332.address = '島根県松江市 学園南二丁目5 '
    complex_place_332.altitude = Decimal('0.000000')
    complex_place_332.latitude = Decimal('35.473154')
    complex_place_332.longitude = Decimal('133.066085')
    complex_place_332.memo = None
    complex_place_332.name = '総合体育館前（バス）'
    complex_place_332.venue = None
    complex_place_332 = importer.save_or_locate(complex_place_332)

    complex_place_333 = Place()
    complex_place_333.address = '島根県松江市 中原町51 '
    complex_place_333.altitude = Decimal('0.000000')
    complex_place_333.latitude = Decimal('35.467363')
    complex_place_333.longitude = Decimal('133.046042')
    complex_place_333.memo = None
    complex_place_333.name = '松江しんじ湖温泉駅'
    complex_place_333.venue = None
    complex_place_333 = importer.save_or_locate(complex_place_333)

    complex_place_334 = Place()
    complex_place_334.address = '島根県松江市 千鳥町18 '
    complex_place_334.altitude = Decimal('0.000000')
    complex_place_334.latitude = Decimal('35.466171')
    complex_place_334.longitude = Decimal('133.045338')
    complex_place_334.memo = None
    complex_place_334.name = 'ホテル一畑'
    complex_place_334.venue = None
    complex_place_334 = importer.save_or_locate(complex_place_334)

    complex_place_335 = Place()
    complex_place_335.address = '神奈川県海老名市 大谷南五丁目2 '
    complex_place_335.altitude = Decimal('0.000000')
    complex_place_335.latitude = Decimal('35.431070')
    complex_place_335.longitude = Decimal('139.401020')
    complex_place_335.memo = None
    complex_place_335.name = '海老名SA (下り)'
    complex_place_335.venue = None
    complex_place_335 = importer.save_or_locate(complex_place_335)

    complex_place_336 = Place()
    complex_place_336.address = '島根県出雲市 大社町杵築東257 '
    complex_place_336.altitude = Decimal('0.000000')
    complex_place_336.latitude = Decimal('35.401545')
    complex_place_336.longitude = Decimal('132.684463')
    complex_place_336.memo = None
    complex_place_336.name = '出雲大社 神楽殿'
    complex_place_336.venue = None
    complex_place_336 = importer.save_or_locate(complex_place_336)

    complex_place_337 = Place()
    complex_place_337.address = '島根県出雲市 大社町杵築東257 '
    complex_place_337.altitude = Decimal('0.000000')
    complex_place_337.latitude = Decimal('35.401493')
    complex_place_337.longitude = Decimal('132.684880')
    complex_place_337.memo = None
    complex_place_337.name = '出雲大社 西十九社'
    complex_place_337.venue = None
    complex_place_337 = importer.save_or_locate(complex_place_337)

    complex_place_338 = Place()
    complex_place_338.address = '島根県出雲市 大社町杵築東257 '
    complex_place_338.altitude = Decimal('0.000000')
    complex_place_338.latitude = Decimal('35.401206')
    complex_place_338.longitude = Decimal('132.685521')
    complex_place_338.memo = None
    complex_place_338.name = '出雲大社 拝殿'
    complex_place_338.venue = None
    complex_place_338 = importer.save_or_locate(complex_place_338)

    complex_place_339 = Place()
    complex_place_339.address = '島根県出雲市 大社町杵築北2844 '
    complex_place_339.altitude = Decimal('0.000000')
    complex_place_339.latitude = Decimal('35.400303')
    complex_place_339.longitude = Decimal('132.671911')
    complex_place_339.memo = None
    complex_place_339.name = '稲佐の浜(弁天島)'
    complex_place_339.venue = None
    complex_place_339 = importer.save_or_locate(complex_place_339)

    complex_place_340 = Place()
    complex_place_340.address = '島根県出雲市 大社町杵築東266 '
    complex_place_340.altitude = Decimal('0.000000')
    complex_place_340.latitude = Decimal('35.399411')
    complex_place_340.longitude = Decimal('132.685205')
    complex_place_340.memo = None
    complex_place_340.name = 'うさぎ！'
    complex_place_340.venue = None
    complex_place_340 = importer.save_or_locate(complex_place_340)

    complex_place_341 = Place()
    complex_place_341.address = '島根県出雲市 大社町杵築東3286 '
    complex_place_341.altitude = Decimal('0.000000')
    complex_place_341.latitude = Decimal('35.396705')
    complex_place_341.longitude = Decimal('132.686374')
    complex_place_341.memo = None
    complex_place_341.name = '出雲大社 勢溜の大鳥居'
    complex_place_341.venue = None
    complex_place_341 = importer.save_or_locate(complex_place_341)

    complex_place_342 = Place()
    complex_place_342.address = '島根県出雲市 大社町杵築南839 '
    complex_place_342.altitude = Decimal('0.000000')
    complex_place_342.latitude = Decimal('35.396254')
    complex_place_342.longitude = Decimal('132.686313')
    complex_place_342.memo = None
    complex_place_342.name = '出雲日本海 出雲大社正門前店'
    complex_place_342.venue = None
    complex_place_342 = importer.save_or_locate(complex_place_342)

    complex_place_343 = Place()
    complex_place_343.address = '島根県出雲市 大社町杵築南775 '
    complex_place_343.altitude = Decimal('0.000000')
    complex_place_343.latitude = Decimal('35.395217')
    complex_place_343.longitude = Decimal('132.686757')
    complex_place_343.memo = None
    complex_place_343.name = '俵屋菓舗 神門店'
    complex_place_343.venue = None
    complex_place_343 = importer.save_or_locate(complex_place_343)

    complex_place_344 = Place()
    complex_place_344.address = '島根県出雲市 大社町杵築南1346 '
    complex_place_344.altitude = Decimal('0.000000')
    complex_place_344.latitude = Decimal('35.393522')
    complex_place_344.longitude = Decimal('132.687073')
    complex_place_344.memo = None
    complex_place_344.name = '出雲大社前駅'
    complex_place_344.venue = None
    complex_place_344 = importer.save_or_locate(complex_place_344)

    complex_place_345 = Place()
    complex_place_345.address = '島根県出雲市 大社町杵築南1386 '
    complex_place_345.altitude = Decimal('0.000000')
    complex_place_345.latitude = Decimal('35.391579')
    complex_place_345.longitude = Decimal('132.687278')
    complex_place_345.memo = None
    complex_place_345.name = '出雲大社 大鳥居'
    complex_place_345.venue = None
    complex_place_345 = importer.save_or_locate(complex_place_345)

    complex_place_346 = Place()
    complex_place_346.address = '島根県出雲市 大社町北荒木452 '
    complex_place_346.altitude = Decimal('0.000000')
    complex_place_346.latitude = Decimal('35.386642')
    complex_place_346.longitude = Decimal('132.690256')
    complex_place_346.memo = None
    complex_place_346.name = '旧大社駅舎'
    complex_place_346.venue = None
    complex_place_346 = importer.save_or_locate(complex_place_346)

    complex_place_347 = Place()
    complex_place_347.address = '島根県出雲市 高松町1215 '
    complex_place_347.altitude = Decimal('0.000000')
    complex_place_347.latitude = Decimal('35.361078')
    complex_place_347.longitude = Decimal('132.718948')
    complex_place_347.memo = None
    complex_place_347.name = 'JR大社線出雲高松駅跡'
    complex_place_347.venue = None
    complex_place_347 = importer.save_or_locate(complex_place_347)

    complex_place_348 = Place()
    complex_place_348.address = '島根県出雲市 駅北町25 '
    complex_place_348.altitude = Decimal('0.000000')
    complex_place_348.latitude = Decimal('35.360839')
    complex_place_348.longitude = Decimal('132.756701')
    complex_place_348.memo = None
    complex_place_348.name = '出雲市駅'
    complex_place_348.venue = None
    complex_place_348 = importer.save_or_locate(complex_place_348)

    complex_place_349 = Place()
    complex_place_349.address = '島根県出雲市 松寄下町599 '
    complex_place_349.altitude = Decimal('0.000000')
    complex_place_349.latitude = Decimal('35.360365')
    complex_place_349.longitude = Decimal('132.723086')
    complex_place_349.memo = None
    complex_place_349.name = '大社線鉄橋跡'
    complex_place_349.venue = None
    complex_place_349 = importer.save_or_locate(complex_place_349)

    complex_place_350 = Place()
    complex_place_350.address = None
    complex_place_350.altitude = Decimal('0.000000')
    complex_place_350.latitude = Decimal('35.182000')
    complex_place_350.longitude = Decimal('135.607300')
    complex_place_350.memo = None
    complex_place_350.name = '第5旅 京都 (camera)'
    complex_place_350.venue = None
    complex_place_350 = importer.save_or_locate(complex_place_350)

    complex_place_351 = Place()
    complex_place_351.address = '千葉県富津市  '
    complex_place_351.altitude = Decimal('0.000000')
    complex_place_351.latitude = Decimal('35.168132')
    complex_place_351.longitude = Decimal('139.822254')
    complex_place_351.memo = None
    complex_place_351.name = '浜金谷駅'
    complex_place_351.venue = None
    complex_place_351 = importer.save_or_locate(complex_place_351)

    complex_place_352 = Place()
    complex_place_352.address = '千葉県富津市  '
    complex_place_352.altitude = Decimal('0.000000')
    complex_place_352.latitude = Decimal('35.162217')
    complex_place_352.longitude = Decimal('139.823080')
    complex_place_352.memo = None
    complex_place_352.name = '鋸山ロープウェー'
    complex_place_352.venue = None
    complex_place_352 = importer.save_or_locate(complex_place_352)

    complex_place_353 = Place()
    complex_place_353.address = '千葉県安房郡 鋸南町 元名'
    complex_place_353.altitude = Decimal('0.000000')
    complex_place_353.latitude = Decimal('35.159265')
    complex_place_353.longitude = Decimal('139.833193')
    complex_place_353.memo = None
    complex_place_353.name = '山頂展望台地獄のぞき'
    complex_place_353.venue = None
    complex_place_353 = importer.save_or_locate(complex_place_353)

    complex_place_354 = Place()
    complex_place_354.address = '千葉県安房郡 鋸南町 元名'
    complex_place_354.altitude = Decimal('0.000000')
    complex_place_354.latitude = Decimal('35.159167')
    complex_place_354.longitude = Decimal('139.832674')
    complex_place_354.memo = None
    complex_place_354.name = '石切場跡(ラピュタの壁)'
    complex_place_354.venue = None
    complex_place_354 = importer.save_or_locate(complex_place_354)

    complex_place_355 = Place()
    complex_place_355.address = '千葉県安房郡 鋸南町 元名'
    complex_place_355.altitude = Decimal('0.000000')
    complex_place_355.latitude = Decimal('35.159042')
    complex_place_355.longitude = Decimal('139.832931')
    complex_place_355.memo = None
    complex_place_355.name = '百尺観音'
    complex_place_355.venue = None
    complex_place_355 = importer.save_or_locate(complex_place_355)

    complex_place_356 = Place()
    complex_place_356.address = '千葉県安房郡 鋸南町 元名'
    complex_place_356.altitude = Decimal('0.000000')
    complex_place_356.latitude = Decimal('35.158802')
    complex_place_356.longitude = Decimal('139.834427')
    complex_place_356.memo = None
    complex_place_356.name = '通天関'
    complex_place_356.venue = None
    complex_place_356 = importer.save_or_locate(complex_place_356)

    complex_place_357 = Place()
    complex_place_357.address = '千葉県富津市  '
    complex_place_357.altitude = Decimal('0.000000')
    complex_place_357.latitude = Decimal('35.158493')
    complex_place_357.longitude = Decimal('139.828477')
    complex_place_357.memo = None
    complex_place_357.name = '鋸山山頂'
    complex_place_357.venue = None
    complex_place_357 = importer.save_or_locate(complex_place_357)

    complex_place_358 = Place()
    complex_place_358.address = '千葉県安房郡 鋸南町 '
    complex_place_358.altitude = Decimal('0.000000')
    complex_place_358.latitude = Decimal('35.158230')
    complex_place_358.longitude = Decimal('139.830836')
    complex_place_358.memo = None
    complex_place_358.name = '西口管理所'
    complex_place_358.venue = None
    complex_place_358 = importer.save_or_locate(complex_place_358)

    complex_place_359 = Place()
    complex_place_359.address = '千葉県安房郡 鋸南町 元名'
    complex_place_359.altitude = Decimal('0.000000')
    complex_place_359.latitude = Decimal('35.158116')
    complex_place_359.longitude = Decimal('139.832891')
    complex_place_359.memo = None
    complex_place_359.name = '千五百羅漢'
    complex_place_359.venue = None
    complex_place_359 = importer.save_or_locate(complex_place_359)

    complex_place_360 = Place()
    complex_place_360.address = '千葉県安房郡 鋸南町 元名'
    complex_place_360.altitude = Decimal('0.000000')
    complex_place_360.latitude = Decimal('35.157670')
    complex_place_360.longitude = Decimal('139.834689')
    complex_place_360.memo = None
    complex_place_360.name = '日本寺 大仏'
    complex_place_360.venue = None
    complex_place_360 = importer.save_or_locate(complex_place_360)

    complex_place_361 = Place()
    complex_place_361.address = None
    complex_place_361.altitude = Decimal('0.000000')
    complex_place_361.latitude = Decimal('35.100000')
    complex_place_361.longitude = Decimal('139.879022')
    complex_place_361.memo = None
    complex_place_361.name = '第23旅 千葉 (camera)'
    complex_place_361.venue = None
    complex_place_361 = importer.save_or_locate(complex_place_361)

    complex_place_362 = Place()
    complex_place_362.address = '京都府京都市 下京区 東塩小路町676'
    complex_place_362.altitude = Decimal('0.000000')
    complex_place_362.latitude = Decimal('34.985849')
    complex_place_362.longitude = Decimal('135.758767')
    complex_place_362.memo = None
    complex_place_362.name = '京都駅'
    complex_place_362.venue = None
    complex_place_362 = importer.save_or_locate(complex_place_362)

    complex_place_363 = Place()
    complex_place_363.address = '千葉県南房総市 千倉町瀬戸 '
    complex_place_363.altitude = Decimal('0.000000')
    complex_place_363.latitude = Decimal('34.976709')
    complex_place_363.longitude = Decimal('139.954712')
    complex_place_363.memo = None
    complex_place_363.name = '千倉駅'
    complex_place_363.venue = None
    complex_place_363 = importer.save_or_locate(complex_place_363)

    complex_place_364 = Place()
    complex_place_364.address = '千葉県南房総市 千倉町瀬戸 '
    complex_place_364.altitude = Decimal('0.000000')
    complex_place_364.latitude = Decimal('34.976704')
    complex_place_364.longitude = Decimal('139.954577')
    complex_place_364.memo = None
    complex_place_364.name = '南房総市観光協会千倉観光案内所(千倉駅構内)'
    complex_place_364.venue = None
    complex_place_364 = importer.save_or_locate(complex_place_364)

    complex_place_365 = Place()
    complex_place_365.address = '千葉県南房総市 千倉町瀬戸 '
    complex_place_365.altitude = Decimal('0.000000')
    complex_place_365.latitude = Decimal('34.973351')
    complex_place_365.longitude = Decimal('139.962721')
    complex_place_365.memo = None
    complex_place_365.name = '瀬戸浜海岸'
    complex_place_365.venue = None
    complex_place_365 = importer.save_or_locate(complex_place_365)

    complex_place_366 = Place()
    complex_place_366.address = '京都府京都市 伏見区 深草一ノ坪町20'
    complex_place_366.altitude = Decimal('0.000000')
    complex_place_366.latitude = Decimal('34.968754')
    complex_place_366.longitude = Decimal('135.769209')
    complex_place_366.memo = None
    complex_place_366.name = '伏見稲荷駅'
    complex_place_366.venue = None
    complex_place_366 = importer.save_or_locate(complex_place_366)

    complex_place_367 = Place()
    complex_place_367.address = '京都府京都市 伏見区 深草一ノ坪町35'
    complex_place_367.altitude = Decimal('0.000000')
    complex_place_367.latitude = Decimal('34.968596')
    complex_place_367.longitude = Decimal('135.768613')
    complex_place_367.memo = None
    complex_place_367.name = 'ラー麺・陽はまた昇る 伏見稲荷駅前本店'
    complex_place_367.venue = None
    complex_place_367 = importer.save_or_locate(complex_place_367)

    complex_place_368 = Place()
    complex_place_368.address = '京都府京都市 伏見区 深草藪之内町1'
    complex_place_368.altitude = Decimal('0.000000')
    complex_place_368.latitude = Decimal('34.967140')
    complex_place_368.longitude = Decimal('135.772672')
    complex_place_368.memo = None
    complex_place_368.name = '伏見稲荷大社'
    complex_place_368.venue = None
    complex_place_368 = importer.save_or_locate(complex_place_368)

    complex_place_369 = Place()
    complex_place_369.address = '千葉県南房総市  '
    complex_place_369.altitude = Decimal('0.000000')
    complex_place_369.latitude = Decimal('34.963892')
    complex_place_369.longitude = Decimal('139.959690')
    complex_place_369.memo = None
    complex_place_369.name = '川尻橋'
    complex_place_369.venue = None
    complex_place_369 = importer.save_or_locate(complex_place_369)

    complex_place_370 = Place()
    complex_place_370.address = '千葉県南房総市 千倉町平舘 '
    complex_place_370.altitude = Decimal('0.000000')
    complex_place_370.latitude = Decimal('34.960282')
    complex_place_370.longitude = Decimal('139.959356')
    complex_place_370.memo = None
    complex_place_370.name = '寿司と地魚料理 大徳家'
    complex_place_370.venue = None
    complex_place_370 = importer.save_or_locate(complex_place_370)

    complex_place_371 = Place()
    complex_place_371.address = '千葉県南房総市 千倉町平舘 '
    complex_place_371.altitude = Decimal('0.000000')
    complex_place_371.latitude = Decimal('34.959360')
    complex_place_371.longitude = Decimal('139.959200')
    complex_place_371.memo = None
    complex_place_371.name = '千葉銀行 千倉支店'
    complex_place_371.venue = None
    complex_place_371 = importer.save_or_locate(complex_place_371)

    complex_place_372 = Place()
    complex_place_372.address = '千葉県南房総市 千倉町平舘 '
    complex_place_372.altitude = Decimal('0.000000')
    complex_place_372.latitude = Decimal('34.957868')
    complex_place_372.longitude = Decimal('139.959096')
    complex_place_372.memo = None
    complex_place_372.name = 'とん亭いとう'
    complex_place_372.venue = None
    complex_place_372 = importer.save_or_locate(complex_place_372)

    complex_place_373 = Place()
    complex_place_373.address = '京都府京都市 伏見区 今町669'
    complex_place_373.altitude = Decimal('0.000000')
    complex_place_373.latitude = Decimal('34.935121')
    complex_place_373.longitude = Decimal('135.762457')
    complex_place_373.memo = None
    complex_place_373.name = '藤岡酒造'
    complex_place_373.venue = None
    complex_place_373 = importer.save_or_locate(complex_place_373)

    complex_place_374 = Place()
    complex_place_374.address = '千葉県南房総市 千倉町千田 '
    complex_place_374.altitude = Decimal('0.000000')
    complex_place_374.latitude = Decimal('34.934808')
    complex_place_374.longitude = Decimal('139.944720')
    complex_place_374.memo = None
    complex_place_374.name = '高皇産霊神社'
    complex_place_374.venue = None
    complex_place_374 = importer.save_or_locate(complex_place_374)

    complex_place_375 = Place()
    complex_place_375.address = '京都府京都市 伏見区 本材木町680'
    complex_place_375.altitude = Decimal('0.000000')
    complex_place_375.latitude = Decimal('34.929136')
    complex_place_375.longitude = Decimal('135.761610')
    complex_place_375.memo = None
    complex_place_375.name = '月桂冠大倉記念館'
    complex_place_375.venue = None
    complex_place_375 = importer.save_or_locate(complex_place_375)

    complex_place_376 = Place()
    complex_place_376.address = '千葉県南房総市 千倉町大川 '
    complex_place_376.altitude = Decimal('0.000000')
    complex_place_376.latitude = Decimal('34.928187')
    complex_place_376.longitude = Decimal('139.948278')
    complex_place_376.memo = None
    complex_place_376.name = '大川港'
    complex_place_376.venue = None
    complex_place_376 = importer.save_or_locate(complex_place_376)

    complex_place_377 = Place()
    complex_place_377.address = '千葉県館山市 大神宮376 '
    complex_place_377.altitude = Decimal('0.000000')
    complex_place_377.latitude = Decimal('34.922467')
    complex_place_377.longitude = Decimal('139.836880')
    complex_place_377.memo = None
    complex_place_377.name = '安房神社'
    complex_place_377.venue = None
    complex_place_377 = importer.save_or_locate(complex_place_377)

    complex_place_378 = Place()
    complex_place_378.address = '千葉県南房総市  '
    complex_place_378.altitude = Decimal('0.000000')
    complex_place_378.latitude = Decimal('34.904775')
    complex_place_378.longitude = Decimal('139.879022')
    complex_place_378.memo = None
    complex_place_378.name = '最南端'
    complex_place_378.venue = None
    complex_place_378 = importer.save_or_locate(complex_place_378)

    complex_place_379 = Place()
    complex_place_379.address = '千葉県南房総市  '
    complex_place_379.altitude = Decimal('0.000000')
    complex_place_379.latitude = Decimal('34.902565')
    complex_place_379.longitude = Decimal('139.887626')
    complex_place_379.memo = None
    complex_place_379.name = '南房総国定公園 野島崎(白浜野島崎園地)'
    complex_place_379.venue = None
    complex_place_379 = importer.save_or_locate(complex_place_379)

    complex_place_380 = Place()
    complex_place_380.address = '千葉県南房総市  '
    complex_place_380.altitude = Decimal('0.000000')
    complex_place_380.latitude = Decimal('34.901727')
    complex_place_380.longitude = Decimal('139.888341')
    complex_place_380.memo = None
    complex_place_380.name = '野島埼灯台'
    complex_place_380.venue = None
    complex_place_380 = importer.save_or_locate(complex_place_380)

    complex_place_381 = Place()
    complex_place_381.address = '千葉県南房総市  '
    complex_place_381.altitude = Decimal('0.000000')
    complex_place_381.latitude = Decimal('34.900395')
    complex_place_381.longitude = Decimal('139.888076')
    complex_place_381.memo = None
    complex_place_381.name = '房総半島最南端之碑'
    complex_place_381.venue = None
    complex_place_381 = importer.save_or_locate(complex_place_381)

    complex_place_382 = Place()
    complex_place_382.address = '千葉県南房総市  '
    complex_place_382.altitude = Decimal('0.000000')
    complex_place_382.latitude = Decimal('34.900221')
    complex_place_382.longitude = Decimal('139.888202')
    complex_place_382.memo = None
    complex_place_382.name = '朝日と夕日の見えるベンチ'
    complex_place_382.venue = None
    complex_place_382 = importer.save_or_locate(complex_place_382)

    complex_place_383 = Place()
    complex_place_383.address = '三重県鈴鹿市 白子本町17 '
    complex_place_383.altitude = Decimal('0.000000')
    complex_place_383.latitude = Decimal('34.830866')
    complex_place_383.longitude = Decimal('136.592541')
    complex_place_383.memo = None
    complex_place_383.name = '白子漁港'
    complex_place_383.venue = None
    complex_place_383 = importer.save_or_locate(complex_place_383)

    complex_place_384 = Place()
    complex_place_384.address = '三重県鈴鹿市 白子一丁目6277 '
    complex_place_384.altitude = Decimal('0.000000')
    complex_place_384.latitude = Decimal('34.827719')
    complex_place_384.longitude = Decimal('136.591964')
    complex_place_384.memo = None
    complex_place_384.name = '鈴鹿市漁業協同組合直販所 魚魚鈴(ととりん)'
    complex_place_384.venue = None
    complex_place_384 = importer.save_or_locate(complex_place_384)

    complex_place_385 = Place()
    complex_place_385.address = '岡山県岡山市 北区 駅元町11'
    complex_place_385.altitude = Decimal('0.000000')
    complex_place_385.latitude = Decimal('34.666121')
    complex_place_385.longitude = Decimal('133.917733')
    complex_place_385.memo = None
    complex_place_385.name = '岡山駅'
    complex_place_385.venue = None
    complex_place_385 = importer.save_or_locate(complex_place_385)

    complex_place_386 = Place()
    complex_place_386.address = None
    complex_place_386.altitude = Decimal('0.000000')
    complex_place_386.latitude = Decimal('34.600000')
    complex_place_386.longitude = Decimal('136.716800')
    complex_place_386.memo = None
    complex_place_386.name = '第8旅 伊勢 (camera)'
    complex_place_386.venue = None
    complex_place_386 = importer.save_or_locate(complex_place_386)

    complex_place_387 = Place()
    complex_place_387.address = '三重県伊勢市 二見町茶屋562 '
    complex_place_387.altitude = Decimal('0.000000')
    complex_place_387.latitude = Decimal('34.509299')
    complex_place_387.longitude = Decimal('136.788328')
    complex_place_387.memo = None
    complex_place_387.name = '夫婦岩'
    complex_place_387.venue = None
    complex_place_387 = importer.save_or_locate(complex_place_387)

    complex_place_388 = Place()
    complex_place_388.address = '三重県伊勢市 二見町茶屋203 '
    complex_place_388.altitude = Decimal('0.000000')
    complex_place_388.latitude = Decimal('34.507308')
    complex_place_388.longitude = Decimal('136.777782')
    complex_place_388.memo = None
    complex_place_388.name = '（株）赤福 二見支店'
    complex_place_388.venue = None
    complex_place_388 = importer.save_or_locate(complex_place_388)

    complex_place_389 = Place()
    complex_place_389.address = '三重県伊勢市 二見町三津48 '
    complex_place_389.altitude = Decimal('0.000000')
    complex_place_389.latitude = Decimal('34.503981')
    complex_place_389.longitude = Decimal('136.777085')
    complex_place_389.memo = None
    complex_place_389.name = '二見浦駅'
    complex_place_389.venue = None
    complex_place_389 = importer.save_or_locate(complex_place_389)

    complex_place_390 = Place()
    complex_place_390.address = '三重県伊勢市 吹上一丁目1 '
    complex_place_390.altitude = Decimal('0.000000')
    complex_place_390.latitude = Decimal('34.491055')
    complex_place_390.longitude = Decimal('136.709700')
    complex_place_390.memo = None
    complex_place_390.name = '伊勢市駅'
    complex_place_390.venue = None
    complex_place_390 = importer.save_or_locate(complex_place_390)

    complex_place_391 = Place()
    complex_place_391.address = '三重県伊勢市 本町18 '
    complex_place_391.altitude = Decimal('0.000000')
    complex_place_391.latitude = Decimal('34.489292')
    complex_place_391.longitude = Decimal('136.707954')
    complex_place_391.memo = None
    complex_place_391.name = '伊勢菊一'
    complex_place_391.venue = None
    complex_place_391 = importer.save_or_locate(complex_place_391)

    complex_place_392 = Place()
    complex_place_392.address = '三重県伊勢市 本町13 '
    complex_place_392.altitude = Decimal('0.000000')
    complex_place_392.latitude = Decimal('34.488500')
    complex_place_392.longitude = Decimal('136.707089')
    complex_place_392.memo = None
    complex_place_392.name = '若松屋 外宮前店'
    complex_place_392.venue = None
    complex_place_392 = importer.save_or_locate(complex_place_392)

    complex_place_393 = Place()
    complex_place_393.address = '三重県伊勢市 本町16 '
    complex_place_393.altitude = Decimal('0.000000')
    complex_place_393.latitude = Decimal('34.487154')
    complex_place_393.longitude = Decimal('136.702923')
    complex_place_393.memo = None
    complex_place_393.name = '伊勢神宮 外宮'
    complex_place_393.venue = None
    complex_place_393 = importer.save_or_locate(complex_place_393)

    complex_place_394 = Place()
    complex_place_394.address = '三重県鳥羽市 鳥羽一丁目8 '
    complex_place_394.altitude = Decimal('0.000000')
    complex_place_394.latitude = Decimal('34.486767')
    complex_place_394.longitude = Decimal('136.843126')
    complex_place_394.memo = None
    complex_place_394.name = '鳥羽駅'
    complex_place_394.venue = None
    complex_place_394 = importer.save_or_locate(complex_place_394)

    complex_place_395 = Place()
    complex_place_395.address = '三重県伊勢市 岡本一丁目2 '
    complex_place_395.altitude = Decimal('0.000000')
    complex_place_395.latitude = Decimal('34.486276')
    complex_place_395.longitude = Decimal('136.707316')
    complex_place_395.memo = None
    complex_place_395.name = '豐川茜稻荷神社（茜社）'
    complex_place_395.venue = None
    complex_place_395 = importer.save_or_locate(complex_place_395)

    complex_place_396 = Place()
    complex_place_396.address = '三重県鳥羽市 鳥羽一丁目9 '
    complex_place_396.altitude = Decimal('0.000000')
    complex_place_396.latitude = Decimal('34.485370')
    complex_place_396.longitude = Decimal('136.844458')
    complex_place_396.memo = None
    complex_place_396.name = '赤福 鳥羽支店'
    complex_place_396.venue = None
    complex_place_396 = importer.save_or_locate(complex_place_396)

    complex_place_397 = Place()
    complex_place_397.address = '三重県鳥羽市 鳥羽一丁目6 '
    complex_place_397.altitude = Decimal('0.000000')
    complex_place_397.latitude = Decimal('34.484743')
    complex_place_397.longitude = Decimal('136.843962')
    complex_place_397.memo = None
    complex_place_397.name = '海月'
    complex_place_397.venue = None
    complex_place_397 = importer.save_or_locate(complex_place_397)

    complex_place_398 = Place()
    complex_place_398.address = '三重県伊勢市 宇治今在家町64 '
    complex_place_398.altitude = Decimal('0.000000')
    complex_place_398.latitude = Decimal('34.459555')
    complex_place_398.longitude = Decimal('136.723090')
    complex_place_398.memo = None
    complex_place_398.name = '赤福 内宮前支店'
    complex_place_398.venue = None
    complex_place_398 = importer.save_or_locate(complex_place_398)

    complex_place_399 = Place()
    complex_place_399.address = '三重県伊勢市 宇治館町98 '
    complex_place_399.altitude = Decimal('0.000000')
    complex_place_399.latitude = Decimal('34.455010')
    complex_place_399.longitude = Decimal('136.725793')
    complex_place_399.memo = None
    complex_place_399.name = '伊勢神宮'
    complex_place_399.venue = None
    complex_place_399 = importer.save_or_locate(complex_place_399)

    complex_place_400 = Place()
    complex_place_400.address = None
    complex_place_400.altitude = Decimal('0.000000')
    complex_place_400.latitude = Decimal('34.445900')
    complex_place_400.longitude = Decimal('134.024900')
    complex_place_400.memo = None
    complex_place_400.name = '第4旅 高松 (camera)'
    complex_place_400.venue = None
    complex_place_400 = importer.save_or_locate(complex_place_400)

    complex_place_401 = Place()
    complex_place_401.address = '広島県尾道市 東土堂町20 '
    complex_place_401.altitude = Decimal('0.000000')
    complex_place_401.latitude = Decimal('34.410686')
    complex_place_401.longitude = Decimal('133.196960')
    complex_place_401.memo = None
    complex_place_401.name = '頂上展望台'
    complex_place_401.venue = None
    complex_place_401 = importer.save_or_locate(complex_place_401)

    complex_place_402 = Place()
    complex_place_402.address = '広島県尾道市 東土堂町5 '
    complex_place_402.altitude = Decimal('0.000000')
    complex_place_402.latitude = Decimal('34.409783')
    complex_place_402.longitude = Decimal('133.197636')
    complex_place_402.memo = None
    complex_place_402.name = '鼓岩（付近）'
    complex_place_402.venue = None
    complex_place_402 = importer.save_or_locate(complex_place_402)

    complex_place_403 = Place()
    complex_place_403.address = '広島県尾道市 東土堂町2 '
    complex_place_403.altitude = Decimal('0.000000')
    complex_place_403.latitude = Decimal('34.408182')
    complex_place_403.longitude = Decimal('133.197812')
    complex_place_403.memo = None
    complex_place_403.name = '清浄山光明寺'
    complex_place_403.venue = None
    complex_place_403 = importer.save_or_locate(complex_place_403)

    complex_place_404 = Place()
    complex_place_404.address = '広島県尾道市 土堂一丁目11 '
    complex_place_404.altitude = Decimal('0.000000')
    complex_place_404.latitude = Decimal('34.405826')
    complex_place_404.longitude = Decimal('133.196029')
    complex_place_404.memo = None
    complex_place_404.name = '尾道ラーメン日乃出食堂'
    complex_place_404.venue = None
    complex_place_404 = importer.save_or_locate(complex_place_404)

    complex_place_405 = Place()
    complex_place_405.address = '広島県尾道市 東御所町1 '
    complex_place_405.altitude = Decimal('0.000000')
    complex_place_405.latitude = Decimal('34.404865')
    complex_place_405.longitude = Decimal('133.193159')
    complex_place_405.memo = None
    complex_place_405.name = '尾道駅'
    complex_place_405.venue = None
    complex_place_405 = importer.save_or_locate(complex_place_405)

    complex_place_406 = Place()
    complex_place_406.address = '広島県広島市 東区 二葉の里三丁目5'
    complex_place_406.altitude = Decimal('0.000000')
    complex_place_406.latitude = Decimal('34.399924')
    complex_place_406.longitude = Decimal('132.475820')
    complex_place_406.memo = None
    complex_place_406.name = '広島テレビ放送'
    complex_place_406.venue = None
    complex_place_406 = importer.save_or_locate(complex_place_406)

    complex_place_407 = Place()
    complex_place_407.address = '広島県広島市 南区 松原町1'
    complex_place_407.altitude = Decimal('0.000000')
    complex_place_407.latitude = Decimal('34.397667')
    complex_place_407.longitude = Decimal('132.475379')
    complex_place_407.memo = None
    complex_place_407.name = '広島駅'
    complex_place_407.venue = None
    complex_place_407 = importer.save_or_locate(complex_place_407)

    complex_place_408 = Place()
    complex_place_408.address = '香川県高松市 牟礼町牟礼3416 '
    complex_place_408.altitude = Decimal('0.000000')
    complex_place_408.latitude = Decimal('34.359907')
    complex_place_408.longitude = Decimal('134.139879')
    complex_place_408.memo = None
    complex_place_408.name = '八栗寺'
    complex_place_408.venue = None
    complex_place_408 = importer.save_or_locate(complex_place_408)

    complex_place_409 = Place()
    complex_place_409.address = '香川県高松市 牟礼町牟礼3369 '
    complex_place_409.altitude = Decimal('0.000000')
    complex_place_409.latitude = Decimal('34.355133')
    complex_place_409.longitude = Decimal('134.133654')
    complex_place_409.memo = None
    complex_place_409.name = '八栗ケーブル'
    complex_place_409.venue = None
    complex_place_409 = importer.save_or_locate(complex_place_409)

    complex_place_410 = Place()
    complex_place_410.address = '香川県高松市 牟礼町牟礼3128 '
    complex_place_410.altitude = Decimal('0.000000')
    complex_place_410.latitude = Decimal('34.353254')
    complex_place_410.longitude = Decimal('134.129625')
    complex_place_410.memo = None
    complex_place_410.name = 'うどん本陣 山田家'
    complex_place_410.venue = None
    complex_place_410 = importer.save_or_locate(complex_place_410)

    complex_place_411 = Place()
    complex_place_411.address = None
    complex_place_411.altitude = Decimal('0.000000')
    complex_place_411.latitude = Decimal('34.353000')
    complex_place_411.longitude = Decimal('132.811400')
    complex_place_411.memo = None
    complex_place_411.name = '第9旅 広島後編 (camera)'
    complex_place_411.venue = None
    complex_place_411 = importer.save_or_locate(complex_place_411)

    complex_place_412 = Place()
    complex_place_412.address = '香川県高松市 寿町一丁目5 '
    complex_place_412.altitude = Decimal('0.000000')
    complex_place_412.latitude = Decimal('34.350757')
    complex_place_412.longitude = Decimal('134.049468')
    complex_place_412.memo = None
    complex_place_412.name = '高松築港駅'
    complex_place_412.venue = None
    complex_place_412 = importer.save_or_locate(complex_place_412)

    complex_place_413 = Place()
    complex_place_413.address = '香川県高松市 西の丸町2 '
    complex_place_413.altitude = Decimal('0.000000')
    complex_place_413.latitude = Decimal('34.350451')
    complex_place_413.longitude = Decimal('134.047056')
    complex_place_413.memo = None
    complex_place_413.name = '高松駅'
    complex_place_413.venue = None
    complex_place_413 = importer.save_or_locate(complex_place_413)

    complex_place_414 = Place()
    complex_place_414.address = '香川県高松市 玉藻町2 '
    complex_place_414.altitude = Decimal('0.000000')
    complex_place_414.latitude = Decimal('34.350316')
    complex_place_414.longitude = Decimal('134.051619')
    complex_place_414.memo = None
    complex_place_414.name = '玉藻公園'
    complex_place_414.venue = None
    complex_place_414 = importer.save_or_locate(complex_place_414)

    complex_place_415 = Place()
    complex_place_415.address = '香川県高松市 西の丸町6 '
    complex_place_415.altitude = Decimal('0.000000')
    complex_place_415.latitude = Decimal('34.349793')
    complex_place_415.longitude = Decimal('134.046932')
    complex_place_415.memo = None
    complex_place_415.name = 'ルピナス'
    complex_place_415.venue = None
    complex_place_415 = importer.save_or_locate(complex_place_415)

    complex_place_416 = Place()
    complex_place_416.address = '香川県高松市 牟礼町牟礼2418 '
    complex_place_416.altitude = Decimal('0.000000')
    complex_place_416.latitude = Decimal('34.345598')
    complex_place_416.longitude = Decimal('134.122319')
    complex_place_416.memo = None
    complex_place_416.name = '総門跡'
    complex_place_416.venue = None
    complex_place_416 = importer.save_or_locate(complex_place_416)

    complex_place_417 = Place()
    complex_place_417.address = '香川県高松市 牟礼町牟礼2210 '
    complex_place_417.altitude = Decimal('0.000000')
    complex_place_417.latitude = Decimal('34.344637')
    complex_place_417.longitude = Decimal('134.122008')
    complex_place_417.memo = None
    complex_place_417.name = '八栗駅'
    complex_place_417.venue = None
    complex_place_417 = importer.save_or_locate(complex_place_417)

    complex_place_418 = Place()
    complex_place_418.address = '香川県高松市 栗林町一丁目20 '
    complex_place_418.altitude = Decimal('0.000000')
    complex_place_418.latitude = Decimal('34.329384')
    complex_place_418.longitude = Decimal('134.044534')
    complex_place_418.memo = None
    complex_place_418.name = '栗林公園'
    complex_place_418.venue = None
    complex_place_418 = importer.save_or_locate(complex_place_418)

    complex_place_419 = Place()
    complex_place_419.address = None
    complex_place_419.altitude = Decimal('0.000000')
    complex_place_419.latitude = Decimal('34.314100')
    complex_place_419.longitude = Decimal('132.370000')
    complex_place_419.memo = None
    complex_place_419.name = '第9旅 広島前編 (camera)'
    complex_place_419.venue = None
    complex_place_419 = importer.save_or_locate(complex_place_419)

    complex_place_420 = Place()
    complex_place_420.address = '広島県廿日市市 宮島口一丁目3 '
    complex_place_420.altitude = Decimal('0.000000')
    complex_place_420.latitude = Decimal('34.312017')
    complex_place_420.longitude = Decimal('132.302931')
    complex_place_420.memo = None
    complex_place_420.name = '宮島口駅'
    complex_place_420.venue = None
    complex_place_420 = importer.save_or_locate(complex_place_420)

    complex_place_421 = Place()
    complex_place_421.address = '広島県廿日市市 宮島口一丁目5 '
    complex_place_421.altitude = Decimal('0.000000')
    complex_place_421.latitude = Decimal('34.311502')
    complex_place_421.longitude = Decimal('132.303511')
    complex_place_421.memo = None
    complex_place_421.name = 'あなごめし うえの 宮島口本店'
    complex_place_421.venue = None
    complex_place_421 = importer.save_or_locate(complex_place_421)

    complex_place_422 = Place()
    complex_place_422.address = '広島県廿日市市 宮島町873 '
    complex_place_422.altitude = Decimal('0.000000')
    complex_place_422.latitude = Decimal('34.302086')
    complex_place_422.longitude = Decimal('132.322215')
    complex_place_422.memo = None
    complex_place_422.name = '宮島桟橋'
    complex_place_422.venue = None
    complex_place_422 = importer.save_or_locate(complex_place_422)

    complex_place_423 = Place()
    complex_place_423.address = '広島県廿日市市 宮島町幸町西浜459 '
    complex_place_423.altitude = Decimal('0.000000')
    complex_place_423.latitude = Decimal('34.297787')
    complex_place_423.longitude = Decimal('132.320873')
    complex_place_423.memo = None
    complex_place_423.name = 'もみじ堂本店'
    complex_place_423.venue = None
    complex_place_423 = importer.save_or_locate(complex_place_423)

    complex_place_424 = Place()
    complex_place_424.address = '  '
    complex_place_424.altitude = Decimal('0.000000')
    complex_place_424.latitude = Decimal('34.297309')
    complex_place_424.longitude = Decimal('132.318128')
    complex_place_424.memo = None
    complex_place_424.name = '嚴島神社 大鳥居（布の中）'
    complex_place_424.venue = None
    complex_place_424 = importer.save_or_locate(complex_place_424)

    complex_place_425 = Place()
    complex_place_425.address = '  '
    complex_place_425.altitude = Decimal('0.000000')
    complex_place_425.latitude = Decimal('34.295988')
    complex_place_425.longitude = Decimal('132.319826')
    complex_place_425.memo = None
    complex_place_425.name = '嚴島神社'
    complex_place_425.venue = None
    complex_place_425 = importer.save_or_locate(complex_place_425)

    complex_place_426 = Place()
    complex_place_426.address = '広島県廿日市市 宮島町滝町215 '
    complex_place_426.altitude = Decimal('0.000000')
    complex_place_426.latitude = Decimal('34.292048')
    complex_place_426.longitude = Decimal('132.318474')
    complex_place_426.memo = None
    complex_place_426.name = '大聖院'
    complex_place_426.venue = None
    complex_place_426 = importer.save_or_locate(complex_place_426)

    complex_place_427 = Place()
    complex_place_427.address = '広島県呉市 宝町2 '
    complex_place_427.altitude = Decimal('0.000000')
    complex_place_427.latitude = Decimal('34.244647')
    complex_place_427.longitude = Decimal('132.557585')
    complex_place_427.memo = None
    complex_place_427.name = '呉駅'
    complex_place_427.venue = None
    complex_place_427 = importer.save_or_locate(complex_place_427)

    complex_place_428 = Place()
    complex_place_428.address = '広島県呉市 宝町2 '
    complex_place_428.altitude = Decimal('0.000000')
    complex_place_428.latitude = Decimal('34.243133')
    complex_place_428.longitude = Decimal('132.558639')
    complex_place_428.memo = None
    complex_place_428.name = 'コンフォートホテル呉'
    complex_place_428.venue = None
    complex_place_428 = importer.save_or_locate(complex_place_428)

    complex_place_429 = Place()
    complex_place_429.address = '広島県呉市 宝町4 '
    complex_place_429.altitude = Decimal('0.000000')
    complex_place_429.latitude = Decimal('34.241557')
    complex_place_429.longitude = Decimal('132.557416')
    complex_place_429.memo = None
    complex_place_429.name = '日招きの里 呉ハイカラ食堂'
    complex_place_429.venue = None
    complex_place_429 = importer.save_or_locate(complex_place_429)

    complex_place_430 = Place()
    complex_place_430.address = '広島県呉市 宝町4 '
    complex_place_430.altitude = Decimal('0.000000')
    complex_place_430.latitude = Decimal('34.241139')
    complex_place_430.longitude = Decimal('132.555856')
    complex_place_430.memo = None
    complex_place_430.name = '大和ミュージアム（呉市海事歴史科学館）'
    complex_place_430.venue = None
    complex_place_430 = importer.save_or_locate(complex_place_430)

    complex_place_431 = Place()
    complex_place_431.address = '広島県呉市 宝町4 '
    complex_place_431.altitude = Decimal('0.000000')
    complex_place_431.latitude = Decimal('34.240558')
    complex_place_431.longitude = Decimal('132.556432')
    complex_place_431.memo = None
    complex_place_431.name = '呉湾艦船めぐり'
    complex_place_431.venue = None
    complex_place_431 = importer.save_or_locate(complex_place_431)

    complex_place_432 = Place()
    complex_place_432.address = ''
    complex_place_432.altitude = Decimal('0.000000')
    complex_place_432.latitude = Decimal('34.236919')
    complex_place_432.longitude = Decimal('134.642387')
    complex_place_432.memo = None
    complex_place_432.name = '名勝 鳴門 碑'
    complex_place_432.venue = None
    complex_place_432 = importer.save_or_locate(complex_place_432)

    complex_place_433 = Place()
    complex_place_433.address = ''
    complex_place_433.altitude = Decimal('0.000000')
    complex_place_433.latitude = Decimal('34.236170')
    complex_place_433.longitude = Decimal('134.641982')
    complex_place_433.memo = None
    complex_place_433.name = '大鳴門橋遊歩道 渦の道'
    complex_place_433.venue = None
    complex_place_433 = importer.save_or_locate(complex_place_433)

    complex_place_434 = Place()
    complex_place_434.address = ''
    complex_place_434.altitude = Decimal('0.000000')
    complex_place_434.latitude = Decimal('34.234161')
    complex_place_434.longitude = Decimal('134.640330')
    complex_place_434.memo = None
    complex_place_434.name = '渦見茶屋'
    complex_place_434.venue = None
    complex_place_434 = importer.save_or_locate(complex_place_434)

    complex_place_435 = Place()
    complex_place_435.address = ''
    complex_place_435.altitude = Decimal('0.000000')
    complex_place_435.latitude = Decimal('34.127454')
    complex_place_435.longitude = Decimal('133.022041')
    complex_place_435.memo = None
    complex_place_435.name = '道の駅 よしうみいきいき館'
    complex_place_435.venue = None
    complex_place_435 = importer.save_or_locate(complex_place_435)

    complex_place_436 = Place()
    complex_place_436.address = ''
    complex_place_436.altitude = Decimal('0.000000')
    complex_place_436.latitude = Decimal('34.127112')
    complex_place_436.longitude = Decimal('133.023994')
    complex_place_436.memo = None
    complex_place_436.name = 'さすが、ぢーちゃん・・・'
    complex_place_436.venue = None
    complex_place_436 = importer.save_or_locate(complex_place_436)

    complex_place_437 = Place()
    complex_place_437.address = ''
    complex_place_437.altitude = Decimal('0.000000')
    complex_place_437.latitude = Decimal('34.118533')
    complex_place_437.longitude = Decimal('132.992699')
    complex_place_437.memo = None
    complex_place_437.name = '来島海峡大橋'
    complex_place_437.venue = None
    complex_place_437 = importer.save_or_locate(complex_place_437)

    complex_place_438 = Place()
    complex_place_438.address = ''
    complex_place_438.altitude = Decimal('0.000000')
    complex_place_438.latitude = Decimal('34.115441')
    complex_place_438.longitude = Decimal('132.984908')
    complex_place_438.memo = None
    complex_place_438.name = '来島海峡第三大橋'
    complex_place_438.venue = None
    complex_place_438 = importer.save_or_locate(complex_place_438)

    complex_place_439 = Place()
    complex_place_439.address = ''
    complex_place_439.altitude = Decimal('0.000000')
    complex_place_439.latitude = Decimal('34.114019')
    complex_place_439.longitude = Decimal('132.977834')
    complex_place_439.memo = None
    complex_place_439.name = '来島海峡展望館'
    complex_place_439.venue = None
    complex_place_439 = importer.save_or_locate(complex_place_439)

    complex_place_440 = Place()
    complex_place_440.address = ''
    complex_place_440.altitude = Decimal('0.000000')
    complex_place_440.latitude = Decimal('34.111737')
    complex_place_440.longitude = Decimal('132.976139')
    complex_place_440.memo = None
    complex_place_440.name = 'のぼったね〜'
    complex_place_440.venue = None
    complex_place_440 = importer.save_or_locate(complex_place_440)

    complex_place_441 = Place()
    complex_place_441.address = ''
    complex_place_441.altitude = Decimal('0.000000')
    complex_place_441.latitude = Decimal('34.111409')
    complex_place_441.longitude = Decimal('132.976498')
    complex_place_441.memo = None
    complex_place_441.name = '橋リベンジしたいんです！'
    complex_place_441.venue = None
    complex_place_441 = importer.save_or_locate(complex_place_441)

    complex_place_442 = Place()
    complex_place_442.address = ''
    complex_place_442.altitude = Decimal('0.000000')
    complex_place_442.latitude = Decimal('34.111239')
    complex_place_442.longitude = Decimal('132.975950')
    complex_place_442.memo = None
    complex_place_442.name = 'しまなみ海道来島海峡第三大橋原付入口'
    complex_place_442.venue = None
    complex_place_442 = importer.save_or_locate(complex_place_442)

    complex_place_443 = Place()
    complex_place_443.address = ''
    complex_place_443.altitude = Decimal('0.000000')
    complex_place_443.latitude = Decimal('34.108893')
    complex_place_443.longitude = Decimal('132.975900')
    complex_place_443.memo = None
    complex_place_443.name = '本当に昨日見た橋に行くの〜？'
    complex_place_443.venue = None
    complex_place_443 = importer.save_or_locate(complex_place_443)

    complex_place_444 = Place()
    complex_place_444.address = None
    complex_place_444.altitude = Decimal('0.000000')
    complex_place_444.latitude = Decimal('34.105000')
    complex_place_444.longitude = Decimal('132.977100')
    complex_place_444.memo = None
    complex_place_444.name = '第27旅 愛媛 (camera)'
    complex_place_444.venue = None
    complex_place_444 = importer.save_or_locate(complex_place_444)

    complex_place_445 = Place()
    complex_place_445.address = ''
    complex_place_445.altitude = Decimal('0.000000')
    complex_place_445.latitude = Decimal('34.074457')
    complex_place_445.longitude = Decimal('134.551357')
    complex_place_445.memo = None
    complex_place_445.name = '徳島駅'
    complex_place_445.venue = None
    complex_place_445 = importer.save_or_locate(complex_place_445)

    complex_place_446 = Place()
    complex_place_446.address = ''
    complex_place_446.altitude = Decimal('0.000000')
    complex_place_446.latitude = Decimal('34.074102')
    complex_place_446.longitude = Decimal('134.550276')
    complex_place_446.memo = None
    complex_place_446.name = '旅館組合 宿泊案内所 (観光案内はしません‼️)'
    complex_place_446.venue = None
    complex_place_446 = importer.save_or_locate(complex_place_446)

    complex_place_447 = Place()
    complex_place_447.address = ''
    complex_place_447.altitude = Decimal('0.000000')
    complex_place_447.latitude = Decimal('34.071527')
    complex_place_447.longitude = Decimal('134.548631')
    complex_place_447.memo = None
    complex_place_447.name = '新町橋'
    complex_place_447.venue = None
    complex_place_447 = importer.save_or_locate(complex_place_447)

    complex_place_448 = Place()
    complex_place_448.address = ''
    complex_place_448.altitude = Decimal('0.000000')
    complex_place_448.latitude = Decimal('34.071150')
    complex_place_448.longitude = Decimal('134.548539')
    complex_place_448.memo = None
    complex_place_448.name = 'ゆれる～'
    complex_place_448.venue = None
    complex_place_448 = importer.save_or_locate(complex_place_448)

    complex_place_449 = Place()
    complex_place_449.address = ''
    complex_place_449.altitude = Decimal('0.000000')
    complex_place_449.latitude = Decimal('34.069841')
    complex_place_449.longitude = Decimal('133.004898')
    complex_place_449.memo = None
    complex_place_449.name = '今治桟橋バス停'
    complex_place_449.venue = None
    complex_place_449 = importer.save_or_locate(complex_place_449)

    complex_place_450 = Place()
    complex_place_450.address = ''
    complex_place_450.altitude = Decimal('0.000000')
    complex_place_450.latitude = Decimal('34.068628')
    complex_place_450.longitude = Decimal('134.549089')
    complex_place_450.memo = None
    complex_place_450.name = '阿波おどり人形'
    complex_place_450.venue = None
    complex_place_450 = importer.save_or_locate(complex_place_450)

    complex_place_451 = Place()
    complex_place_451.address = ''
    complex_place_451.altitude = Decimal('0.000000')
    complex_place_451.latitude = Decimal('34.068563')
    complex_place_451.longitude = Decimal('134.549615')
    complex_place_451.memo = None
    complex_place_451.name = '銀座一福 本店'
    complex_place_451.venue = None
    complex_place_451 = importer.save_or_locate(complex_place_451)

    complex_place_452 = Place()
    complex_place_452.address = ''
    complex_place_452.altitude = Decimal('0.000000')
    complex_place_452.latitude = Decimal('34.068500')
    complex_place_452.longitude = Decimal('134.474384')
    complex_place_452.memo = None
    complex_place_452.name = '観音寺'
    complex_place_452.venue = None
    complex_place_452 = importer.save_or_locate(complex_place_452)

    complex_place_453 = Place()
    complex_place_453.address = ''
    complex_place_453.altitude = Decimal('0.000000')
    complex_place_453.latitude = Decimal('34.066597')
    complex_place_453.longitude = Decimal('133.008071')
    complex_place_453.memo = None
    complex_place_453.name = '今治港港湾緑地'
    complex_place_453.venue = None
    complex_place_453 = importer.save_or_locate(complex_place_453)

    complex_place_454 = Place()
    complex_place_454.address = ''
    complex_place_454.altitude = Decimal('0.000000')
    complex_place_454.latitude = Decimal('34.065365')
    complex_place_454.longitude = Decimal('133.007437')
    complex_place_454.memo = None
    complex_place_454.name = '恵美須町２丁目７−２'
    complex_place_454.venue = None
    complex_place_454 = importer.save_or_locate(complex_place_454)

    complex_place_455 = Place()
    complex_place_455.address = ''
    complex_place_455.altitude = Decimal('0.000000')
    complex_place_455.latitude = Decimal('34.064834')
    complex_place_455.longitude = Decimal('134.588910')
    complex_place_455.memo = None
    complex_place_455.name = 'モダンパック 徳島店'
    complex_place_455.venue = None
    complex_place_455 = importer.save_or_locate(complex_place_455)

    complex_place_456 = Place()
    complex_place_456.address = ''
    complex_place_456.altitude = Decimal('0.000000')
    complex_place_456.latitude = Decimal('34.064831')
    complex_place_456.longitude = Decimal('133.000015')
    complex_place_456.memo = None
    complex_place_456.name = 'アサイ薬局'
    complex_place_456.venue = None
    complex_place_456 = importer.save_or_locate(complex_place_456)

    complex_place_457 = Place()
    complex_place_457.address = ''
    complex_place_457.altitude = Decimal('0.000000')
    complex_place_457.latitude = Decimal('34.064348')
    complex_place_457.longitude = Decimal('132.998700')
    complex_place_457.memo = None
    complex_place_457.name = '白楽天 今治本店'
    complex_place_457.venue = None
    complex_place_457 = importer.save_or_locate(complex_place_457)

    complex_place_458 = Place()
    complex_place_458.address = ''
    complex_place_458.altitude = Decimal('0.000000')
    complex_place_458.latitude = Decimal('34.064251')
    complex_place_458.longitude = Decimal('132.994776')
    complex_place_458.memo = None
    complex_place_458.name = 'サイクルスタンド'
    complex_place_458.venue = None
    complex_place_458 = importer.save_or_locate(complex_place_458)

    complex_place_459 = Place()
    complex_place_459.address = ''
    complex_place_459.altitude = Decimal('0.000000')
    complex_place_459.latitude = Decimal('34.064205')
    complex_place_459.longitude = Decimal('132.993636')
    complex_place_459.memo = None
    complex_place_459.name = '今治駅'
    complex_place_459.venue = None
    complex_place_459 = importer.save_or_locate(complex_place_459)

    complex_place_460 = Place()
    complex_place_460.address = ''
    complex_place_460.altitude = Decimal('0.000000')
    complex_place_460.latitude = Decimal('34.063371')
    complex_place_460.longitude = Decimal('133.006779')
    complex_place_460.memo = None
    complex_place_460.name = '今治城'
    complex_place_460.venue = None
    complex_place_460 = importer.save_or_locate(complex_place_460)

    complex_place_461 = Place()
    complex_place_461.address = ''
    complex_place_461.altitude = Decimal('0.000000')
    complex_place_461.latitude = Decimal('34.062061')
    complex_place_461.longitude = Decimal('133.000585')
    complex_place_461.memo = None
    complex_place_461.name = '今治国際ホテル'
    complex_place_461.venue = None
    complex_place_461 = importer.save_or_locate(complex_place_461)

    complex_place_462 = Place()
    complex_place_462.address = ''
    complex_place_462.altitude = Decimal('0.000000')
    complex_place_462.latitude = Decimal('34.061682')
    complex_place_462.longitude = Decimal('134.587699')
    complex_place_462.memo = None
    complex_place_462.name = '谷川モータース'
    complex_place_462.venue = None
    complex_place_462 = importer.save_or_locate(complex_place_462)

    complex_place_463 = Place()
    complex_place_463.address = ''
    complex_place_463.altitude = Decimal('0.000000')
    complex_place_463.latitude = Decimal('34.058814')
    complex_place_463.longitude = Decimal('133.003632')
    complex_place_463.memo = None
    complex_place_463.name = '今治焼鳥 まる屋'
    complex_place_463.venue = None
    complex_place_463 = importer.save_or_locate(complex_place_463)

    complex_place_464 = Place()
    complex_place_464.address = ''
    complex_place_464.altitude = Decimal('0.000000')
    complex_place_464.latitude = Decimal('34.058791')
    complex_place_464.longitude = Decimal('133.004926')
    complex_place_464.memo = None
    complex_place_464.name = 'スーパーホテル今治'
    complex_place_464.venue = None
    complex_place_464 = importer.save_or_locate(complex_place_464)

    complex_place_465 = Place()
    complex_place_465.address = ''
    complex_place_465.altitude = Decimal('0.000000')
    complex_place_465.latitude = Decimal('34.058427')
    complex_place_465.longitude = Decimal('134.586274')
    complex_place_465.memo = None
    complex_place_465.name = '海女料理 ししくい'
    complex_place_465.venue = None
    complex_place_465 = importer.save_or_locate(complex_place_465)

    complex_place_466 = Place()
    complex_place_466.address = ''
    complex_place_466.altitude = Decimal('0.000000')
    complex_place_466.latitude = Decimal('34.055618')
    complex_place_466.longitude = Decimal('134.473635')
    complex_place_466.memo = None
    complex_place_466.name = '國分寺'
    complex_place_466.venue = None
    complex_place_466 = importer.save_or_locate(complex_place_466)

    complex_place_467 = Place()
    complex_place_467.address = '  '
    complex_place_467.altitude = Decimal('0.000000')
    complex_place_467.latitude = Decimal('34.054033')
    complex_place_467.longitude = Decimal('134.596643')
    complex_place_467.memo = None
    complex_place_467.name = 'オーシャン東九フェリー 徳島港 (沖洲) のりば'
    complex_place_467.venue = None
    complex_place_467 = importer.save_or_locate(complex_place_467)

    complex_place_468 = Place()
    complex_place_468.address = ''
    complex_place_468.altitude = Decimal('0.000000')
    complex_place_468.latitude = Decimal('34.053634')
    complex_place_468.longitude = Decimal('134.587296')
    complex_place_468.memo = None
    complex_place_468.name = '四国横断自動車道 徳島南部自動車道 新町川橋'
    complex_place_468.venue = None
    complex_place_468 = importer.save_or_locate(complex_place_468)

    complex_place_469 = Place()
    complex_place_469.address = ''
    complex_place_469.altitude = Decimal('0.000000')
    complex_place_469.latitude = Decimal('34.050299')
    complex_place_469.longitude = Decimal('134.475707')
    complex_place_469.memo = None
    complex_place_469.name = '常楽寺'
    complex_place_469.venue = None
    complex_place_469 = importer.save_or_locate(complex_place_469)

    complex_place_470 = Place()
    complex_place_470.address = None
    complex_place_470.altitude = Decimal('0.000000')
    complex_place_470.latitude = Decimal('34.043921')
    complex_place_470.longitude = Decimal('134.442508')
    complex_place_470.memo = None
    complex_place_470.name = '第26旅 徳島後編 (camera)'
    complex_place_470.venue = None
    complex_place_470 = importer.save_or_locate(complex_place_470)

    complex_place_471 = Place()
    complex_place_471.address = ''
    complex_place_471.altitude = Decimal('0.000000')
    complex_place_471.latitude = Decimal('34.038018')
    complex_place_471.longitude = Decimal('134.462856')
    complex_place_471.memo = None
    complex_place_471.name = '大日寺'
    complex_place_471.venue = None
    complex_place_471 = importer.save_or_locate(complex_place_471)

    complex_place_472 = Place()
    complex_place_472.address = ''
    complex_place_472.altitude = Decimal('0.000000')
    complex_place_472.latitude = Decimal('33.974011')
    complex_place_472.longitude = Decimal('134.370151')
    complex_place_472.memo = None
    complex_place_472.name = '神山温泉バス停'
    complex_place_472.venue = None
    complex_place_472 = importer.save_or_locate(complex_place_472)

    complex_place_473 = Place()
    complex_place_473.address = ''
    complex_place_473.altitude = Decimal('0.000000')
    complex_place_473.latitude = Decimal('33.971875')
    complex_place_473.longitude = Decimal('134.369995')
    complex_place_473.memo = None
    complex_place_473.name = '神山温泉ホテル四季の里＆いやしの湯'
    complex_place_473.venue = None
    complex_place_473 = importer.save_or_locate(complex_place_473)

    complex_place_474 = Place()
    complex_place_474.address = ''
    complex_place_474.altitude = Decimal('0.000000')
    complex_place_474.latitude = Decimal('33.970900')
    complex_place_474.longitude = Decimal('134.366872')
    complex_place_474.memo = None
    complex_place_474.name = '上一宮大粟神社'
    complex_place_474.venue = None
    complex_place_474 = importer.save_or_locate(complex_place_474)

    complex_place_475 = Place()
    complex_place_475.address = '福岡県北九州市 小倉北区 浅野二丁目14'
    complex_place_475.altitude = Decimal('0.000000')
    complex_place_475.latitude = Decimal('33.887012')
    complex_place_475.longitude = Decimal('130.884924')
    complex_place_475.memo = None
    complex_place_475.name = 'バジェット・レンタカー 小倉駅前店'
    complex_place_475.venue = None
    complex_place_475 = importer.save_or_locate(complex_place_475)

    complex_place_476 = Place()
    complex_place_476.address = '福岡県北九州市 小倉北区 京町三丁目8'
    complex_place_476.altitude = Decimal('0.000000')
    complex_place_476.latitude = Decimal('33.886968')
    complex_place_476.longitude = Decimal('130.882576')
    complex_place_476.memo = None
    complex_place_476.name = '小倉駅'
    complex_place_476.venue = None
    complex_place_476 = importer.save_or_locate(complex_place_476)

    complex_place_477 = Place()
    complex_place_477.address = '和歌山県田辺市 本宮町本宮 '
    complex_place_477.altitude = Decimal('0.000000')
    complex_place_477.latitude = Decimal('33.840571')
    complex_place_477.longitude = Decimal('135.773475')
    complex_place_477.memo = None
    complex_place_477.name = '熊野本宮大社'
    complex_place_477.venue = None
    complex_place_477 = importer.save_or_locate(complex_place_477)

    complex_place_478 = Place()
    complex_place_478.address = '和歌山県田辺市 本宮町本宮 '
    complex_place_478.altitude = Decimal('0.000000')
    complex_place_478.latitude = Decimal('33.834421')
    complex_place_478.longitude = Decimal('135.772393')
    complex_place_478.memo = None
    complex_place_478.name = 'くまのこ食堂'
    complex_place_478.venue = None
    complex_place_478 = importer.save_or_locate(complex_place_478)

    complex_place_479 = Place()
    complex_place_479.address = None
    complex_place_479.altitude = Decimal('0.000000')
    complex_place_479.latitude = Decimal('33.748300')
    complex_place_479.longitude = Decimal('135.797700')
    complex_place_479.memo = None
    complex_place_479.name = '第11旅 和歌山 (camera)'
    complex_place_479.venue = None
    complex_place_479 = importer.save_or_locate(complex_place_479)

    complex_place_480 = Place()
    complex_place_480.address = '和歌山県新宮市 徐福一丁目3 '
    complex_place_480.altitude = Decimal('0.000000')
    complex_place_480.latitude = Decimal('33.725424')
    complex_place_480.longitude = Decimal('135.994697')
    complex_place_480.memo = None
    complex_place_480.name = '新宮市観光協会 shingu tourist information centre'
    complex_place_480.venue = None
    complex_place_480 = importer.save_or_locate(complex_place_480)

    complex_place_481 = Place()
    complex_place_481.address = '和歌山県新宮市 徐福一丁目3 '
    complex_place_481.altitude = Decimal('0.000000')
    complex_place_481.latitude = Decimal('33.725151')
    complex_place_481.longitude = Decimal('135.994147')
    complex_place_481.memo = None
    complex_place_481.name = '新宮駅'
    complex_place_481.venue = None
    complex_place_481 = importer.save_or_locate(complex_place_481)

    complex_place_482 = Place()
    complex_place_482.address = None
    complex_place_482.altitude = Decimal('0.000000')
    complex_place_482.latitude = Decimal('33.606600')
    complex_place_482.longitude = Decimal('131.205600')
    complex_place_482.memo = None
    complex_place_482.name = '第17旅 九州後編 (camera)'
    complex_place_482.venue = None
    complex_place_482 = importer.save_or_locate(complex_place_482)

    complex_place_483 = Place()
    complex_place_483.address = '高知県南国市 駅前町二丁目3 '
    complex_place_483.altitude = Decimal('0.000000')
    complex_place_483.latitude = Decimal('33.579140')
    complex_place_483.longitude = Decimal('133.645406')
    complex_place_483.memo = None
    complex_place_483.name = '後免駅'
    complex_place_483.venue = None
    complex_place_483 = importer.save_or_locate(complex_place_483)

    complex_place_484 = Place()
    complex_place_484.address = '高知県南国市 駅前町二丁目3 '
    complex_place_484.altitude = Decimal('0.000000')
    complex_place_484.latitude = Decimal('33.578833')
    complex_place_484.longitude = Decimal('133.645819')
    complex_place_484.memo = None
    complex_place_484.name = '師匠はよしてって～'
    complex_place_484.venue = None
    complex_place_484 = importer.save_or_locate(complex_place_484)

    complex_place_485 = Place()
    complex_place_485.address = '高知県南国市 駅前町二丁目3 '
    complex_place_485.altitude = Decimal('0.000000')
    complex_place_485.latitude = Decimal('33.578697')
    complex_place_485.longitude = Decimal('133.645386')
    complex_place_485.memo = None
    complex_place_485.name = 'ショッピングセンター パステポコ・ア・ポコ南国店'
    complex_place_485.venue = None
    complex_place_485 = importer.save_or_locate(complex_place_485)

    complex_place_486 = Place()
    complex_place_486.address = '高知県南国市 後免町一丁目4 '
    complex_place_486.altitude = Decimal('0.000000')
    complex_place_486.latitude = Decimal('33.577017')
    complex_place_486.longitude = Decimal('133.644535')
    complex_place_486.memo = None
    complex_place_486.name = 'たかはし'
    complex_place_486.venue = None
    complex_place_486 = importer.save_or_locate(complex_place_486)

    complex_place_487 = Place()
    complex_place_487.address = '高知県南国市 日吉町一丁目2 '
    complex_place_487.altitude = Decimal('0.000000')
    complex_place_487.latitude = Decimal('33.577010')
    complex_place_487.longitude = Decimal('133.643707')
    complex_place_487.memo = None
    complex_place_487.name = '日吉神社'
    complex_place_487.venue = None
    complex_place_487 = importer.save_or_locate(complex_place_487)

    complex_place_488 = Place()
    complex_place_488.address = '高知県南国市 篠原1795 '
    complex_place_488.altitude = Decimal('0.000000')
    complex_place_488.latitude = Decimal('33.576415')
    complex_place_488.longitude = Decimal('133.638078')
    complex_place_488.memo = None
    complex_place_488.name = '東工業前駅'
    complex_place_488.venue = None
    complex_place_488 = importer.save_or_locate(complex_place_488)

    complex_place_489 = Place()
    complex_place_489.address = '高知県南国市 後免町144 '
    complex_place_489.altitude = Decimal('0.000000')
    complex_place_489.latitude = Decimal('33.575130')
    complex_place_489.longitude = Decimal('133.644001')
    complex_place_489.memo = None
    complex_place_489.name = 'サンシャイン カルディア店'
    complex_place_489.venue = None
    complex_place_489 = importer.save_or_locate(complex_place_489)

    complex_place_490 = Place()
    complex_place_490.address = '大分県国東市  '
    complex_place_490.altitude = Decimal('0.000000')
    complex_place_490.latitude = Decimal('33.574001')
    complex_place_490.longitude = Decimal('131.603241')
    complex_place_490.memo = None
    complex_place_490.name = '両子寺'
    complex_place_490.venue = None
    complex_place_490 = importer.save_or_locate(complex_place_490)

    complex_place_491 = Place()
    complex_place_491.address = '大分県国東市  '
    complex_place_491.altitude = Decimal('0.000000')
    complex_place_491.latitude = Decimal('33.572880')
    complex_place_491.longitude = Decimal('131.604622')
    complex_place_491.memo = None
    complex_place_491.name = '両子寺 仁王'
    complex_place_491.venue = None
    complex_place_491 = importer.save_or_locate(complex_place_491)

    complex_place_492 = Place()
    complex_place_492.address = '高知県高知市 栄田町二丁目1 '
    complex_place_492.altitude = Decimal('0.000000')
    complex_place_492.latitude = Decimal('33.567227')
    complex_place_492.longitude = Decimal('133.543645')
    complex_place_492.memo = None
    complex_place_492.name = '高知駅'
    complex_place_492.venue = None
    complex_place_492 = importer.save_or_locate(complex_place_492)

    complex_place_493 = Place()
    complex_place_493.address = '高知県高知市 北本町二丁目10 '
    complex_place_493.altitude = Decimal('0.000000')
    complex_place_493.latitude = Decimal('33.566418')
    complex_place_493.longitude = Decimal('133.543025')
    complex_place_493.memo = None
    complex_place_493.name = '土佐三志士の像'
    complex_place_493.venue = None
    complex_place_493 = importer.save_or_locate(complex_place_493)

    complex_place_494 = Place()
    complex_place_494.address = '高知県高知市 はりまや町一丁目1 '
    complex_place_494.altitude = Decimal('0.000000')
    complex_place_494.latitude = Decimal('33.559944')
    complex_place_494.longitude = Decimal('133.542657')
    complex_place_494.memo = None
    complex_place_494.name = 'はりまや橋'
    complex_place_494.venue = None
    complex_place_494 = importer.save_or_locate(complex_place_494)

    complex_place_495 = Place()
    complex_place_495.address = None
    complex_place_495.altitude = Decimal('0.000000')
    complex_place_495.latitude = Decimal('33.555746')
    complex_place_495.longitude = Decimal('133.773484')
    complex_place_495.memo = None
    complex_place_495.name = '第20旅 高知後編 (camera)'
    complex_place_495.venue = None
    complex_place_495 = importer.save_or_locate(complex_place_495)

    complex_place_496 = Place()
    complex_place_496.address = '高知県高知市 桟橋通五丁目3 '
    complex_place_496.altitude = Decimal('0.000000')
    complex_place_496.latitude = Decimal('33.540476')
    complex_place_496.longitude = Decimal('133.552751')
    complex_place_496.memo = None
    complex_place_496.name = '桟橋通五丁目駅'
    complex_place_496.venue = None
    complex_place_496 = importer.save_or_locate(complex_place_496)

    complex_place_497 = Place()
    complex_place_497.address = '高知県高知市 孕西町214 '
    complex_place_497.altitude = Decimal('0.000000')
    complex_place_497.latitude = Decimal('33.537381')
    complex_place_497.longitude = Decimal('133.550542')
    complex_place_497.memo = None
    complex_place_497.name = 'ホームセンターブリコ 桟橋店'
    complex_place_497.venue = None
    complex_place_497 = importer.save_or_locate(complex_place_497)

    complex_place_498 = Place()
    complex_place_498.address = None
    complex_place_498.altitude = Decimal('0.000000')
    complex_place_498.latitude = Decimal('33.532182')
    complex_place_498.longitude = Decimal('133.616653')
    complex_place_498.memo = None
    complex_place_498.name = '第20旅 高知前編 (camera)'
    complex_place_498.venue = None
    complex_place_498 = importer.save_or_locate(complex_place_498)

    complex_place_499 = Place()
    complex_place_499.address = '高知県高知市 横浜50 '
    complex_place_499.altitude = Decimal('0.000000')
    complex_place_499.latitude = Decimal('33.532151')
    complex_place_499.longitude = Decimal('133.551201')
    complex_place_499.memo = None
    complex_place_499.name = '新宇津野トンネル'
    complex_place_499.venue = None
    complex_place_499 = importer.save_or_locate(complex_place_499)

    complex_place_500 = Place()
    complex_place_500.address = '大分県宇佐市 南宇佐2218 '
    complex_place_500.altitude = Decimal('0.000000')
    complex_place_500.latitude = Decimal('33.527909')
    complex_place_500.longitude = Decimal('131.375080')
    complex_place_500.memo = None
    complex_place_500.name = '宇佐参宮線26号蒸気機関車'
    complex_place_500.venue = None
    complex_place_500 = importer.save_or_locate(complex_place_500)

    complex_place_501 = Place()
    complex_place_501.address = '大分県宇佐市 南宇佐2859 '
    complex_place_501.altitude = Decimal('0.000000')
    complex_place_501.latitude = Decimal('33.526002')
    complex_place_501.longitude = Decimal('131.374638')
    complex_place_501.memo = None
    complex_place_501.name = 'USA（宇佐）神宮'
    complex_place_501.venue = None
    complex_place_501 = importer.save_or_locate(complex_place_501)

    complex_place_502 = Place()
    complex_place_502.address = '高知県高知市 横浜東町5 '
    complex_place_502.altitude = Decimal('0.000000')
    complex_place_502.latitude = Decimal('33.521597')
    complex_place_502.longitude = Decimal('133.545798')
    complex_place_502.memo = None
    complex_place_502.name = '佐々木酒食品'
    complex_place_502.venue = None
    complex_place_502 = importer.save_or_locate(complex_place_502)

    complex_place_503 = Place()
    complex_place_503.address = '高知県高知市 横浜東町8 '
    complex_place_503.altitude = Decimal('0.000000')
    complex_place_503.latitude = Decimal('33.520943')
    complex_place_503.longitude = Decimal('133.550631')
    complex_place_503.memo = None
    complex_place_503.name = 'ツヅキ島'
    complex_place_503.venue = None
    complex_place_503 = importer.save_or_locate(complex_place_503)

    complex_place_504 = Place()
    complex_place_504.address = '大分県中津市 本耶馬渓町樋田 '
    complex_place_504.altitude = Decimal('0.000000')
    complex_place_504.latitude = Decimal('33.500125')
    complex_place_504.longitude = Decimal('131.171797')
    complex_place_504.memo = None
    complex_place_504.name = '青の洞門'
    complex_place_504.venue = None
    complex_place_504 = importer.save_or_locate(complex_place_504)

    complex_place_505 = Place()
    complex_place_505.address = '高知県高知市 浦戸18 '
    complex_place_505.altitude = Decimal('0.000000')
    complex_place_505.latitude = Decimal('33.499188')
    complex_place_505.longitude = Decimal('133.572166')
    complex_place_505.memo = None
    complex_place_505.name = '民宿まさご'
    complex_place_505.venue = None
    complex_place_505 = importer.save_or_locate(complex_place_505)

    complex_place_506 = Place()
    complex_place_506.address = '高知県高知市 浦戸6 '
    complex_place_506.altitude = Decimal('0.000000')
    complex_place_506.latitude = Decimal('33.498619')
    complex_place_506.longitude = Decimal('133.575482')
    complex_place_506.memo = None
    complex_place_506.name = '坂本龍馬像'
    complex_place_506.venue = None
    complex_place_506 = importer.save_or_locate(complex_place_506)

    complex_place_507 = Place()
    complex_place_507.address = '高知県高知市 浦戸778 '
    complex_place_507.altitude = Decimal('0.000000')
    complex_place_507.latitude = Decimal('33.497137')
    complex_place_507.longitude = Decimal('133.574921')
    complex_place_507.memo = None
    complex_place_507.name = '桂浜'
    complex_place_507.venue = None
    complex_place_507 = importer.save_or_locate(complex_place_507)

    complex_place_508 = Place()
    complex_place_508.address = '高知県高知市 浦戸778 '
    complex_place_508.altitude = Decimal('0.000000')
    complex_place_508.latitude = Decimal('33.496944')
    complex_place_508.longitude = Decimal('133.573611')
    complex_place_508.memo = None
    complex_place_508.name = '桂浜水族館'
    complex_place_508.venue = None
    complex_place_508 = importer.save_or_locate(complex_place_508)

    complex_place_509 = Place()
    complex_place_509.address = '高知県高知市 浦戸278 '
    complex_place_509.altitude = Decimal('0.000000')
    complex_place_509.latitude = Decimal('33.496776')
    complex_place_509.longitude = Decimal('133.567558')
    complex_place_509.memo = None
    complex_place_509.name = '切り通し'
    complex_place_509.venue = None
    complex_place_509 = importer.save_or_locate(complex_place_509)

    complex_place_510 = Place()
    complex_place_510.address = '高知県高知市 浦戸830 '
    complex_place_510.altitude = Decimal('0.000000')
    complex_place_510.latitude = Decimal('33.495628')
    complex_place_510.longitude = Decimal('133.574656')
    complex_place_510.memo = None
    complex_place_510.name = '龍王宮'
    complex_place_510.venue = None
    complex_place_510 = importer.save_or_locate(complex_place_510)

    complex_place_511 = Place()
    complex_place_511.address = '高知県高知市 浦戸830 '
    complex_place_511.altitude = Decimal('0.000000')
    complex_place_511.latitude = Decimal('33.495590')
    complex_place_511.longitude = Decimal('133.574388')
    complex_place_511.memo = None
    complex_place_511.name = '龍王岬展望台'
    complex_place_511.venue = None
    complex_place_511 = importer.save_or_locate(complex_place_511)

    complex_place_512 = Place()
    complex_place_512.address = '大分県中津市 本耶馬渓町樋田 '
    complex_place_512.altitude = Decimal('0.000000')
    complex_place_512.latitude = Decimal('33.494700')
    complex_place_512.longitude = Decimal('131.177937')
    complex_place_512.memo = None
    complex_place_512.name = '耶馬溪'
    complex_place_512.venue = None
    complex_place_512 = importer.save_or_locate(complex_place_512)

    complex_place_513 = Place()
    complex_place_513.address = '高知県高知市 長浜4063 '
    complex_place_513.altitude = Decimal('0.000000')
    complex_place_513.latitude = Decimal('33.494666')
    complex_place_513.longitude = Decimal('133.543908')
    complex_place_513.memo = None
    complex_place_513.name = '若宮八幡宮'
    complex_place_513.venue = None
    complex_place_513 = importer.save_or_locate(complex_place_513)

    complex_place_514 = Place()
    complex_place_514.address = '高知県高知市 長浜5714 '
    complex_place_514.altitude = Decimal('0.000000')
    complex_place_514.latitude = Decimal('33.493063')
    complex_place_514.longitude = Decimal('133.546291')
    complex_place_514.memo = None
    complex_place_514.name = '長宗我部元親像'
    complex_place_514.venue = None
    complex_place_514 = importer.save_or_locate(complex_place_514)

    complex_place_515 = Place()
    complex_place_515.address = '高知県高知市 長浜4129 '
    complex_place_515.altitude = Decimal('0.000000')
    complex_place_515.latitude = Decimal('33.492435')
    complex_place_515.longitude = Decimal('133.546429')
    complex_place_515.memo = None
    complex_place_515.name = '鎮守の森公園'
    complex_place_515.venue = None
    complex_place_515 = importer.save_or_locate(complex_place_515)

    complex_place_516 = Place()
    complex_place_516.address = '高知県高知市 長浜4450 '
    complex_place_516.altitude = Decimal('0.000000')
    complex_place_516.latitude = Decimal('33.488778')
    complex_place_516.longitude = Decimal('133.548873')
    complex_place_516.memo = None
    complex_place_516.name = '桂浜花街道'
    complex_place_516.venue = None
    complex_place_516 = importer.save_or_locate(complex_place_516)

    complex_place_517 = Place()
    complex_place_517.address = '和歌山県東牟婁郡 串本町 串本40'
    complex_place_517.altitude = Decimal('0.000000')
    complex_place_517.latitude = Decimal('33.475527')
    complex_place_517.longitude = Decimal('135.781603')
    complex_place_517.memo = None
    complex_place_517.name = '串本駅'
    complex_place_517.venue = None
    complex_place_517 = importer.save_or_locate(complex_place_517)

    complex_place_518 = Place()
    complex_place_518.address = '和歌山県東牟婁郡 串本町 串本40'
    complex_place_518.altitude = Decimal('0.000000')
    complex_place_518.latitude = Decimal('33.474975')
    complex_place_518.longitude = Decimal('135.782048')
    complex_place_518.memo = None
    complex_place_518.name = 'ビジネスホテル串本 駅前店'
    complex_place_518.venue = None
    complex_place_518 = importer.save_or_locate(complex_place_518)

    complex_place_519 = Place()
    complex_place_519.address = '和歌山県東牟婁郡 串本町 串本43'
    complex_place_519.altitude = Decimal('0.000000')
    complex_place_519.latitude = Decimal('33.474593')
    complex_place_519.longitude = Decimal('135.781732')
    complex_place_519.memo = None
    complex_place_519.name = '料理 萬口'
    complex_place_519.venue = None
    complex_place_519 = importer.save_or_locate(complex_place_519)

    complex_place_520 = Place()
    complex_place_520.address = '和歌山県東牟婁郡 串本町 串本913'
    complex_place_520.altitude = Decimal('0.000000')
    complex_place_520.latitude = Decimal('33.470176')
    complex_place_520.longitude = Decimal('135.780565')
    complex_place_520.memo = None
    complex_place_520.name = 'ビーフショップまるみ支店'
    complex_place_520.venue = None
    complex_place_520 = importer.save_or_locate(complex_place_520)

    complex_place_521 = Place()
    complex_place_521.address = '和歌山県東牟婁郡 串本町 串本1403'
    complex_place_521.altitude = Decimal('0.000000')
    complex_place_521.latitude = Decimal('33.458049')
    complex_place_521.longitude = Decimal('135.771851')
    complex_place_521.memo = None
    complex_place_521.name = 'この辺歩いてるよ'
    complex_place_521.venue = None
    complex_place_521 = importer.save_or_locate(complex_place_521)

    complex_place_522 = Place()
    complex_place_522.address = '和歌山県東牟婁郡 串本町 '
    complex_place_522.altitude = Decimal('0.000000')
    complex_place_522.latitude = Decimal('33.437849')
    complex_place_522.longitude = Decimal('135.754685')
    complex_place_522.memo = None
    complex_place_522.name = 'この辺まで来たよ'
    complex_place_522.venue = None
    complex_place_522 = importer.save_or_locate(complex_place_522)

    complex_place_523 = Place()
    complex_place_523.address = '和歌山県東牟婁郡 串本町 '
    complex_place_523.altitude = Decimal('0.000000')
    complex_place_523.latitude = Decimal('33.437806')
    complex_place_523.longitude = Decimal('135.761368')
    complex_place_523.memo = None
    complex_place_523.name = '潮岬観光タワー'
    complex_place_523.venue = None
    complex_place_523 = importer.save_or_locate(complex_place_523)

    complex_place_524 = Place()
    complex_place_524.address = '和歌山県東牟婁郡 串本町 '
    complex_place_524.altitude = Decimal('0.000000')
    complex_place_524.latitude = Decimal('33.437562')
    complex_place_524.longitude = Decimal('135.754464')
    complex_place_524.memo = None
    complex_place_524.name = '潮岬灯台'
    complex_place_524.venue = None
    complex_place_524 = importer.save_or_locate(complex_place_524)

    complex_place_525 = Place()
    complex_place_525.address = '和歌山県東牟婁郡 串本町 '
    complex_place_525.altitude = Decimal('0.000000')
    complex_place_525.latitude = Decimal('33.436240')
    complex_place_525.longitude = Decimal('135.762120')
    complex_place_525.memo = None
    complex_place_525.name = '本州最南端の碑'
    complex_place_525.venue = None
    complex_place_525 = importer.save_or_locate(complex_place_525)

    complex_place_526 = Place()
    complex_place_526.address = '高知県安芸郡 田野町 （大字なし）18'
    complex_place_526.altitude = Decimal('0.000000')
    complex_place_526.latitude = Decimal('33.435086')
    complex_place_526.longitude = Decimal('134.021034')
    complex_place_526.memo = None
    complex_place_526.name = '旧魚梁瀬森林鉄道 立岡第二号桟道'
    complex_place_526.venue = None
    complex_place_526 = importer.save_or_locate(complex_place_526)

    complex_place_527 = Place()
    complex_place_527.address = '高知県安芸郡 田野町 （大字なし）267'
    complex_place_527.altitude = Decimal('0.000000')
    complex_place_527.latitude = Decimal('33.434948')
    complex_place_527.longitude = Decimal('134.019373')
    complex_place_527.memo = None
    complex_place_527.name = 'う"ぇい"～'
    complex_place_527.venue = None
    complex_place_527 = importer.save_or_locate(complex_place_527)

    complex_place_528 = Place()
    complex_place_528.address = '高知県安芸郡 奈半利町 乙978'
    complex_place_528.altitude = Decimal('0.000000')
    complex_place_528.latitude = Decimal('33.425030')
    complex_place_528.longitude = Decimal('134.018081')
    complex_place_528.memo = None
    complex_place_528.name = '奈半利駅'
    complex_place_528.venue = None
    complex_place_528 = importer.save_or_locate(complex_place_528)

    complex_place_529 = Place()
    complex_place_529.address = '高知県安芸郡 奈半利町 乙301'
    complex_place_529.altitude = Decimal('0.000000')
    complex_place_529.latitude = Decimal('33.420352')
    complex_place_529.longitude = Decimal('134.023841')
    complex_place_529.memo = None
    complex_place_529.name = '長谷橋'
    complex_place_529.venue = None
    complex_place_529 = importer.save_or_locate(complex_place_529)

    complex_place_530 = Place()
    complex_place_530.address = '大分県中津市  '
    complex_place_530.altitude = Decimal('0.000000')
    complex_place_530.latitude = Decimal('33.418720')
    complex_place_530.longitude = Decimal('131.245893')
    complex_place_530.memo = None
    complex_place_530.name = '国道500号線'
    complex_place_530.venue = None
    complex_place_530 = importer.save_or_locate(complex_place_530)

    complex_place_531 = Place()
    complex_place_531.address = '高知県安芸郡 奈半利町 乙234'
    complex_place_531.altitude = Decimal('0.000000')
    complex_place_531.latitude = Decimal('33.417870')
    complex_place_531.longitude = Decimal('134.025895')
    complex_place_531.memo = None
    complex_place_531.name = '旧魚梁瀬森林鉄道 法恩寺跨線橋'
    complex_place_531.venue = None
    complex_place_531 = importer.save_or_locate(complex_place_531)

    complex_place_532 = Place()
    complex_place_532.address = '大分県中津市  '
    complex_place_532.altitude = Decimal('0.000000')
    complex_place_532.latitude = Decimal('33.377945')
    complex_place_532.longitude = Decimal('131.164768')
    complex_place_532.memo = None
    complex_place_532.name = '楓乃木'
    complex_place_532.venue = None
    complex_place_532 = importer.save_or_locate(complex_place_532)

    complex_place_533 = Place()
    complex_place_533.address = '大分県宇佐市 院内町野地 '
    complex_place_533.altitude = Decimal('0.000000')
    complex_place_533.latitude = Decimal('33.374434')
    complex_place_533.longitude = Decimal('131.267588')
    complex_place_533.memo = None
    complex_place_533.name = '宇佐のマチュピチュ展望所'
    complex_place_533.venue = None
    complex_place_533 = importer.save_or_locate(complex_place_533)

    complex_place_534 = Place()
    complex_place_534.address = '大分県中津市  '
    complex_place_534.altitude = Decimal('0.000000')
    complex_place_534.latitude = Decimal('33.371860')
    complex_place_534.longitude = Decimal('131.165107')
    complex_place_534.memo = None
    complex_place_534.name = '一目八景展望台'
    complex_place_534.venue = None
    complex_place_534 = importer.save_or_locate(complex_place_534)

    complex_place_535 = Place()
    complex_place_535.address = '大分県玖珠郡 玖珠町 '
    complex_place_535.altitude = Decimal('0.000000')
    complex_place_535.latitude = Decimal('33.347179')
    complex_place_535.longitude = Decimal('131.242417')
    complex_place_535.memo = None
    complex_place_535.name = '川底第一トンネル'
    complex_place_535.venue = None
    complex_place_535 = importer.save_or_locate(complex_place_535)

    complex_place_536 = Place()
    complex_place_536.address = '大分県玖珠郡 玖珠町 '
    complex_place_536.altitude = Decimal('0.000000')
    complex_place_536.latitude = Decimal('33.332064')
    complex_place_536.longitude = Decimal('131.202027')
    complex_place_536.memo = None
    complex_place_536.name = '田舎食堂いいとこ焙（ばい）'
    complex_place_536.venue = None
    complex_place_536 = importer.save_or_locate(complex_place_536)

    complex_place_537 = Place()
    complex_place_537.address = None
    complex_place_537.altitude = Decimal('0.000000')
    complex_place_537.latitude = Decimal('31.600000')
    complex_place_537.longitude = Decimal('130.617624')
    complex_place_537.memo = None
    complex_place_537.name = '第25旅 鹿児島 (camera)'
    complex_place_537.venue = None
    complex_place_537 = importer.save_or_locate(complex_place_537)

    complex_place_538 = Place()
    complex_place_538.address = '鹿児島県鹿児島市 本港新町4 '
    complex_place_538.altitude = Decimal('0.000000')
    complex_place_538.latitude = Decimal('31.596454')
    complex_place_538.longitude = Decimal('130.562820')
    complex_place_538.memo = None
    complex_place_538.name = '桜島フェリー乗り場'
    complex_place_538.venue = None
    complex_place_538 = importer.save_or_locate(complex_place_538)

    complex_place_539 = Place()
    complex_place_539.address = '鹿児島県鹿児島市 本港新町5 '
    complex_place_539.altitude = Decimal('0.000000')
    complex_place_539.latitude = Decimal('31.593519')
    complex_place_539.longitude = Decimal('130.563103')
    complex_place_539.memo = None
    complex_place_539.name = 'ウォーターフロントパーク'
    complex_place_539.venue = None
    complex_place_539 = importer.save_or_locate(complex_place_539)

    complex_place_540 = Place()
    complex_place_540.address = '鹿児島県鹿児島市 金生町3 '
    complex_place_540.altitude = Decimal('0.000000')
    complex_place_540.latitude = Decimal('31.593266')
    complex_place_540.longitude = Decimal('130.557065')
    complex_place_540.memo = None
    complex_place_540.name = '山形屋1号館'
    complex_place_540.venue = None
    complex_place_540 = importer.save_or_locate(complex_place_540)

    complex_place_541 = Place()
    complex_place_541.address = '鹿児島県鹿児島市 桜島小池町 '
    complex_place_541.altitude = Decimal('0.000000')
    complex_place_541.latitude = Decimal('31.592095')
    complex_place_541.longitude = Decimal('130.599756')
    complex_place_541.memo = None
    complex_place_541.name = '桜島港フェリーターミナル'
    complex_place_541.venue = None
    complex_place_541 = importer.save_or_locate(complex_place_541)

    complex_place_542 = Place()
    complex_place_542.address = '鹿児島県鹿児島市 東千石町8 '
    complex_place_542.altitude = Decimal('0.000000')
    complex_place_542.latitude = Decimal('31.591403')
    complex_place_542.longitude = Decimal('130.553828')
    complex_place_542.memo = None
    complex_place_542.name = 'くろいわラーメン 本店'
    complex_place_542.venue = None
    complex_place_542 = importer.save_or_locate(complex_place_542)

    complex_place_543 = Place()
    complex_place_543.address = '鹿児島県鹿児島市 千日町15 '
    complex_place_543.altitude = Decimal('0.000000')
    complex_place_543.latitude = Decimal('31.590571')
    complex_place_543.longitude = Decimal('130.555195')
    complex_place_543.memo = None
    complex_place_543.name = '天文館'
    complex_place_543.venue = None
    complex_place_543 = importer.save_or_locate(complex_place_543)

    complex_place_544 = Place()
    complex_place_544.address = '鹿児島県鹿児島市 千日町5 '
    complex_place_544.altitude = Decimal('0.000000')
    complex_place_544.latitude = Decimal('31.589238')
    complex_place_544.longitude = Decimal('130.555969')
    complex_place_544.memo = None
    complex_place_544.name = '天文館むじゃき 本店'
    complex_place_544.venue = None
    complex_place_544 = importer.save_or_locate(complex_place_544)

    complex_place_545 = Place()
    complex_place_545.address = '鹿児島県鹿児島市 西千石町17 '
    complex_place_545.altitude = Decimal('0.000000')
    complex_place_545.latitude = Decimal('31.588991')
    complex_place_545.longitude = Decimal('130.551024')
    complex_place_545.memo = None
    complex_place_545.name = '樺山、黒田、大いに語る碑'
    complex_place_545.venue = None
    complex_place_545 = importer.save_or_locate(complex_place_545)

    complex_place_546 = Place()
    complex_place_546.address = '鹿児島県鹿児島市 西千石町1 '
    complex_place_546.altitude = Decimal('0.000000')
    complex_place_546.latitude = Decimal('31.586993')
    complex_place_546.longitude = Decimal('130.547223')
    complex_place_546.memo = None
    complex_place_546.name = '灰の集積所'
    complex_place_546.venue = None
    complex_place_546 = importer.save_or_locate(complex_place_546)

    complex_place_547 = Place()
    complex_place_547.address = '鹿児島県鹿児島市 西田一丁目5 '
    complex_place_547.altitude = Decimal('0.000000')
    complex_place_547.latitude = Decimal('31.586563')
    complex_place_547.longitude = Decimal('130.546107')
    complex_place_547.memo = None
    complex_place_547.name = '大久保利通像'
    complex_place_547.venue = None
    complex_place_547 = importer.save_or_locate(complex_place_547)

    complex_place_548 = Place()
    complex_place_548.address = '鹿児島県鹿児島市 黒神町258 '
    complex_place_548.altitude = Decimal('0.000000')
    complex_place_548.latitude = Decimal('31.584777')
    complex_place_548.longitude = Decimal('130.706477')
    complex_place_548.memo = None
    complex_place_548.name = '椿の里(椿チャンポン)'
    complex_place_548.venue = None
    complex_place_548 = importer.save_or_locate(complex_place_548)

    complex_place_549 = Place()
    complex_place_549.address = '鹿児島県鹿児島市 黒神町258 '
    complex_place_549.altitude = Decimal('0.000000')
    complex_place_549.latitude = Decimal('31.584558')
    complex_place_549.longitude = Decimal('130.706257')
    complex_place_549.memo = None
    complex_place_549.name = '黒神埋没鳥居'
    complex_place_549.venue = None
    complex_place_549 = importer.save_or_locate(complex_place_549)

    complex_place_550 = Place()
    complex_place_550.address = '鹿児島県鹿児島市 武一丁目1 '
    complex_place_550.altitude = Decimal('0.000000')
    complex_place_550.latitude = Decimal('31.583689')
    complex_place_550.longitude = Decimal('130.541715')
    complex_place_550.memo = None
    complex_place_550.name = '鹿児島中央駅'
    complex_place_550.venue = None
    complex_place_550 = importer.save_or_locate(complex_place_550)

    complex_place_551 = Place()
    complex_place_551.address = '鹿児島県鹿児島市  '
    complex_place_551.altitude = Decimal('0.000000')
    complex_place_551.latitude = Decimal('31.557061')
    complex_place_551.longitude = Decimal('130.703316')
    complex_place_551.memo = None
    complex_place_551.name = '桜島口'
    complex_place_551.venue = None
    complex_place_551 = importer.save_or_locate(complex_place_551)

    complex_place_552 = Place()
    complex_place_552.address = '鹿児島県鹿児島市 有村町5 '
    complex_place_552.altitude = Decimal('0.000000')
    complex_place_552.latitude = Decimal('31.553048')
    complex_place_552.longitude = Decimal('130.661147')
    complex_place_552.memo = None
    complex_place_552.name = '待避壕'
    complex_place_552.venue = None
    complex_place_552 = importer.save_or_locate(complex_place_552)

    complex_place_553 = Place()
    complex_place_553.address = '鹿児島県鹿児島市 古里町1076 '
    complex_place_553.altitude = Decimal('0.000000')
    complex_place_553.latitude = Decimal('31.552150')
    complex_place_553.longitude = Decimal('130.658730')
    complex_place_553.memo = None
    complex_place_553.name = '桜島シーサイドホテル'
    complex_place_553.venue = None
    complex_place_553 = importer.save_or_locate(complex_place_553)

    # Processing model: complex.models.Step

    from complex.models import Step

    complex_step_1 = Step()
    complex_step_1.datetime = None
    complex_step_1.number = 1
    complex_step_1.place = complex_place_117
    complex_step_1.route = complex_route_1
    complex_step_1 = importer.save_or_locate(complex_step_1)

    complex_step_2 = Step()
    complex_step_2.datetime = None
    complex_step_2.number = 2
    complex_step_2.place = complex_place_112
    complex_step_2.route = complex_route_1
    complex_step_2 = importer.save_or_locate(complex_step_2)

    complex_step_3 = Step()
    complex_step_3.datetime = None
    complex_step_3.number = 3
    complex_step_3.place = complex_place_105
    complex_step_3.route = complex_route_1
    complex_step_3 = importer.save_or_locate(complex_step_3)

    complex_step_4 = Step()
    complex_step_4.datetime = None
    complex_step_4.number = 4
    complex_step_4.place = complex_place_106
    complex_step_4.route = complex_route_1
    complex_step_4 = importer.save_or_locate(complex_step_4)

    complex_step_5 = Step()
    complex_step_5.datetime = None
    complex_step_5.number = 5
    complex_step_5.place = complex_place_107
    complex_step_5.route = complex_route_1
    complex_step_5 = importer.save_or_locate(complex_step_5)

    complex_step_6 = Step()
    complex_step_6.datetime = None
    complex_step_6.number = 6
    complex_step_6.place = complex_place_109
    complex_step_6.route = complex_route_1
    complex_step_6 = importer.save_or_locate(complex_step_6)

    complex_step_7 = Step()
    complex_step_7.datetime = None
    complex_step_7.number = 7
    complex_step_7.place = complex_place_114
    complex_step_7.route = complex_route_1
    complex_step_7 = importer.save_or_locate(complex_step_7)

    complex_step_8 = Step()
    complex_step_8.datetime = None
    complex_step_8.number = 8
    complex_step_8.place = complex_place_115
    complex_step_8.route = complex_route_1
    complex_step_8 = importer.save_or_locate(complex_step_8)

    complex_step_9 = Step()
    complex_step_9.datetime = None
    complex_step_9.number = 9
    complex_step_9.place = complex_place_116
    complex_step_9.route = complex_route_1
    complex_step_9 = importer.save_or_locate(complex_step_9)

    complex_step_10 = Step()
    complex_step_10.datetime = None
    complex_step_10.number = 10
    complex_step_10.place = complex_place_113
    complex_step_10.route = complex_route_1
    complex_step_10 = importer.save_or_locate(complex_step_10)

    complex_step_11 = Step()
    complex_step_11.datetime = None
    complex_step_11.number = 11
    complex_step_11.place = complex_place_111
    complex_step_11.route = complex_route_1
    complex_step_11 = importer.save_or_locate(complex_step_11)

    complex_step_12 = Step()
    complex_step_12.datetime = None
    complex_step_12.number = 12
    complex_step_12.place = complex_place_108
    complex_step_12.route = complex_route_1
    complex_step_12 = importer.save_or_locate(complex_step_12)

    complex_step_13 = Step()
    complex_step_13.datetime = None
    complex_step_13.number = 1
    complex_step_13.place = complex_place_104
    complex_step_13.route = complex_route_2
    complex_step_13 = importer.save_or_locate(complex_step_13)

    complex_step_14 = Step()
    complex_step_14.datetime = None
    complex_step_14.number = 2
    complex_step_14.place = complex_place_99
    complex_step_14.route = complex_route_2
    complex_step_14 = importer.save_or_locate(complex_step_14)

    complex_step_15 = Step()
    complex_step_15.datetime = None
    complex_step_15.number = 3
    complex_step_15.place = complex_place_96
    complex_step_15.route = complex_route_2
    complex_step_15 = importer.save_or_locate(complex_step_15)

    complex_step_16 = Step()
    complex_step_16.datetime = None
    complex_step_16.number = 4
    complex_step_16.place = complex_place_100
    complex_step_16.route = complex_route_2
    complex_step_16 = importer.save_or_locate(complex_step_16)

    complex_step_17 = Step()
    complex_step_17.datetime = None
    complex_step_17.number = 5
    complex_step_17.place = complex_place_102
    complex_step_17.route = complex_route_2
    complex_step_17 = importer.save_or_locate(complex_step_17)

    complex_step_18 = Step()
    complex_step_18.datetime = None
    complex_step_18.number = 6
    complex_step_18.place = complex_place_101
    complex_step_18.route = complex_route_2
    complex_step_18 = importer.save_or_locate(complex_step_18)

    complex_step_19 = Step()
    complex_step_19.datetime = None
    complex_step_19.number = 7
    complex_step_19.place = complex_place_97
    complex_step_19.route = complex_route_2
    complex_step_19 = importer.save_or_locate(complex_step_19)

    complex_step_20 = Step()
    complex_step_20.datetime = None
    complex_step_20.number = 8
    complex_step_20.place = complex_place_93
    complex_step_20.route = complex_route_2
    complex_step_20 = importer.save_or_locate(complex_step_20)

    complex_step_21 = Step()
    complex_step_21.datetime = None
    complex_step_21.number = 9
    complex_step_21.place = complex_place_94
    complex_step_21.route = complex_route_2
    complex_step_21 = importer.save_or_locate(complex_step_21)

    complex_step_22 = Step()
    complex_step_22.datetime = None
    complex_step_22.number = 10
    complex_step_22.place = complex_place_91
    complex_step_22.route = complex_route_2
    complex_step_22 = importer.save_or_locate(complex_step_22)

    complex_step_23 = Step()
    complex_step_23.datetime = None
    complex_step_23.number = 11
    complex_step_23.place = complex_place_95
    complex_step_23.route = complex_route_2
    complex_step_23 = importer.save_or_locate(complex_step_23)

    complex_step_24 = Step()
    complex_step_24.datetime = None
    complex_step_24.number = 12
    complex_step_24.place = complex_place_92
    complex_step_24.route = complex_route_2
    complex_step_24 = importer.save_or_locate(complex_step_24)

    complex_step_25 = Step()
    complex_step_25.datetime = None
    complex_step_25.number = 13
    complex_step_25.place = complex_place_98
    complex_step_25.route = complex_route_2
    complex_step_25 = importer.save_or_locate(complex_step_25)

    complex_step_26 = Step()
    complex_step_26.datetime = None
    complex_step_26.number = 1
    complex_step_26.place = complex_place_235
    complex_step_26.route = complex_route_3
    complex_step_26 = importer.save_or_locate(complex_step_26)

    complex_step_27 = Step()
    complex_step_27.datetime = None
    complex_step_27.number = 2
    complex_step_27.place = complex_place_121
    complex_step_27.route = complex_route_3
    complex_step_27 = importer.save_or_locate(complex_step_27)

    complex_step_28 = Step()
    complex_step_28.datetime = None
    complex_step_28.number = 3
    complex_step_28.place = complex_place_122
    complex_step_28.route = complex_route_3
    complex_step_28 = importer.save_or_locate(complex_step_28)

    complex_step_29 = Step()
    complex_step_29.datetime = None
    complex_step_29.number = 4
    complex_step_29.place = complex_place_119
    complex_step_29.route = complex_route_3
    complex_step_29 = importer.save_or_locate(complex_step_29)

    complex_step_30 = Step()
    complex_step_30.datetime = None
    complex_step_30.number = 5
    complex_step_30.place = complex_place_120
    complex_step_30.route = complex_route_3
    complex_step_30 = importer.save_or_locate(complex_step_30)

    complex_step_31 = Step()
    complex_step_31.datetime = None
    complex_step_31.number = 6
    complex_step_31.place = complex_place_123
    complex_step_31.route = complex_route_3
    complex_step_31 = importer.save_or_locate(complex_step_31)

    complex_step_32 = Step()
    complex_step_32.datetime = None
    complex_step_32.number = 7
    complex_step_32.place = complex_place_126
    complex_step_32.route = complex_route_3
    complex_step_32 = importer.save_or_locate(complex_step_32)

    complex_step_33 = Step()
    complex_step_33.datetime = None
    complex_step_33.number = 8
    complex_step_33.place = complex_place_125
    complex_step_33.route = complex_route_3
    complex_step_33 = importer.save_or_locate(complex_step_33)

    complex_step_34 = Step()
    complex_step_34.datetime = None
    complex_step_34.number = 9
    complex_step_34.place = complex_place_129
    complex_step_34.route = complex_route_3
    complex_step_34 = importer.save_or_locate(complex_step_34)

    complex_step_35 = Step()
    complex_step_35.datetime = None
    complex_step_35.number = 10
    complex_step_35.place = complex_place_127
    complex_step_35.route = complex_route_3
    complex_step_35 = importer.save_or_locate(complex_step_35)

    complex_step_36 = Step()
    complex_step_36.datetime = None
    complex_step_36.number = 11
    complex_step_36.place = complex_place_128
    complex_step_36.route = complex_route_3
    complex_step_36 = importer.save_or_locate(complex_step_36)

    complex_step_37 = Step()
    complex_step_37.datetime = None
    complex_step_37.number = 12
    complex_step_37.place = complex_place_118
    complex_step_37.route = complex_route_3
    complex_step_37 = importer.save_or_locate(complex_step_37)

    complex_step_38 = Step()
    complex_step_38.datetime = None
    complex_step_38.number = 1
    complex_step_38.place = complex_place_235
    complex_step_38.route = complex_route_4
    complex_step_38 = importer.save_or_locate(complex_step_38)

    complex_step_39 = Step()
    complex_step_39.datetime = None
    complex_step_39.number = 2
    complex_step_39.place = complex_place_385
    complex_step_39.route = complex_route_4
    complex_step_39 = importer.save_or_locate(complex_step_39)

    complex_step_40 = Step()
    complex_step_40.datetime = None
    complex_step_40.number = 3
    complex_step_40.place = complex_place_413
    complex_step_40.route = complex_route_4
    complex_step_40 = importer.save_or_locate(complex_step_40)

    complex_step_41 = Step()
    complex_step_41.datetime = None
    complex_step_41.number = 4
    complex_step_41.place = complex_place_412
    complex_step_41.route = complex_route_4
    complex_step_41 = importer.save_or_locate(complex_step_41)

    complex_step_42 = Step()
    complex_step_42.datetime = None
    complex_step_42.number = 5
    complex_step_42.place = complex_place_417
    complex_step_42.route = complex_route_4
    complex_step_42 = importer.save_or_locate(complex_step_42)

    complex_step_43 = Step()
    complex_step_43.datetime = None
    complex_step_43.number = 6
    complex_step_43.place = complex_place_416
    complex_step_43.route = complex_route_4
    complex_step_43 = importer.save_or_locate(complex_step_43)

    complex_step_44 = Step()
    complex_step_44.datetime = None
    complex_step_44.number = 7
    complex_step_44.place = complex_place_410
    complex_step_44.route = complex_route_4
    complex_step_44 = importer.save_or_locate(complex_step_44)

    complex_step_45 = Step()
    complex_step_45.datetime = None
    complex_step_45.number = 8
    complex_step_45.place = complex_place_409
    complex_step_45.route = complex_route_4
    complex_step_45 = importer.save_or_locate(complex_step_45)

    complex_step_46 = Step()
    complex_step_46.datetime = None
    complex_step_46.number = 9
    complex_step_46.place = complex_place_408
    complex_step_46.route = complex_route_4
    complex_step_46 = importer.save_or_locate(complex_step_46)

    complex_step_47 = Step()
    complex_step_47.datetime = None
    complex_step_47.number = 10
    complex_step_47.place = complex_place_415
    complex_step_47.route = complex_route_4
    complex_step_47 = importer.save_or_locate(complex_step_47)

    complex_step_48 = Step()
    complex_step_48.datetime = None
    complex_step_48.number = 11
    complex_step_48.place = complex_place_414
    complex_step_48.route = complex_route_4
    complex_step_48 = importer.save_or_locate(complex_step_48)

    complex_step_49 = Step()
    complex_step_49.datetime = None
    complex_step_49.number = 12
    complex_step_49.place = complex_place_418
    complex_step_49.route = complex_route_4
    complex_step_49 = importer.save_or_locate(complex_step_49)

    complex_step_50 = Step()
    complex_step_50.datetime = None
    complex_step_50.number = 1
    complex_step_50.place = complex_place_368
    complex_step_50.route = complex_route_5
    complex_step_50 = importer.save_or_locate(complex_step_50)

    complex_step_51 = Step()
    complex_step_51.datetime = None
    complex_step_51.number = 2
    complex_step_51.place = complex_place_362
    complex_step_51.route = complex_route_5
    complex_step_51 = importer.save_or_locate(complex_step_51)

    complex_step_52 = Step()
    complex_step_52.datetime = None
    complex_step_52.number = 3
    complex_step_52.place = complex_place_373
    complex_step_52.route = complex_route_5
    complex_step_52 = importer.save_or_locate(complex_step_52)

    complex_step_53 = Step()
    complex_step_53.datetime = None
    complex_step_53.number = 4
    complex_step_53.place = complex_place_375
    complex_step_53.route = complex_route_5
    complex_step_53 = importer.save_or_locate(complex_step_53)

    complex_step_54 = Step()
    complex_step_54.datetime = None
    complex_step_54.number = 5
    complex_step_54.place = complex_place_367
    complex_step_54.route = complex_route_5
    complex_step_54 = importer.save_or_locate(complex_step_54)

    complex_step_55 = Step()
    complex_step_55.datetime = None
    complex_step_55.number = 6
    complex_step_55.place = complex_place_366
    complex_step_55.route = complex_route_5
    complex_step_55 = importer.save_or_locate(complex_step_55)

    complex_step_56 = Step()
    complex_step_56.datetime = None
    complex_step_56.number = 7
    complex_step_56.place = complex_place_329
    complex_step_56.route = complex_route_5
    complex_step_56 = importer.save_or_locate(complex_step_56)

    complex_step_57 = Step()
    complex_step_57.datetime = None
    complex_step_57.number = 8
    complex_step_57.place = complex_place_327
    complex_step_57.route = complex_route_5
    complex_step_57 = importer.save_or_locate(complex_step_57)

    complex_step_58 = Step()
    complex_step_58.datetime = None
    complex_step_58.number = 9
    complex_step_58.place = complex_place_326
    complex_step_58.route = complex_route_5
    complex_step_58 = importer.save_or_locate(complex_step_58)

    complex_step_59 = Step()
    complex_step_59.datetime = None
    complex_step_59.number = 10
    complex_step_59.place = complex_place_319
    complex_step_59.route = complex_route_5
    complex_step_59 = importer.save_or_locate(complex_step_59)

    complex_step_60 = Step()
    complex_step_60.datetime = None
    complex_step_60.number = 11
    complex_step_60.place = complex_place_320
    complex_step_60.route = complex_route_5
    complex_step_60 = importer.save_or_locate(complex_step_60)

    complex_step_61 = Step()
    complex_step_61.datetime = None
    complex_step_61.number = 12
    complex_step_61.place = complex_place_306
    complex_step_61.route = complex_route_5
    complex_step_61 = importer.save_or_locate(complex_step_61)

    complex_step_62 = Step()
    complex_step_62.datetime = None
    complex_step_62.number = 13
    complex_step_62.place = complex_place_313
    complex_step_62.route = complex_route_5
    complex_step_62 = importer.save_or_locate(complex_step_62)

    complex_step_63 = Step()
    complex_step_63.datetime = None
    complex_step_63.number = 14
    complex_step_63.place = complex_place_304
    complex_step_63.route = complex_route_5
    complex_step_63 = importer.save_or_locate(complex_step_63)

    complex_step_64 = Step()
    complex_step_64.datetime = None
    complex_step_64.number = 15
    complex_step_64.place = complex_place_312
    complex_step_64.route = complex_route_5
    complex_step_64 = importer.save_or_locate(complex_step_64)

    complex_step_65 = Step()
    complex_step_65.datetime = None
    complex_step_65.number = 1
    complex_step_65.place = complex_place_156
    complex_step_65.route = complex_route_6
    complex_step_65 = importer.save_or_locate(complex_step_65)

    complex_step_66 = Step()
    complex_step_66.datetime = None
    complex_step_66.number = 2
    complex_step_66.place = complex_place_141
    complex_step_66.route = complex_route_6
    complex_step_66 = importer.save_or_locate(complex_step_66)

    complex_step_67 = Step()
    complex_step_67.datetime = None
    complex_step_67.number = 3
    complex_step_67.place = complex_place_142
    complex_step_67.route = complex_route_6
    complex_step_67 = importer.save_or_locate(complex_step_67)

    complex_step_68 = Step()
    complex_step_68.datetime = None
    complex_step_68.number = 4
    complex_step_68.place = complex_place_143
    complex_step_68.route = complex_route_6
    complex_step_68 = importer.save_or_locate(complex_step_68)

    complex_step_69 = Step()
    complex_step_69.datetime = None
    complex_step_69.number = 5
    complex_step_69.place = complex_place_135
    complex_step_69.route = complex_route_6
    complex_step_69 = importer.save_or_locate(complex_step_69)

    complex_step_70 = Step()
    complex_step_70.datetime = None
    complex_step_70.number = 6
    complex_step_70.place = complex_place_134
    complex_step_70.route = complex_route_6
    complex_step_70 = importer.save_or_locate(complex_step_70)

    complex_step_71 = Step()
    complex_step_71.datetime = None
    complex_step_71.number = 7
    complex_step_71.place = complex_place_136
    complex_step_71.route = complex_route_6
    complex_step_71 = importer.save_or_locate(complex_step_71)

    complex_step_72 = Step()
    complex_step_72.datetime = None
    complex_step_72.number = 8
    complex_step_72.place = complex_place_139
    complex_step_72.route = complex_route_6
    complex_step_72 = importer.save_or_locate(complex_step_72)

    complex_step_73 = Step()
    complex_step_73.datetime = None
    complex_step_73.number = 9
    complex_step_73.place = complex_place_138
    complex_step_73.route = complex_route_6
    complex_step_73 = importer.save_or_locate(complex_step_73)

    complex_step_74 = Step()
    complex_step_74.datetime = None
    complex_step_74.number = 10
    complex_step_74.place = complex_place_137
    complex_step_74.route = complex_route_6
    complex_step_74 = importer.save_or_locate(complex_step_74)

    complex_step_75 = Step()
    complex_step_75.datetime = None
    complex_step_75.number = 11
    complex_step_75.place = complex_place_140
    complex_step_75.route = complex_route_6
    complex_step_75 = importer.save_or_locate(complex_step_75)

    complex_step_76 = Step()
    complex_step_76.datetime = None
    complex_step_76.number = 1
    complex_step_76.place = complex_place_86
    complex_step_76.route = complex_route_7
    complex_step_76 = importer.save_or_locate(complex_step_76)

    complex_step_77 = Step()
    complex_step_77.datetime = None
    complex_step_77.number = 2
    complex_step_77.place = complex_place_88
    complex_step_77.route = complex_route_7
    complex_step_77 = importer.save_or_locate(complex_step_77)

    complex_step_78 = Step()
    complex_step_78.datetime = None
    complex_step_78.number = 3
    complex_step_78.place = complex_place_89
    complex_step_78.route = complex_route_7
    complex_step_78 = importer.save_or_locate(complex_step_78)

    complex_step_79 = Step()
    complex_step_79.datetime = None
    complex_step_79.number = 4
    complex_step_79.place = complex_place_87
    complex_step_79.route = complex_route_7
    complex_step_79 = importer.save_or_locate(complex_step_79)

    complex_step_80 = Step()
    complex_step_80.datetime = None
    complex_step_80.number = 5
    complex_step_80.place = complex_place_85
    complex_step_80.route = complex_route_7
    complex_step_80 = importer.save_or_locate(complex_step_80)

    complex_step_81 = Step()
    complex_step_81.datetime = None
    complex_step_81.number = 6
    complex_step_81.place = complex_place_84
    complex_step_81.route = complex_route_7
    complex_step_81 = importer.save_or_locate(complex_step_81)

    complex_step_82 = Step()
    complex_step_82.datetime = None
    complex_step_82.number = 1
    complex_step_82.place = complex_place_383
    complex_step_82.route = complex_route_8
    complex_step_82 = importer.save_or_locate(complex_step_82)

    complex_step_83 = Step()
    complex_step_83.datetime = None
    complex_step_83.number = 2
    complex_step_83.place = complex_place_384
    complex_step_83.route = complex_route_8
    complex_step_83 = importer.save_or_locate(complex_step_83)

    complex_step_84 = Step()
    complex_step_84.datetime = None
    complex_step_84.number = 3
    complex_step_84.place = complex_place_390
    complex_step_84.route = complex_route_8
    complex_step_84 = importer.save_or_locate(complex_step_84)

    complex_step_85 = Step()
    complex_step_85.datetime = None
    complex_step_85.number = 4
    complex_step_85.place = complex_place_391
    complex_step_85.route = complex_route_8
    complex_step_85 = importer.save_or_locate(complex_step_85)

    complex_step_86 = Step()
    complex_step_86.datetime = None
    complex_step_86.number = 5
    complex_step_86.place = complex_place_392
    complex_step_86.route = complex_route_8
    complex_step_86 = importer.save_or_locate(complex_step_86)

    complex_step_87 = Step()
    complex_step_87.datetime = None
    complex_step_87.number = 6
    complex_step_87.place = complex_place_393
    complex_step_87.route = complex_route_8
    complex_step_87 = importer.save_or_locate(complex_step_87)

    complex_step_88 = Step()
    complex_step_88.datetime = None
    complex_step_88.number = 7
    complex_step_88.place = complex_place_399
    complex_step_88.route = complex_route_8
    complex_step_88 = importer.save_or_locate(complex_step_88)

    complex_step_89 = Step()
    complex_step_89.datetime = None
    complex_step_89.number = 8
    complex_step_89.place = complex_place_398
    complex_step_89.route = complex_route_8
    complex_step_89 = importer.save_or_locate(complex_step_89)

    complex_step_90 = Step()
    complex_step_90.datetime = None
    complex_step_90.number = 9
    complex_step_90.place = complex_place_394
    complex_step_90.route = complex_route_8
    complex_step_90 = importer.save_or_locate(complex_step_90)

    complex_step_91 = Step()
    complex_step_91.datetime = None
    complex_step_91.number = 10
    complex_step_91.place = complex_place_396
    complex_step_91.route = complex_route_8
    complex_step_91 = importer.save_or_locate(complex_step_91)

    complex_step_92 = Step()
    complex_step_92.datetime = None
    complex_step_92.number = 11
    complex_step_92.place = complex_place_397
    complex_step_92.route = complex_route_8
    complex_step_92 = importer.save_or_locate(complex_step_92)

    complex_step_93 = Step()
    complex_step_93.datetime = None
    complex_step_93.number = 12
    complex_step_93.place = complex_place_389
    complex_step_93.route = complex_route_8
    complex_step_93 = importer.save_or_locate(complex_step_93)

    complex_step_94 = Step()
    complex_step_94.datetime = None
    complex_step_94.number = 13
    complex_step_94.place = complex_place_387
    complex_step_94.route = complex_route_8
    complex_step_94 = importer.save_or_locate(complex_step_94)

    complex_step_95 = Step()
    complex_step_95.datetime = None
    complex_step_95.number = 14
    complex_step_95.place = complex_place_388
    complex_step_95.route = complex_route_8
    complex_step_95 = importer.save_or_locate(complex_step_95)

    complex_step_96 = Step()
    complex_step_96.datetime = None
    complex_step_96.number = 15
    complex_step_96.place = complex_place_395
    complex_step_96.route = complex_route_8
    complex_step_96 = importer.save_or_locate(complex_step_96)

    complex_step_97 = Step()
    complex_step_97.datetime = None
    complex_step_97.number = 1
    complex_step_97.place = complex_place_220
    complex_step_97.route = complex_route_9
    complex_step_97 = importer.save_or_locate(complex_step_97)

    complex_step_98 = Step()
    complex_step_98.datetime = None
    complex_step_98.number = 2
    complex_step_98.place = complex_place_335
    complex_step_98.route = complex_route_9
    complex_step_98 = importer.save_or_locate(complex_step_98)

    complex_step_99 = Step()
    complex_step_99.datetime = None
    complex_step_99.number = 3
    complex_step_99.place = complex_place_406
    complex_step_99.route = complex_route_9
    complex_step_99 = importer.save_or_locate(complex_step_99)

    complex_step_100 = Step()
    complex_step_100.datetime = None
    complex_step_100.number = 4
    complex_step_100.place = complex_place_407
    complex_step_100.route = complex_route_9
    complex_step_100 = importer.save_or_locate(complex_step_100)

    complex_step_101 = Step()
    complex_step_101.datetime = None
    complex_step_101.number = 5
    complex_step_101.place = complex_place_420
    complex_step_101.route = complex_route_9
    complex_step_101 = importer.save_or_locate(complex_step_101)

    complex_step_102 = Step()
    complex_step_102.datetime = None
    complex_step_102.number = 6
    complex_step_102.place = complex_place_421
    complex_step_102.route = complex_route_9
    complex_step_102 = importer.save_or_locate(complex_step_102)

    complex_step_103 = Step()
    complex_step_103.datetime = None
    complex_step_103.number = 7
    complex_step_103.place = complex_place_422
    complex_step_103.route = complex_route_9
    complex_step_103 = importer.save_or_locate(complex_step_103)

    complex_step_104 = Step()
    complex_step_104.datetime = None
    complex_step_104.number = 8
    complex_step_104.place = complex_place_424
    complex_step_104.route = complex_route_9
    complex_step_104 = importer.save_or_locate(complex_step_104)

    complex_step_105 = Step()
    complex_step_105.datetime = None
    complex_step_105.number = 1
    complex_step_105.place = complex_place_425
    complex_step_105.route = complex_route_10
    complex_step_105 = importer.save_or_locate(complex_step_105)

    complex_step_106 = Step()
    complex_step_106.datetime = None
    complex_step_106.number = 2
    complex_step_106.place = complex_place_426
    complex_step_106.route = complex_route_10
    complex_step_106 = importer.save_or_locate(complex_step_106)

    complex_step_107 = Step()
    complex_step_107.datetime = None
    complex_step_107.number = 3
    complex_step_107.place = complex_place_423
    complex_step_107.route = complex_route_10
    complex_step_107 = importer.save_or_locate(complex_step_107)

    complex_step_108 = Step()
    complex_step_108.datetime = None
    complex_step_108.number = 4
    complex_step_108.place = complex_place_427
    complex_step_108.route = complex_route_10
    complex_step_108 = importer.save_or_locate(complex_step_108)

    complex_step_109 = Step()
    complex_step_109.datetime = None
    complex_step_109.number = 5
    complex_step_109.place = complex_place_428
    complex_step_109.route = complex_route_10
    complex_step_109 = importer.save_or_locate(complex_step_109)

    complex_step_110 = Step()
    complex_step_110.datetime = None
    complex_step_110.number = 6
    complex_step_110.place = complex_place_431
    complex_step_110.route = complex_route_10
    complex_step_110 = importer.save_or_locate(complex_step_110)

    complex_step_111 = Step()
    complex_step_111.datetime = None
    complex_step_111.number = 7
    complex_step_111.place = complex_place_430
    complex_step_111.route = complex_route_10
    complex_step_111 = importer.save_or_locate(complex_step_111)

    complex_step_112 = Step()
    complex_step_112.datetime = None
    complex_step_112.number = 8
    complex_step_112.place = complex_place_429
    complex_step_112.route = complex_route_10
    complex_step_112 = importer.save_or_locate(complex_step_112)

    complex_step_113 = Step()
    complex_step_113.datetime = None
    complex_step_113.number = 9
    complex_step_113.place = complex_place_405
    complex_step_113.route = complex_route_10
    complex_step_113 = importer.save_or_locate(complex_step_113)

    complex_step_114 = Step()
    complex_step_114.datetime = None
    complex_step_114.number = 10
    complex_step_114.place = complex_place_403
    complex_step_114.route = complex_route_10
    complex_step_114 = importer.save_or_locate(complex_step_114)

    complex_step_115 = Step()
    complex_step_115.datetime = None
    complex_step_115.number = 11
    complex_step_115.place = complex_place_401
    complex_step_115.route = complex_route_10
    complex_step_115 = importer.save_or_locate(complex_step_115)

    complex_step_116 = Step()
    complex_step_116.datetime = None
    complex_step_116.number = 12
    complex_step_116.place = complex_place_404
    complex_step_116.route = complex_route_10
    complex_step_116 = importer.save_or_locate(complex_step_116)

    complex_step_117 = Step()
    complex_step_117.datetime = None
    complex_step_117.number = 13
    complex_step_117.place = complex_place_402
    complex_step_117.route = complex_route_10
    complex_step_117 = importer.save_or_locate(complex_step_117)

    complex_step_118 = Step()
    complex_step_118.datetime = None
    complex_step_118.number = 1
    complex_step_118.place = complex_place_65
    complex_step_118.route = complex_route_11
    complex_step_118 = importer.save_or_locate(complex_step_118)

    complex_step_119 = Step()
    complex_step_119.datetime = None
    complex_step_119.number = 2
    complex_step_119.place = complex_place_64
    complex_step_119.route = complex_route_11
    complex_step_119 = importer.save_or_locate(complex_step_119)

    complex_step_120 = Step()
    complex_step_120.datetime = None
    complex_step_120.number = 3
    complex_step_120.place = complex_place_66
    complex_step_120.route = complex_route_11
    complex_step_120 = importer.save_or_locate(complex_step_120)

    complex_step_121 = Step()
    complex_step_121.datetime = None
    complex_step_121.number = 4
    complex_step_121.place = complex_place_67
    complex_step_121.route = complex_route_11
    complex_step_121 = importer.save_or_locate(complex_step_121)

    complex_step_122 = Step()
    complex_step_122.datetime = None
    complex_step_122.number = 5
    complex_step_122.place = complex_place_62
    complex_step_122.route = complex_route_11
    complex_step_122 = importer.save_or_locate(complex_step_122)

    complex_step_123 = Step()
    complex_step_123.datetime = None
    complex_step_123.number = 6
    complex_step_123.place = complex_place_60
    complex_step_123.route = complex_route_11
    complex_step_123 = importer.save_or_locate(complex_step_123)

    complex_step_124 = Step()
    complex_step_124.datetime = None
    complex_step_124.number = 7
    complex_step_124.place = complex_place_58
    complex_step_124.route = complex_route_11
    complex_step_124 = importer.save_or_locate(complex_step_124)

    complex_step_125 = Step()
    complex_step_125.datetime = None
    complex_step_125.number = 8
    complex_step_125.place = complex_place_59
    complex_step_125.route = complex_route_11
    complex_step_125 = importer.save_or_locate(complex_step_125)

    complex_step_126 = Step()
    complex_step_126.datetime = None
    complex_step_126.number = 9
    complex_step_126.place = complex_place_57
    complex_step_126.route = complex_route_11
    complex_step_126 = importer.save_or_locate(complex_step_126)

    complex_step_127 = Step()
    complex_step_127.datetime = None
    complex_step_127.number = 10
    complex_step_127.place = complex_place_61
    complex_step_127.route = complex_route_11
    complex_step_127 = importer.save_or_locate(complex_step_127)

    complex_step_128 = Step()
    complex_step_128.datetime = None
    complex_step_128.number = 1
    complex_step_128.place = complex_place_517
    complex_step_128.route = complex_route_12
    complex_step_128 = importer.save_or_locate(complex_step_128)

    complex_step_129 = Step()
    complex_step_129.datetime = None
    complex_step_129.number = 2
    complex_step_129.place = complex_place_521
    complex_step_129.route = complex_route_12
    complex_step_129 = importer.save_or_locate(complex_step_129)

    complex_step_130 = Step()
    complex_step_130.datetime = None
    complex_step_130.number = 3
    complex_step_130.place = complex_place_522
    complex_step_130.route = complex_route_12
    complex_step_130 = importer.save_or_locate(complex_step_130)

    complex_step_131 = Step()
    complex_step_131.datetime = None
    complex_step_131.number = 4
    complex_step_131.place = complex_place_524
    complex_step_131.route = complex_route_12
    complex_step_131 = importer.save_or_locate(complex_step_131)

    complex_step_132 = Step()
    complex_step_132.datetime = None
    complex_step_132.number = 5
    complex_step_132.place = complex_place_525
    complex_step_132.route = complex_route_12
    complex_step_132 = importer.save_or_locate(complex_step_132)

    complex_step_133 = Step()
    complex_step_133.datetime = None
    complex_step_133.number = 6
    complex_step_133.place = complex_place_518
    complex_step_133.route = complex_route_12
    complex_step_133 = importer.save_or_locate(complex_step_133)

    complex_step_134 = Step()
    complex_step_134.datetime = None
    complex_step_134.number = 7
    complex_step_134.place = complex_place_520
    complex_step_134.route = complex_route_12
    complex_step_134 = importer.save_or_locate(complex_step_134)

    complex_step_135 = Step()
    complex_step_135.datetime = None
    complex_step_135.number = 8
    complex_step_135.place = complex_place_523
    complex_step_135.route = complex_route_12
    complex_step_135 = importer.save_or_locate(complex_step_135)

    complex_step_136 = Step()
    complex_step_136.datetime = None
    complex_step_136.number = 9
    complex_step_136.place = complex_place_481
    complex_step_136.route = complex_route_12
    complex_step_136 = importer.save_or_locate(complex_step_136)

    complex_step_137 = Step()
    complex_step_137.datetime = None
    complex_step_137.number = 10
    complex_step_137.place = complex_place_480
    complex_step_137.route = complex_route_12
    complex_step_137 = importer.save_or_locate(complex_step_137)

    complex_step_138 = Step()
    complex_step_138.datetime = None
    complex_step_138.number = 11
    complex_step_138.place = complex_place_478
    complex_step_138.route = complex_route_12
    complex_step_138 = importer.save_or_locate(complex_step_138)

    complex_step_139 = Step()
    complex_step_139.datetime = None
    complex_step_139.number = 12
    complex_step_139.place = complex_place_477
    complex_step_139.route = complex_route_12
    complex_step_139 = importer.save_or_locate(complex_step_139)

    complex_step_140 = Step()
    complex_step_140.datetime = None
    complex_step_140.number = 13
    complex_step_140.place = complex_place_519
    complex_step_140.route = complex_route_12
    complex_step_140 = importer.save_or_locate(complex_step_140)

    complex_step_141 = Step()
    complex_step_141.datetime = None
    complex_step_141.number = 1
    complex_step_141.place = complex_place_71
    complex_step_141.route = complex_route_13
    complex_step_141 = importer.save_or_locate(complex_step_141)

    complex_step_142 = Step()
    complex_step_142.datetime = None
    complex_step_142.number = 2
    complex_step_142.place = complex_place_72
    complex_step_142.route = complex_route_13
    complex_step_142 = importer.save_or_locate(complex_step_142)

    complex_step_143 = Step()
    complex_step_143.datetime = None
    complex_step_143.number = 3
    complex_step_143.place = complex_place_75
    complex_step_143.route = complex_route_13
    complex_step_143 = importer.save_or_locate(complex_step_143)

    complex_step_144 = Step()
    complex_step_144.datetime = None
    complex_step_144.number = 4
    complex_step_144.place = complex_place_74
    complex_step_144.route = complex_route_13
    complex_step_144 = importer.save_or_locate(complex_step_144)

    complex_step_145 = Step()
    complex_step_145.datetime = None
    complex_step_145.number = 5
    complex_step_145.place = complex_place_73
    complex_step_145.route = complex_route_13
    complex_step_145 = importer.save_or_locate(complex_step_145)

    complex_step_146 = Step()
    complex_step_146.datetime = None
    complex_step_146.number = 6
    complex_step_146.place = complex_place_70
    complex_step_146.route = complex_route_13
    complex_step_146 = importer.save_or_locate(complex_step_146)

    complex_step_147 = Step()
    complex_step_147.datetime = None
    complex_step_147.number = 7
    complex_step_147.place = complex_place_77
    complex_step_147.route = complex_route_13
    complex_step_147 = importer.save_or_locate(complex_step_147)

    complex_step_148 = Step()
    complex_step_148.datetime = None
    complex_step_148.number = 8
    complex_step_148.place = complex_place_78
    complex_step_148.route = complex_route_13
    complex_step_148 = importer.save_or_locate(complex_step_148)

    complex_step_149 = Step()
    complex_step_149.datetime = None
    complex_step_149.number = 9
    complex_step_149.place = complex_place_68
    complex_step_149.route = complex_route_13
    complex_step_149 = importer.save_or_locate(complex_step_149)

    complex_step_150 = Step()
    complex_step_150.datetime = None
    complex_step_150.number = 10
    complex_step_150.place = complex_place_69
    complex_step_150.route = complex_route_13
    complex_step_150 = importer.save_or_locate(complex_step_150)

    complex_step_151 = Step()
    complex_step_151.datetime = None
    complex_step_151.number = 11
    complex_step_151.place = complex_place_79
    complex_step_151.route = complex_route_13
    complex_step_151 = importer.save_or_locate(complex_step_151)

    complex_step_152 = Step()
    complex_step_152.datetime = None
    complex_step_152.number = 12
    complex_step_152.place = complex_place_80
    complex_step_152.route = complex_route_13
    complex_step_152 = importer.save_or_locate(complex_step_152)

    complex_step_153 = Step()
    complex_step_153.datetime = None
    complex_step_153.number = 13
    complex_step_153.place = complex_place_81
    complex_step_153.route = complex_route_13
    complex_step_153 = importer.save_or_locate(complex_step_153)

    complex_step_154 = Step()
    complex_step_154.datetime = None
    complex_step_154.number = 14
    complex_step_154.place = complex_place_83
    complex_step_154.route = complex_route_13
    complex_step_154 = importer.save_or_locate(complex_step_154)

    complex_step_155 = Step()
    complex_step_155.datetime = None
    complex_step_155.number = 15
    complex_step_155.place = complex_place_76
    complex_step_155.route = complex_route_13
    complex_step_155 = importer.save_or_locate(complex_step_155)

    complex_step_156 = Step()
    complex_step_156.datetime = None
    complex_step_156.number = 1
    complex_step_156.place = complex_place_348
    complex_step_156.route = complex_route_14
    complex_step_156 = importer.save_or_locate(complex_step_156)

    complex_step_157 = Step()
    complex_step_157.datetime = None
    complex_step_157.number = 2
    complex_step_157.place = complex_place_349
    complex_step_157.route = complex_route_14
    complex_step_157 = importer.save_or_locate(complex_step_157)

    complex_step_158 = Step()
    complex_step_158.datetime = None
    complex_step_158.number = 3
    complex_step_158.place = complex_place_347
    complex_step_158.route = complex_route_14
    complex_step_158 = importer.save_or_locate(complex_step_158)

    complex_step_159 = Step()
    complex_step_159.datetime = None
    complex_step_159.number = 4
    complex_step_159.place = complex_place_346
    complex_step_159.route = complex_route_14
    complex_step_159 = importer.save_or_locate(complex_step_159)

    complex_step_160 = Step()
    complex_step_160.datetime = None
    complex_step_160.number = 5
    complex_step_160.place = complex_place_345
    complex_step_160.route = complex_route_14
    complex_step_160 = importer.save_or_locate(complex_step_160)

    complex_step_161 = Step()
    complex_step_161.datetime = None
    complex_step_161.number = 6
    complex_step_161.place = complex_place_343
    complex_step_161.route = complex_route_14
    complex_step_161 = importer.save_or_locate(complex_step_161)

    complex_step_162 = Step()
    complex_step_162.datetime = None
    complex_step_162.number = 7
    complex_step_162.place = complex_place_342
    complex_step_162.route = complex_route_14
    complex_step_162 = importer.save_or_locate(complex_step_162)

    complex_step_163 = Step()
    complex_step_163.datetime = None
    complex_step_163.number = 8
    complex_step_163.place = complex_place_341
    complex_step_163.route = complex_route_14
    complex_step_163 = importer.save_or_locate(complex_step_163)

    complex_step_164 = Step()
    complex_step_164.datetime = None
    complex_step_164.number = 9
    complex_step_164.place = complex_place_340
    complex_step_164.route = complex_route_14
    complex_step_164 = importer.save_or_locate(complex_step_164)

    complex_step_165 = Step()
    complex_step_165.datetime = None
    complex_step_165.number = 10
    complex_step_165.place = complex_place_338
    complex_step_165.route = complex_route_14
    complex_step_165 = importer.save_or_locate(complex_step_165)

    complex_step_166 = Step()
    complex_step_166.datetime = None
    complex_step_166.number = 11
    complex_step_166.place = complex_place_337
    complex_step_166.route = complex_route_14
    complex_step_166 = importer.save_or_locate(complex_step_166)

    complex_step_167 = Step()
    complex_step_167.datetime = None
    complex_step_167.number = 12
    complex_step_167.place = complex_place_336
    complex_step_167.route = complex_route_14
    complex_step_167 = importer.save_or_locate(complex_step_167)

    complex_step_168 = Step()
    complex_step_168.datetime = None
    complex_step_168.number = 13
    complex_step_168.place = complex_place_339
    complex_step_168.route = complex_route_14
    complex_step_168 = importer.save_or_locate(complex_step_168)

    complex_step_169 = Step()
    complex_step_169.datetime = None
    complex_step_169.number = 14
    complex_step_169.place = complex_place_344
    complex_step_169.route = complex_route_14
    complex_step_169 = importer.save_or_locate(complex_step_169)

    complex_step_170 = Step()
    complex_step_170.datetime = None
    complex_step_170.number = 15
    complex_step_170.place = complex_place_333
    complex_step_170.route = complex_route_14
    complex_step_170 = importer.save_or_locate(complex_step_170)

    complex_step_171 = Step()
    complex_step_171.datetime = None
    complex_step_171.number = 16
    complex_step_171.place = complex_place_334
    complex_step_171.route = complex_route_14
    complex_step_171 = importer.save_or_locate(complex_step_171)

    complex_step_172 = Step()
    complex_step_172.datetime = None
    complex_step_172.number = 17
    complex_step_172.place = complex_place_331
    complex_step_172.route = complex_route_14
    complex_step_172 = importer.save_or_locate(complex_step_172)

    complex_step_173 = Step()
    complex_step_173.datetime = None
    complex_step_173.number = 1
    complex_step_173.place = complex_place_314
    complex_step_173.route = complex_route_15
    complex_step_173 = importer.save_or_locate(complex_step_173)

    complex_step_174 = Step()
    complex_step_174.datetime = None
    complex_step_174.number = 2
    complex_step_174.place = complex_place_332
    complex_step_174.route = complex_route_15
    complex_step_174 = importer.save_or_locate(complex_step_174)

    complex_step_175 = Step()
    complex_step_175.datetime = None
    complex_step_175.number = 3
    complex_step_175.place = complex_place_328
    complex_step_175.route = complex_route_15
    complex_step_175 = importer.save_or_locate(complex_step_175)

    complex_step_176 = Step()
    complex_step_176.datetime = None
    complex_step_176.number = 4
    complex_step_176.place = complex_place_317
    complex_step_176.route = complex_route_15
    complex_step_176 = importer.save_or_locate(complex_step_176)

    complex_step_177 = Step()
    complex_step_177.datetime = None
    complex_step_177.number = 5
    complex_step_177.place = complex_place_316
    complex_step_177.route = complex_route_15
    complex_step_177 = importer.save_or_locate(complex_step_177)

    complex_step_178 = Step()
    complex_step_178.datetime = None
    complex_step_178.number = 6
    complex_step_178.place = complex_place_315
    complex_step_178.route = complex_route_15
    complex_step_178 = importer.save_or_locate(complex_step_178)

    complex_step_179 = Step()
    complex_step_179.datetime = None
    complex_step_179.number = 7
    complex_step_179.place = complex_place_307
    complex_step_179.route = complex_route_15
    complex_step_179 = importer.save_or_locate(complex_step_179)

    complex_step_180 = Step()
    complex_step_180.datetime = None
    complex_step_180.number = 8
    complex_step_180.place = complex_place_308
    complex_step_180.route = complex_route_15
    complex_step_180 = importer.save_or_locate(complex_step_180)

    complex_step_181 = Step()
    complex_step_181.datetime = None
    complex_step_181.number = 9
    complex_step_181.place = complex_place_309
    complex_step_181.route = complex_route_15
    complex_step_181 = importer.save_or_locate(complex_step_181)

    complex_step_182 = Step()
    complex_step_182.datetime = None
    complex_step_182.number = 10
    complex_step_182.place = complex_place_311
    complex_step_182.route = complex_route_15
    complex_step_182 = importer.save_or_locate(complex_step_182)

    complex_step_183 = Step()
    complex_step_183.datetime = None
    complex_step_183.number = 1
    complex_step_183.place = complex_place_235
    complex_step_183.route = complex_route_16
    complex_step_183 = importer.save_or_locate(complex_step_183)

    complex_step_184 = Step()
    complex_step_184.datetime = None
    complex_step_184.number = 2
    complex_step_184.place = complex_place_222
    complex_step_184.route = complex_route_16
    complex_step_184 = importer.save_or_locate(complex_step_184)

    complex_step_185 = Step()
    complex_step_185.datetime = None
    complex_step_185.number = 3
    complex_step_185.place = complex_place_215
    complex_step_185.route = complex_route_16
    complex_step_185 = importer.save_or_locate(complex_step_185)

    complex_step_186 = Step()
    complex_step_186.datetime = None
    complex_step_186.number = 4
    complex_step_186.place = complex_place_205
    complex_step_186.route = complex_route_16
    complex_step_186 = importer.save_or_locate(complex_step_186)

    complex_step_187 = Step()
    complex_step_187.datetime = None
    complex_step_187.number = 5
    complex_step_187.place = complex_place_206
    complex_step_187.route = complex_route_16
    complex_step_187 = importer.save_or_locate(complex_step_187)

    complex_step_188 = Step()
    complex_step_188.datetime = None
    complex_step_188.number = 6
    complex_step_188.place = complex_place_208
    complex_step_188.route = complex_route_16
    complex_step_188 = importer.save_or_locate(complex_step_188)

    complex_step_189 = Step()
    complex_step_189.datetime = None
    complex_step_189.number = 7
    complex_step_189.place = complex_place_213
    complex_step_189.route = complex_route_16
    complex_step_189 = importer.save_or_locate(complex_step_189)

    complex_step_190 = Step()
    complex_step_190.datetime = None
    complex_step_190.number = 8
    complex_step_190.place = complex_place_211
    complex_step_190.route = complex_route_16
    complex_step_190 = importer.save_or_locate(complex_step_190)

    complex_step_191 = Step()
    complex_step_191.datetime = None
    complex_step_191.number = 9
    complex_step_191.place = complex_place_210
    complex_step_191.route = complex_route_16
    complex_step_191 = importer.save_or_locate(complex_step_191)

    complex_step_192 = Step()
    complex_step_192.datetime = None
    complex_step_192.number = 10
    complex_step_192.place = complex_place_212
    complex_step_192.route = complex_route_16
    complex_step_192 = importer.save_or_locate(complex_step_192)

    complex_step_193 = Step()
    complex_step_193.datetime = None
    complex_step_193.number = 11
    complex_step_193.place = complex_place_207
    complex_step_193.route = complex_route_16
    complex_step_193 = importer.save_or_locate(complex_step_193)

    complex_step_194 = Step()
    complex_step_194.datetime = None
    complex_step_194.number = 12
    complex_step_194.place = complex_place_217
    complex_step_194.route = complex_route_16
    complex_step_194 = importer.save_or_locate(complex_step_194)

    complex_step_195 = Step()
    complex_step_195.datetime = None
    complex_step_195.number = 13
    complex_step_195.place = complex_place_216
    complex_step_195.route = complex_route_16
    complex_step_195 = importer.save_or_locate(complex_step_195)

    complex_step_196 = Step()
    complex_step_196.datetime = None
    complex_step_196.number = 14
    complex_step_196.place = complex_place_209
    complex_step_196.route = complex_route_16
    complex_step_196 = importer.save_or_locate(complex_step_196)

    complex_step_197 = Step()
    complex_step_197.datetime = None
    complex_step_197.number = 1
    complex_step_197.place = complex_place_235
    complex_step_197.route = complex_route_17
    complex_step_197 = importer.save_or_locate(complex_step_197)

    complex_step_198 = Step()
    complex_step_198.datetime = None
    complex_step_198.number = 2
    complex_step_198.place = complex_place_279
    complex_step_198.route = complex_route_17
    complex_step_198 = importer.save_or_locate(complex_step_198)

    complex_step_199 = Step()
    complex_step_199.datetime = None
    complex_step_199.number = 3
    complex_step_199.place = complex_place_275
    complex_step_199.route = complex_route_17
    complex_step_199 = importer.save_or_locate(complex_step_199)

    complex_step_200 = Step()
    complex_step_200.datetime = None
    complex_step_200.number = 4
    complex_step_200.place = complex_place_248
    complex_step_200.route = complex_route_17
    complex_step_200 = importer.save_or_locate(complex_step_200)

    complex_step_201 = Step()
    complex_step_201.datetime = None
    complex_step_201.number = 5
    complex_step_201.place = complex_place_250
    complex_step_201.route = complex_route_17
    complex_step_201 = importer.save_or_locate(complex_step_201)

    complex_step_202 = Step()
    complex_step_202.datetime = None
    complex_step_202.number = 6
    complex_step_202.place = complex_place_269
    complex_step_202.route = complex_route_17
    complex_step_202 = importer.save_or_locate(complex_step_202)

    complex_step_203 = Step()
    complex_step_203.datetime = None
    complex_step_203.number = 7
    complex_step_203.place = complex_place_254
    complex_step_203.route = complex_route_17
    complex_step_203 = importer.save_or_locate(complex_step_203)

    complex_step_204 = Step()
    complex_step_204.datetime = None
    complex_step_204.number = 8
    complex_step_204.place = complex_place_276
    complex_step_204.route = complex_route_17
    complex_step_204 = importer.save_or_locate(complex_step_204)

    complex_step_205 = Step()
    complex_step_205.datetime = None
    complex_step_205.number = 9
    complex_step_205.place = complex_place_270
    complex_step_205.route = complex_route_17
    complex_step_205 = importer.save_or_locate(complex_step_205)

    complex_step_206 = Step()
    complex_step_206.datetime = None
    complex_step_206.number = 10
    complex_step_206.place = complex_place_272
    complex_step_206.route = complex_route_17
    complex_step_206 = importer.save_or_locate(complex_step_206)

    complex_step_207 = Step()
    complex_step_207.datetime = None
    complex_step_207.number = 11
    complex_step_207.place = complex_place_277
    complex_step_207.route = complex_route_17
    complex_step_207 = importer.save_or_locate(complex_step_207)

    complex_step_208 = Step()
    complex_step_208.datetime = None
    complex_step_208.number = 12
    complex_step_208.place = complex_place_280
    complex_step_208.route = complex_route_17
    complex_step_208 = importer.save_or_locate(complex_step_208)

    complex_step_209 = Step()
    complex_step_209.datetime = None
    complex_step_209.number = 13
    complex_step_209.place = complex_place_284
    complex_step_209.route = complex_route_17
    complex_step_209 = importer.save_or_locate(complex_step_209)

    complex_step_210 = Step()
    complex_step_210.datetime = None
    complex_step_210.number = 14
    complex_step_210.place = complex_place_283
    complex_step_210.route = complex_route_17
    complex_step_210 = importer.save_or_locate(complex_step_210)

    complex_step_211 = Step()
    complex_step_211.datetime = None
    complex_step_211.number = 15
    complex_step_211.place = complex_place_285
    complex_step_211.route = complex_route_17
    complex_step_211 = importer.save_or_locate(complex_step_211)

    complex_step_212 = Step()
    complex_step_212.datetime = None
    complex_step_212.number = 16
    complex_step_212.place = complex_place_287
    complex_step_212.route = complex_route_17
    complex_step_212 = importer.save_or_locate(complex_step_212)

    complex_step_213 = Step()
    complex_step_213.datetime = None
    complex_step_213.number = 17
    complex_step_213.place = complex_place_294
    complex_step_213.route = complex_route_17
    complex_step_213 = importer.save_or_locate(complex_step_213)

    complex_step_214 = Step()
    complex_step_214.datetime = None
    complex_step_214.number = 18
    complex_step_214.place = complex_place_292
    complex_step_214.route = complex_route_17
    complex_step_214 = importer.save_or_locate(complex_step_214)

    complex_step_215 = Step()
    complex_step_215.datetime = None
    complex_step_215.number = 19
    complex_step_215.place = complex_place_282
    complex_step_215.route = complex_route_17
    complex_step_215 = importer.save_or_locate(complex_step_215)

    complex_step_216 = Step()
    complex_step_216.datetime = None
    complex_step_216.number = 20
    complex_step_216.place = complex_place_288
    complex_step_216.route = complex_route_17
    complex_step_216 = importer.save_or_locate(complex_step_216)

    complex_step_217 = Step()
    complex_step_217.datetime = None
    complex_step_217.number = 21
    complex_step_217.place = complex_place_299
    complex_step_217.route = complex_route_17
    complex_step_217 = importer.save_or_locate(complex_step_217)

    complex_step_218 = Step()
    complex_step_218.datetime = None
    complex_step_218.number = 22
    complex_step_218.place = complex_place_290
    complex_step_218.route = complex_route_17
    complex_step_218 = importer.save_or_locate(complex_step_218)

    complex_step_219 = Step()
    complex_step_219.datetime = None
    complex_step_219.number = 23
    complex_step_219.place = complex_place_301
    complex_step_219.route = complex_route_17
    complex_step_219 = importer.save_or_locate(complex_step_219)

    complex_step_220 = Step()
    complex_step_220.datetime = None
    complex_step_220.number = 1
    complex_step_220.place = complex_place_235
    complex_step_220.route = complex_route_18
    complex_step_220 = importer.save_or_locate(complex_step_220)

    complex_step_221 = Step()
    complex_step_221.datetime = None
    complex_step_221.number = 2
    complex_step_221.place = complex_place_173
    complex_step_221.route = complex_route_18
    complex_step_221 = importer.save_or_locate(complex_step_221)

    complex_step_222 = Step()
    complex_step_222.datetime = None
    complex_step_222.number = 3
    complex_step_222.place = complex_place_175
    complex_step_222.route = complex_route_18
    complex_step_222 = importer.save_or_locate(complex_step_222)

    complex_step_223 = Step()
    complex_step_223.datetime = None
    complex_step_223.number = 4
    complex_step_223.place = complex_place_176
    complex_step_223.route = complex_route_18
    complex_step_223 = importer.save_or_locate(complex_step_223)

    complex_step_224 = Step()
    complex_step_224.datetime = None
    complex_step_224.number = 5
    complex_step_224.place = complex_place_174
    complex_step_224.route = complex_route_18
    complex_step_224 = importer.save_or_locate(complex_step_224)

    complex_step_225 = Step()
    complex_step_225.datetime = None
    complex_step_225.number = 6
    complex_step_225.place = complex_place_167
    complex_step_225.route = complex_route_18
    complex_step_225 = importer.save_or_locate(complex_step_225)

    complex_step_226 = Step()
    complex_step_226.datetime = None
    complex_step_226.number = 7
    complex_step_226.place = complex_place_168
    complex_step_226.route = complex_route_18
    complex_step_226 = importer.save_or_locate(complex_step_226)

    complex_step_227 = Step()
    complex_step_227.datetime = None
    complex_step_227.number = 8
    complex_step_227.place = complex_place_166
    complex_step_227.route = complex_route_18
    complex_step_227 = importer.save_or_locate(complex_step_227)

    complex_step_228 = Step()
    complex_step_228.datetime = None
    complex_step_228.number = 9
    complex_step_228.place = complex_place_164
    complex_step_228.route = complex_route_18
    complex_step_228 = importer.save_or_locate(complex_step_228)

    complex_step_229 = Step()
    complex_step_229.datetime = None
    complex_step_229.number = 10
    complex_step_229.place = complex_place_163
    complex_step_229.route = complex_route_18
    complex_step_229 = importer.save_or_locate(complex_step_229)

    complex_step_230 = Step()
    complex_step_230.datetime = None
    complex_step_230.number = 11
    complex_step_230.place = complex_place_161
    complex_step_230.route = complex_route_18
    complex_step_230 = importer.save_or_locate(complex_step_230)

    complex_step_231 = Step()
    complex_step_231.datetime = None
    complex_step_231.number = 12
    complex_step_231.place = complex_place_160
    complex_step_231.route = complex_route_18
    complex_step_231 = importer.save_or_locate(complex_step_231)

    complex_step_232 = Step()
    complex_step_232.datetime = None
    complex_step_232.number = 13
    complex_step_232.place = complex_place_158
    complex_step_232.route = complex_route_18
    complex_step_232 = importer.save_or_locate(complex_step_232)

    complex_step_233 = Step()
    complex_step_233.datetime = None
    complex_step_233.number = 14
    complex_step_233.place = complex_place_157
    complex_step_233.route = complex_route_18
    complex_step_233 = importer.save_or_locate(complex_step_233)

    complex_step_234 = Step()
    complex_step_234.datetime = None
    complex_step_234.number = 15
    complex_step_234.place = complex_place_159
    complex_step_234.route = complex_route_18
    complex_step_234 = importer.save_or_locate(complex_step_234)

    complex_step_235 = Step()
    complex_step_235.datetime = None
    complex_step_235.number = 16
    complex_step_235.place = complex_place_133
    complex_step_235.route = complex_route_18
    complex_step_235 = importer.save_or_locate(complex_step_235)

    complex_step_236 = Step()
    complex_step_236.datetime = None
    complex_step_236.number = 17
    complex_step_236.place = complex_place_144
    complex_step_236.route = complex_route_18
    complex_step_236 = importer.save_or_locate(complex_step_236)

    complex_step_237 = Step()
    complex_step_237.datetime = None
    complex_step_237.number = 18
    complex_step_237.place = complex_place_165
    complex_step_237.route = complex_route_18
    complex_step_237 = importer.save_or_locate(complex_step_237)

    complex_step_238 = Step()
    complex_step_238.datetime = None
    complex_step_238.number = 1
    complex_step_238.place = complex_place_146
    complex_step_238.route = complex_route_19
    complex_step_238 = importer.save_or_locate(complex_step_238)

    complex_step_239 = Step()
    complex_step_239.datetime = None
    complex_step_239.number = 2
    complex_step_239.place = complex_place_145
    complex_step_239.route = complex_route_19
    complex_step_239 = importer.save_or_locate(complex_step_239)

    complex_step_240 = Step()
    complex_step_240.datetime = None
    complex_step_240.number = 3
    complex_step_240.place = complex_place_148
    complex_step_240.route = complex_route_19
    complex_step_240 = importer.save_or_locate(complex_step_240)

    complex_step_241 = Step()
    complex_step_241.datetime = None
    complex_step_241.number = 4
    complex_step_241.place = complex_place_147
    complex_step_241.route = complex_route_19
    complex_step_241 = importer.save_or_locate(complex_step_241)

    complex_step_242 = Step()
    complex_step_242.datetime = None
    complex_step_242.number = 5
    complex_step_242.place = complex_place_149
    complex_step_242.route = complex_route_19
    complex_step_242 = importer.save_or_locate(complex_step_242)

    complex_step_243 = Step()
    complex_step_243.datetime = None
    complex_step_243.number = 6
    complex_step_243.place = complex_place_150
    complex_step_243.route = complex_route_19
    complex_step_243 = importer.save_or_locate(complex_step_243)

    complex_step_244 = Step()
    complex_step_244.datetime = None
    complex_step_244.number = 7
    complex_step_244.place = complex_place_153
    complex_step_244.route = complex_route_19
    complex_step_244 = importer.save_or_locate(complex_step_244)

    complex_step_245 = Step()
    complex_step_245.datetime = None
    complex_step_245.number = 1
    complex_step_245.place = complex_place_235
    complex_step_245.route = complex_route_20
    complex_step_245 = importer.save_or_locate(complex_step_245)

    complex_step_246 = Step()
    complex_step_246.datetime = None
    complex_step_246.number = 2
    complex_step_246.place = complex_place_476
    complex_step_246.route = complex_route_20
    complex_step_246 = importer.save_or_locate(complex_step_246)

    complex_step_247 = Step()
    complex_step_247.datetime = None
    complex_step_247.number = 3
    complex_step_247.place = complex_place_475
    complex_step_247.route = complex_route_20
    complex_step_247 = importer.save_or_locate(complex_step_247)

    complex_step_248 = Step()
    complex_step_248.datetime = None
    complex_step_248.number = 4
    complex_step_248.place = complex_place_512
    complex_step_248.route = complex_route_20
    complex_step_248 = importer.save_or_locate(complex_step_248)

    complex_step_249 = Step()
    complex_step_249.datetime = None
    complex_step_249.number = 5
    complex_step_249.place = complex_place_504
    complex_step_249.route = complex_route_20
    complex_step_249 = importer.save_or_locate(complex_step_249)

    complex_step_250 = Step()
    complex_step_250.datetime = None
    complex_step_250.number = 6
    complex_step_250.place = complex_place_532
    complex_step_250.route = complex_route_20
    complex_step_250 = importer.save_or_locate(complex_step_250)

    complex_step_251 = Step()
    complex_step_251.datetime = None
    complex_step_251.number = 7
    complex_step_251.place = complex_place_535
    complex_step_251.route = complex_route_20
    complex_step_251 = importer.save_or_locate(complex_step_251)

    complex_step_252 = Step()
    complex_step_252.datetime = None
    complex_step_252.number = 8
    complex_step_252.place = complex_place_536
    complex_step_252.route = complex_route_20
    complex_step_252 = importer.save_or_locate(complex_step_252)

    complex_step_253 = Step()
    complex_step_253.datetime = None
    complex_step_253.number = 9
    complex_step_253.place = complex_place_533
    complex_step_253.route = complex_route_20
    complex_step_253 = importer.save_or_locate(complex_step_253)

    complex_step_254 = Step()
    complex_step_254.datetime = None
    complex_step_254.number = 10
    complex_step_254.place = complex_place_534
    complex_step_254.route = complex_route_20
    complex_step_254 = importer.save_or_locate(complex_step_254)

    complex_step_255 = Step()
    complex_step_255.datetime = None
    complex_step_255.number = 1
    complex_step_255.place = complex_place_530
    complex_step_255.route = complex_route_21
    complex_step_255 = importer.save_or_locate(complex_step_255)

    complex_step_256 = Step()
    complex_step_256.datetime = None
    complex_step_256.number = 2
    complex_step_256.place = complex_place_491
    complex_step_256.route = complex_route_21
    complex_step_256 = importer.save_or_locate(complex_step_256)

    complex_step_257 = Step()
    complex_step_257.datetime = None
    complex_step_257.number = 3
    complex_step_257.place = complex_place_490
    complex_step_257.route = complex_route_21
    complex_step_257 = importer.save_or_locate(complex_step_257)

    complex_step_258 = Step()
    complex_step_258.datetime = None
    complex_step_258.number = 4
    complex_step_258.place = complex_place_501
    complex_step_258.route = complex_route_21
    complex_step_258 = importer.save_or_locate(complex_step_258)

    complex_step_259 = Step()
    complex_step_259.datetime = None
    complex_step_259.number = 5
    complex_step_259.place = complex_place_500
    complex_step_259.route = complex_route_21
    complex_step_259 = importer.save_or_locate(complex_step_259)

    complex_step_260 = Step()
    complex_step_260.datetime = None
    complex_step_260.number = 1
    complex_step_260.place = complex_place_235
    complex_step_260.route = complex_route_22
    complex_step_260 = importer.save_or_locate(complex_step_260)

    complex_step_261 = Step()
    complex_step_261.datetime = None
    complex_step_261.number = 2
    complex_step_261.place = complex_place_233
    complex_step_261.route = complex_route_22
    complex_step_261 = importer.save_or_locate(complex_step_261)

    complex_step_262 = Step()
    complex_step_262.datetime = None
    complex_step_262.number = 3
    complex_step_262.place = complex_place_237
    complex_step_262.route = complex_route_22
    complex_step_262 = importer.save_or_locate(complex_step_262)

    complex_step_263 = Step()
    complex_step_263.datetime = None
    complex_step_263.number = 4
    complex_step_263.place = complex_place_234
    complex_step_263.route = complex_route_22
    complex_step_263 = importer.save_or_locate(complex_step_263)

    complex_step_264 = Step()
    complex_step_264.datetime = None
    complex_step_264.number = 5
    complex_step_264.place = complex_place_232
    complex_step_264.route = complex_route_22
    complex_step_264 = importer.save_or_locate(complex_step_264)

    complex_step_265 = Step()
    complex_step_265.datetime = None
    complex_step_265.number = 6
    complex_step_265.place = complex_place_239
    complex_step_265.route = complex_route_22
    complex_step_265 = importer.save_or_locate(complex_step_265)

    complex_step_266 = Step()
    complex_step_266.datetime = None
    complex_step_266.number = 7
    complex_step_266.place = complex_place_243
    complex_step_266.route = complex_route_22
    complex_step_266 = importer.save_or_locate(complex_step_266)

    complex_step_267 = Step()
    complex_step_267.datetime = None
    complex_step_267.number = 8
    complex_step_267.place = complex_place_247
    complex_step_267.route = complex_route_22
    complex_step_267 = importer.save_or_locate(complex_step_267)

    complex_step_268 = Step()
    complex_step_268.datetime = None
    complex_step_268.number = 9
    complex_step_268.place = complex_place_249
    complex_step_268.route = complex_route_22
    complex_step_268 = importer.save_or_locate(complex_step_268)

    complex_step_269 = Step()
    complex_step_269.datetime = None
    complex_step_269.number = 10
    complex_step_269.place = complex_place_244
    complex_step_269.route = complex_route_22
    complex_step_269 = importer.save_or_locate(complex_step_269)

    complex_step_270 = Step()
    complex_step_270.datetime = None
    complex_step_270.number = 11
    complex_step_270.place = complex_place_245
    complex_step_270.route = complex_route_22
    complex_step_270 = importer.save_or_locate(complex_step_270)

    complex_step_271 = Step()
    complex_step_271.datetime = None
    complex_step_271.number = 12
    complex_step_271.place = complex_place_242
    complex_step_271.route = complex_route_22
    complex_step_271 = importer.save_or_locate(complex_step_271)

    complex_step_272 = Step()
    complex_step_272.datetime = None
    complex_step_272.number = 13
    complex_step_272.place = complex_place_236
    complex_step_272.route = complex_route_22
    complex_step_272 = importer.save_or_locate(complex_step_272)

    complex_step_273 = Step()
    complex_step_273.datetime = None
    complex_step_273.number = 14
    complex_step_273.place = complex_place_241
    complex_step_273.route = complex_route_22
    complex_step_273 = importer.save_or_locate(complex_step_273)

    complex_step_274 = Step()
    complex_step_274.datetime = None
    complex_step_274.number = 15
    complex_step_274.place = complex_place_251
    complex_step_274.route = complex_route_22
    complex_step_274 = importer.save_or_locate(complex_step_274)

    complex_step_275 = Step()
    complex_step_275.datetime = None
    complex_step_275.number = 16
    complex_step_275.place = complex_place_240
    complex_step_275.route = complex_route_22
    complex_step_275 = importer.save_or_locate(complex_step_275)

    complex_step_276 = Step()
    complex_step_276.datetime = None
    complex_step_276.number = 17
    complex_step_276.place = complex_place_231
    complex_step_276.route = complex_route_22
    complex_step_276 = importer.save_or_locate(complex_step_276)

    complex_step_277 = Step()
    complex_step_277.datetime = None
    complex_step_277.number = 18
    complex_step_277.place = complex_place_225
    complex_step_277.route = complex_route_22
    complex_step_277 = importer.save_or_locate(complex_step_277)

    complex_step_278 = Step()
    complex_step_278.datetime = None
    complex_step_278.number = 19
    complex_step_278.place = complex_place_228
    complex_step_278.route = complex_route_22
    complex_step_278 = importer.save_or_locate(complex_step_278)

    complex_step_279 = Step()
    complex_step_279.datetime = None
    complex_step_279.number = 20
    complex_step_279.place = complex_place_226
    complex_step_279.route = complex_route_22
    complex_step_279 = importer.save_or_locate(complex_step_279)

    complex_step_280 = Step()
    complex_step_280.datetime = None
    complex_step_280.number = 21
    complex_step_280.place = complex_place_227
    complex_step_280.route = complex_route_22
    complex_step_280 = importer.save_or_locate(complex_step_280)

    complex_step_281 = Step()
    complex_step_281.datetime = None
    complex_step_281.number = 22
    complex_step_281.place = complex_place_229
    complex_step_281.route = complex_route_22
    complex_step_281 = importer.save_or_locate(complex_step_281)

    complex_step_282 = Step()
    complex_step_282.datetime = None
    complex_step_282.number = 23
    complex_step_282.place = complex_place_230
    complex_step_282.route = complex_route_22
    complex_step_282 = importer.save_or_locate(complex_step_282)

    complex_step_283 = Step()
    complex_step_283.datetime = None
    complex_step_283.number = 24
    complex_step_283.place = complex_place_255
    complex_step_283.route = complex_route_22
    complex_step_283 = importer.save_or_locate(complex_step_283)

    complex_step_284 = Step()
    complex_step_284.datetime = None
    complex_step_284.number = 25
    complex_step_284.place = complex_place_252
    complex_step_284.route = complex_route_22
    complex_step_284 = importer.save_or_locate(complex_step_284)

    complex_step_285 = Step()
    complex_step_285.datetime = None
    complex_step_285.number = 26
    complex_step_285.place = complex_place_221
    complex_step_285.route = complex_route_22
    complex_step_285 = importer.save_or_locate(complex_step_285)

    complex_step_286 = Step()
    complex_step_286.datetime = None
    complex_step_286.number = 27
    complex_step_286.place = complex_place_256
    complex_step_286.route = complex_route_22
    complex_step_286 = importer.save_or_locate(complex_step_286)

    complex_step_287 = Step()
    complex_step_287.datetime = None
    complex_step_287.number = 1
    complex_step_287.place = complex_place_235
    complex_step_287.route = complex_route_23
    complex_step_287 = importer.save_or_locate(complex_step_287)

    complex_step_288 = Step()
    complex_step_288.datetime = None
    complex_step_288.number = 2
    complex_step_288.place = complex_place_298
    complex_step_288.route = complex_route_23
    complex_step_288 = importer.save_or_locate(complex_step_288)

    complex_step_289 = Step()
    complex_step_289.datetime = None
    complex_step_289.number = 3
    complex_step_289.place = complex_place_264
    complex_step_289.route = complex_route_23
    complex_step_289 = importer.save_or_locate(complex_step_289)

    complex_step_290 = Step()
    complex_step_290.datetime = None
    complex_step_290.number = 4
    complex_step_290.place = complex_place_246
    complex_step_290.route = complex_route_23
    complex_step_290 = importer.save_or_locate(complex_step_290)

    complex_step_291 = Step()
    complex_step_291.datetime = None
    complex_step_291.number = 1
    complex_step_291.place = complex_place_235
    complex_step_291.route = complex_route_24
    complex_step_291 = importer.save_or_locate(complex_step_291)

    complex_step_292 = Step()
    complex_step_292.datetime = None
    complex_step_292.number = 2
    complex_step_292.place = complex_place_224
    complex_step_292.route = complex_route_24
    complex_step_292 = importer.save_or_locate(complex_step_292)

    complex_step_293 = Step()
    complex_step_293.datetime = None
    complex_step_293.number = 3
    complex_step_293.place = complex_place_219
    complex_step_293.route = complex_route_24
    complex_step_293 = importer.save_or_locate(complex_step_293)

    complex_step_294 = Step()
    complex_step_294.datetime = None
    complex_step_294.number = 4
    complex_step_294.place = complex_place_214
    complex_step_294.route = complex_route_24
    complex_step_294 = importer.save_or_locate(complex_step_294)

    complex_step_295 = Step()
    complex_step_295.datetime = None
    complex_step_295.number = 5
    complex_step_295.place = complex_place_178
    complex_step_295.route = complex_route_24
    complex_step_295 = importer.save_or_locate(complex_step_295)

    complex_step_296 = Step()
    complex_step_296.datetime = None
    complex_step_296.number = 6
    complex_step_296.place = complex_place_172
    complex_step_296.route = complex_route_24
    complex_step_296 = importer.save_or_locate(complex_step_296)

    complex_step_297 = Step()
    complex_step_297.datetime = None
    complex_step_297.number = 7
    complex_step_297.place = complex_place_170
    complex_step_297.route = complex_route_24
    complex_step_297 = importer.save_or_locate(complex_step_297)

    complex_step_298 = Step()
    complex_step_298.datetime = None
    complex_step_298.number = 8
    complex_step_298.place = complex_place_162
    complex_step_298.route = complex_route_24
    complex_step_298 = importer.save_or_locate(complex_step_298)

    complex_step_299 = Step()
    complex_step_299.datetime = None
    complex_step_299.number = 9
    complex_step_299.place = complex_place_155
    complex_step_299.route = complex_route_24
    complex_step_299 = importer.save_or_locate(complex_step_299)

    complex_step_300 = Step()
    complex_step_300.datetime = None
    complex_step_300.number = 10
    complex_step_300.place = complex_place_154
    complex_step_300.route = complex_route_24
    complex_step_300 = importer.save_or_locate(complex_step_300)

    complex_step_301 = Step()
    complex_step_301.datetime = None
    complex_step_301.number = 11
    complex_step_301.place = complex_place_152
    complex_step_301.route = complex_route_24
    complex_step_301 = importer.save_or_locate(complex_step_301)

    complex_step_302 = Step()
    complex_step_302.datetime = None
    complex_step_302.number = 12
    complex_step_302.place = complex_place_131
    complex_step_302.route = complex_route_24
    complex_step_302 = importer.save_or_locate(complex_step_302)

    complex_step_303 = Step()
    complex_step_303.datetime = None
    complex_step_303.number = 13
    complex_step_303.place = complex_place_130
    complex_step_303.route = complex_route_24
    complex_step_303 = importer.save_or_locate(complex_step_303)

    complex_step_304 = Step()
    complex_step_304.datetime = None
    complex_step_304.number = 14
    complex_step_304.place = complex_place_132
    complex_step_304.route = complex_route_24
    complex_step_304 = importer.save_or_locate(complex_step_304)

    complex_step_305 = Step()
    complex_step_305.datetime = None
    complex_step_305.number = 15
    complex_step_305.place = complex_place_177
    complex_step_305.route = complex_route_24
    complex_step_305 = importer.save_or_locate(complex_step_305)

    complex_step_306 = Step()
    complex_step_306.datetime = None
    complex_step_306.number = 1
    complex_step_306.place = complex_place_488
    complex_step_306.route = complex_route_25
    complex_step_306 = importer.save_or_locate(complex_step_306)

    complex_step_307 = Step()
    complex_step_307.datetime = None
    complex_step_307.number = 2
    complex_step_307.place = complex_place_483
    complex_step_307.route = complex_route_25
    complex_step_307 = importer.save_or_locate(complex_step_307)

    complex_step_308 = Step()
    complex_step_308.datetime = None
    complex_step_308.number = 3
    complex_step_308.place = complex_place_484
    complex_step_308.route = complex_route_25
    complex_step_308 = importer.save_or_locate(complex_step_308)

    complex_step_309 = Step()
    complex_step_309.datetime = None
    complex_step_309.number = 4
    complex_step_309.place = complex_place_485
    complex_step_309.route = complex_route_25
    complex_step_309 = importer.save_or_locate(complex_step_309)

    complex_step_310 = Step()
    complex_step_310.datetime = None
    complex_step_310.number = 5
    complex_step_310.place = complex_place_486
    complex_step_310.route = complex_route_25
    complex_step_310 = importer.save_or_locate(complex_step_310)

    complex_step_311 = Step()
    complex_step_311.datetime = None
    complex_step_311.number = 6
    complex_step_311.place = complex_place_487
    complex_step_311.route = complex_route_25
    complex_step_311 = importer.save_or_locate(complex_step_311)

    complex_step_312 = Step()
    complex_step_312.datetime = None
    complex_step_312.number = 7
    complex_step_312.place = complex_place_489
    complex_step_312.route = complex_route_25
    complex_step_312 = importer.save_or_locate(complex_step_312)

    complex_step_313 = Step()
    complex_step_313.datetime = None
    complex_step_313.number = 8
    complex_step_313.place = complex_place_494
    complex_step_313.route = complex_route_25
    complex_step_313 = importer.save_or_locate(complex_step_313)

    complex_step_314 = Step()
    complex_step_314.datetime = None
    complex_step_314.number = 9
    complex_step_314.place = complex_place_496
    complex_step_314.route = complex_route_25
    complex_step_314 = importer.save_or_locate(complex_step_314)

    complex_step_315 = Step()
    complex_step_315.datetime = None
    complex_step_315.number = 10
    complex_step_315.place = complex_place_497
    complex_step_315.route = complex_route_25
    complex_step_315 = importer.save_or_locate(complex_step_315)

    complex_step_316 = Step()
    complex_step_316.datetime = None
    complex_step_316.number = 11
    complex_step_316.place = complex_place_499
    complex_step_316.route = complex_route_25
    complex_step_316 = importer.save_or_locate(complex_step_316)

    complex_step_317 = Step()
    complex_step_317.datetime = None
    complex_step_317.number = 12
    complex_step_317.place = complex_place_502
    complex_step_317.route = complex_route_25
    complex_step_317 = importer.save_or_locate(complex_step_317)

    complex_step_318 = Step()
    complex_step_318.datetime = None
    complex_step_318.number = 13
    complex_step_318.place = complex_place_513
    complex_step_318.route = complex_route_25
    complex_step_318 = importer.save_or_locate(complex_step_318)

    complex_step_319 = Step()
    complex_step_319.datetime = None
    complex_step_319.number = 14
    complex_step_319.place = complex_place_515
    complex_step_319.route = complex_route_25
    complex_step_319 = importer.save_or_locate(complex_step_319)

    complex_step_320 = Step()
    complex_step_320.datetime = None
    complex_step_320.number = 15
    complex_step_320.place = complex_place_514
    complex_step_320.route = complex_route_25
    complex_step_320 = importer.save_or_locate(complex_step_320)

    complex_step_321 = Step()
    complex_step_321.datetime = None
    complex_step_321.number = 16
    complex_step_321.place = complex_place_516
    complex_step_321.route = complex_route_25
    complex_step_321 = importer.save_or_locate(complex_step_321)

    complex_step_322 = Step()
    complex_step_322.datetime = None
    complex_step_322.number = 17
    complex_step_322.place = complex_place_509
    complex_step_322.route = complex_route_25
    complex_step_322 = importer.save_or_locate(complex_step_322)

    complex_step_323 = Step()
    complex_step_323.datetime = None
    complex_step_323.number = 18
    complex_step_323.place = complex_place_505
    complex_step_323.route = complex_route_25
    complex_step_323 = importer.save_or_locate(complex_step_323)

    complex_step_324 = Step()
    complex_step_324.datetime = None
    complex_step_324.number = 19
    complex_step_324.place = complex_place_503
    complex_step_324.route = complex_route_25
    complex_step_324 = importer.save_or_locate(complex_step_324)

    complex_step_325 = Step()
    complex_step_325.datetime = None
    complex_step_325.number = 1
    complex_step_325.place = complex_place_235
    complex_step_325.route = complex_route_26
    complex_step_325 = importer.save_or_locate(complex_step_325)

    complex_step_326 = Step()
    complex_step_326.datetime = None
    complex_step_326.number = 2
    complex_step_326.place = complex_place_507
    complex_step_326.route = complex_route_26
    complex_step_326 = importer.save_or_locate(complex_step_326)

    complex_step_327 = Step()
    complex_step_327.datetime = None
    complex_step_327.number = 3
    complex_step_327.place = complex_place_506
    complex_step_327.route = complex_route_26
    complex_step_327 = importer.save_or_locate(complex_step_327)

    complex_step_328 = Step()
    complex_step_328.datetime = None
    complex_step_328.number = 4
    complex_step_328.place = complex_place_508
    complex_step_328.route = complex_route_26
    complex_step_328 = importer.save_or_locate(complex_step_328)

    complex_step_329 = Step()
    complex_step_329.datetime = None
    complex_step_329.number = 5
    complex_step_329.place = complex_place_510
    complex_step_329.route = complex_route_26
    complex_step_329 = importer.save_or_locate(complex_step_329)

    complex_step_330 = Step()
    complex_step_330.datetime = None
    complex_step_330.number = 6
    complex_step_330.place = complex_place_492
    complex_step_330.route = complex_route_26
    complex_step_330 = importer.save_or_locate(complex_step_330)

    complex_step_331 = Step()
    complex_step_331.datetime = None
    complex_step_331.number = 7
    complex_step_331.place = complex_place_493
    complex_step_331.route = complex_route_26
    complex_step_331 = importer.save_or_locate(complex_step_331)

    complex_step_332 = Step()
    complex_step_332.datetime = None
    complex_step_332.number = 8
    complex_step_332.place = complex_place_528
    complex_step_332.route = complex_route_26
    complex_step_332 = importer.save_or_locate(complex_step_332)

    complex_step_333 = Step()
    complex_step_333.datetime = None
    complex_step_333.number = 9
    complex_step_333.place = complex_place_529
    complex_step_333.route = complex_route_26
    complex_step_333 = importer.save_or_locate(complex_step_333)

    complex_step_334 = Step()
    complex_step_334.datetime = None
    complex_step_334.number = 10
    complex_step_334.place = complex_place_531
    complex_step_334.route = complex_route_26
    complex_step_334 = importer.save_or_locate(complex_step_334)

    complex_step_335 = Step()
    complex_step_335.datetime = None
    complex_step_335.number = 11
    complex_step_335.place = complex_place_527
    complex_step_335.route = complex_route_26
    complex_step_335 = importer.save_or_locate(complex_step_335)

    complex_step_336 = Step()
    complex_step_336.datetime = None
    complex_step_336.number = 12
    complex_step_336.place = complex_place_526
    complex_step_336.route = complex_route_26
    complex_step_336 = importer.save_or_locate(complex_step_336)

    complex_step_337 = Step()
    complex_step_337.datetime = None
    complex_step_337.number = 13
    complex_step_337.place = complex_place_511
    complex_step_337.route = complex_route_26
    complex_step_337 = importer.save_or_locate(complex_step_337)

    complex_step_338 = Step()
    complex_step_338.datetime = None
    complex_step_338.number = 1
    complex_step_338.place = complex_place_40
    complex_step_338.route = complex_route_27
    complex_step_338 = importer.save_or_locate(complex_step_338)

    complex_step_339 = Step()
    complex_step_339.datetime = None
    complex_step_339.number = 2
    complex_step_339.place = complex_place_28
    complex_step_339.route = complex_route_27
    complex_step_339 = importer.save_or_locate(complex_step_339)

    complex_step_340 = Step()
    complex_step_340.datetime = None
    complex_step_340.number = 3
    complex_step_340.place = complex_place_29
    complex_step_340.route = complex_route_27
    complex_step_340 = importer.save_or_locate(complex_step_340)

    complex_step_341 = Step()
    complex_step_341.datetime = None
    complex_step_341.number = 4
    complex_step_341.place = complex_place_31
    complex_step_341.route = complex_route_27
    complex_step_341 = importer.save_or_locate(complex_step_341)

    complex_step_342 = Step()
    complex_step_342.datetime = None
    complex_step_342.number = 5
    complex_step_342.place = complex_place_30
    complex_step_342.route = complex_route_27
    complex_step_342 = importer.save_or_locate(complex_step_342)

    complex_step_343 = Step()
    complex_step_343.datetime = None
    complex_step_343.number = 6
    complex_step_343.place = complex_place_44
    complex_step_343.route = complex_route_27
    complex_step_343 = importer.save_or_locate(complex_step_343)

    complex_step_344 = Step()
    complex_step_344.datetime = None
    complex_step_344.number = 7
    complex_step_344.place = complex_place_45
    complex_step_344.route = complex_route_27
    complex_step_344 = importer.save_or_locate(complex_step_344)

    complex_step_345 = Step()
    complex_step_345.datetime = None
    complex_step_345.number = 8
    complex_step_345.place = complex_place_50
    complex_step_345.route = complex_route_27
    complex_step_345 = importer.save_or_locate(complex_step_345)

    complex_step_346 = Step()
    complex_step_346.datetime = None
    complex_step_346.number = 9
    complex_step_346.place = complex_place_51
    complex_step_346.route = complex_route_27
    complex_step_346 = importer.save_or_locate(complex_step_346)

    complex_step_347 = Step()
    complex_step_347.datetime = None
    complex_step_347.number = 10
    complex_step_347.place = complex_place_52
    complex_step_347.route = complex_route_27
    complex_step_347 = importer.save_or_locate(complex_step_347)

    complex_step_348 = Step()
    complex_step_348.datetime = None
    complex_step_348.number = 11
    complex_step_348.place = complex_place_53
    complex_step_348.route = complex_route_27
    complex_step_348 = importer.save_or_locate(complex_step_348)

    complex_step_349 = Step()
    complex_step_349.datetime = None
    complex_step_349.number = 12
    complex_step_349.place = complex_place_54
    complex_step_349.route = complex_route_27
    complex_step_349 = importer.save_or_locate(complex_step_349)

    complex_step_350 = Step()
    complex_step_350.datetime = None
    complex_step_350.number = 13
    complex_step_350.place = complex_place_37
    complex_step_350.route = complex_route_27
    complex_step_350 = importer.save_or_locate(complex_step_350)

    complex_step_351 = Step()
    complex_step_351.datetime = None
    complex_step_351.number = 1
    complex_step_351.place = complex_place_34
    complex_step_351.route = complex_route_28
    complex_step_351 = importer.save_or_locate(complex_step_351)

    complex_step_352 = Step()
    complex_step_352.datetime = None
    complex_step_352.number = 2
    complex_step_352.place = complex_place_33
    complex_step_352.route = complex_route_28
    complex_step_352 = importer.save_or_locate(complex_step_352)

    complex_step_353 = Step()
    complex_step_353.datetime = None
    complex_step_353.number = 3
    complex_step_353.place = complex_place_47
    complex_step_353.route = complex_route_28
    complex_step_353 = importer.save_or_locate(complex_step_353)

    complex_step_354 = Step()
    complex_step_354.datetime = None
    complex_step_354.number = 4
    complex_step_354.place = complex_place_35
    complex_step_354.route = complex_route_28
    complex_step_354 = importer.save_or_locate(complex_step_354)

    complex_step_355 = Step()
    complex_step_355.datetime = None
    complex_step_355.number = 5
    complex_step_355.place = complex_place_36
    complex_step_355.route = complex_route_28
    complex_step_355 = importer.save_or_locate(complex_step_355)

    complex_step_356 = Step()
    complex_step_356.datetime = None
    complex_step_356.number = 6
    complex_step_356.place = complex_place_39
    complex_step_356.route = complex_route_28
    complex_step_356 = importer.save_or_locate(complex_step_356)

    complex_step_357 = Step()
    complex_step_357.datetime = None
    complex_step_357.number = 7
    complex_step_357.place = complex_place_42
    complex_step_357.route = complex_route_28
    complex_step_357 = importer.save_or_locate(complex_step_357)

    complex_step_358 = Step()
    complex_step_358.datetime = None
    complex_step_358.number = 8
    complex_step_358.place = complex_place_38
    complex_step_358.route = complex_route_28
    complex_step_358 = importer.save_or_locate(complex_step_358)

    complex_step_359 = Step()
    complex_step_359.datetime = None
    complex_step_359.number = 9
    complex_step_359.place = complex_place_41
    complex_step_359.route = complex_route_28
    complex_step_359 = importer.save_or_locate(complex_step_359)

    complex_step_360 = Step()
    complex_step_360.datetime = None
    complex_step_360.number = 10
    complex_step_360.place = complex_place_43
    complex_step_360.route = complex_route_28
    complex_step_360 = importer.save_or_locate(complex_step_360)

    complex_step_361 = Step()
    complex_step_361.datetime = None
    complex_step_361.number = 11
    complex_step_361.place = complex_place_46
    complex_step_361.route = complex_route_28
    complex_step_361 = importer.save_or_locate(complex_step_361)

    complex_step_362 = Step()
    complex_step_362.datetime = None
    complex_step_362.number = 12
    complex_step_362.place = complex_place_48
    complex_step_362.route = complex_route_28
    complex_step_362 = importer.save_or_locate(complex_step_362)

    complex_step_363 = Step()
    complex_step_363.datetime = None
    complex_step_363.number = 13
    complex_step_363.place = complex_place_49
    complex_step_363.route = complex_route_28
    complex_step_363 = importer.save_or_locate(complex_step_363)

    complex_step_364 = Step()
    complex_step_364.datetime = None
    complex_step_364.number = 14
    complex_step_364.place = complex_place_55
    complex_step_364.route = complex_route_28
    complex_step_364 = importer.save_or_locate(complex_step_364)

    complex_step_365 = Step()
    complex_step_365.datetime = None
    complex_step_365.number = 15
    complex_step_365.place = complex_place_56
    complex_step_365.route = complex_route_28
    complex_step_365 = importer.save_or_locate(complex_step_365)

    complex_step_366 = Step()
    complex_step_366.datetime = None
    complex_step_366.number = 16
    complex_step_366.place = complex_place_25
    complex_step_366.route = complex_route_28
    complex_step_366 = importer.save_or_locate(complex_step_366)

    complex_step_367 = Step()
    complex_step_367.datetime = None
    complex_step_367.number = 17
    complex_step_367.place = complex_place_24
    complex_step_367.route = complex_route_28
    complex_step_367 = importer.save_or_locate(complex_step_367)

    complex_step_368 = Step()
    complex_step_368.datetime = None
    complex_step_368.number = 18
    complex_step_368.place = complex_place_27
    complex_step_368.route = complex_route_28
    complex_step_368 = importer.save_or_locate(complex_step_368)

    complex_step_369 = Step()
    complex_step_369.datetime = None
    complex_step_369.number = 19
    complex_step_369.place = complex_place_26
    complex_step_369.route = complex_route_28
    complex_step_369 = importer.save_or_locate(complex_step_369)

    complex_step_370 = Step()
    complex_step_370.datetime = None
    complex_step_370.number = 1
    complex_step_370.place = complex_place_295
    complex_step_370.route = complex_route_29
    complex_step_370 = importer.save_or_locate(complex_step_370)

    complex_step_371 = Step()
    complex_step_371.datetime = None
    complex_step_371.number = 2
    complex_step_371.place = complex_place_321
    complex_step_371.route = complex_route_29
    complex_step_371 = importer.save_or_locate(complex_step_371)

    complex_step_372 = Step()
    complex_step_372.datetime = None
    complex_step_372.number = 3
    complex_step_372.place = complex_place_322
    complex_step_372.route = complex_route_29
    complex_step_372 = importer.save_or_locate(complex_step_372)

    complex_step_373 = Step()
    complex_step_373.datetime = None
    complex_step_373.number = 4
    complex_step_373.place = complex_place_5
    complex_step_373.route = complex_route_29
    complex_step_373 = importer.save_or_locate(complex_step_373)

    complex_step_374 = Step()
    complex_step_374.datetime = None
    complex_step_374.number = 5
    complex_step_374.place = complex_place_4
    complex_step_374.route = complex_route_29
    complex_step_374 = importer.save_or_locate(complex_step_374)

    complex_step_375 = Step()
    complex_step_375.datetime = None
    complex_step_375.number = 6
    complex_step_375.place = complex_place_3
    complex_step_375.route = complex_route_29
    complex_step_375 = importer.save_or_locate(complex_step_375)

    complex_step_376 = Step()
    complex_step_376.datetime = None
    complex_step_376.number = 7
    complex_step_376.place = complex_place_2
    complex_step_376.route = complex_route_29
    complex_step_376 = importer.save_or_locate(complex_step_376)

    complex_step_377 = Step()
    complex_step_377.datetime = None
    complex_step_377.number = 8
    complex_step_377.place = complex_place_1
    complex_step_377.route = complex_route_29
    complex_step_377 = importer.save_or_locate(complex_step_377)

    complex_step_378 = Step()
    complex_step_378.datetime = None
    complex_step_378.number = 9
    complex_step_378.place = complex_place_9
    complex_step_378.route = complex_route_29
    complex_step_378 = importer.save_or_locate(complex_step_378)

    complex_step_379 = Step()
    complex_step_379.datetime = None
    complex_step_379.number = 1
    complex_step_379.place = complex_place_223
    complex_step_379.route = complex_route_30
    complex_step_379 = importer.save_or_locate(complex_step_379)

    complex_step_380 = Step()
    complex_step_380.datetime = None
    complex_step_380.number = 2
    complex_step_380.place = complex_place_13
    complex_step_380.route = complex_route_30
    complex_step_380 = importer.save_or_locate(complex_step_380)

    complex_step_381 = Step()
    complex_step_381.datetime = None
    complex_step_381.number = 3
    complex_step_381.place = complex_place_21
    complex_step_381.route = complex_route_30
    complex_step_381 = importer.save_or_locate(complex_step_381)

    complex_step_382 = Step()
    complex_step_382.datetime = None
    complex_step_382.number = 4
    complex_step_382.place = complex_place_20
    complex_step_382.route = complex_route_30
    complex_step_382 = importer.save_or_locate(complex_step_382)

    complex_step_383 = Step()
    complex_step_383.datetime = None
    complex_step_383.number = 5
    complex_step_383.place = complex_place_11
    complex_step_383.route = complex_route_30
    complex_step_383 = importer.save_or_locate(complex_step_383)

    complex_step_384 = Step()
    complex_step_384.datetime = None
    complex_step_384.number = 6
    complex_step_384.place = complex_place_12
    complex_step_384.route = complex_route_30
    complex_step_384 = importer.save_or_locate(complex_step_384)

    complex_step_385 = Step()
    complex_step_385.datetime = None
    complex_step_385.number = 7
    complex_step_385.place = complex_place_22
    complex_step_385.route = complex_route_30
    complex_step_385 = importer.save_or_locate(complex_step_385)

    complex_step_386 = Step()
    complex_step_386.datetime = None
    complex_step_386.number = 8
    complex_step_386.place = complex_place_19
    complex_step_386.route = complex_route_30
    complex_step_386 = importer.save_or_locate(complex_step_386)

    complex_step_387 = Step()
    complex_step_387.datetime = None
    complex_step_387.number = 9
    complex_step_387.place = complex_place_18
    complex_step_387.route = complex_route_30
    complex_step_387 = importer.save_or_locate(complex_step_387)

    complex_step_388 = Step()
    complex_step_388.datetime = None
    complex_step_388.number = 10
    complex_step_388.place = complex_place_14
    complex_step_388.route = complex_route_30
    complex_step_388 = importer.save_or_locate(complex_step_388)

    complex_step_389 = Step()
    complex_step_389.datetime = None
    complex_step_389.number = 11
    complex_step_389.place = complex_place_15
    complex_step_389.route = complex_route_30
    complex_step_389 = importer.save_or_locate(complex_step_389)

    complex_step_390 = Step()
    complex_step_390.datetime = None
    complex_step_390.number = 12
    complex_step_390.place = complex_place_17
    complex_step_390.route = complex_route_30
    complex_step_390 = importer.save_or_locate(complex_step_390)

    complex_step_391 = Step()
    complex_step_391.datetime = None
    complex_step_391.number = 13
    complex_step_391.place = complex_place_16
    complex_step_391.route = complex_route_30
    complex_step_391 = importer.save_or_locate(complex_step_391)

    complex_step_392 = Step()
    complex_step_392.datetime = None
    complex_step_392.number = 14
    complex_step_392.place = complex_place_23
    complex_step_392.route = complex_route_30
    complex_step_392 = importer.save_or_locate(complex_step_392)

    complex_step_393 = Step()
    complex_step_393.datetime = None
    complex_step_393.number = 15
    complex_step_393.place = complex_place_8
    complex_step_393.route = complex_route_30
    complex_step_393 = importer.save_or_locate(complex_step_393)

    complex_step_394 = Step()
    complex_step_394.datetime = None
    complex_step_394.number = 16
    complex_step_394.place = complex_place_6
    complex_step_394.route = complex_route_30
    complex_step_394 = importer.save_or_locate(complex_step_394)

    complex_step_395 = Step()
    complex_step_395.datetime = None
    complex_step_395.number = 17
    complex_step_395.place = complex_place_303
    complex_step_395.route = complex_route_30
    complex_step_395 = importer.save_or_locate(complex_step_395)

    complex_step_396 = Step()
    complex_step_396.datetime = None
    complex_step_396.number = 1
    complex_step_396.place = complex_place_379
    complex_step_396.route = complex_route_31
    complex_step_396 = importer.save_or_locate(complex_step_396)

    complex_step_397 = Step()
    complex_step_397.datetime = None
    complex_step_397.number = 2
    complex_step_397.place = complex_place_363
    complex_step_397.route = complex_route_31
    complex_step_397 = importer.save_or_locate(complex_step_397)

    complex_step_398 = Step()
    complex_step_398.datetime = None
    complex_step_398.number = 3
    complex_step_398.place = complex_place_365
    complex_step_398.route = complex_route_31
    complex_step_398 = importer.save_or_locate(complex_step_398)

    complex_step_399 = Step()
    complex_step_399.datetime = None
    complex_step_399.number = 4
    complex_step_399.place = complex_place_369
    complex_step_399.route = complex_route_31
    complex_step_399 = importer.save_or_locate(complex_step_399)

    complex_step_400 = Step()
    complex_step_400.datetime = None
    complex_step_400.number = 5
    complex_step_400.place = complex_place_364
    complex_step_400.route = complex_route_31
    complex_step_400 = importer.save_or_locate(complex_step_400)

    complex_step_401 = Step()
    complex_step_401.datetime = None
    complex_step_401.number = 6
    complex_step_401.place = complex_place_370
    complex_step_401.route = complex_route_31
    complex_step_401 = importer.save_or_locate(complex_step_401)

    complex_step_402 = Step()
    complex_step_402.datetime = None
    complex_step_402.number = 7
    complex_step_402.place = complex_place_371
    complex_step_402.route = complex_route_31
    complex_step_402 = importer.save_or_locate(complex_step_402)

    complex_step_403 = Step()
    complex_step_403.datetime = None
    complex_step_403.number = 8
    complex_step_403.place = complex_place_372
    complex_step_403.route = complex_route_31
    complex_step_403 = importer.save_or_locate(complex_step_403)

    complex_step_404 = Step()
    complex_step_404.datetime = None
    complex_step_404.number = 9
    complex_step_404.place = complex_place_376
    complex_step_404.route = complex_route_31
    complex_step_404 = importer.save_or_locate(complex_step_404)

    complex_step_405 = Step()
    complex_step_405.datetime = None
    complex_step_405.number = 10
    complex_step_405.place = complex_place_374
    complex_step_405.route = complex_route_31
    complex_step_405 = importer.save_or_locate(complex_step_405)

    complex_step_406 = Step()
    complex_step_406.datetime = None
    complex_step_406.number = 11
    complex_step_406.place = complex_place_381
    complex_step_406.route = complex_route_31
    complex_step_406 = importer.save_or_locate(complex_step_406)

    complex_step_407 = Step()
    complex_step_407.datetime = None
    complex_step_407.number = 12
    complex_step_407.place = complex_place_380
    complex_step_407.route = complex_route_31
    complex_step_407 = importer.save_or_locate(complex_step_407)

    complex_step_408 = Step()
    complex_step_408.datetime = None
    complex_step_408.number = 13
    complex_step_408.place = complex_place_378
    complex_step_408.route = complex_route_31
    complex_step_408 = importer.save_or_locate(complex_step_408)

    complex_step_409 = Step()
    complex_step_409.datetime = None
    complex_step_409.number = 14
    complex_step_409.place = complex_place_377
    complex_step_409.route = complex_route_31
    complex_step_409 = importer.save_or_locate(complex_step_409)

    complex_step_410 = Step()
    complex_step_410.datetime = None
    complex_step_410.number = 15
    complex_step_410.place = complex_place_351
    complex_step_410.route = complex_route_31
    complex_step_410 = importer.save_or_locate(complex_step_410)

    complex_step_411 = Step()
    complex_step_411.datetime = None
    complex_step_411.number = 16
    complex_step_411.place = complex_place_352
    complex_step_411.route = complex_route_31
    complex_step_411 = importer.save_or_locate(complex_step_411)

    complex_step_412 = Step()
    complex_step_412.datetime = None
    complex_step_412.number = 17
    complex_step_412.place = complex_place_357
    complex_step_412.route = complex_route_31
    complex_step_412 = importer.save_or_locate(complex_step_412)

    complex_step_413 = Step()
    complex_step_413.datetime = None
    complex_step_413.number = 18
    complex_step_413.place = complex_place_358
    complex_step_413.route = complex_route_31
    complex_step_413 = importer.save_or_locate(complex_step_413)

    complex_step_414 = Step()
    complex_step_414.datetime = None
    complex_step_414.number = 19
    complex_step_414.place = complex_place_354
    complex_step_414.route = complex_route_31
    complex_step_414 = importer.save_or_locate(complex_step_414)

    complex_step_415 = Step()
    complex_step_415.datetime = None
    complex_step_415.number = 20
    complex_step_415.place = complex_place_355
    complex_step_415.route = complex_route_31
    complex_step_415 = importer.save_or_locate(complex_step_415)

    complex_step_416 = Step()
    complex_step_416.datetime = None
    complex_step_416.number = 21
    complex_step_416.place = complex_place_353
    complex_step_416.route = complex_route_31
    complex_step_416 = importer.save_or_locate(complex_step_416)

    complex_step_417 = Step()
    complex_step_417.datetime = None
    complex_step_417.number = 22
    complex_step_417.place = complex_place_359
    complex_step_417.route = complex_route_31
    complex_step_417 = importer.save_or_locate(complex_step_417)

    complex_step_418 = Step()
    complex_step_418.datetime = None
    complex_step_418.number = 23
    complex_step_418.place = complex_place_356
    complex_step_418.route = complex_route_31
    complex_step_418 = importer.save_or_locate(complex_step_418)

    complex_step_419 = Step()
    complex_step_419.datetime = None
    complex_step_419.number = 24
    complex_step_419.place = complex_place_360
    complex_step_419.route = complex_route_31
    complex_step_419 = importer.save_or_locate(complex_step_419)

    complex_step_420 = Step()
    complex_step_420.datetime = None
    complex_step_420.number = 25
    complex_step_420.place = complex_place_382
    complex_step_420.route = complex_route_31
    complex_step_420 = importer.save_or_locate(complex_step_420)

    complex_step_421 = Step()
    complex_step_421.datetime = None
    complex_step_421.number = 1
    complex_step_421.place = complex_place_258
    complex_step_421.route = complex_route_32
    complex_step_421 = importer.save_or_locate(complex_step_421)

    complex_step_422 = Step()
    complex_step_422.datetime = None
    complex_step_422.number = 2
    complex_step_422.place = complex_place_259
    complex_step_422.route = complex_route_32
    complex_step_422 = importer.save_or_locate(complex_step_422)

    complex_step_423 = Step()
    complex_step_423.datetime = None
    complex_step_423.number = 3
    complex_step_423.place = complex_place_267
    complex_step_423.route = complex_route_32
    complex_step_423 = importer.save_or_locate(complex_step_423)

    complex_step_424 = Step()
    complex_step_424.datetime = None
    complex_step_424.number = 4
    complex_step_424.place = complex_place_268
    complex_step_424.route = complex_route_32
    complex_step_424 = importer.save_or_locate(complex_step_424)

    complex_step_425 = Step()
    complex_step_425.datetime = None
    complex_step_425.number = 5
    complex_step_425.place = complex_place_261
    complex_step_425.route = complex_route_32
    complex_step_425 = importer.save_or_locate(complex_step_425)

    complex_step_426 = Step()
    complex_step_426.datetime = None
    complex_step_426.number = 6
    complex_step_426.place = complex_place_262
    complex_step_426.route = complex_route_32
    complex_step_426 = importer.save_or_locate(complex_step_426)

    complex_step_427 = Step()
    complex_step_427.datetime = None
    complex_step_427.number = 7
    complex_step_427.place = complex_place_263
    complex_step_427.route = complex_route_32
    complex_step_427 = importer.save_or_locate(complex_step_427)

    complex_step_428 = Step()
    complex_step_428.datetime = None
    complex_step_428.number = 8
    complex_step_428.place = complex_place_260
    complex_step_428.route = complex_route_32
    complex_step_428 = importer.save_or_locate(complex_step_428)

    complex_step_429 = Step()
    complex_step_429.datetime = None
    complex_step_429.number = 9
    complex_step_429.place = complex_place_271
    complex_step_429.route = complex_route_32
    complex_step_429 = importer.save_or_locate(complex_step_429)

    complex_step_430 = Step()
    complex_step_430.datetime = None
    complex_step_430.number = 10
    complex_step_430.place = complex_place_257
    complex_step_430.route = complex_route_32
    complex_step_430 = importer.save_or_locate(complex_step_430)

    complex_step_431 = Step()
    complex_step_431.datetime = None
    complex_step_431.number = 11
    complex_step_431.place = complex_place_274
    complex_step_431.route = complex_route_32
    complex_step_431 = importer.save_or_locate(complex_step_431)

    complex_step_432 = Step()
    complex_step_432.datetime = None
    complex_step_432.number = 12
    complex_step_432.place = complex_place_291
    complex_step_432.route = complex_route_32
    complex_step_432 = importer.save_or_locate(complex_step_432)

    complex_step_433 = Step()
    complex_step_433.datetime = None
    complex_step_433.number = 13
    complex_step_433.place = complex_place_278
    complex_step_433.route = complex_route_32
    complex_step_433 = importer.save_or_locate(complex_step_433)

    complex_step_434 = Step()
    complex_step_434.datetime = None
    complex_step_434.number = 14
    complex_step_434.place = complex_place_281
    complex_step_434.route = complex_route_32
    complex_step_434 = importer.save_or_locate(complex_step_434)

    complex_step_435 = Step()
    complex_step_435.datetime = None
    complex_step_435.number = 15
    complex_step_435.place = complex_place_297
    complex_step_435.route = complex_route_32
    complex_step_435 = importer.save_or_locate(complex_step_435)

    complex_step_436 = Step()
    complex_step_436.datetime = None
    complex_step_436.number = 16
    complex_step_436.place = complex_place_289
    complex_step_436.route = complex_route_32
    complex_step_436 = importer.save_or_locate(complex_step_436)

    complex_step_437 = Step()
    complex_step_437.datetime = None
    complex_step_437.number = 17
    complex_step_437.place = complex_place_265
    complex_step_437.route = complex_route_32
    complex_step_437 = importer.save_or_locate(complex_step_437)

    complex_step_438 = Step()
    complex_step_438.datetime = None
    complex_step_438.number = 18
    complex_step_438.place = complex_place_266
    complex_step_438.route = complex_route_32
    complex_step_438 = importer.save_or_locate(complex_step_438)

    complex_step_439 = Step()
    complex_step_439.datetime = None
    complex_step_439.number = 19
    complex_step_439.place = complex_place_253
    complex_step_439.route = complex_route_32
    complex_step_439 = importer.save_or_locate(complex_step_439)

    complex_step_440 = Step()
    complex_step_440.datetime = None
    complex_step_440.number = 1
    complex_step_440.place = complex_place_551
    complex_step_440.route = complex_route_33
    complex_step_440 = importer.save_or_locate(complex_step_440)

    complex_step_441 = Step()
    complex_step_441.datetime = None
    complex_step_441.number = 2
    complex_step_441.place = complex_place_550
    complex_step_441.route = complex_route_33
    complex_step_441 = importer.save_or_locate(complex_step_441)

    complex_step_442 = Step()
    complex_step_442.datetime = None
    complex_step_442.number = 3
    complex_step_442.place = complex_place_547
    complex_step_442.route = complex_route_33
    complex_step_442 = importer.save_or_locate(complex_step_442)

    complex_step_443 = Step()
    complex_step_443.datetime = None
    complex_step_443.number = 4
    complex_step_443.place = complex_place_546
    complex_step_443.route = complex_route_33
    complex_step_443 = importer.save_or_locate(complex_step_443)

    complex_step_444 = Step()
    complex_step_444.datetime = None
    complex_step_444.number = 5
    complex_step_444.place = complex_place_545
    complex_step_444.route = complex_route_33
    complex_step_444 = importer.save_or_locate(complex_step_444)

    complex_step_445 = Step()
    complex_step_445.datetime = None
    complex_step_445.number = 6
    complex_step_445.place = complex_place_542
    complex_step_445.route = complex_route_33
    complex_step_445 = importer.save_or_locate(complex_step_445)

    complex_step_446 = Step()
    complex_step_446.datetime = None
    complex_step_446.number = 7
    complex_step_446.place = complex_place_543
    complex_step_446.route = complex_route_33
    complex_step_446 = importer.save_or_locate(complex_step_446)

    complex_step_447 = Step()
    complex_step_447.datetime = None
    complex_step_447.number = 8
    complex_step_447.place = complex_place_544
    complex_step_447.route = complex_route_33
    complex_step_447 = importer.save_or_locate(complex_step_447)

    complex_step_448 = Step()
    complex_step_448.datetime = None
    complex_step_448.number = 9
    complex_step_448.place = complex_place_540
    complex_step_448.route = complex_route_33
    complex_step_448 = importer.save_or_locate(complex_step_448)

    complex_step_449 = Step()
    complex_step_449.datetime = None
    complex_step_449.number = 10
    complex_step_449.place = complex_place_539
    complex_step_449.route = complex_route_33
    complex_step_449 = importer.save_or_locate(complex_step_449)

    complex_step_450 = Step()
    complex_step_450.datetime = None
    complex_step_450.number = 11
    complex_step_450.place = complex_place_538
    complex_step_450.route = complex_route_33
    complex_step_450 = importer.save_or_locate(complex_step_450)

    complex_step_451 = Step()
    complex_step_451.datetime = None
    complex_step_451.number = 12
    complex_step_451.place = complex_place_553
    complex_step_451.route = complex_route_33
    complex_step_451 = importer.save_or_locate(complex_step_451)

    complex_step_452 = Step()
    complex_step_452.datetime = None
    complex_step_452.number = 13
    complex_step_452.place = complex_place_549
    complex_step_452.route = complex_route_33
    complex_step_452 = importer.save_or_locate(complex_step_452)

    complex_step_453 = Step()
    complex_step_453.datetime = None
    complex_step_453.number = 14
    complex_step_453.place = complex_place_548
    complex_step_453.route = complex_route_33
    complex_step_453 = importer.save_or_locate(complex_step_453)

    complex_step_454 = Step()
    complex_step_454.datetime = None
    complex_step_454.number = 15
    complex_step_454.place = complex_place_541
    complex_step_454.route = complex_route_33
    complex_step_454 = importer.save_or_locate(complex_step_454)

    complex_step_455 = Step()
    complex_step_455.datetime = None
    complex_step_455.number = 16
    complex_step_455.place = complex_place_552
    complex_step_455.route = complex_route_33
    complex_step_455 = importer.save_or_locate(complex_step_455)

    complex_step_456 = Step()
    complex_step_456.datetime = None
    complex_step_456.number = 1
    complex_step_456.place = complex_place_523
    complex_step_456.route = complex_route_34
    complex_step_456 = importer.save_or_locate(complex_step_456)

    complex_step_457 = Step()
    complex_step_457.datetime = None
    complex_step_457.number = 2
    complex_step_457.place = complex_place_293
    complex_step_457.route = complex_route_34
    complex_step_457 = importer.save_or_locate(complex_step_457)

    complex_step_458 = Step()
    complex_step_458.datetime = None
    complex_step_458.number = 3
    complex_step_458.place = complex_place_296
    complex_step_458.route = complex_route_34
    complex_step_458 = importer.save_or_locate(complex_step_458)

    complex_step_459 = Step()
    complex_step_459.datetime = None
    complex_step_459.number = 4
    complex_step_459.place = complex_place_300
    complex_step_459.route = complex_route_34
    complex_step_459 = importer.save_or_locate(complex_step_459)

    complex_step_460 = Step()
    complex_step_460.datetime = None
    complex_step_460.number = 5
    complex_step_460.place = complex_place_302
    complex_step_460.route = complex_route_34
    complex_step_460 = importer.save_or_locate(complex_step_460)

    complex_step_461 = Step()
    complex_step_461.datetime = None
    complex_step_461.number = 6
    complex_step_461.place = complex_place_467
    complex_step_461.route = complex_route_34
    complex_step_461 = importer.save_or_locate(complex_step_461)

    complex_step_462 = Step()
    complex_step_462.datetime = None
    complex_step_462.number = 1
    complex_step_462.place = complex_place_450
    complex_step_462.route = complex_route_35
    complex_step_462 = importer.save_or_locate(complex_step_462)

    complex_step_463 = Step()
    complex_step_463.datetime = None
    complex_step_463.number = 2
    complex_step_463.place = complex_place_468
    complex_step_463.route = complex_route_35
    complex_step_463 = importer.save_or_locate(complex_step_463)

    complex_step_464 = Step()
    complex_step_464.datetime = None
    complex_step_464.number = 3
    complex_step_464.place = complex_place_465
    complex_step_464.route = complex_route_35
    complex_step_464 = importer.save_or_locate(complex_step_464)

    complex_step_465 = Step()
    complex_step_465.datetime = None
    complex_step_465.number = 4
    complex_step_465.place = complex_place_462
    complex_step_465.route = complex_route_35
    complex_step_465 = importer.save_or_locate(complex_step_465)

    complex_step_466 = Step()
    complex_step_466.datetime = None
    complex_step_466.number = 5
    complex_step_466.place = complex_place_455
    complex_step_466.route = complex_route_35
    complex_step_466 = importer.save_or_locate(complex_step_466)

    complex_step_467 = Step()
    complex_step_467.datetime = None
    complex_step_467.number = 6
    complex_step_467.place = complex_place_445
    complex_step_467.route = complex_route_35
    complex_step_467 = importer.save_or_locate(complex_step_467)

    complex_step_468 = Step()
    complex_step_468.datetime = None
    complex_step_468.number = 7
    complex_step_468.place = complex_place_446
    complex_step_468.route = complex_route_35
    complex_step_468 = importer.save_or_locate(complex_step_468)

    complex_step_469 = Step()
    complex_step_469.datetime = None
    complex_step_469.number = 8
    complex_step_469.place = complex_place_447
    complex_step_469.route = complex_route_35
    complex_step_469 = importer.save_or_locate(complex_step_469)

    complex_step_470 = Step()
    complex_step_470.datetime = None
    complex_step_470.number = 9
    complex_step_470.place = complex_place_448
    complex_step_470.route = complex_route_35
    complex_step_470 = importer.save_or_locate(complex_step_470)

    complex_step_471 = Step()
    complex_step_471.datetime = None
    complex_step_471.number = 10
    complex_step_471.place = complex_place_451
    complex_step_471.route = complex_route_35
    complex_step_471 = importer.save_or_locate(complex_step_471)

    complex_step_472 = Step()
    complex_step_472.datetime = None
    complex_step_472.number = 11
    complex_step_472.place = complex_place_472
    complex_step_472.route = complex_route_35
    complex_step_472 = importer.save_or_locate(complex_step_472)

    complex_step_473 = Step()
    complex_step_473.datetime = None
    complex_step_473.number = 12
    complex_step_473.place = complex_place_473
    complex_step_473.route = complex_route_35
    complex_step_473 = importer.save_or_locate(complex_step_473)

    complex_step_474 = Step()
    complex_step_474.datetime = None
    complex_step_474.number = 13
    complex_step_474.place = complex_place_474
    complex_step_474.route = complex_route_35
    complex_step_474 = importer.save_or_locate(complex_step_474)

    complex_step_475 = Step()
    complex_step_475.datetime = None
    complex_step_475.number = 14
    complex_step_475.place = complex_place_471
    complex_step_475.route = complex_route_35
    complex_step_475 = importer.save_or_locate(complex_step_475)

    complex_step_476 = Step()
    complex_step_476.datetime = None
    complex_step_476.number = 15
    complex_step_476.place = complex_place_469
    complex_step_476.route = complex_route_35
    complex_step_476 = importer.save_or_locate(complex_step_476)

    complex_step_477 = Step()
    complex_step_477.datetime = None
    complex_step_477.number = 16
    complex_step_477.place = complex_place_466
    complex_step_477.route = complex_route_35
    complex_step_477 = importer.save_or_locate(complex_step_477)

    complex_step_478 = Step()
    complex_step_478.datetime = None
    complex_step_478.number = 17
    complex_step_478.place = complex_place_452
    complex_step_478.route = complex_route_35
    complex_step_478 = importer.save_or_locate(complex_step_478)

    complex_step_479 = Step()
    complex_step_479.datetime = None
    complex_step_479.number = 18
    complex_step_479.place = complex_place_434
    complex_step_479.route = complex_route_35
    complex_step_479 = importer.save_or_locate(complex_step_479)

    complex_step_480 = Step()
    complex_step_480.datetime = None
    complex_step_480.number = 19
    complex_step_480.place = complex_place_433
    complex_step_480.route = complex_route_35
    complex_step_480 = importer.save_or_locate(complex_step_480)

    complex_step_481 = Step()
    complex_step_481.datetime = None
    complex_step_481.number = 20
    complex_step_481.place = complex_place_432
    complex_step_481.route = complex_route_35
    complex_step_481 = importer.save_or_locate(complex_step_481)

    complex_step_482 = Step()
    complex_step_482.datetime = None
    complex_step_482.number = 1
    complex_step_482.place = complex_place_442
    complex_step_482.route = complex_route_36
    complex_step_482 = importer.save_or_locate(complex_step_482)

    complex_step_483 = Step()
    complex_step_483.datetime = None
    complex_step_483.number = 2
    complex_step_483.place = complex_place_459
    complex_step_483.route = complex_route_36
    complex_step_483 = importer.save_or_locate(complex_step_483)

    complex_step_484 = Step()
    complex_step_484.datetime = None
    complex_step_484.number = 3
    complex_step_484.place = complex_place_458
    complex_step_484.route = complex_route_36
    complex_step_484 = importer.save_or_locate(complex_step_484)

    complex_step_485 = Step()
    complex_step_485.datetime = None
    complex_step_485.number = 4
    complex_step_485.place = complex_place_457
    complex_step_485.route = complex_route_36
    complex_step_485 = importer.save_or_locate(complex_step_485)

    complex_step_486 = Step()
    complex_step_486.datetime = None
    complex_step_486.number = 5
    complex_step_486.place = complex_place_456
    complex_step_486.route = complex_route_36
    complex_step_486 = importer.save_or_locate(complex_step_486)

    complex_step_487 = Step()
    complex_step_487.datetime = None
    complex_step_487.number = 6
    complex_step_487.place = complex_place_461
    complex_step_487.route = complex_route_36
    complex_step_487 = importer.save_or_locate(complex_step_487)

    complex_step_488 = Step()
    complex_step_488.datetime = None
    complex_step_488.number = 7
    complex_step_488.place = complex_place_460
    complex_step_488.route = complex_route_36
    complex_step_488 = importer.save_or_locate(complex_step_488)

    complex_step_489 = Step()
    complex_step_489.datetime = None
    complex_step_489.number = 8
    complex_step_489.place = complex_place_437
    complex_step_489.route = complex_route_36
    complex_step_489 = importer.save_or_locate(complex_step_489)

    complex_step_490 = Step()
    complex_step_490.datetime = None
    complex_step_490.number = 9
    complex_step_490.place = complex_place_454
    complex_step_490.route = complex_route_36
    complex_step_490 = importer.save_or_locate(complex_step_490)

    complex_step_491 = Step()
    complex_step_491.datetime = None
    complex_step_491.number = 10
    complex_step_491.place = complex_place_453
    complex_step_491.route = complex_route_36
    complex_step_491 = importer.save_or_locate(complex_step_491)

    complex_step_492 = Step()
    complex_step_492.datetime = None
    complex_step_492.number = 11
    complex_step_492.place = complex_place_449
    complex_step_492.route = complex_route_36
    complex_step_492 = importer.save_or_locate(complex_step_492)

    complex_step_493 = Step()
    complex_step_493.datetime = None
    complex_step_493.number = 12
    complex_step_493.place = complex_place_464
    complex_step_493.route = complex_route_36
    complex_step_493 = importer.save_or_locate(complex_step_493)

    complex_step_494 = Step()
    complex_step_494.datetime = None
    complex_step_494.number = 13
    complex_step_494.place = complex_place_463
    complex_step_494.route = complex_route_36
    complex_step_494 = importer.save_or_locate(complex_step_494)

    complex_step_495 = Step()
    complex_step_495.datetime = None
    complex_step_495.number = 14
    complex_step_495.place = complex_place_443
    complex_step_495.route = complex_route_36
    complex_step_495 = importer.save_or_locate(complex_step_495)

    complex_step_496 = Step()
    complex_step_496.datetime = None
    complex_step_496.number = 15
    complex_step_496.place = complex_place_441
    complex_step_496.route = complex_route_36
    complex_step_496 = importer.save_or_locate(complex_step_496)

    complex_step_497 = Step()
    complex_step_497.datetime = None
    complex_step_497.number = 16
    complex_step_497.place = complex_place_440
    complex_step_497.route = complex_route_36
    complex_step_497 = importer.save_or_locate(complex_step_497)

    complex_step_498 = Step()
    complex_step_498.datetime = None
    complex_step_498.number = 17
    complex_step_498.place = complex_place_439
    complex_step_498.route = complex_route_36
    complex_step_498 = importer.save_or_locate(complex_step_498)

    complex_step_499 = Step()
    complex_step_499.datetime = None
    complex_step_499.number = 18
    complex_step_499.place = complex_place_438
    complex_step_499.route = complex_route_36
    complex_step_499 = importer.save_or_locate(complex_step_499)

    complex_step_500 = Step()
    complex_step_500.datetime = None
    complex_step_500.number = 19
    complex_step_500.place = complex_place_435
    complex_step_500.route = complex_route_36
    complex_step_500 = importer.save_or_locate(complex_step_500)

    complex_step_501 = Step()
    complex_step_501.datetime = None
    complex_step_501.number = 20
    complex_step_501.place = complex_place_436
    complex_step_501.route = complex_route_36
    complex_step_501 = importer.save_or_locate(complex_step_501)

    complex_step_502 = Step()
    complex_step_502.datetime = None
    complex_step_502.number = 1
    complex_step_502.place = complex_place_202
    complex_step_502.route = complex_route_37
    complex_step_502 = importer.save_or_locate(complex_step_502)

    complex_step_503 = Step()
    complex_step_503.datetime = None
    complex_step_503.number = 2
    complex_step_503.place = complex_place_186
    complex_step_503.route = complex_route_37
    complex_step_503 = importer.save_or_locate(complex_step_503)

    complex_step_504 = Step()
    complex_step_504.datetime = None
    complex_step_504.number = 3
    complex_step_504.place = complex_place_198
    complex_step_504.route = complex_route_37
    complex_step_504 = importer.save_or_locate(complex_step_504)

    complex_step_505 = Step()
    complex_step_505.datetime = None
    complex_step_505.number = 4
    complex_step_505.place = complex_place_200
    complex_step_505.route = complex_route_37
    complex_step_505 = importer.save_or_locate(complex_step_505)

    complex_step_506 = Step()
    complex_step_506.datetime = None
    complex_step_506.number = 5
    complex_step_506.place = complex_place_201
    complex_step_506.route = complex_route_37
    complex_step_506 = importer.save_or_locate(complex_step_506)

    complex_step_507 = Step()
    complex_step_507.datetime = None
    complex_step_507.number = 6
    complex_step_507.place = complex_place_199
    complex_step_507.route = complex_route_37
    complex_step_507 = importer.save_or_locate(complex_step_507)

    complex_step_508 = Step()
    complex_step_508.datetime = None
    complex_step_508.number = 7
    complex_step_508.place = complex_place_195
    complex_step_508.route = complex_route_37
    complex_step_508 = importer.save_or_locate(complex_step_508)

    complex_step_509 = Step()
    complex_step_509.datetime = None
    complex_step_509.number = 8
    complex_step_509.place = complex_place_189
    complex_step_509.route = complex_route_37
    complex_step_509 = importer.save_or_locate(complex_step_509)

    complex_step_510 = Step()
    complex_step_510.datetime = None
    complex_step_510.number = 9
    complex_step_510.place = complex_place_188
    complex_step_510.route = complex_route_37
    complex_step_510 = importer.save_or_locate(complex_step_510)

    complex_step_511 = Step()
    complex_step_511.datetime = None
    complex_step_511.number = 10
    complex_step_511.place = complex_place_183
    complex_step_511.route = complex_route_37
    complex_step_511 = importer.save_or_locate(complex_step_511)

    complex_step_512 = Step()
    complex_step_512.datetime = None
    complex_step_512.number = 11
    complex_step_512.place = complex_place_184
    complex_step_512.route = complex_route_37
    complex_step_512 = importer.save_or_locate(complex_step_512)

    complex_step_513 = Step()
    complex_step_513.datetime = None
    complex_step_513.number = 12
    complex_step_513.place = complex_place_181
    complex_step_513.route = complex_route_37
    complex_step_513 = importer.save_or_locate(complex_step_513)

    complex_step_514 = Step()
    complex_step_514.datetime = None
    complex_step_514.number = 13
    complex_step_514.place = complex_place_182
    complex_step_514.route = complex_route_37
    complex_step_514 = importer.save_or_locate(complex_step_514)

    complex_step_515 = Step()
    complex_step_515.datetime = None
    complex_step_515.number = 14
    complex_step_515.place = complex_place_185
    complex_step_515.route = complex_route_37
    complex_step_515 = importer.save_or_locate(complex_step_515)

    complex_step_516 = Step()
    complex_step_516.datetime = None
    complex_step_516.number = 15
    complex_step_516.place = complex_place_187
    complex_step_516.route = complex_route_37
    complex_step_516 = importer.save_or_locate(complex_step_516)

    complex_step_517 = Step()
    complex_step_517.datetime = None
    complex_step_517.number = 16
    complex_step_517.place = complex_place_191
    complex_step_517.route = complex_route_37
    complex_step_517 = importer.save_or_locate(complex_step_517)

    complex_step_518 = Step()
    complex_step_518.datetime = None
    complex_step_518.number = 17
    complex_step_518.place = complex_place_192
    complex_step_518.route = complex_route_37
    complex_step_518 = importer.save_or_locate(complex_step_518)

    complex_step_519 = Step()
    complex_step_519.datetime = None
    complex_step_519.number = 18
    complex_step_519.place = complex_place_196
    complex_step_519.route = complex_route_37
    complex_step_519 = importer.save_or_locate(complex_step_519)

    complex_step_520 = Step()
    complex_step_520.datetime = None
    complex_step_520.number = 19
    complex_step_520.place = complex_place_193
    complex_step_520.route = complex_route_37
    complex_step_520 = importer.save_or_locate(complex_step_520)

    complex_step_521 = Step()
    complex_step_521.datetime = None
    complex_step_521.number = 20
    complex_step_521.place = complex_place_194
    complex_step_521.route = complex_route_37
    complex_step_521 = importer.save_or_locate(complex_step_521)

    complex_step_522 = Step()
    complex_step_522.datetime = None
    complex_step_522.number = 21
    complex_step_522.place = complex_place_197
    complex_step_522.route = complex_route_37
    complex_step_522 = importer.save_or_locate(complex_step_522)

    complex_step_523 = Step()
    complex_step_523.datetime = None
    complex_step_523.number = 22
    complex_step_523.place = complex_place_203
    complex_step_523.route = complex_route_37
    complex_step_523 = importer.save_or_locate(complex_step_523)

    complex_step_524 = Step()
    complex_step_524.datetime = None
    complex_step_524.number = 23
    complex_step_524.place = complex_place_204
    complex_step_524.route = complex_route_37
    complex_step_524 = importer.save_or_locate(complex_step_524)

    complex_step_525 = Step()
    complex_step_525.datetime = None
    complex_step_525.number = 1
    complex_step_525.place = complex_place_180
    complex_step_525.route = complex_route_38
    complex_step_525 = importer.save_or_locate(complex_step_525)

    # Re-processing model: complex.models.Scene

    complex_scene_1.place = complex_place_383
    complex_scene_1.story = complex_story_8
    complex_scene_1 = importer.save_or_locate(complex_scene_1)

    complex_scene_2.place = complex_place_424
    complex_scene_2.story = complex_story_9
    complex_scene_2 = importer.save_or_locate(complex_scene_2)

    complex_scene_3.place = complex_place_314
    complex_scene_3.story = complex_story_15
    complex_scene_3 = importer.save_or_locate(complex_scene_3)

    complex_scene_4.place = complex_place_317
    complex_scene_4.story = complex_story_15
    complex_scene_4 = importer.save_or_locate(complex_scene_4)

    complex_scene_5.place = complex_place_155
    complex_scene_5.story = complex_story_24
    complex_scene_5 = importer.save_or_locate(complex_scene_5)

    complex_scene_6.place = complex_place_40
    complex_scene_6.story = complex_story_27
    complex_scene_6 = importer.save_or_locate(complex_scene_6)

    complex_scene_7.place = complex_place_379
    complex_scene_7.story = complex_story_31
    complex_scene_7 = importer.save_or_locate(complex_scene_7)

    complex_scene_8.place = complex_place_357
    complex_scene_8.story = complex_story_31
    complex_scene_8 = importer.save_or_locate(complex_scene_8)

    complex_scene_9.place = complex_place_117
    complex_scene_9.story = complex_story_1
    complex_scene_9 = importer.save_or_locate(complex_scene_9)

    complex_scene_10.place = complex_place_112
    complex_scene_10.story = complex_story_1
    complex_scene_10 = importer.save_or_locate(complex_scene_10)

    complex_scene_11.place = complex_place_105
    complex_scene_11.story = complex_story_1
    complex_scene_11 = importer.save_or_locate(complex_scene_11)

    complex_scene_12.place = complex_place_106
    complex_scene_12.story = complex_story_1
    complex_scene_12 = importer.save_or_locate(complex_scene_12)

    complex_scene_13.place = complex_place_107
    complex_scene_13.story = complex_story_1
    complex_scene_13 = importer.save_or_locate(complex_scene_13)

    complex_scene_14.place = complex_place_109
    complex_scene_14.story = complex_story_1
    complex_scene_14 = importer.save_or_locate(complex_scene_14)

    complex_scene_15.place = complex_place_114
    complex_scene_15.story = complex_story_1
    complex_scene_15 = importer.save_or_locate(complex_scene_15)

    complex_scene_16.place = complex_place_115
    complex_scene_16.story = complex_story_1
    complex_scene_16 = importer.save_or_locate(complex_scene_16)

    complex_scene_17.place = complex_place_116
    complex_scene_17.story = complex_story_1
    complex_scene_17 = importer.save_or_locate(complex_scene_17)

    complex_scene_18.place = complex_place_113
    complex_scene_18.story = complex_story_1
    complex_scene_18 = importer.save_or_locate(complex_scene_18)

    complex_scene_19.place = complex_place_111
    complex_scene_19.story = complex_story_1
    complex_scene_19 = importer.save_or_locate(complex_scene_19)

    complex_scene_20.place = complex_place_108
    complex_scene_20.story = complex_story_1
    complex_scene_20 = importer.save_or_locate(complex_scene_20)

    complex_scene_21.place = complex_place_104
    complex_scene_21.story = complex_story_2
    complex_scene_21 = importer.save_or_locate(complex_scene_21)

    complex_scene_22.place = complex_place_99
    complex_scene_22.story = complex_story_2
    complex_scene_22 = importer.save_or_locate(complex_scene_22)

    complex_scene_23.place = complex_place_96
    complex_scene_23.story = complex_story_2
    complex_scene_23 = importer.save_or_locate(complex_scene_23)

    complex_scene_24.place = complex_place_100
    complex_scene_24.story = complex_story_2
    complex_scene_24 = importer.save_or_locate(complex_scene_24)

    complex_scene_25.place = complex_place_102
    complex_scene_25.story = complex_story_2
    complex_scene_25 = importer.save_or_locate(complex_scene_25)

    complex_scene_26.place = complex_place_101
    complex_scene_26.story = complex_story_2
    complex_scene_26 = importer.save_or_locate(complex_scene_26)

    complex_scene_27.place = complex_place_97
    complex_scene_27.story = complex_story_2
    complex_scene_27 = importer.save_or_locate(complex_scene_27)

    complex_scene_28.place = complex_place_93
    complex_scene_28.story = complex_story_2
    complex_scene_28 = importer.save_or_locate(complex_scene_28)

    complex_scene_29.place = complex_place_94
    complex_scene_29.story = complex_story_2
    complex_scene_29 = importer.save_or_locate(complex_scene_29)

    complex_scene_30.place = complex_place_91
    complex_scene_30.story = complex_story_2
    complex_scene_30 = importer.save_or_locate(complex_scene_30)

    complex_scene_31.place = complex_place_95
    complex_scene_31.story = complex_story_2
    complex_scene_31 = importer.save_or_locate(complex_scene_31)

    complex_scene_32.place = complex_place_92
    complex_scene_32.story = complex_story_2
    complex_scene_32 = importer.save_or_locate(complex_scene_32)

    complex_scene_33.place = complex_place_98
    complex_scene_33.story = complex_story_2
    complex_scene_33 = importer.save_or_locate(complex_scene_33)

    complex_scene_34.place = complex_place_235
    complex_scene_34.story = complex_story_3
    complex_scene_34 = importer.save_or_locate(complex_scene_34)

    complex_scene_35.place = complex_place_121
    complex_scene_35.story = complex_story_3
    complex_scene_35 = importer.save_or_locate(complex_scene_35)

    complex_scene_36.place = complex_place_122
    complex_scene_36.story = complex_story_3
    complex_scene_36 = importer.save_or_locate(complex_scene_36)

    complex_scene_37.place = complex_place_119
    complex_scene_37.story = complex_story_3
    complex_scene_37 = importer.save_or_locate(complex_scene_37)

    complex_scene_38.place = complex_place_120
    complex_scene_38.story = complex_story_3
    complex_scene_38 = importer.save_or_locate(complex_scene_38)

    complex_scene_39.place = complex_place_123
    complex_scene_39.story = complex_story_3
    complex_scene_39 = importer.save_or_locate(complex_scene_39)

    complex_scene_40.place = complex_place_126
    complex_scene_40.story = complex_story_3
    complex_scene_40 = importer.save_or_locate(complex_scene_40)

    complex_scene_41.place = complex_place_125
    complex_scene_41.story = complex_story_3
    complex_scene_41 = importer.save_or_locate(complex_scene_41)

    complex_scene_42.place = complex_place_129
    complex_scene_42.story = complex_story_3
    complex_scene_42 = importer.save_or_locate(complex_scene_42)

    complex_scene_43.place = complex_place_127
    complex_scene_43.story = complex_story_3
    complex_scene_43 = importer.save_or_locate(complex_scene_43)

    complex_scene_44.place = complex_place_128
    complex_scene_44.story = complex_story_3
    complex_scene_44 = importer.save_or_locate(complex_scene_44)

    complex_scene_45.place = complex_place_118
    complex_scene_45.story = complex_story_3
    complex_scene_45 = importer.save_or_locate(complex_scene_45)

    complex_scene_46.place = complex_place_235
    complex_scene_46.story = complex_story_4
    complex_scene_46 = importer.save_or_locate(complex_scene_46)

    complex_scene_47.place = complex_place_385
    complex_scene_47.story = complex_story_4
    complex_scene_47 = importer.save_or_locate(complex_scene_47)

    complex_scene_48.place = complex_place_413
    complex_scene_48.story = complex_story_4
    complex_scene_48 = importer.save_or_locate(complex_scene_48)

    complex_scene_49.place = complex_place_412
    complex_scene_49.story = complex_story_4
    complex_scene_49 = importer.save_or_locate(complex_scene_49)

    complex_scene_50.place = complex_place_417
    complex_scene_50.story = complex_story_4
    complex_scene_50 = importer.save_or_locate(complex_scene_50)

    complex_scene_51.place = complex_place_416
    complex_scene_51.story = complex_story_4
    complex_scene_51 = importer.save_or_locate(complex_scene_51)

    complex_scene_52.place = complex_place_410
    complex_scene_52.story = complex_story_4
    complex_scene_52 = importer.save_or_locate(complex_scene_52)

    complex_scene_53.place = complex_place_409
    complex_scene_53.story = complex_story_4
    complex_scene_53 = importer.save_or_locate(complex_scene_53)

    complex_scene_54.place = complex_place_408
    complex_scene_54.story = complex_story_4
    complex_scene_54 = importer.save_or_locate(complex_scene_54)

    complex_scene_55.place = complex_place_415
    complex_scene_55.story = complex_story_4
    complex_scene_55 = importer.save_or_locate(complex_scene_55)

    complex_scene_56.place = complex_place_414
    complex_scene_56.story = complex_story_4
    complex_scene_56 = importer.save_or_locate(complex_scene_56)

    complex_scene_57.place = complex_place_418
    complex_scene_57.story = complex_story_4
    complex_scene_57 = importer.save_or_locate(complex_scene_57)

    complex_scene_58.place = complex_place_368
    complex_scene_58.story = complex_story_5
    complex_scene_58 = importer.save_or_locate(complex_scene_58)

    complex_scene_59.place = complex_place_362
    complex_scene_59.story = complex_story_5
    complex_scene_59 = importer.save_or_locate(complex_scene_59)

    complex_scene_60.place = complex_place_373
    complex_scene_60.story = complex_story_5
    complex_scene_60 = importer.save_or_locate(complex_scene_60)

    complex_scene_61.place = complex_place_375
    complex_scene_61.story = complex_story_5
    complex_scene_61 = importer.save_or_locate(complex_scene_61)

    complex_scene_62.place = complex_place_367
    complex_scene_62.story = complex_story_5
    complex_scene_62 = importer.save_or_locate(complex_scene_62)

    complex_scene_63.place = complex_place_366
    complex_scene_63.story = complex_story_5
    complex_scene_63 = importer.save_or_locate(complex_scene_63)

    complex_scene_64.place = complex_place_329
    complex_scene_64.story = complex_story_5
    complex_scene_64 = importer.save_or_locate(complex_scene_64)

    complex_scene_65.place = complex_place_327
    complex_scene_65.story = complex_story_5
    complex_scene_65 = importer.save_or_locate(complex_scene_65)

    complex_scene_66.place = complex_place_326
    complex_scene_66.story = complex_story_5
    complex_scene_66 = importer.save_or_locate(complex_scene_66)

    complex_scene_67.place = complex_place_319
    complex_scene_67.story = complex_story_5
    complex_scene_67 = importer.save_or_locate(complex_scene_67)

    complex_scene_68.place = complex_place_320
    complex_scene_68.story = complex_story_5
    complex_scene_68 = importer.save_or_locate(complex_scene_68)

    complex_scene_69.place = complex_place_306
    complex_scene_69.story = complex_story_5
    complex_scene_69 = importer.save_or_locate(complex_scene_69)

    complex_scene_70.place = complex_place_313
    complex_scene_70.story = complex_story_5
    complex_scene_70 = importer.save_or_locate(complex_scene_70)

    complex_scene_71.place = complex_place_304
    complex_scene_71.story = complex_story_5
    complex_scene_71 = importer.save_or_locate(complex_scene_71)

    complex_scene_72.place = complex_place_312
    complex_scene_72.story = complex_story_5
    complex_scene_72 = importer.save_or_locate(complex_scene_72)

    complex_scene_73.place = complex_place_156
    complex_scene_73.story = complex_story_6
    complex_scene_73 = importer.save_or_locate(complex_scene_73)

    complex_scene_74.place = complex_place_141
    complex_scene_74.story = complex_story_6
    complex_scene_74 = importer.save_or_locate(complex_scene_74)

    complex_scene_75.place = complex_place_142
    complex_scene_75.story = complex_story_6
    complex_scene_75 = importer.save_or_locate(complex_scene_75)

    complex_scene_76.place = complex_place_143
    complex_scene_76.story = complex_story_6
    complex_scene_76 = importer.save_or_locate(complex_scene_76)

    complex_scene_77.place = complex_place_135
    complex_scene_77.story = complex_story_6
    complex_scene_77 = importer.save_or_locate(complex_scene_77)

    complex_scene_78.place = complex_place_134
    complex_scene_78.story = complex_story_6
    complex_scene_78 = importer.save_or_locate(complex_scene_78)

    complex_scene_79.place = complex_place_136
    complex_scene_79.story = complex_story_6
    complex_scene_79 = importer.save_or_locate(complex_scene_79)

    complex_scene_80.place = complex_place_139
    complex_scene_80.story = complex_story_6
    complex_scene_80 = importer.save_or_locate(complex_scene_80)

    complex_scene_81.place = complex_place_138
    complex_scene_81.story = complex_story_6
    complex_scene_81 = importer.save_or_locate(complex_scene_81)

    complex_scene_82.place = complex_place_137
    complex_scene_82.story = complex_story_6
    complex_scene_82 = importer.save_or_locate(complex_scene_82)

    complex_scene_83.place = complex_place_140
    complex_scene_83.story = complex_story_6
    complex_scene_83 = importer.save_or_locate(complex_scene_83)

    complex_scene_84.place = complex_place_86
    complex_scene_84.story = complex_story_7
    complex_scene_84 = importer.save_or_locate(complex_scene_84)

    complex_scene_85.place = complex_place_88
    complex_scene_85.story = complex_story_7
    complex_scene_85 = importer.save_or_locate(complex_scene_85)

    complex_scene_86.place = complex_place_89
    complex_scene_86.story = complex_story_7
    complex_scene_86 = importer.save_or_locate(complex_scene_86)

    complex_scene_87.place = complex_place_87
    complex_scene_87.story = complex_story_7
    complex_scene_87 = importer.save_or_locate(complex_scene_87)

    complex_scene_88.place = complex_place_85
    complex_scene_88.story = complex_story_7
    complex_scene_88 = importer.save_or_locate(complex_scene_88)

    complex_scene_89.place = complex_place_84
    complex_scene_89.story = complex_story_7
    complex_scene_89 = importer.save_or_locate(complex_scene_89)

    complex_scene_90.place = complex_place_384
    complex_scene_90.story = complex_story_8
    complex_scene_90 = importer.save_or_locate(complex_scene_90)

    complex_scene_91.place = complex_place_390
    complex_scene_91.story = complex_story_8
    complex_scene_91 = importer.save_or_locate(complex_scene_91)

    complex_scene_92.place = complex_place_391
    complex_scene_92.story = complex_story_8
    complex_scene_92 = importer.save_or_locate(complex_scene_92)

    complex_scene_93.place = complex_place_392
    complex_scene_93.story = complex_story_8
    complex_scene_93 = importer.save_or_locate(complex_scene_93)

    complex_scene_94.place = complex_place_393
    complex_scene_94.story = complex_story_8
    complex_scene_94 = importer.save_or_locate(complex_scene_94)

    complex_scene_95.place = complex_place_399
    complex_scene_95.story = complex_story_8
    complex_scene_95 = importer.save_or_locate(complex_scene_95)

    complex_scene_96.place = complex_place_398
    complex_scene_96.story = complex_story_8
    complex_scene_96 = importer.save_or_locate(complex_scene_96)

    complex_scene_97.place = complex_place_394
    complex_scene_97.story = complex_story_8
    complex_scene_97 = importer.save_or_locate(complex_scene_97)

    complex_scene_98.place = complex_place_396
    complex_scene_98.story = complex_story_8
    complex_scene_98 = importer.save_or_locate(complex_scene_98)

    complex_scene_99.place = complex_place_397
    complex_scene_99.story = complex_story_8
    complex_scene_99 = importer.save_or_locate(complex_scene_99)

    complex_scene_100.place = complex_place_389
    complex_scene_100.story = complex_story_8
    complex_scene_100 = importer.save_or_locate(complex_scene_100)

    complex_scene_101.place = complex_place_387
    complex_scene_101.story = complex_story_8
    complex_scene_101 = importer.save_or_locate(complex_scene_101)

    complex_scene_102.place = complex_place_388
    complex_scene_102.story = complex_story_8
    complex_scene_102 = importer.save_or_locate(complex_scene_102)

    complex_scene_103.place = complex_place_395
    complex_scene_103.story = complex_story_8
    complex_scene_103 = importer.save_or_locate(complex_scene_103)

    complex_scene_104.place = complex_place_220
    complex_scene_104.story = complex_story_9
    complex_scene_104 = importer.save_or_locate(complex_scene_104)

    complex_scene_105.place = complex_place_335
    complex_scene_105.story = complex_story_9
    complex_scene_105 = importer.save_or_locate(complex_scene_105)

    complex_scene_106.place = complex_place_406
    complex_scene_106.story = complex_story_9
    complex_scene_106 = importer.save_or_locate(complex_scene_106)

    complex_scene_107.place = complex_place_407
    complex_scene_107.story = complex_story_9
    complex_scene_107 = importer.save_or_locate(complex_scene_107)

    complex_scene_108.place = complex_place_420
    complex_scene_108.story = complex_story_9
    complex_scene_108 = importer.save_or_locate(complex_scene_108)

    complex_scene_109.place = complex_place_421
    complex_scene_109.story = complex_story_9
    complex_scene_109 = importer.save_or_locate(complex_scene_109)

    complex_scene_110.place = complex_place_422
    complex_scene_110.story = complex_story_9
    complex_scene_110 = importer.save_or_locate(complex_scene_110)

    complex_scene_111.place = complex_place_425
    complex_scene_111.story = complex_story_10
    complex_scene_111 = importer.save_or_locate(complex_scene_111)

    complex_scene_112.place = complex_place_426
    complex_scene_112.story = complex_story_10
    complex_scene_112 = importer.save_or_locate(complex_scene_112)

    complex_scene_113.place = complex_place_423
    complex_scene_113.story = complex_story_10
    complex_scene_113 = importer.save_or_locate(complex_scene_113)

    complex_scene_114.place = complex_place_427
    complex_scene_114.story = complex_story_10
    complex_scene_114 = importer.save_or_locate(complex_scene_114)

    complex_scene_115.place = complex_place_428
    complex_scene_115.story = complex_story_10
    complex_scene_115 = importer.save_or_locate(complex_scene_115)

    complex_scene_116.place = complex_place_431
    complex_scene_116.story = complex_story_10
    complex_scene_116 = importer.save_or_locate(complex_scene_116)

    complex_scene_117.place = complex_place_430
    complex_scene_117.story = complex_story_10
    complex_scene_117 = importer.save_or_locate(complex_scene_117)

    complex_scene_118.place = complex_place_429
    complex_scene_118.story = complex_story_10
    complex_scene_118 = importer.save_or_locate(complex_scene_118)

    complex_scene_119.place = complex_place_405
    complex_scene_119.story = complex_story_10
    complex_scene_119 = importer.save_or_locate(complex_scene_119)

    complex_scene_120.place = complex_place_403
    complex_scene_120.story = complex_story_10
    complex_scene_120 = importer.save_or_locate(complex_scene_120)

    complex_scene_121.place = complex_place_401
    complex_scene_121.story = complex_story_10
    complex_scene_121 = importer.save_or_locate(complex_scene_121)

    complex_scene_122.place = complex_place_404
    complex_scene_122.story = complex_story_10
    complex_scene_122 = importer.save_or_locate(complex_scene_122)

    complex_scene_123.place = complex_place_402
    complex_scene_123.story = complex_story_10
    complex_scene_123 = importer.save_or_locate(complex_scene_123)

    complex_scene_124.place = complex_place_65
    complex_scene_124.story = complex_story_11
    complex_scene_124 = importer.save_or_locate(complex_scene_124)

    complex_scene_125.place = complex_place_64
    complex_scene_125.story = complex_story_11
    complex_scene_125 = importer.save_or_locate(complex_scene_125)

    complex_scene_126.place = complex_place_66
    complex_scene_126.story = complex_story_11
    complex_scene_126 = importer.save_or_locate(complex_scene_126)

    complex_scene_127.place = complex_place_67
    complex_scene_127.story = complex_story_11
    complex_scene_127 = importer.save_or_locate(complex_scene_127)

    complex_scene_128.place = complex_place_62
    complex_scene_128.story = complex_story_11
    complex_scene_128 = importer.save_or_locate(complex_scene_128)

    complex_scene_129.place = complex_place_60
    complex_scene_129.story = complex_story_11
    complex_scene_129 = importer.save_or_locate(complex_scene_129)

    complex_scene_130.place = complex_place_58
    complex_scene_130.story = complex_story_11
    complex_scene_130 = importer.save_or_locate(complex_scene_130)

    complex_scene_131.place = complex_place_59
    complex_scene_131.story = complex_story_11
    complex_scene_131 = importer.save_or_locate(complex_scene_131)

    complex_scene_132.place = complex_place_57
    complex_scene_132.story = complex_story_11
    complex_scene_132 = importer.save_or_locate(complex_scene_132)

    complex_scene_133.place = complex_place_61
    complex_scene_133.story = complex_story_11
    complex_scene_133 = importer.save_or_locate(complex_scene_133)

    complex_scene_134.place = complex_place_517
    complex_scene_134.story = complex_story_12
    complex_scene_134 = importer.save_or_locate(complex_scene_134)

    complex_scene_135.place = complex_place_521
    complex_scene_135.story = complex_story_12
    complex_scene_135 = importer.save_or_locate(complex_scene_135)

    complex_scene_136.place = complex_place_522
    complex_scene_136.story = complex_story_12
    complex_scene_136 = importer.save_or_locate(complex_scene_136)

    complex_scene_137.place = complex_place_524
    complex_scene_137.story = complex_story_12
    complex_scene_137 = importer.save_or_locate(complex_scene_137)

    complex_scene_138.place = complex_place_525
    complex_scene_138.story = complex_story_12
    complex_scene_138 = importer.save_or_locate(complex_scene_138)

    complex_scene_139.place = complex_place_518
    complex_scene_139.story = complex_story_12
    complex_scene_139 = importer.save_or_locate(complex_scene_139)

    complex_scene_140.place = complex_place_520
    complex_scene_140.story = complex_story_12
    complex_scene_140 = importer.save_or_locate(complex_scene_140)

    complex_scene_141.place = complex_place_523
    complex_scene_141.story = complex_story_12
    complex_scene_141 = importer.save_or_locate(complex_scene_141)

    complex_scene_142.place = complex_place_481
    complex_scene_142.story = complex_story_12
    complex_scene_142 = importer.save_or_locate(complex_scene_142)

    complex_scene_143.place = complex_place_480
    complex_scene_143.story = complex_story_12
    complex_scene_143 = importer.save_or_locate(complex_scene_143)

    complex_scene_144.place = complex_place_478
    complex_scene_144.story = complex_story_12
    complex_scene_144 = importer.save_or_locate(complex_scene_144)

    complex_scene_145.place = complex_place_477
    complex_scene_145.story = complex_story_12
    complex_scene_145 = importer.save_or_locate(complex_scene_145)

    complex_scene_146.place = complex_place_519
    complex_scene_146.story = complex_story_12
    complex_scene_146 = importer.save_or_locate(complex_scene_146)

    complex_scene_147.place = complex_place_71
    complex_scene_147.story = complex_story_13
    complex_scene_147 = importer.save_or_locate(complex_scene_147)

    complex_scene_148.place = complex_place_72
    complex_scene_148.story = complex_story_13
    complex_scene_148 = importer.save_or_locate(complex_scene_148)

    complex_scene_149.place = complex_place_75
    complex_scene_149.story = complex_story_13
    complex_scene_149 = importer.save_or_locate(complex_scene_149)

    complex_scene_150.place = complex_place_74
    complex_scene_150.story = complex_story_13
    complex_scene_150 = importer.save_or_locate(complex_scene_150)

    complex_scene_151.place = complex_place_73
    complex_scene_151.story = complex_story_13
    complex_scene_151 = importer.save_or_locate(complex_scene_151)

    complex_scene_152.place = complex_place_70
    complex_scene_152.story = complex_story_13
    complex_scene_152 = importer.save_or_locate(complex_scene_152)

    complex_scene_153.place = complex_place_77
    complex_scene_153.story = complex_story_13
    complex_scene_153 = importer.save_or_locate(complex_scene_153)

    complex_scene_154.place = complex_place_78
    complex_scene_154.story = complex_story_13
    complex_scene_154 = importer.save_or_locate(complex_scene_154)

    complex_scene_155.place = complex_place_68
    complex_scene_155.story = complex_story_13
    complex_scene_155 = importer.save_or_locate(complex_scene_155)

    complex_scene_156.place = complex_place_69
    complex_scene_156.story = complex_story_13
    complex_scene_156 = importer.save_or_locate(complex_scene_156)

    complex_scene_157.place = complex_place_79
    complex_scene_157.story = complex_story_13
    complex_scene_157 = importer.save_or_locate(complex_scene_157)

    complex_scene_158.place = complex_place_80
    complex_scene_158.story = complex_story_13
    complex_scene_158 = importer.save_or_locate(complex_scene_158)

    complex_scene_159.place = complex_place_81
    complex_scene_159.story = complex_story_13
    complex_scene_159 = importer.save_or_locate(complex_scene_159)

    complex_scene_160.place = complex_place_83
    complex_scene_160.story = complex_story_13
    complex_scene_160 = importer.save_or_locate(complex_scene_160)

    complex_scene_161.place = complex_place_76
    complex_scene_161.story = complex_story_13
    complex_scene_161 = importer.save_or_locate(complex_scene_161)

    complex_scene_162.place = complex_place_348
    complex_scene_162.story = complex_story_14
    complex_scene_162 = importer.save_or_locate(complex_scene_162)

    complex_scene_163.place = complex_place_349
    complex_scene_163.story = complex_story_14
    complex_scene_163 = importer.save_or_locate(complex_scene_163)

    complex_scene_164.place = complex_place_347
    complex_scene_164.story = complex_story_14
    complex_scene_164 = importer.save_or_locate(complex_scene_164)

    complex_scene_165.place = complex_place_346
    complex_scene_165.story = complex_story_14
    complex_scene_165 = importer.save_or_locate(complex_scene_165)

    complex_scene_166.place = complex_place_345
    complex_scene_166.story = complex_story_14
    complex_scene_166 = importer.save_or_locate(complex_scene_166)

    complex_scene_167.place = complex_place_343
    complex_scene_167.story = complex_story_14
    complex_scene_167 = importer.save_or_locate(complex_scene_167)

    complex_scene_168.place = complex_place_342
    complex_scene_168.story = complex_story_14
    complex_scene_168 = importer.save_or_locate(complex_scene_168)

    complex_scene_169.place = complex_place_341
    complex_scene_169.story = complex_story_14
    complex_scene_169 = importer.save_or_locate(complex_scene_169)

    complex_scene_170.place = complex_place_340
    complex_scene_170.story = complex_story_14
    complex_scene_170 = importer.save_or_locate(complex_scene_170)

    complex_scene_171.place = complex_place_338
    complex_scene_171.story = complex_story_14
    complex_scene_171 = importer.save_or_locate(complex_scene_171)

    complex_scene_172.place = complex_place_337
    complex_scene_172.story = complex_story_14
    complex_scene_172 = importer.save_or_locate(complex_scene_172)

    complex_scene_173.place = complex_place_336
    complex_scene_173.story = complex_story_14
    complex_scene_173 = importer.save_or_locate(complex_scene_173)

    complex_scene_174.place = complex_place_339
    complex_scene_174.story = complex_story_14
    complex_scene_174 = importer.save_or_locate(complex_scene_174)

    complex_scene_175.place = complex_place_344
    complex_scene_175.story = complex_story_14
    complex_scene_175 = importer.save_or_locate(complex_scene_175)

    complex_scene_176.place = complex_place_333
    complex_scene_176.story = complex_story_14
    complex_scene_176 = importer.save_or_locate(complex_scene_176)

    complex_scene_177.place = complex_place_334
    complex_scene_177.story = complex_story_14
    complex_scene_177 = importer.save_or_locate(complex_scene_177)

    complex_scene_178.place = complex_place_331
    complex_scene_178.story = complex_story_14
    complex_scene_178 = importer.save_or_locate(complex_scene_178)

    complex_scene_179.place = complex_place_332
    complex_scene_179.story = complex_story_15
    complex_scene_179 = importer.save_or_locate(complex_scene_179)

    complex_scene_180.place = complex_place_328
    complex_scene_180.story = complex_story_15
    complex_scene_180 = importer.save_or_locate(complex_scene_180)

    complex_scene_181.place = complex_place_316
    complex_scene_181.story = complex_story_15
    complex_scene_181 = importer.save_or_locate(complex_scene_181)

    complex_scene_182.place = complex_place_315
    complex_scene_182.story = complex_story_15
    complex_scene_182 = importer.save_or_locate(complex_scene_182)

    complex_scene_183.place = complex_place_307
    complex_scene_183.story = complex_story_15
    complex_scene_183 = importer.save_or_locate(complex_scene_183)

    complex_scene_184.place = complex_place_308
    complex_scene_184.story = complex_story_15
    complex_scene_184 = importer.save_or_locate(complex_scene_184)

    complex_scene_185.place = complex_place_309
    complex_scene_185.story = complex_story_15
    complex_scene_185 = importer.save_or_locate(complex_scene_185)

    complex_scene_186.place = complex_place_311
    complex_scene_186.story = complex_story_15
    complex_scene_186 = importer.save_or_locate(complex_scene_186)

    complex_scene_187.place = complex_place_235
    complex_scene_187.story = complex_story_16
    complex_scene_187 = importer.save_or_locate(complex_scene_187)

    complex_scene_188.place = complex_place_222
    complex_scene_188.story = complex_story_16
    complex_scene_188 = importer.save_or_locate(complex_scene_188)

    complex_scene_189.place = complex_place_215
    complex_scene_189.story = complex_story_16
    complex_scene_189 = importer.save_or_locate(complex_scene_189)

    complex_scene_190.place = complex_place_205
    complex_scene_190.story = complex_story_16
    complex_scene_190 = importer.save_or_locate(complex_scene_190)

    complex_scene_191.place = complex_place_206
    complex_scene_191.story = complex_story_16
    complex_scene_191 = importer.save_or_locate(complex_scene_191)

    complex_scene_192.place = complex_place_208
    complex_scene_192.story = complex_story_16
    complex_scene_192 = importer.save_or_locate(complex_scene_192)

    complex_scene_193.place = complex_place_213
    complex_scene_193.story = complex_story_16
    complex_scene_193 = importer.save_or_locate(complex_scene_193)

    complex_scene_194.place = complex_place_211
    complex_scene_194.story = complex_story_16
    complex_scene_194 = importer.save_or_locate(complex_scene_194)

    complex_scene_195.place = complex_place_210
    complex_scene_195.story = complex_story_16
    complex_scene_195 = importer.save_or_locate(complex_scene_195)

    complex_scene_196.place = complex_place_212
    complex_scene_196.story = complex_story_16
    complex_scene_196 = importer.save_or_locate(complex_scene_196)

    complex_scene_197.place = complex_place_207
    complex_scene_197.story = complex_story_16
    complex_scene_197 = importer.save_or_locate(complex_scene_197)

    complex_scene_198.place = complex_place_217
    complex_scene_198.story = complex_story_16
    complex_scene_198 = importer.save_or_locate(complex_scene_198)

    complex_scene_199.place = complex_place_216
    complex_scene_199.story = complex_story_16
    complex_scene_199 = importer.save_or_locate(complex_scene_199)

    complex_scene_200.place = complex_place_209
    complex_scene_200.story = complex_story_16
    complex_scene_200 = importer.save_or_locate(complex_scene_200)

    complex_scene_201.place = complex_place_235
    complex_scene_201.story = complex_story_17
    complex_scene_201 = importer.save_or_locate(complex_scene_201)

    complex_scene_202.place = complex_place_279
    complex_scene_202.story = complex_story_17
    complex_scene_202 = importer.save_or_locate(complex_scene_202)

    complex_scene_203.place = complex_place_275
    complex_scene_203.story = complex_story_17
    complex_scene_203 = importer.save_or_locate(complex_scene_203)

    complex_scene_204.place = complex_place_248
    complex_scene_204.story = complex_story_17
    complex_scene_204 = importer.save_or_locate(complex_scene_204)

    complex_scene_205.place = complex_place_250
    complex_scene_205.story = complex_story_17
    complex_scene_205 = importer.save_or_locate(complex_scene_205)

    complex_scene_206.place = complex_place_269
    complex_scene_206.story = complex_story_17
    complex_scene_206 = importer.save_or_locate(complex_scene_206)

    complex_scene_207.place = complex_place_254
    complex_scene_207.story = complex_story_17
    complex_scene_207 = importer.save_or_locate(complex_scene_207)

    complex_scene_208.place = complex_place_276
    complex_scene_208.story = complex_story_17
    complex_scene_208 = importer.save_or_locate(complex_scene_208)

    complex_scene_209.place = complex_place_270
    complex_scene_209.story = complex_story_17
    complex_scene_209 = importer.save_or_locate(complex_scene_209)

    complex_scene_210.place = complex_place_272
    complex_scene_210.story = complex_story_17
    complex_scene_210 = importer.save_or_locate(complex_scene_210)

    complex_scene_211.place = complex_place_277
    complex_scene_211.story = complex_story_17
    complex_scene_211 = importer.save_or_locate(complex_scene_211)

    complex_scene_212.place = complex_place_280
    complex_scene_212.story = complex_story_17
    complex_scene_212 = importer.save_or_locate(complex_scene_212)

    complex_scene_213.place = complex_place_284
    complex_scene_213.story = complex_story_17
    complex_scene_213 = importer.save_or_locate(complex_scene_213)

    complex_scene_214.place = complex_place_283
    complex_scene_214.story = complex_story_17
    complex_scene_214 = importer.save_or_locate(complex_scene_214)

    complex_scene_215.place = complex_place_285
    complex_scene_215.story = complex_story_17
    complex_scene_215 = importer.save_or_locate(complex_scene_215)

    complex_scene_216.place = complex_place_287
    complex_scene_216.story = complex_story_17
    complex_scene_216 = importer.save_or_locate(complex_scene_216)

    complex_scene_217.place = complex_place_294
    complex_scene_217.story = complex_story_17
    complex_scene_217 = importer.save_or_locate(complex_scene_217)

    complex_scene_218.place = complex_place_292
    complex_scene_218.story = complex_story_17
    complex_scene_218 = importer.save_or_locate(complex_scene_218)

    complex_scene_219.place = complex_place_282
    complex_scene_219.story = complex_story_17
    complex_scene_219 = importer.save_or_locate(complex_scene_219)

    complex_scene_220.place = complex_place_288
    complex_scene_220.story = complex_story_17
    complex_scene_220 = importer.save_or_locate(complex_scene_220)

    complex_scene_221.place = complex_place_299
    complex_scene_221.story = complex_story_17
    complex_scene_221 = importer.save_or_locate(complex_scene_221)

    complex_scene_222.place = complex_place_290
    complex_scene_222.story = complex_story_17
    complex_scene_222 = importer.save_or_locate(complex_scene_222)

    complex_scene_223.place = complex_place_301
    complex_scene_223.story = complex_story_17
    complex_scene_223 = importer.save_or_locate(complex_scene_223)

    complex_scene_224.place = complex_place_235
    complex_scene_224.story = complex_story_18
    complex_scene_224 = importer.save_or_locate(complex_scene_224)

    complex_scene_225.place = complex_place_173
    complex_scene_225.story = complex_story_18
    complex_scene_225 = importer.save_or_locate(complex_scene_225)

    complex_scene_226.place = complex_place_175
    complex_scene_226.story = complex_story_18
    complex_scene_226 = importer.save_or_locate(complex_scene_226)

    complex_scene_227.place = complex_place_176
    complex_scene_227.story = complex_story_18
    complex_scene_227 = importer.save_or_locate(complex_scene_227)

    complex_scene_228.place = complex_place_174
    complex_scene_228.story = complex_story_18
    complex_scene_228 = importer.save_or_locate(complex_scene_228)

    complex_scene_229.place = complex_place_167
    complex_scene_229.story = complex_story_18
    complex_scene_229 = importer.save_or_locate(complex_scene_229)

    complex_scene_230.place = complex_place_168
    complex_scene_230.story = complex_story_18
    complex_scene_230 = importer.save_or_locate(complex_scene_230)

    complex_scene_231.place = complex_place_166
    complex_scene_231.story = complex_story_18
    complex_scene_231 = importer.save_or_locate(complex_scene_231)

    complex_scene_232.place = complex_place_164
    complex_scene_232.story = complex_story_18
    complex_scene_232 = importer.save_or_locate(complex_scene_232)

    complex_scene_233.place = complex_place_163
    complex_scene_233.story = complex_story_18
    complex_scene_233 = importer.save_or_locate(complex_scene_233)

    complex_scene_234.place = complex_place_161
    complex_scene_234.story = complex_story_18
    complex_scene_234 = importer.save_or_locate(complex_scene_234)

    complex_scene_235.place = complex_place_160
    complex_scene_235.story = complex_story_18
    complex_scene_235 = importer.save_or_locate(complex_scene_235)

    complex_scene_236.place = complex_place_158
    complex_scene_236.story = complex_story_18
    complex_scene_236 = importer.save_or_locate(complex_scene_236)

    complex_scene_237.place = complex_place_157
    complex_scene_237.story = complex_story_18
    complex_scene_237 = importer.save_or_locate(complex_scene_237)

    complex_scene_238.place = complex_place_159
    complex_scene_238.story = complex_story_18
    complex_scene_238 = importer.save_or_locate(complex_scene_238)

    complex_scene_239.place = complex_place_133
    complex_scene_239.story = complex_story_18
    complex_scene_239 = importer.save_or_locate(complex_scene_239)

    complex_scene_240.place = complex_place_144
    complex_scene_240.story = complex_story_18
    complex_scene_240 = importer.save_or_locate(complex_scene_240)

    complex_scene_241.place = complex_place_165
    complex_scene_241.story = complex_story_18
    complex_scene_241 = importer.save_or_locate(complex_scene_241)

    complex_scene_242.place = complex_place_146
    complex_scene_242.story = complex_story_19
    complex_scene_242 = importer.save_or_locate(complex_scene_242)

    complex_scene_243.place = complex_place_145
    complex_scene_243.story = complex_story_19
    complex_scene_243 = importer.save_or_locate(complex_scene_243)

    complex_scene_244.place = complex_place_148
    complex_scene_244.story = complex_story_19
    complex_scene_244 = importer.save_or_locate(complex_scene_244)

    complex_scene_245.place = complex_place_147
    complex_scene_245.story = complex_story_19
    complex_scene_245 = importer.save_or_locate(complex_scene_245)

    complex_scene_246.place = complex_place_149
    complex_scene_246.story = complex_story_19
    complex_scene_246 = importer.save_or_locate(complex_scene_246)

    complex_scene_247.place = complex_place_150
    complex_scene_247.story = complex_story_19
    complex_scene_247 = importer.save_or_locate(complex_scene_247)

    complex_scene_248.place = complex_place_153
    complex_scene_248.story = complex_story_19
    complex_scene_248 = importer.save_or_locate(complex_scene_248)

    complex_scene_249.place = complex_place_235
    complex_scene_249.story = complex_story_20
    complex_scene_249 = importer.save_or_locate(complex_scene_249)

    complex_scene_250.place = complex_place_476
    complex_scene_250.story = complex_story_20
    complex_scene_250 = importer.save_or_locate(complex_scene_250)

    complex_scene_251.place = complex_place_475
    complex_scene_251.story = complex_story_20
    complex_scene_251 = importer.save_or_locate(complex_scene_251)

    complex_scene_252.place = complex_place_512
    complex_scene_252.story = complex_story_20
    complex_scene_252 = importer.save_or_locate(complex_scene_252)

    complex_scene_253.place = complex_place_504
    complex_scene_253.story = complex_story_20
    complex_scene_253 = importer.save_or_locate(complex_scene_253)

    complex_scene_254.place = complex_place_532
    complex_scene_254.story = complex_story_20
    complex_scene_254 = importer.save_or_locate(complex_scene_254)

    complex_scene_255.place = complex_place_535
    complex_scene_255.story = complex_story_20
    complex_scene_255 = importer.save_or_locate(complex_scene_255)

    complex_scene_256.place = complex_place_536
    complex_scene_256.story = complex_story_20
    complex_scene_256 = importer.save_or_locate(complex_scene_256)

    complex_scene_257.place = complex_place_533
    complex_scene_257.story = complex_story_20
    complex_scene_257 = importer.save_or_locate(complex_scene_257)

    complex_scene_258.place = complex_place_534
    complex_scene_258.story = complex_story_20
    complex_scene_258 = importer.save_or_locate(complex_scene_258)

    complex_scene_259.place = complex_place_530
    complex_scene_259.story = complex_story_21
    complex_scene_259 = importer.save_or_locate(complex_scene_259)

    complex_scene_260.place = complex_place_491
    complex_scene_260.story = complex_story_21
    complex_scene_260 = importer.save_or_locate(complex_scene_260)

    complex_scene_261.place = complex_place_490
    complex_scene_261.story = complex_story_21
    complex_scene_261 = importer.save_or_locate(complex_scene_261)

    complex_scene_262.place = complex_place_501
    complex_scene_262.story = complex_story_21
    complex_scene_262 = importer.save_or_locate(complex_scene_262)

    complex_scene_263.place = complex_place_500
    complex_scene_263.story = complex_story_21
    complex_scene_263 = importer.save_or_locate(complex_scene_263)

    complex_scene_264.place = complex_place_235
    complex_scene_264.story = complex_story_22
    complex_scene_264 = importer.save_or_locate(complex_scene_264)

    complex_scene_265.place = complex_place_233
    complex_scene_265.story = complex_story_22
    complex_scene_265 = importer.save_or_locate(complex_scene_265)

    complex_scene_266.place = complex_place_237
    complex_scene_266.story = complex_story_22
    complex_scene_266 = importer.save_or_locate(complex_scene_266)

    complex_scene_267.place = complex_place_234
    complex_scene_267.story = complex_story_22
    complex_scene_267 = importer.save_or_locate(complex_scene_267)

    complex_scene_268.place = complex_place_232
    complex_scene_268.story = complex_story_22
    complex_scene_268 = importer.save_or_locate(complex_scene_268)

    complex_scene_269.place = complex_place_239
    complex_scene_269.story = complex_story_22
    complex_scene_269 = importer.save_or_locate(complex_scene_269)

    complex_scene_270.place = complex_place_243
    complex_scene_270.story = complex_story_22
    complex_scene_270 = importer.save_or_locate(complex_scene_270)

    complex_scene_271.place = complex_place_247
    complex_scene_271.story = complex_story_22
    complex_scene_271 = importer.save_or_locate(complex_scene_271)

    complex_scene_272.place = complex_place_249
    complex_scene_272.story = complex_story_22
    complex_scene_272 = importer.save_or_locate(complex_scene_272)

    complex_scene_273.place = complex_place_244
    complex_scene_273.story = complex_story_22
    complex_scene_273 = importer.save_or_locate(complex_scene_273)

    complex_scene_274.place = complex_place_245
    complex_scene_274.story = complex_story_22
    complex_scene_274 = importer.save_or_locate(complex_scene_274)

    complex_scene_275.place = complex_place_242
    complex_scene_275.story = complex_story_22
    complex_scene_275 = importer.save_or_locate(complex_scene_275)

    complex_scene_276.place = complex_place_236
    complex_scene_276.story = complex_story_22
    complex_scene_276 = importer.save_or_locate(complex_scene_276)

    complex_scene_277.place = complex_place_241
    complex_scene_277.story = complex_story_22
    complex_scene_277 = importer.save_or_locate(complex_scene_277)

    complex_scene_278.place = complex_place_251
    complex_scene_278.story = complex_story_22
    complex_scene_278 = importer.save_or_locate(complex_scene_278)

    complex_scene_279.place = complex_place_240
    complex_scene_279.story = complex_story_22
    complex_scene_279 = importer.save_or_locate(complex_scene_279)

    complex_scene_280.place = complex_place_231
    complex_scene_280.story = complex_story_22
    complex_scene_280 = importer.save_or_locate(complex_scene_280)

    complex_scene_281.place = complex_place_225
    complex_scene_281.story = complex_story_22
    complex_scene_281 = importer.save_or_locate(complex_scene_281)

    complex_scene_282.place = complex_place_228
    complex_scene_282.story = complex_story_22
    complex_scene_282 = importer.save_or_locate(complex_scene_282)

    complex_scene_283.place = complex_place_226
    complex_scene_283.story = complex_story_22
    complex_scene_283 = importer.save_or_locate(complex_scene_283)

    complex_scene_284.place = complex_place_227
    complex_scene_284.story = complex_story_22
    complex_scene_284 = importer.save_or_locate(complex_scene_284)

    complex_scene_285.place = complex_place_229
    complex_scene_285.story = complex_story_22
    complex_scene_285 = importer.save_or_locate(complex_scene_285)

    complex_scene_286.place = complex_place_230
    complex_scene_286.story = complex_story_22
    complex_scene_286 = importer.save_or_locate(complex_scene_286)

    complex_scene_287.place = complex_place_255
    complex_scene_287.story = complex_story_22
    complex_scene_287 = importer.save_or_locate(complex_scene_287)

    complex_scene_288.place = complex_place_252
    complex_scene_288.story = complex_story_22
    complex_scene_288 = importer.save_or_locate(complex_scene_288)

    complex_scene_289.place = complex_place_221
    complex_scene_289.story = complex_story_22
    complex_scene_289 = importer.save_or_locate(complex_scene_289)

    complex_scene_290.place = complex_place_256
    complex_scene_290.story = complex_story_22
    complex_scene_290 = importer.save_or_locate(complex_scene_290)

    complex_scene_291.place = complex_place_235
    complex_scene_291.story = complex_story_23
    complex_scene_291 = importer.save_or_locate(complex_scene_291)

    complex_scene_292.place = complex_place_298
    complex_scene_292.story = complex_story_23
    complex_scene_292 = importer.save_or_locate(complex_scene_292)

    complex_scene_293.place = complex_place_264
    complex_scene_293.story = complex_story_23
    complex_scene_293 = importer.save_or_locate(complex_scene_293)

    complex_scene_294.place = complex_place_246
    complex_scene_294.story = complex_story_23
    complex_scene_294 = importer.save_or_locate(complex_scene_294)

    complex_scene_295.place = complex_place_235
    complex_scene_295.story = complex_story_24
    complex_scene_295 = importer.save_or_locate(complex_scene_295)

    complex_scene_296.place = complex_place_224
    complex_scene_296.story = complex_story_24
    complex_scene_296 = importer.save_or_locate(complex_scene_296)

    complex_scene_297.place = complex_place_219
    complex_scene_297.story = complex_story_24
    complex_scene_297 = importer.save_or_locate(complex_scene_297)

    complex_scene_298.place = complex_place_214
    complex_scene_298.story = complex_story_24
    complex_scene_298 = importer.save_or_locate(complex_scene_298)

    complex_scene_299.place = complex_place_178
    complex_scene_299.story = complex_story_24
    complex_scene_299 = importer.save_or_locate(complex_scene_299)

    complex_scene_300.place = complex_place_172
    complex_scene_300.story = complex_story_24
    complex_scene_300 = importer.save_or_locate(complex_scene_300)

    complex_scene_301.place = complex_place_170
    complex_scene_301.story = complex_story_24
    complex_scene_301 = importer.save_or_locate(complex_scene_301)

    complex_scene_302.place = complex_place_162
    complex_scene_302.story = complex_story_24
    complex_scene_302 = importer.save_or_locate(complex_scene_302)

    complex_scene_303.place = complex_place_154
    complex_scene_303.story = complex_story_24
    complex_scene_303 = importer.save_or_locate(complex_scene_303)

    complex_scene_304.place = complex_place_152
    complex_scene_304.story = complex_story_24
    complex_scene_304 = importer.save_or_locate(complex_scene_304)

    complex_scene_305.place = complex_place_131
    complex_scene_305.story = complex_story_24
    complex_scene_305 = importer.save_or_locate(complex_scene_305)

    complex_scene_306.place = complex_place_130
    complex_scene_306.story = complex_story_24
    complex_scene_306 = importer.save_or_locate(complex_scene_306)

    complex_scene_307.place = complex_place_132
    complex_scene_307.story = complex_story_24
    complex_scene_307 = importer.save_or_locate(complex_scene_307)

    complex_scene_308.place = complex_place_177
    complex_scene_308.story = complex_story_24
    complex_scene_308 = importer.save_or_locate(complex_scene_308)

    complex_scene_309.place = complex_place_488
    complex_scene_309.story = complex_story_25
    complex_scene_309 = importer.save_or_locate(complex_scene_309)

    complex_scene_310.place = complex_place_483
    complex_scene_310.story = complex_story_25
    complex_scene_310 = importer.save_or_locate(complex_scene_310)

    complex_scene_311.place = complex_place_484
    complex_scene_311.story = complex_story_25
    complex_scene_311 = importer.save_or_locate(complex_scene_311)

    complex_scene_312.place = complex_place_485
    complex_scene_312.story = complex_story_25
    complex_scene_312 = importer.save_or_locate(complex_scene_312)

    complex_scene_313.place = complex_place_486
    complex_scene_313.story = complex_story_25
    complex_scene_313 = importer.save_or_locate(complex_scene_313)

    complex_scene_314.place = complex_place_487
    complex_scene_314.story = complex_story_25
    complex_scene_314 = importer.save_or_locate(complex_scene_314)

    complex_scene_315.place = complex_place_489
    complex_scene_315.story = complex_story_25
    complex_scene_315 = importer.save_or_locate(complex_scene_315)

    complex_scene_316.place = complex_place_494
    complex_scene_316.story = complex_story_25
    complex_scene_316 = importer.save_or_locate(complex_scene_316)

    complex_scene_317.place = complex_place_496
    complex_scene_317.story = complex_story_25
    complex_scene_317 = importer.save_or_locate(complex_scene_317)

    complex_scene_318.place = complex_place_497
    complex_scene_318.story = complex_story_25
    complex_scene_318 = importer.save_or_locate(complex_scene_318)

    complex_scene_319.place = complex_place_499
    complex_scene_319.story = complex_story_25
    complex_scene_319 = importer.save_or_locate(complex_scene_319)

    complex_scene_320.place = complex_place_502
    complex_scene_320.story = complex_story_25
    complex_scene_320 = importer.save_or_locate(complex_scene_320)

    complex_scene_321.place = complex_place_513
    complex_scene_321.story = complex_story_25
    complex_scene_321 = importer.save_or_locate(complex_scene_321)

    complex_scene_322.place = complex_place_515
    complex_scene_322.story = complex_story_25
    complex_scene_322 = importer.save_or_locate(complex_scene_322)

    complex_scene_323.place = complex_place_514
    complex_scene_323.story = complex_story_25
    complex_scene_323 = importer.save_or_locate(complex_scene_323)

    complex_scene_324.place = complex_place_516
    complex_scene_324.story = complex_story_25
    complex_scene_324 = importer.save_or_locate(complex_scene_324)

    complex_scene_325.place = complex_place_509
    complex_scene_325.story = complex_story_25
    complex_scene_325 = importer.save_or_locate(complex_scene_325)

    complex_scene_326.place = complex_place_505
    complex_scene_326.story = complex_story_25
    complex_scene_326 = importer.save_or_locate(complex_scene_326)

    complex_scene_327.place = complex_place_503
    complex_scene_327.story = complex_story_25
    complex_scene_327 = importer.save_or_locate(complex_scene_327)

    complex_scene_328.place = complex_place_235
    complex_scene_328.story = complex_story_26
    complex_scene_328 = importer.save_or_locate(complex_scene_328)

    complex_scene_329.place = complex_place_507
    complex_scene_329.story = complex_story_26
    complex_scene_329 = importer.save_or_locate(complex_scene_329)

    complex_scene_330.place = complex_place_506
    complex_scene_330.story = complex_story_26
    complex_scene_330 = importer.save_or_locate(complex_scene_330)

    complex_scene_331.place = complex_place_508
    complex_scene_331.story = complex_story_26
    complex_scene_331 = importer.save_or_locate(complex_scene_331)

    complex_scene_332.place = complex_place_510
    complex_scene_332.story = complex_story_26
    complex_scene_332 = importer.save_or_locate(complex_scene_332)

    complex_scene_333.place = complex_place_492
    complex_scene_333.story = complex_story_26
    complex_scene_333 = importer.save_or_locate(complex_scene_333)

    complex_scene_334.place = complex_place_493
    complex_scene_334.story = complex_story_26
    complex_scene_334 = importer.save_or_locate(complex_scene_334)

    complex_scene_335.place = complex_place_528
    complex_scene_335.story = complex_story_26
    complex_scene_335 = importer.save_or_locate(complex_scene_335)

    complex_scene_336.place = complex_place_529
    complex_scene_336.story = complex_story_26
    complex_scene_336 = importer.save_or_locate(complex_scene_336)

    complex_scene_337.place = complex_place_531
    complex_scene_337.story = complex_story_26
    complex_scene_337 = importer.save_or_locate(complex_scene_337)

    complex_scene_338.place = complex_place_527
    complex_scene_338.story = complex_story_26
    complex_scene_338 = importer.save_or_locate(complex_scene_338)

    complex_scene_339.place = complex_place_526
    complex_scene_339.story = complex_story_26
    complex_scene_339 = importer.save_or_locate(complex_scene_339)

    complex_scene_340.place = complex_place_511
    complex_scene_340.story = complex_story_26
    complex_scene_340 = importer.save_or_locate(complex_scene_340)

    complex_scene_341.place = complex_place_28
    complex_scene_341.story = complex_story_27
    complex_scene_341 = importer.save_or_locate(complex_scene_341)

    complex_scene_342.place = complex_place_29
    complex_scene_342.story = complex_story_27
    complex_scene_342 = importer.save_or_locate(complex_scene_342)

    complex_scene_343.place = complex_place_31
    complex_scene_343.story = complex_story_27
    complex_scene_343 = importer.save_or_locate(complex_scene_343)

    complex_scene_344.place = complex_place_30
    complex_scene_344.story = complex_story_27
    complex_scene_344 = importer.save_or_locate(complex_scene_344)

    complex_scene_345.place = complex_place_44
    complex_scene_345.story = complex_story_27
    complex_scene_345 = importer.save_or_locate(complex_scene_345)

    complex_scene_346.place = complex_place_45
    complex_scene_346.story = complex_story_27
    complex_scene_346 = importer.save_or_locate(complex_scene_346)

    complex_scene_347.place = complex_place_50
    complex_scene_347.story = complex_story_27
    complex_scene_347 = importer.save_or_locate(complex_scene_347)

    complex_scene_348.place = complex_place_51
    complex_scene_348.story = complex_story_27
    complex_scene_348 = importer.save_or_locate(complex_scene_348)

    complex_scene_349.place = complex_place_52
    complex_scene_349.story = complex_story_27
    complex_scene_349 = importer.save_or_locate(complex_scene_349)

    complex_scene_350.place = complex_place_53
    complex_scene_350.story = complex_story_27
    complex_scene_350 = importer.save_or_locate(complex_scene_350)

    complex_scene_351.place = complex_place_54
    complex_scene_351.story = complex_story_27
    complex_scene_351 = importer.save_or_locate(complex_scene_351)

    complex_scene_352.place = complex_place_37
    complex_scene_352.story = complex_story_27
    complex_scene_352 = importer.save_or_locate(complex_scene_352)

    complex_scene_353.place = complex_place_34
    complex_scene_353.story = complex_story_28
    complex_scene_353 = importer.save_or_locate(complex_scene_353)

    complex_scene_354.place = complex_place_33
    complex_scene_354.story = complex_story_28
    complex_scene_354 = importer.save_or_locate(complex_scene_354)

    complex_scene_355.place = complex_place_47
    complex_scene_355.story = complex_story_28
    complex_scene_355 = importer.save_or_locate(complex_scene_355)

    complex_scene_356.place = complex_place_35
    complex_scene_356.story = complex_story_28
    complex_scene_356 = importer.save_or_locate(complex_scene_356)

    complex_scene_357.place = complex_place_36
    complex_scene_357.story = complex_story_28
    complex_scene_357 = importer.save_or_locate(complex_scene_357)

    complex_scene_358.place = complex_place_39
    complex_scene_358.story = complex_story_28
    complex_scene_358 = importer.save_or_locate(complex_scene_358)

    complex_scene_359.place = complex_place_42
    complex_scene_359.story = complex_story_28
    complex_scene_359 = importer.save_or_locate(complex_scene_359)

    complex_scene_360.place = complex_place_38
    complex_scene_360.story = complex_story_28
    complex_scene_360 = importer.save_or_locate(complex_scene_360)

    complex_scene_361.place = complex_place_41
    complex_scene_361.story = complex_story_28
    complex_scene_361 = importer.save_or_locate(complex_scene_361)

    complex_scene_362.place = complex_place_43
    complex_scene_362.story = complex_story_28
    complex_scene_362 = importer.save_or_locate(complex_scene_362)

    complex_scene_363.place = complex_place_46
    complex_scene_363.story = complex_story_28
    complex_scene_363 = importer.save_or_locate(complex_scene_363)

    complex_scene_364.place = complex_place_48
    complex_scene_364.story = complex_story_28
    complex_scene_364 = importer.save_or_locate(complex_scene_364)

    complex_scene_365.place = complex_place_49
    complex_scene_365.story = complex_story_28
    complex_scene_365 = importer.save_or_locate(complex_scene_365)

    complex_scene_366.place = complex_place_55
    complex_scene_366.story = complex_story_28
    complex_scene_366 = importer.save_or_locate(complex_scene_366)

    complex_scene_367.place = complex_place_56
    complex_scene_367.story = complex_story_28
    complex_scene_367 = importer.save_or_locate(complex_scene_367)

    complex_scene_368.place = complex_place_25
    complex_scene_368.story = complex_story_28
    complex_scene_368 = importer.save_or_locate(complex_scene_368)

    complex_scene_369.place = complex_place_24
    complex_scene_369.story = complex_story_28
    complex_scene_369 = importer.save_or_locate(complex_scene_369)

    complex_scene_370.place = complex_place_27
    complex_scene_370.story = complex_story_28
    complex_scene_370 = importer.save_or_locate(complex_scene_370)

    complex_scene_371.place = complex_place_26
    complex_scene_371.story = complex_story_28
    complex_scene_371 = importer.save_or_locate(complex_scene_371)

    complex_scene_372.place = complex_place_295
    complex_scene_372.story = complex_story_29
    complex_scene_372 = importer.save_or_locate(complex_scene_372)

    complex_scene_373.place = complex_place_321
    complex_scene_373.story = complex_story_29
    complex_scene_373 = importer.save_or_locate(complex_scene_373)

    complex_scene_374.place = complex_place_322
    complex_scene_374.story = complex_story_29
    complex_scene_374 = importer.save_or_locate(complex_scene_374)

    complex_scene_375.place = complex_place_5
    complex_scene_375.story = complex_story_29
    complex_scene_375 = importer.save_or_locate(complex_scene_375)

    complex_scene_376.place = complex_place_4
    complex_scene_376.story = complex_story_29
    complex_scene_376 = importer.save_or_locate(complex_scene_376)

    complex_scene_377.place = complex_place_3
    complex_scene_377.story = complex_story_29
    complex_scene_377 = importer.save_or_locate(complex_scene_377)

    complex_scene_378.place = complex_place_2
    complex_scene_378.story = complex_story_29
    complex_scene_378 = importer.save_or_locate(complex_scene_378)

    complex_scene_379.place = complex_place_1
    complex_scene_379.story = complex_story_29
    complex_scene_379 = importer.save_or_locate(complex_scene_379)

    complex_scene_380.place = complex_place_9
    complex_scene_380.story = complex_story_29
    complex_scene_380 = importer.save_or_locate(complex_scene_380)

    complex_scene_381.place = complex_place_223
    complex_scene_381.story = complex_story_30
    complex_scene_381 = importer.save_or_locate(complex_scene_381)

    complex_scene_382.place = complex_place_13
    complex_scene_382.story = complex_story_30
    complex_scene_382 = importer.save_or_locate(complex_scene_382)

    complex_scene_383.place = complex_place_21
    complex_scene_383.story = complex_story_30
    complex_scene_383 = importer.save_or_locate(complex_scene_383)

    complex_scene_384.place = complex_place_20
    complex_scene_384.story = complex_story_30
    complex_scene_384 = importer.save_or_locate(complex_scene_384)

    complex_scene_385.place = complex_place_11
    complex_scene_385.story = complex_story_30
    complex_scene_385 = importer.save_or_locate(complex_scene_385)

    complex_scene_386.place = complex_place_12
    complex_scene_386.story = complex_story_30
    complex_scene_386 = importer.save_or_locate(complex_scene_386)

    complex_scene_387.place = complex_place_22
    complex_scene_387.story = complex_story_30
    complex_scene_387 = importer.save_or_locate(complex_scene_387)

    complex_scene_388.place = complex_place_19
    complex_scene_388.story = complex_story_30
    complex_scene_388 = importer.save_or_locate(complex_scene_388)

    complex_scene_389.place = complex_place_18
    complex_scene_389.story = complex_story_30
    complex_scene_389 = importer.save_or_locate(complex_scene_389)

    complex_scene_390.place = complex_place_14
    complex_scene_390.story = complex_story_30
    complex_scene_390 = importer.save_or_locate(complex_scene_390)

    complex_scene_391.place = complex_place_15
    complex_scene_391.story = complex_story_30
    complex_scene_391 = importer.save_or_locate(complex_scene_391)

    complex_scene_392.place = complex_place_17
    complex_scene_392.story = complex_story_30
    complex_scene_392 = importer.save_or_locate(complex_scene_392)

    complex_scene_393.place = complex_place_16
    complex_scene_393.story = complex_story_30
    complex_scene_393 = importer.save_or_locate(complex_scene_393)

    complex_scene_394.place = complex_place_23
    complex_scene_394.story = complex_story_30
    complex_scene_394 = importer.save_or_locate(complex_scene_394)

    complex_scene_395.place = complex_place_8
    complex_scene_395.story = complex_story_30
    complex_scene_395 = importer.save_or_locate(complex_scene_395)

    complex_scene_396.place = complex_place_6
    complex_scene_396.story = complex_story_30
    complex_scene_396 = importer.save_or_locate(complex_scene_396)

    complex_scene_397.place = complex_place_303
    complex_scene_397.story = complex_story_30
    complex_scene_397 = importer.save_or_locate(complex_scene_397)

    complex_scene_398.place = complex_place_363
    complex_scene_398.story = complex_story_31
    complex_scene_398 = importer.save_or_locate(complex_scene_398)

    complex_scene_399.place = complex_place_365
    complex_scene_399.story = complex_story_31
    complex_scene_399 = importer.save_or_locate(complex_scene_399)

    complex_scene_400.place = complex_place_369
    complex_scene_400.story = complex_story_31
    complex_scene_400 = importer.save_or_locate(complex_scene_400)

    complex_scene_401.place = complex_place_364
    complex_scene_401.story = complex_story_31
    complex_scene_401 = importer.save_or_locate(complex_scene_401)

    complex_scene_402.place = complex_place_370
    complex_scene_402.story = complex_story_31
    complex_scene_402 = importer.save_or_locate(complex_scene_402)

    complex_scene_403.place = complex_place_371
    complex_scene_403.story = complex_story_31
    complex_scene_403 = importer.save_or_locate(complex_scene_403)

    complex_scene_404.place = complex_place_372
    complex_scene_404.story = complex_story_31
    complex_scene_404 = importer.save_or_locate(complex_scene_404)

    complex_scene_405.place = complex_place_376
    complex_scene_405.story = complex_story_31
    complex_scene_405 = importer.save_or_locate(complex_scene_405)

    complex_scene_406.place = complex_place_374
    complex_scene_406.story = complex_story_31
    complex_scene_406 = importer.save_or_locate(complex_scene_406)

    complex_scene_407.place = complex_place_381
    complex_scene_407.story = complex_story_31
    complex_scene_407 = importer.save_or_locate(complex_scene_407)

    complex_scene_408.place = complex_place_380
    complex_scene_408.story = complex_story_31
    complex_scene_408 = importer.save_or_locate(complex_scene_408)

    complex_scene_409.place = complex_place_378
    complex_scene_409.story = complex_story_31
    complex_scene_409 = importer.save_or_locate(complex_scene_409)

    complex_scene_410.place = complex_place_377
    complex_scene_410.story = complex_story_31
    complex_scene_410 = importer.save_or_locate(complex_scene_410)

    complex_scene_411.place = complex_place_351
    complex_scene_411.story = complex_story_31
    complex_scene_411 = importer.save_or_locate(complex_scene_411)

    complex_scene_412.place = complex_place_352
    complex_scene_412.story = complex_story_31
    complex_scene_412 = importer.save_or_locate(complex_scene_412)

    complex_scene_413.place = complex_place_358
    complex_scene_413.story = complex_story_31
    complex_scene_413 = importer.save_or_locate(complex_scene_413)

    complex_scene_414.place = complex_place_354
    complex_scene_414.story = complex_story_31
    complex_scene_414 = importer.save_or_locate(complex_scene_414)

    complex_scene_415.place = complex_place_355
    complex_scene_415.story = complex_story_31
    complex_scene_415 = importer.save_or_locate(complex_scene_415)

    complex_scene_416.place = complex_place_353
    complex_scene_416.story = complex_story_31
    complex_scene_416 = importer.save_or_locate(complex_scene_416)

    complex_scene_417.place = complex_place_359
    complex_scene_417.story = complex_story_31
    complex_scene_417 = importer.save_or_locate(complex_scene_417)

    complex_scene_418.place = complex_place_356
    complex_scene_418.story = complex_story_31
    complex_scene_418 = importer.save_or_locate(complex_scene_418)

    complex_scene_419.place = complex_place_360
    complex_scene_419.story = complex_story_31
    complex_scene_419 = importer.save_or_locate(complex_scene_419)

    complex_scene_420.place = complex_place_382
    complex_scene_420.story = complex_story_31
    complex_scene_420 = importer.save_or_locate(complex_scene_420)

    complex_scene_421.place = complex_place_258
    complex_scene_421.story = complex_story_32
    complex_scene_421 = importer.save_or_locate(complex_scene_421)

    complex_scene_422.place = complex_place_259
    complex_scene_422.story = complex_story_32
    complex_scene_422 = importer.save_or_locate(complex_scene_422)

    complex_scene_423.place = complex_place_267
    complex_scene_423.story = complex_story_32
    complex_scene_423 = importer.save_or_locate(complex_scene_423)

    complex_scene_424.place = complex_place_268
    complex_scene_424.story = complex_story_32
    complex_scene_424 = importer.save_or_locate(complex_scene_424)

    complex_scene_425.place = complex_place_261
    complex_scene_425.story = complex_story_32
    complex_scene_425 = importer.save_or_locate(complex_scene_425)

    complex_scene_426.place = complex_place_262
    complex_scene_426.story = complex_story_32
    complex_scene_426 = importer.save_or_locate(complex_scene_426)

    complex_scene_427.place = complex_place_263
    complex_scene_427.story = complex_story_32
    complex_scene_427 = importer.save_or_locate(complex_scene_427)

    complex_scene_428.place = complex_place_260
    complex_scene_428.story = complex_story_32
    complex_scene_428 = importer.save_or_locate(complex_scene_428)

    complex_scene_429.place = complex_place_271
    complex_scene_429.story = complex_story_32
    complex_scene_429 = importer.save_or_locate(complex_scene_429)

    complex_scene_430.place = complex_place_257
    complex_scene_430.story = complex_story_32
    complex_scene_430 = importer.save_or_locate(complex_scene_430)

    complex_scene_431.place = complex_place_274
    complex_scene_431.story = complex_story_32
    complex_scene_431 = importer.save_or_locate(complex_scene_431)

    complex_scene_432.place = complex_place_291
    complex_scene_432.story = complex_story_32
    complex_scene_432 = importer.save_or_locate(complex_scene_432)

    complex_scene_433.place = complex_place_278
    complex_scene_433.story = complex_story_32
    complex_scene_433 = importer.save_or_locate(complex_scene_433)

    complex_scene_434.place = complex_place_281
    complex_scene_434.story = complex_story_32
    complex_scene_434 = importer.save_or_locate(complex_scene_434)

    complex_scene_435.place = complex_place_297
    complex_scene_435.story = complex_story_32
    complex_scene_435 = importer.save_or_locate(complex_scene_435)

    complex_scene_436.place = complex_place_289
    complex_scene_436.story = complex_story_32
    complex_scene_436 = importer.save_or_locate(complex_scene_436)

    complex_scene_437.place = complex_place_265
    complex_scene_437.story = complex_story_32
    complex_scene_437 = importer.save_or_locate(complex_scene_437)

    complex_scene_438.place = complex_place_266
    complex_scene_438.story = complex_story_32
    complex_scene_438 = importer.save_or_locate(complex_scene_438)

    complex_scene_439.place = complex_place_253
    complex_scene_439.story = complex_story_32
    complex_scene_439 = importer.save_or_locate(complex_scene_439)

    complex_scene_440.place = complex_place_551
    complex_scene_440.story = complex_story_33
    complex_scene_440 = importer.save_or_locate(complex_scene_440)

    complex_scene_441.place = complex_place_550
    complex_scene_441.story = complex_story_33
    complex_scene_441 = importer.save_or_locate(complex_scene_441)

    complex_scene_442.place = complex_place_547
    complex_scene_442.story = complex_story_33
    complex_scene_442 = importer.save_or_locate(complex_scene_442)

    complex_scene_443.place = complex_place_546
    complex_scene_443.story = complex_story_33
    complex_scene_443 = importer.save_or_locate(complex_scene_443)

    complex_scene_444.place = complex_place_545
    complex_scene_444.story = complex_story_33
    complex_scene_444 = importer.save_or_locate(complex_scene_444)

    complex_scene_445.place = complex_place_542
    complex_scene_445.story = complex_story_33
    complex_scene_445 = importer.save_or_locate(complex_scene_445)

    complex_scene_446.place = complex_place_543
    complex_scene_446.story = complex_story_33
    complex_scene_446 = importer.save_or_locate(complex_scene_446)

    complex_scene_447.place = complex_place_544
    complex_scene_447.story = complex_story_33
    complex_scene_447 = importer.save_or_locate(complex_scene_447)

    complex_scene_448.place = complex_place_540
    complex_scene_448.story = complex_story_33
    complex_scene_448 = importer.save_or_locate(complex_scene_448)

    complex_scene_449.place = complex_place_539
    complex_scene_449.story = complex_story_33
    complex_scene_449 = importer.save_or_locate(complex_scene_449)

    complex_scene_450.place = complex_place_538
    complex_scene_450.story = complex_story_33
    complex_scene_450 = importer.save_or_locate(complex_scene_450)

    complex_scene_451.place = complex_place_553
    complex_scene_451.story = complex_story_33
    complex_scene_451 = importer.save_or_locate(complex_scene_451)

    complex_scene_452.place = complex_place_549
    complex_scene_452.story = complex_story_33
    complex_scene_452 = importer.save_or_locate(complex_scene_452)

    complex_scene_453.place = complex_place_548
    complex_scene_453.story = complex_story_33
    complex_scene_453 = importer.save_or_locate(complex_scene_453)

    complex_scene_454.place = complex_place_541
    complex_scene_454.story = complex_story_33
    complex_scene_454 = importer.save_or_locate(complex_scene_454)

    complex_scene_455.place = complex_place_552
    complex_scene_455.story = complex_story_33
    complex_scene_455 = importer.save_or_locate(complex_scene_455)

    complex_scene_456.place = complex_place_523
    complex_scene_456.story = complex_story_34
    complex_scene_456 = importer.save_or_locate(complex_scene_456)

    complex_scene_457.place = complex_place_296
    complex_scene_457.story = complex_story_34
    complex_scene_457 = importer.save_or_locate(complex_scene_457)

    complex_scene_458.place = complex_place_300
    complex_scene_458.story = complex_story_34
    complex_scene_458 = importer.save_or_locate(complex_scene_458)

    complex_scene_459.place = complex_place_302
    complex_scene_459.story = complex_story_34
    complex_scene_459 = importer.save_or_locate(complex_scene_459)

    complex_scene_460.place = complex_place_467
    complex_scene_460.story = complex_story_34
    complex_scene_460 = importer.save_or_locate(complex_scene_460)

    # Re-processing model: complex.models.Photo

    complex_photo_1.step = complex_step_6
    complex_photo_1 = importer.save_or_locate(complex_photo_1)

    complex_photo_2.step = complex_step_7
    complex_photo_2 = importer.save_or_locate(complex_photo_2)

    complex_photo_3.step = complex_step_8
    complex_photo_3 = importer.save_or_locate(complex_photo_3)

    complex_photo_4.step = complex_step_9
    complex_photo_4 = importer.save_or_locate(complex_photo_4)

    complex_photo_5.step = complex_step_10
    complex_photo_5 = importer.save_or_locate(complex_photo_5)

    complex_photo_6.step = complex_step_12
    complex_photo_6 = importer.save_or_locate(complex_photo_6)

    complex_photo_7.step = complex_step_15
    complex_photo_7 = importer.save_or_locate(complex_photo_7)

    complex_photo_8.step = complex_step_16
    complex_photo_8 = importer.save_or_locate(complex_photo_8)

    complex_photo_9.step = complex_step_18
    complex_photo_9 = importer.save_or_locate(complex_photo_9)

    complex_photo_10.step = complex_step_19
    complex_photo_10 = importer.save_or_locate(complex_photo_10)

    complex_photo_11.step = complex_step_21
    complex_photo_11 = importer.save_or_locate(complex_photo_11)

    complex_photo_12.step = complex_step_22
    complex_photo_12 = importer.save_or_locate(complex_photo_12)

    complex_photo_13.step = complex_step_23
    complex_photo_13 = importer.save_or_locate(complex_photo_13)

    complex_photo_14.step = complex_step_24
    complex_photo_14 = importer.save_or_locate(complex_photo_14)

    complex_photo_15.step = complex_step_25
    complex_photo_15 = importer.save_or_locate(complex_photo_15)

    complex_photo_16.step = complex_step_27
    complex_photo_16 = importer.save_or_locate(complex_photo_16)

    complex_photo_17.step = complex_step_28
    complex_photo_17 = importer.save_or_locate(complex_photo_17)

    complex_photo_18.step = complex_step_29
    complex_photo_18 = importer.save_or_locate(complex_photo_18)

    complex_photo_19.step = complex_step_30
    complex_photo_19 = importer.save_or_locate(complex_photo_19)

    complex_photo_20.step = complex_step_31
    complex_photo_20 = importer.save_or_locate(complex_photo_20)

    complex_photo_21.step = complex_step_32
    complex_photo_21 = importer.save_or_locate(complex_photo_21)

    complex_photo_22.step = complex_step_33
    complex_photo_22 = importer.save_or_locate(complex_photo_22)

    complex_photo_23.step = complex_step_34
    complex_photo_23 = importer.save_or_locate(complex_photo_23)

    complex_photo_24.step = complex_step_35
    complex_photo_24 = importer.save_or_locate(complex_photo_24)

    complex_photo_25.step = complex_step_36
    complex_photo_25 = importer.save_or_locate(complex_photo_25)

    complex_photo_26.step = complex_step_37
    complex_photo_26 = importer.save_or_locate(complex_photo_26)

    complex_photo_27.step = complex_step_42
    complex_photo_27 = importer.save_or_locate(complex_photo_27)

    complex_photo_28.step = complex_step_43
    complex_photo_28 = importer.save_or_locate(complex_photo_28)

    complex_photo_29.step = complex_step_45
    complex_photo_29 = importer.save_or_locate(complex_photo_29)

    complex_photo_30.step = complex_step_46
    complex_photo_30 = importer.save_or_locate(complex_photo_30)

    complex_photo_31.step = complex_step_47
    complex_photo_31 = importer.save_or_locate(complex_photo_31)

    complex_photo_32.step = complex_step_48
    complex_photo_32 = importer.save_or_locate(complex_photo_32)

    complex_photo_33.step = complex_step_52
    complex_photo_33 = importer.save_or_locate(complex_photo_33)

    complex_photo_34.step = complex_step_53
    complex_photo_34 = importer.save_or_locate(complex_photo_34)

    complex_photo_35.step = complex_step_54
    complex_photo_35 = importer.save_or_locate(complex_photo_35)

    complex_photo_36.step = complex_step_55
    complex_photo_36 = importer.save_or_locate(complex_photo_36)

    complex_photo_37.step = complex_step_56
    complex_photo_37 = importer.save_or_locate(complex_photo_37)

    complex_photo_38.step = complex_step_57
    complex_photo_38 = importer.save_or_locate(complex_photo_38)

    complex_photo_39.step = complex_step_58
    complex_photo_39 = importer.save_or_locate(complex_photo_39)

    complex_photo_40.step = complex_step_59
    complex_photo_40 = importer.save_or_locate(complex_photo_40)

    complex_photo_41.step = complex_step_60
    complex_photo_41 = importer.save_or_locate(complex_photo_41)

    complex_photo_42.step = complex_step_61
    complex_photo_42 = importer.save_or_locate(complex_photo_42)

    complex_photo_43.step = complex_step_62
    complex_photo_43 = importer.save_or_locate(complex_photo_43)

    complex_photo_44.step = complex_step_63
    complex_photo_44 = importer.save_or_locate(complex_photo_44)

    complex_photo_45.step = complex_step_64
    complex_photo_45 = importer.save_or_locate(complex_photo_45)

    complex_photo_46.step = complex_step_66
    complex_photo_46 = importer.save_or_locate(complex_photo_46)

    complex_photo_47.step = complex_step_67
    complex_photo_47 = importer.save_or_locate(complex_photo_47)

    complex_photo_48.step = complex_step_68
    complex_photo_48 = importer.save_or_locate(complex_photo_48)

    complex_photo_49.step = complex_step_69
    complex_photo_49 = importer.save_or_locate(complex_photo_49)

    complex_photo_50.step = complex_step_71
    complex_photo_50 = importer.save_or_locate(complex_photo_50)

    complex_photo_51.step = complex_step_73
    complex_photo_51 = importer.save_or_locate(complex_photo_51)

    complex_photo_52.step = complex_step_76
    complex_photo_52 = importer.save_or_locate(complex_photo_52)

    complex_photo_53.step = complex_step_79
    complex_photo_53 = importer.save_or_locate(complex_photo_53)

    complex_photo_54.step = complex_step_80
    complex_photo_54 = importer.save_or_locate(complex_photo_54)

    complex_photo_55.step = complex_step_82
    complex_photo_55 = importer.save_or_locate(complex_photo_55)

    complex_photo_56.step = complex_step_83
    complex_photo_56 = importer.save_or_locate(complex_photo_56)

    complex_photo_57.step = complex_step_85
    complex_photo_57 = importer.save_or_locate(complex_photo_57)

    complex_photo_58.step = complex_step_86
    complex_photo_58 = importer.save_or_locate(complex_photo_58)

    complex_photo_59.step = complex_step_87
    complex_photo_59 = importer.save_or_locate(complex_photo_59)

    complex_photo_60.step = complex_step_89
    complex_photo_60 = importer.save_or_locate(complex_photo_60)

    complex_photo_61.step = complex_step_91
    complex_photo_61 = importer.save_or_locate(complex_photo_61)

    complex_photo_62.step = complex_step_92
    complex_photo_62 = importer.save_or_locate(complex_photo_62)

    complex_photo_63.step = complex_step_93
    complex_photo_63 = importer.save_or_locate(complex_photo_63)

    complex_photo_64.step = complex_step_95
    complex_photo_64 = importer.save_or_locate(complex_photo_64)

    complex_photo_65.step = complex_step_96
    complex_photo_65 = importer.save_or_locate(complex_photo_65)

    complex_photo_66.step = complex_step_97
    complex_photo_66 = importer.save_or_locate(complex_photo_66)

    complex_photo_67.step = complex_step_99
    complex_photo_67 = importer.save_or_locate(complex_photo_67)

    complex_photo_68.step = complex_step_102
    complex_photo_68 = importer.save_or_locate(complex_photo_68)

    complex_photo_69.step = complex_step_103
    complex_photo_69 = importer.save_or_locate(complex_photo_69)

    complex_photo_70.step = complex_step_104
    complex_photo_70 = importer.save_or_locate(complex_photo_70)

    complex_photo_71.step = complex_step_105
    complex_photo_71 = importer.save_or_locate(complex_photo_71)

    complex_photo_72.step = complex_step_106
    complex_photo_72 = importer.save_or_locate(complex_photo_72)

    complex_photo_73.step = complex_step_109
    complex_photo_73 = importer.save_or_locate(complex_photo_73)

    complex_photo_74.step = complex_step_110
    complex_photo_74 = importer.save_or_locate(complex_photo_74)

    complex_photo_75.step = complex_step_111
    complex_photo_75 = importer.save_or_locate(complex_photo_75)

    complex_photo_76.step = complex_step_112
    complex_photo_76 = importer.save_or_locate(complex_photo_76)

    complex_photo_77.step = complex_step_114
    complex_photo_77 = importer.save_or_locate(complex_photo_77)

    complex_photo_78.step = complex_step_115
    complex_photo_78 = importer.save_or_locate(complex_photo_78)

    complex_photo_79.step = complex_step_116
    complex_photo_79 = importer.save_or_locate(complex_photo_79)

    complex_photo_80.step = complex_step_117
    complex_photo_80 = importer.save_or_locate(complex_photo_80)

    complex_photo_81.step = complex_step_118
    complex_photo_81 = importer.save_or_locate(complex_photo_81)

    complex_photo_82.step = complex_step_119
    complex_photo_82 = importer.save_or_locate(complex_photo_82)

    complex_photo_83.step = complex_step_120
    complex_photo_83 = importer.save_or_locate(complex_photo_83)

    complex_photo_84.step = complex_step_121
    complex_photo_84 = importer.save_or_locate(complex_photo_84)

    complex_photo_85.step = complex_step_122
    complex_photo_85 = importer.save_or_locate(complex_photo_85)

    complex_photo_86.step = complex_step_123
    complex_photo_86 = importer.save_or_locate(complex_photo_86)

    complex_photo_87.step = complex_step_124
    complex_photo_87 = importer.save_or_locate(complex_photo_87)

    complex_photo_88.step = complex_step_125
    complex_photo_88 = importer.save_or_locate(complex_photo_88)

    complex_photo_89.step = complex_step_126
    complex_photo_89 = importer.save_or_locate(complex_photo_89)

    complex_photo_90.step = complex_step_127
    complex_photo_90 = importer.save_or_locate(complex_photo_90)

    complex_photo_91.step = complex_step_129
    complex_photo_91 = importer.save_or_locate(complex_photo_91)

    complex_photo_92.step = complex_step_130
    complex_photo_92 = importer.save_or_locate(complex_photo_92)

    complex_photo_93.step = complex_step_131
    complex_photo_93 = importer.save_or_locate(complex_photo_93)

    complex_photo_94.step = complex_step_132
    complex_photo_94 = importer.save_or_locate(complex_photo_94)

    complex_photo_95.step = complex_step_133
    complex_photo_95 = importer.save_or_locate(complex_photo_95)

    complex_photo_96.step = complex_step_135
    complex_photo_96 = importer.save_or_locate(complex_photo_96)

    complex_photo_97.step = complex_step_137
    complex_photo_97 = importer.save_or_locate(complex_photo_97)

    complex_photo_98.step = complex_step_138
    complex_photo_98 = importer.save_or_locate(complex_photo_98)

    complex_photo_99.step = complex_step_140
    complex_photo_99 = importer.save_or_locate(complex_photo_99)

    complex_photo_100.step = complex_step_141
    complex_photo_100 = importer.save_or_locate(complex_photo_100)

    complex_photo_101.step = complex_step_142
    complex_photo_101 = importer.save_or_locate(complex_photo_101)

    complex_photo_102.step = complex_step_143
    complex_photo_102 = importer.save_or_locate(complex_photo_102)

    complex_photo_103.step = complex_step_144
    complex_photo_103 = importer.save_or_locate(complex_photo_103)

    complex_photo_104.step = complex_step_147
    complex_photo_104 = importer.save_or_locate(complex_photo_104)

    complex_photo_105.step = complex_step_148
    complex_photo_105 = importer.save_or_locate(complex_photo_105)

    complex_photo_106.step = complex_step_149
    complex_photo_106 = importer.save_or_locate(complex_photo_106)

    complex_photo_107.step = complex_step_150
    complex_photo_107 = importer.save_or_locate(complex_photo_107)

    complex_photo_108.step = complex_step_154
    complex_photo_108 = importer.save_or_locate(complex_photo_108)

    complex_photo_109.step = complex_step_155
    complex_photo_109 = importer.save_or_locate(complex_photo_109)

    complex_photo_110.step = complex_step_159
    complex_photo_110 = importer.save_or_locate(complex_photo_110)

    complex_photo_111.step = complex_step_160
    complex_photo_111 = importer.save_or_locate(complex_photo_111)

    complex_photo_112.step = complex_step_161
    complex_photo_112 = importer.save_or_locate(complex_photo_112)

    complex_photo_113.step = complex_step_162
    complex_photo_113 = importer.save_or_locate(complex_photo_113)

    complex_photo_114.step = complex_step_163
    complex_photo_114 = importer.save_or_locate(complex_photo_114)

    complex_photo_115.step = complex_step_164
    complex_photo_115 = importer.save_or_locate(complex_photo_115)

    complex_photo_116.step = complex_step_165
    complex_photo_116 = importer.save_or_locate(complex_photo_116)

    complex_photo_117.step = complex_step_166
    complex_photo_117 = importer.save_or_locate(complex_photo_117)

    complex_photo_118.step = complex_step_167
    complex_photo_118 = importer.save_or_locate(complex_photo_118)

    complex_photo_119.step = complex_step_168
    complex_photo_119 = importer.save_or_locate(complex_photo_119)

    complex_photo_120.step = complex_step_170
    complex_photo_120 = importer.save_or_locate(complex_photo_120)

    complex_photo_121.step = complex_step_171
    complex_photo_121 = importer.save_or_locate(complex_photo_121)

    complex_photo_122.step = complex_step_173
    complex_photo_122 = importer.save_or_locate(complex_photo_122)

    complex_photo_123.step = complex_step_174
    complex_photo_123 = importer.save_or_locate(complex_photo_123)

    complex_photo_124.step = complex_step_175
    complex_photo_124 = importer.save_or_locate(complex_photo_124)

    complex_photo_125.step = complex_step_176
    complex_photo_125 = importer.save_or_locate(complex_photo_125)

    complex_photo_126.step = complex_step_177
    complex_photo_126 = importer.save_or_locate(complex_photo_126)

    complex_photo_127.step = complex_step_178
    complex_photo_127 = importer.save_or_locate(complex_photo_127)

    complex_photo_128.step = complex_step_179
    complex_photo_128 = importer.save_or_locate(complex_photo_128)

    complex_photo_129.step = complex_step_180
    complex_photo_129 = importer.save_or_locate(complex_photo_129)

    complex_photo_130.step = complex_step_181
    complex_photo_130 = importer.save_or_locate(complex_photo_130)

    complex_photo_131.step = complex_step_182
    complex_photo_131 = importer.save_or_locate(complex_photo_131)

    complex_photo_132.step = complex_step_186
    complex_photo_132 = importer.save_or_locate(complex_photo_132)

    complex_photo_133.step = complex_step_187
    complex_photo_133 = importer.save_or_locate(complex_photo_133)

    complex_photo_134.step = complex_step_188
    complex_photo_134 = importer.save_or_locate(complex_photo_134)

    complex_photo_135.step = complex_step_189
    complex_photo_135 = importer.save_or_locate(complex_photo_135)

    complex_photo_136.step = complex_step_190
    complex_photo_136 = importer.save_or_locate(complex_photo_136)

    complex_photo_137.step = complex_step_191
    complex_photo_137 = importer.save_or_locate(complex_photo_137)

    complex_photo_138.step = complex_step_192
    complex_photo_138 = importer.save_or_locate(complex_photo_138)

    complex_photo_139.step = complex_step_196
    complex_photo_139 = importer.save_or_locate(complex_photo_139)

    complex_photo_140.step = complex_step_198
    complex_photo_140 = importer.save_or_locate(complex_photo_140)

    complex_photo_141.step = complex_step_200
    complex_photo_141 = importer.save_or_locate(complex_photo_141)

    complex_photo_142.step = complex_step_201
    complex_photo_142 = importer.save_or_locate(complex_photo_142)

    complex_photo_143.step = complex_step_203
    complex_photo_143 = importer.save_or_locate(complex_photo_143)

    complex_photo_144.step = complex_step_204
    complex_photo_144 = importer.save_or_locate(complex_photo_144)

    complex_photo_145.step = complex_step_205
    complex_photo_145 = importer.save_or_locate(complex_photo_145)

    complex_photo_146.step = complex_step_206
    complex_photo_146 = importer.save_or_locate(complex_photo_146)

    complex_photo_147.step = complex_step_207
    complex_photo_147 = importer.save_or_locate(complex_photo_147)

    complex_photo_148.step = complex_step_208
    complex_photo_148 = importer.save_or_locate(complex_photo_148)

    complex_photo_149.step = complex_step_209
    complex_photo_149 = importer.save_or_locate(complex_photo_149)

    complex_photo_150.step = complex_step_210
    complex_photo_150 = importer.save_or_locate(complex_photo_150)

    complex_photo_151.step = complex_step_211
    complex_photo_151 = importer.save_or_locate(complex_photo_151)

    complex_photo_152.step = complex_step_212
    complex_photo_152 = importer.save_or_locate(complex_photo_152)

    complex_photo_153.step = complex_step_216
    complex_photo_153 = importer.save_or_locate(complex_photo_153)

    complex_photo_154.step = complex_step_219
    complex_photo_154 = importer.save_or_locate(complex_photo_154)

    complex_photo_155.step = complex_step_221
    complex_photo_155 = importer.save_or_locate(complex_photo_155)

    complex_photo_156.step = complex_step_223
    complex_photo_156 = importer.save_or_locate(complex_photo_156)

    complex_photo_157.step = complex_step_226
    complex_photo_157 = importer.save_or_locate(complex_photo_157)

    complex_photo_158.step = complex_step_227
    complex_photo_158 = importer.save_or_locate(complex_photo_158)

    complex_photo_159.step = complex_step_228
    complex_photo_159 = importer.save_or_locate(complex_photo_159)

    complex_photo_160.step = complex_step_229
    complex_photo_160 = importer.save_or_locate(complex_photo_160)

    complex_photo_161.step = complex_step_230
    complex_photo_161 = importer.save_or_locate(complex_photo_161)

    complex_photo_162.step = complex_step_231
    complex_photo_162 = importer.save_or_locate(complex_photo_162)

    complex_photo_163.step = complex_step_232
    complex_photo_163 = importer.save_or_locate(complex_photo_163)

    complex_photo_164.step = complex_step_237
    complex_photo_164 = importer.save_or_locate(complex_photo_164)

    complex_photo_165.step = complex_step_238
    complex_photo_165 = importer.save_or_locate(complex_photo_165)

    complex_photo_166.step = complex_step_239
    complex_photo_166 = importer.save_or_locate(complex_photo_166)

    complex_photo_167.step = complex_step_240
    complex_photo_167 = importer.save_or_locate(complex_photo_167)

    complex_photo_168.step = complex_step_243
    complex_photo_168 = importer.save_or_locate(complex_photo_168)

    complex_photo_169.step = complex_step_244
    complex_photo_169 = importer.save_or_locate(complex_photo_169)

    complex_photo_170.step = complex_step_247
    complex_photo_170 = importer.save_or_locate(complex_photo_170)

    complex_photo_171.step = complex_step_249
    complex_photo_171 = importer.save_or_locate(complex_photo_171)

    complex_photo_172.step = complex_step_253
    complex_photo_172 = importer.save_or_locate(complex_photo_172)

    complex_photo_173.step = complex_step_254
    complex_photo_173 = importer.save_or_locate(complex_photo_173)

    complex_photo_174.step = complex_step_256
    complex_photo_174 = importer.save_or_locate(complex_photo_174)

    complex_photo_175.step = complex_step_257
    complex_photo_175 = importer.save_or_locate(complex_photo_175)

    complex_photo_176.step = complex_step_258
    complex_photo_176 = importer.save_or_locate(complex_photo_176)

    complex_photo_177.step = complex_step_259
    complex_photo_177 = importer.save_or_locate(complex_photo_177)

    complex_photo_178.step = complex_step_269
    complex_photo_178 = importer.save_or_locate(complex_photo_178)

    complex_photo_179.step = complex_step_270
    complex_photo_179 = importer.save_or_locate(complex_photo_179)

    complex_photo_180.step = complex_step_275
    complex_photo_180 = importer.save_or_locate(complex_photo_180)

    complex_photo_181.step = complex_step_276
    complex_photo_181 = importer.save_or_locate(complex_photo_181)

    complex_photo_182.step = complex_step_278
    complex_photo_182 = importer.save_or_locate(complex_photo_182)

    complex_photo_183.step = complex_step_279
    complex_photo_183 = importer.save_or_locate(complex_photo_183)

    complex_photo_184.step = complex_step_281
    complex_photo_184 = importer.save_or_locate(complex_photo_184)

    complex_photo_185.step = complex_step_283
    complex_photo_185 = importer.save_or_locate(complex_photo_185)

    complex_photo_186.step = complex_step_284
    complex_photo_186 = importer.save_or_locate(complex_photo_186)

    complex_photo_187.step = complex_step_288
    complex_photo_187 = importer.save_or_locate(complex_photo_187)

    complex_photo_188.step = complex_step_289
    complex_photo_188 = importer.save_or_locate(complex_photo_188)

    complex_photo_189.step = complex_step_290
    complex_photo_189 = importer.save_or_locate(complex_photo_189)

    complex_photo_190.step = complex_step_292
    complex_photo_190 = importer.save_or_locate(complex_photo_190)

    complex_photo_191.step = complex_step_293
    complex_photo_191 = importer.save_or_locate(complex_photo_191)

    complex_photo_192.step = complex_step_294
    complex_photo_192 = importer.save_or_locate(complex_photo_192)

    complex_photo_193.step = complex_step_299
    complex_photo_193 = importer.save_or_locate(complex_photo_193)

    complex_photo_194.step = complex_step_300
    complex_photo_194 = importer.save_or_locate(complex_photo_194)

    complex_photo_195.step = complex_step_301
    complex_photo_195 = importer.save_or_locate(complex_photo_195)

    complex_photo_196.step = complex_step_303
    complex_photo_196 = importer.save_or_locate(complex_photo_196)

    complex_photo_197.step = complex_step_304
    complex_photo_197 = importer.save_or_locate(complex_photo_197)

    complex_photo_198.step = complex_step_308
    complex_photo_198 = importer.save_or_locate(complex_photo_198)

    complex_photo_199.step = complex_step_309
    complex_photo_199 = importer.save_or_locate(complex_photo_199)

    complex_photo_200.step = complex_step_314
    complex_photo_200 = importer.save_or_locate(complex_photo_200)

    complex_photo_201.step = complex_step_315
    complex_photo_201 = importer.save_or_locate(complex_photo_201)

    complex_photo_202.step = complex_step_317
    complex_photo_202 = importer.save_or_locate(complex_photo_202)

    complex_photo_203.step = complex_step_319
    complex_photo_203 = importer.save_or_locate(complex_photo_203)

    complex_photo_204.step = complex_step_320
    complex_photo_204 = importer.save_or_locate(complex_photo_204)

    complex_photo_205.step = complex_step_321
    complex_photo_205 = importer.save_or_locate(complex_photo_205)

    complex_photo_206.step = complex_step_323
    complex_photo_206 = importer.save_or_locate(complex_photo_206)

    complex_photo_207.step = complex_step_328
    complex_photo_207 = importer.save_or_locate(complex_photo_207)

    complex_photo_208.step = complex_step_329
    complex_photo_208 = importer.save_or_locate(complex_photo_208)

    complex_photo_209.step = complex_step_331
    complex_photo_209 = importer.save_or_locate(complex_photo_209)

    complex_photo_210.step = complex_step_332
    complex_photo_210 = importer.save_or_locate(complex_photo_210)

    complex_photo_211.step = complex_step_337
    complex_photo_211 = importer.save_or_locate(complex_photo_211)

    complex_photo_212.step = complex_step_340
    complex_photo_212 = importer.save_or_locate(complex_photo_212)

    complex_photo_213.step = complex_step_343
    complex_photo_213 = importer.save_or_locate(complex_photo_213)

    complex_photo_214.step = complex_step_344
    complex_photo_214 = importer.save_or_locate(complex_photo_214)

    complex_photo_215.step = complex_step_345
    complex_photo_215 = importer.save_or_locate(complex_photo_215)

    complex_photo_216.step = complex_step_346
    complex_photo_216 = importer.save_or_locate(complex_photo_216)

    complex_photo_217.step = complex_step_347
    complex_photo_217 = importer.save_or_locate(complex_photo_217)

    complex_photo_218.step = complex_step_348
    complex_photo_218 = importer.save_or_locate(complex_photo_218)

    complex_photo_219.step = complex_step_349
    complex_photo_219 = importer.save_or_locate(complex_photo_219)

    complex_photo_220.step = complex_step_350
    complex_photo_220 = importer.save_or_locate(complex_photo_220)

    complex_photo_221.step = complex_step_351
    complex_photo_221 = importer.save_or_locate(complex_photo_221)

    complex_photo_222.step = complex_step_353
    complex_photo_222 = importer.save_or_locate(complex_photo_222)

    complex_photo_223.step = complex_step_354
    complex_photo_223 = importer.save_or_locate(complex_photo_223)

    complex_photo_224.step = complex_step_355
    complex_photo_224 = importer.save_or_locate(complex_photo_224)

    complex_photo_225.step = complex_step_356
    complex_photo_225 = importer.save_or_locate(complex_photo_225)

    complex_photo_226.step = complex_step_357
    complex_photo_226 = importer.save_or_locate(complex_photo_226)

    complex_photo_227.step = complex_step_358
    complex_photo_227 = importer.save_or_locate(complex_photo_227)

    complex_photo_228.step = complex_step_359
    complex_photo_228 = importer.save_or_locate(complex_photo_228)

    complex_photo_229.step = complex_step_360
    complex_photo_229 = importer.save_or_locate(complex_photo_229)

    complex_photo_230.step = complex_step_361
    complex_photo_230 = importer.save_or_locate(complex_photo_230)

    complex_photo_231.step = complex_step_362
    complex_photo_231 = importer.save_or_locate(complex_photo_231)

    complex_photo_232.step = complex_step_363
    complex_photo_232 = importer.save_or_locate(complex_photo_232)

    complex_photo_233.step = complex_step_364
    complex_photo_233 = importer.save_or_locate(complex_photo_233)

    complex_photo_234.step = complex_step_365
    complex_photo_234 = importer.save_or_locate(complex_photo_234)

    complex_photo_235.step = complex_step_366
    complex_photo_235 = importer.save_or_locate(complex_photo_235)

    complex_photo_236.step = complex_step_369
    complex_photo_236 = importer.save_or_locate(complex_photo_236)

    complex_photo_237.step = complex_step_374
    complex_photo_237 = importer.save_or_locate(complex_photo_237)

    complex_photo_238.step = complex_step_379
    complex_photo_238 = importer.save_or_locate(complex_photo_238)

    complex_photo_239.step = complex_step_380
    complex_photo_239 = importer.save_or_locate(complex_photo_239)

    complex_photo_240.step = complex_step_381
    complex_photo_240 = importer.save_or_locate(complex_photo_240)

    complex_photo_241.step = complex_step_382
    complex_photo_241 = importer.save_or_locate(complex_photo_241)

    complex_photo_242.step = complex_step_383
    complex_photo_242 = importer.save_or_locate(complex_photo_242)

    complex_photo_243.step = complex_step_384
    complex_photo_243 = importer.save_or_locate(complex_photo_243)

    complex_photo_244.step = complex_step_387
    complex_photo_244 = importer.save_or_locate(complex_photo_244)

    complex_photo_245.step = complex_step_388
    complex_photo_245 = importer.save_or_locate(complex_photo_245)

    complex_photo_246.step = complex_step_390
    complex_photo_246 = importer.save_or_locate(complex_photo_246)

    complex_photo_247.step = complex_step_391
    complex_photo_247 = importer.save_or_locate(complex_photo_247)

    complex_photo_248.step = complex_step_392
    complex_photo_248 = importer.save_or_locate(complex_photo_248)

    complex_photo_249.step = complex_step_395
    complex_photo_249 = importer.save_or_locate(complex_photo_249)

    complex_photo_250.step = complex_step_396
    complex_photo_250 = importer.save_or_locate(complex_photo_250)

    complex_photo_251.step = complex_step_397
    complex_photo_251 = importer.save_or_locate(complex_photo_251)

    complex_photo_252.step = complex_step_398
    complex_photo_252 = importer.save_or_locate(complex_photo_252)

    complex_photo_253.step = complex_step_399
    complex_photo_253 = importer.save_or_locate(complex_photo_253)

    complex_photo_254.step = complex_step_400
    complex_photo_254 = importer.save_or_locate(complex_photo_254)

    complex_photo_255.step = complex_step_401
    complex_photo_255 = importer.save_or_locate(complex_photo_255)

    complex_photo_256.step = complex_step_402
    complex_photo_256 = importer.save_or_locate(complex_photo_256)

    complex_photo_257.step = complex_step_403
    complex_photo_257 = importer.save_or_locate(complex_photo_257)

    complex_photo_258.step = complex_step_406
    complex_photo_258 = importer.save_or_locate(complex_photo_258)

    complex_photo_259.step = complex_step_410
    complex_photo_259 = importer.save_or_locate(complex_photo_259)

    complex_photo_260.step = complex_step_411
    complex_photo_260 = importer.save_or_locate(complex_photo_260)

    complex_photo_261.step = complex_step_412
    complex_photo_261 = importer.save_or_locate(complex_photo_261)

    complex_photo_262.step = complex_step_413
    complex_photo_262 = importer.save_or_locate(complex_photo_262)

    complex_photo_263.step = complex_step_414
    complex_photo_263 = importer.save_or_locate(complex_photo_263)

    complex_photo_264.step = complex_step_415
    complex_photo_264 = importer.save_or_locate(complex_photo_264)

    complex_photo_265.step = complex_step_416
    complex_photo_265 = importer.save_or_locate(complex_photo_265)

    complex_photo_266.step = complex_step_417
    complex_photo_266 = importer.save_or_locate(complex_photo_266)

    complex_photo_267.step = complex_step_418
    complex_photo_267 = importer.save_or_locate(complex_photo_267)

    complex_photo_268.step = complex_step_419
    complex_photo_268 = importer.save_or_locate(complex_photo_268)

    complex_photo_269.step = complex_step_420
    complex_photo_269 = importer.save_or_locate(complex_photo_269)

    complex_photo_270.step = complex_step_421
    complex_photo_270 = importer.save_or_locate(complex_photo_270)

    complex_photo_271.step = complex_step_422
    complex_photo_271 = importer.save_or_locate(complex_photo_271)

    complex_photo_272.step = complex_step_423
    complex_photo_272 = importer.save_or_locate(complex_photo_272)

    complex_photo_273.step = complex_step_425
    complex_photo_273 = importer.save_or_locate(complex_photo_273)

    complex_photo_274.step = complex_step_426
    complex_photo_274 = importer.save_or_locate(complex_photo_274)

    complex_photo_275.step = complex_step_429
    complex_photo_275 = importer.save_or_locate(complex_photo_275)

    complex_photo_276.step = complex_step_433
    complex_photo_276 = importer.save_or_locate(complex_photo_276)

    complex_photo_277.step = complex_step_438
    complex_photo_277 = importer.save_or_locate(complex_photo_277)

    complex_photo_278.step = complex_step_440
    complex_photo_278 = importer.save_or_locate(complex_photo_278)

    complex_photo_279.step = complex_step_442
    complex_photo_279 = importer.save_or_locate(complex_photo_279)

    complex_photo_280.step = complex_step_443
    complex_photo_280 = importer.save_or_locate(complex_photo_280)

    complex_photo_281.step = complex_step_444
    complex_photo_281 = importer.save_or_locate(complex_photo_281)

    complex_photo_282.step = complex_step_445
    complex_photo_282 = importer.save_or_locate(complex_photo_282)

    complex_photo_283.step = complex_step_447
    complex_photo_283 = importer.save_or_locate(complex_photo_283)

    complex_photo_284.step = complex_step_448
    complex_photo_284 = importer.save_or_locate(complex_photo_284)

    complex_photo_285.step = complex_step_449
    complex_photo_285 = importer.save_or_locate(complex_photo_285)

    complex_photo_286.step = complex_step_450
    complex_photo_286 = importer.save_or_locate(complex_photo_286)

    complex_photo_287.step = complex_step_451
    complex_photo_287 = importer.save_or_locate(complex_photo_287)

    complex_photo_288.step = complex_step_453
    complex_photo_288 = importer.save_or_locate(complex_photo_288)

    complex_photo_289.step = complex_step_455
    complex_photo_289 = importer.save_or_locate(complex_photo_289)

    complex_photo_290.step = complex_step_456
    complex_photo_290 = importer.save_or_locate(complex_photo_290)

    complex_photo_291.step = complex_step_458
    complex_photo_291 = importer.save_or_locate(complex_photo_291)

    complex_photo_292.step = complex_step_459
    complex_photo_292 = importer.save_or_locate(complex_photo_292)

    complex_photo_293.step = complex_step_460
    complex_photo_293 = importer.save_or_locate(complex_photo_293)

    complex_photo_294.step = complex_step_461
    complex_photo_294 = importer.save_or_locate(complex_photo_294)

    complex_photo_295.step = complex_step_462
    complex_photo_295 = importer.save_or_locate(complex_photo_295)

    complex_photo_296.step = complex_step_463
    complex_photo_296 = importer.save_or_locate(complex_photo_296)

    complex_photo_297.step = complex_step_464
    complex_photo_297 = importer.save_or_locate(complex_photo_297)

    complex_photo_298.step = complex_step_467
    complex_photo_298 = importer.save_or_locate(complex_photo_298)

    complex_photo_299.step = complex_step_468
    complex_photo_299 = importer.save_or_locate(complex_photo_299)

    complex_photo_300.step = complex_step_469
    complex_photo_300 = importer.save_or_locate(complex_photo_300)

    complex_photo_301.step = complex_step_470
    complex_photo_301 = importer.save_or_locate(complex_photo_301)

    complex_photo_302.step = complex_step_471
    complex_photo_302 = importer.save_or_locate(complex_photo_302)

    complex_photo_303.step = complex_step_472
    complex_photo_303 = importer.save_or_locate(complex_photo_303)

    complex_photo_304.step = complex_step_473
    complex_photo_304 = importer.save_or_locate(complex_photo_304)

    complex_photo_305.step = complex_step_474
    complex_photo_305 = importer.save_or_locate(complex_photo_305)

    complex_photo_306.step = complex_step_475
    complex_photo_306 = importer.save_or_locate(complex_photo_306)

    complex_photo_307.step = complex_step_476
    complex_photo_307 = importer.save_or_locate(complex_photo_307)

    complex_photo_308.step = complex_step_477
    complex_photo_308 = importer.save_or_locate(complex_photo_308)

    complex_photo_309.step = complex_step_478
    complex_photo_309 = importer.save_or_locate(complex_photo_309)

    complex_photo_310.step = complex_step_479
    complex_photo_310 = importer.save_or_locate(complex_photo_310)

    complex_photo_311.step = complex_step_480
    complex_photo_311 = importer.save_or_locate(complex_photo_311)

    complex_photo_312.step = complex_step_481
    complex_photo_312 = importer.save_or_locate(complex_photo_312)

    complex_photo_313.step = complex_step_482
    complex_photo_313 = importer.save_or_locate(complex_photo_313)

    complex_photo_314.step = complex_step_483
    complex_photo_314 = importer.save_or_locate(complex_photo_314)

    complex_photo_315.step = complex_step_484
    complex_photo_315 = importer.save_or_locate(complex_photo_315)

    complex_photo_316.step = complex_step_485
    complex_photo_316 = importer.save_or_locate(complex_photo_316)

    complex_photo_317.step = complex_step_486
    complex_photo_317 = importer.save_or_locate(complex_photo_317)

    complex_photo_318.step = complex_step_487
    complex_photo_318 = importer.save_or_locate(complex_photo_318)

    complex_photo_319.step = complex_step_488
    complex_photo_319 = importer.save_or_locate(complex_photo_319)

    complex_photo_320.step = complex_step_489
    complex_photo_320 = importer.save_or_locate(complex_photo_320)

    complex_photo_321.step = complex_step_490
    complex_photo_321 = importer.save_or_locate(complex_photo_321)

    complex_photo_322.step = complex_step_491
    complex_photo_322 = importer.save_or_locate(complex_photo_322)

    complex_photo_323.step = complex_step_492
    complex_photo_323 = importer.save_or_locate(complex_photo_323)

    complex_photo_324.step = complex_step_495
    complex_photo_324 = importer.save_or_locate(complex_photo_324)

    complex_photo_325.step = complex_step_496
    complex_photo_325 = importer.save_or_locate(complex_photo_325)

    complex_photo_326.step = complex_step_497
    complex_photo_326 = importer.save_or_locate(complex_photo_326)

    complex_photo_327.step = complex_step_498
    complex_photo_327 = importer.save_or_locate(complex_photo_327)

    complex_photo_328.step = complex_step_499
    complex_photo_328 = importer.save_or_locate(complex_photo_328)

    complex_photo_329.step = complex_step_500
    complex_photo_329 = importer.save_or_locate(complex_photo_329)

    complex_photo_330.step = complex_step_501
    complex_photo_330 = importer.save_or_locate(complex_photo_330)

    complex_photo_331.step = complex_step_502
    complex_photo_331 = importer.save_or_locate(complex_photo_331)

    complex_photo_332.step = complex_step_503
    complex_photo_332 = importer.save_or_locate(complex_photo_332)

    complex_photo_333.step = complex_step_504
    complex_photo_333 = importer.save_or_locate(complex_photo_333)

    complex_photo_334.step = complex_step_505
    complex_photo_334 = importer.save_or_locate(complex_photo_334)

    complex_photo_335.step = complex_step_506
    complex_photo_335 = importer.save_or_locate(complex_photo_335)

    complex_photo_336.step = complex_step_507
    complex_photo_336 = importer.save_or_locate(complex_photo_336)

    complex_photo_337.step = complex_step_508
    complex_photo_337 = importer.save_or_locate(complex_photo_337)

    complex_photo_338.step = complex_step_509
    complex_photo_338 = importer.save_or_locate(complex_photo_338)

    complex_photo_339.step = complex_step_510
    complex_photo_339 = importer.save_or_locate(complex_photo_339)

    complex_photo_340.step = complex_step_511
    complex_photo_340 = importer.save_or_locate(complex_photo_340)

    complex_photo_341.step = complex_step_512
    complex_photo_341 = importer.save_or_locate(complex_photo_341)

    complex_photo_342.step = complex_step_513
    complex_photo_342 = importer.save_or_locate(complex_photo_342)

    complex_photo_343.step = complex_step_514
    complex_photo_343 = importer.save_or_locate(complex_photo_343)

    complex_photo_344.step = complex_step_515
    complex_photo_344 = importer.save_or_locate(complex_photo_344)

    complex_photo_345.step = complex_step_517
    complex_photo_345 = importer.save_or_locate(complex_photo_345)

    complex_photo_346.step = complex_step_518
    complex_photo_346 = importer.save_or_locate(complex_photo_346)

    complex_photo_347.step = complex_step_519
    complex_photo_347 = importer.save_or_locate(complex_photo_347)

    complex_photo_348.step = complex_step_520
    complex_photo_348 = importer.save_or_locate(complex_photo_348)

    complex_photo_349.step = complex_step_521
    complex_photo_349 = importer.save_or_locate(complex_photo_349)

    complex_photo_350.step = complex_step_522
    complex_photo_350 = importer.save_or_locate(complex_photo_350)

    complex_photo_351.step = complex_step_523
    complex_photo_351 = importer.save_or_locate(complex_photo_351)

    complex_photo_352.step = complex_step_524
    complex_photo_352 = importer.save_or_locate(complex_photo_352)

    complex_photo_353.step = complex_step_525
    complex_photo_353 = importer.save_or_locate(complex_photo_353)

    # Re-processing model: complex.models.Tweet

    complex_tweet_1.step = complex_step_1
    complex_tweet_1 = importer.save_or_locate(complex_tweet_1)

    complex_tweet_2.step = complex_step_2
    complex_tweet_2 = importer.save_or_locate(complex_tweet_2)

    complex_tweet_3.step = complex_step_3
    complex_tweet_3 = importer.save_or_locate(complex_tweet_3)

    complex_tweet_4.step = complex_step_4
    complex_tweet_4 = importer.save_or_locate(complex_tweet_4)

    complex_tweet_5.step = complex_step_13
    complex_tweet_5 = importer.save_or_locate(complex_tweet_5)

    complex_tweet_6.step = complex_step_14
    complex_tweet_6 = importer.save_or_locate(complex_tweet_6)

    complex_tweet_7.step = complex_step_17
    complex_tweet_7 = importer.save_or_locate(complex_tweet_7)

    complex_tweet_8.step = complex_step_20
    complex_tweet_8 = importer.save_or_locate(complex_tweet_8)

    complex_tweet_9.step = complex_step_26
    complex_tweet_9 = importer.save_or_locate(complex_tweet_9)

    complex_tweet_10.step = complex_step_38
    complex_tweet_10 = importer.save_or_locate(complex_tweet_10)

    complex_tweet_11.step = complex_step_39
    complex_tweet_11 = importer.save_or_locate(complex_tweet_11)

    complex_tweet_12.step = complex_step_40
    complex_tweet_12 = importer.save_or_locate(complex_tweet_12)

    complex_tweet_13.step = complex_step_41
    complex_tweet_13 = importer.save_or_locate(complex_tweet_13)

    complex_tweet_14.step = complex_step_44
    complex_tweet_14 = importer.save_or_locate(complex_tweet_14)

    complex_tweet_15.step = complex_step_49
    complex_tweet_15 = importer.save_or_locate(complex_tweet_15)

    complex_tweet_16.step = complex_step_50
    complex_tweet_16 = importer.save_or_locate(complex_tweet_16)

    complex_tweet_17.step = complex_step_51
    complex_tweet_17 = importer.save_or_locate(complex_tweet_17)

    complex_tweet_18.step = complex_step_65
    complex_tweet_18 = importer.save_or_locate(complex_tweet_18)

    complex_tweet_19.step = complex_step_72
    complex_tweet_19 = importer.save_or_locate(complex_tweet_19)

    complex_tweet_20.step = complex_step_84
    complex_tweet_20 = importer.save_or_locate(complex_tweet_20)

    complex_tweet_21.step = complex_step_88
    complex_tweet_21 = importer.save_or_locate(complex_tweet_21)

    complex_tweet_22.step = complex_step_90
    complex_tweet_22 = importer.save_or_locate(complex_tweet_22)

    complex_tweet_23.step = complex_step_94
    complex_tweet_23 = importer.save_or_locate(complex_tweet_23)

    complex_tweet_24.step = complex_step_98
    complex_tweet_24 = importer.save_or_locate(complex_tweet_24)

    complex_tweet_25.step = complex_step_100
    complex_tweet_25 = importer.save_or_locate(complex_tweet_25)

    complex_tweet_26.step = complex_step_101
    complex_tweet_26 = importer.save_or_locate(complex_tweet_26)

    complex_tweet_27.step = complex_step_107
    complex_tweet_27 = importer.save_or_locate(complex_tweet_27)

    complex_tweet_28.step = complex_step_108
    complex_tweet_28 = importer.save_or_locate(complex_tweet_28)

    complex_tweet_29.step = complex_step_113
    complex_tweet_29 = importer.save_or_locate(complex_tweet_29)

    complex_tweet_30.step = complex_step_128
    complex_tweet_30 = importer.save_or_locate(complex_tweet_30)

    complex_tweet_31.step = complex_step_136
    complex_tweet_31 = importer.save_or_locate(complex_tweet_31)

    complex_tweet_32.step = complex_step_139
    complex_tweet_32 = importer.save_or_locate(complex_tweet_32)

    complex_tweet_33.step = complex_step_156
    complex_tweet_33 = importer.save_or_locate(complex_tweet_33)

    complex_tweet_34.step = complex_step_169
    complex_tweet_34 = importer.save_or_locate(complex_tweet_34)

    complex_tweet_35.step = complex_step_172
    complex_tweet_35 = importer.save_or_locate(complex_tweet_35)

    complex_tweet_36.step = complex_step_183
    complex_tweet_36 = importer.save_or_locate(complex_tweet_36)

    complex_tweet_37.step = complex_step_184
    complex_tweet_37 = importer.save_or_locate(complex_tweet_37)

    complex_tweet_38.step = complex_step_185
    complex_tweet_38 = importer.save_or_locate(complex_tweet_38)

    complex_tweet_39.step = complex_step_193
    complex_tweet_39 = importer.save_or_locate(complex_tweet_39)

    complex_tweet_40.step = complex_step_194
    complex_tweet_40 = importer.save_or_locate(complex_tweet_40)

    complex_tweet_41.step = complex_step_195
    complex_tweet_41 = importer.save_or_locate(complex_tweet_41)

    complex_tweet_42.step = complex_step_197
    complex_tweet_42 = importer.save_or_locate(complex_tweet_42)

    complex_tweet_43.step = complex_step_199
    complex_tweet_43 = importer.save_or_locate(complex_tweet_43)

    complex_tweet_44.step = complex_step_202
    complex_tweet_44 = importer.save_or_locate(complex_tweet_44)

    complex_tweet_45.step = complex_step_213
    complex_tweet_45 = importer.save_or_locate(complex_tweet_45)

    complex_tweet_46.step = complex_step_214
    complex_tweet_46 = importer.save_or_locate(complex_tweet_46)

    complex_tweet_47.step = complex_step_215
    complex_tweet_47 = importer.save_or_locate(complex_tweet_47)

    complex_tweet_48.step = complex_step_217
    complex_tweet_48 = importer.save_or_locate(complex_tweet_48)

    complex_tweet_49.step = complex_step_218
    complex_tweet_49 = importer.save_or_locate(complex_tweet_49)

    complex_tweet_50.step = complex_step_220
    complex_tweet_50 = importer.save_or_locate(complex_tweet_50)

    complex_tweet_51.step = complex_step_222
    complex_tweet_51 = importer.save_or_locate(complex_tweet_51)

    complex_tweet_52.step = complex_step_224
    complex_tweet_52 = importer.save_or_locate(complex_tweet_52)

    complex_tweet_53.step = complex_step_225
    complex_tweet_53 = importer.save_or_locate(complex_tweet_53)

    complex_tweet_54.step = complex_step_242
    complex_tweet_54 = importer.save_or_locate(complex_tweet_54)

    complex_tweet_55.step = complex_step_245
    complex_tweet_55 = importer.save_or_locate(complex_tweet_55)

    complex_tweet_56.step = complex_step_246
    complex_tweet_56 = importer.save_or_locate(complex_tweet_56)

    complex_tweet_57.step = complex_step_260
    complex_tweet_57 = importer.save_or_locate(complex_tweet_57)

    complex_tweet_58.step = complex_step_261
    complex_tweet_58 = importer.save_or_locate(complex_tweet_58)

    complex_tweet_59.step = complex_step_262
    complex_tweet_59 = importer.save_or_locate(complex_tweet_59)

    complex_tweet_60.step = complex_step_263
    complex_tweet_60 = importer.save_or_locate(complex_tweet_60)

    complex_tweet_61.step = complex_step_264
    complex_tweet_61 = importer.save_or_locate(complex_tweet_61)

    complex_tweet_62.step = complex_step_265
    complex_tweet_62 = importer.save_or_locate(complex_tweet_62)

    complex_tweet_63.step = complex_step_266
    complex_tweet_63 = importer.save_or_locate(complex_tweet_63)

    complex_tweet_64.step = complex_step_267
    complex_tweet_64 = importer.save_or_locate(complex_tweet_64)

    complex_tweet_65.step = complex_step_268
    complex_tweet_65 = importer.save_or_locate(complex_tweet_65)

    complex_tweet_66.step = complex_step_271
    complex_tweet_66 = importer.save_or_locate(complex_tweet_66)

    complex_tweet_67.step = complex_step_272
    complex_tweet_67 = importer.save_or_locate(complex_tweet_67)

    complex_tweet_68.step = complex_step_273
    complex_tweet_68 = importer.save_or_locate(complex_tweet_68)

    complex_tweet_69.step = complex_step_274
    complex_tweet_69 = importer.save_or_locate(complex_tweet_69)

    complex_tweet_70.step = complex_step_277
    complex_tweet_70 = importer.save_or_locate(complex_tweet_70)

    complex_tweet_71.step = complex_step_280
    complex_tweet_71 = importer.save_or_locate(complex_tweet_71)

    complex_tweet_72.step = complex_step_282
    complex_tweet_72 = importer.save_or_locate(complex_tweet_72)

    complex_tweet_73.step = complex_step_285
    complex_tweet_73 = importer.save_or_locate(complex_tweet_73)

    complex_tweet_74.step = complex_step_286
    complex_tweet_74 = importer.save_or_locate(complex_tweet_74)

    complex_tweet_75.step = complex_step_287
    complex_tweet_75 = importer.save_or_locate(complex_tweet_75)

    complex_tweet_76.step = complex_step_291
    complex_tweet_76 = importer.save_or_locate(complex_tweet_76)

    complex_tweet_77.step = complex_step_297
    complex_tweet_77 = importer.save_or_locate(complex_tweet_77)

    complex_tweet_78.step = complex_step_302
    complex_tweet_78 = importer.save_or_locate(complex_tweet_78)

    complex_tweet_79.step = complex_step_307
    complex_tweet_79 = importer.save_or_locate(complex_tweet_79)

    complex_tweet_80.step = complex_step_313
    complex_tweet_80 = importer.save_or_locate(complex_tweet_80)

    complex_tweet_81.step = complex_step_325
    complex_tweet_81 = importer.save_or_locate(complex_tweet_81)

    complex_tweet_82.step = complex_step_326
    complex_tweet_82 = importer.save_or_locate(complex_tweet_82)

    complex_tweet_83.step = complex_step_327
    complex_tweet_83 = importer.save_or_locate(complex_tweet_83)

    complex_tweet_84.step = complex_step_330
    complex_tweet_84 = importer.save_or_locate(complex_tweet_84)

    complex_tweet_85.step = complex_step_338
    complex_tweet_85 = importer.save_or_locate(complex_tweet_85)

    complex_tweet_86.step = complex_step_339
    complex_tweet_86 = importer.save_or_locate(complex_tweet_86)

    complex_tweet_87.step = complex_step_342
    complex_tweet_87 = importer.save_or_locate(complex_tweet_87)

    complex_tweet_88.step = complex_step_352
    complex_tweet_88 = importer.save_or_locate(complex_tweet_88)

    complex_tweet_89.step = complex_step_367
    complex_tweet_89 = importer.save_or_locate(complex_tweet_89)

    complex_tweet_90.step = complex_step_368
    complex_tweet_90 = importer.save_or_locate(complex_tweet_90)

    complex_tweet_91.step = complex_step_370
    complex_tweet_91 = importer.save_or_locate(complex_tweet_91)

    complex_tweet_92.step = complex_step_371
    complex_tweet_92 = importer.save_or_locate(complex_tweet_92)

    complex_tweet_93.step = complex_step_372
    complex_tweet_93 = importer.save_or_locate(complex_tweet_93)

    complex_tweet_94.step = complex_step_373
    complex_tweet_94 = importer.save_or_locate(complex_tweet_94)

    complex_tweet_95.step = complex_step_385
    complex_tweet_95 = importer.save_or_locate(complex_tweet_95)

    complex_tweet_96.step = complex_step_389
    complex_tweet_96 = importer.save_or_locate(complex_tweet_96)

    complex_tweet_97.step = complex_step_393
    complex_tweet_97 = importer.save_or_locate(complex_tweet_97)

    complex_tweet_98.step = complex_step_407
    complex_tweet_98 = importer.save_or_locate(complex_tweet_98)

    complex_tweet_99.step = complex_step_408
    complex_tweet_99 = importer.save_or_locate(complex_tweet_99)

    complex_tweet_100.step = complex_step_409
    complex_tweet_100 = importer.save_or_locate(complex_tweet_100)

    complex_tweet_101.step = complex_step_427
    complex_tweet_101 = importer.save_or_locate(complex_tweet_101)

    complex_tweet_102.step = complex_step_428
    complex_tweet_102 = importer.save_or_locate(complex_tweet_102)

    complex_tweet_103.step = complex_step_437
    complex_tweet_103 = importer.save_or_locate(complex_tweet_103)

    complex_tweet_104.step = complex_step_441
    complex_tweet_104 = importer.save_or_locate(complex_tweet_104)

    complex_tweet_105.step = complex_step_446
    complex_tweet_105 = importer.save_or_locate(complex_tweet_105)

    complex_tweet_106.step = complex_step_452
    complex_tweet_106 = importer.save_or_locate(complex_tweet_106)

    complex_tweet_107.step = complex_step_454
    complex_tweet_107 = importer.save_or_locate(complex_tweet_107)

    complex_tweet_108.step = complex_step_457
    complex_tweet_108 = importer.save_or_locate(complex_tweet_108)

    # Re-processing model: complex.models.Web_comic

    # Re-processing model: complex.models.Fragment

    # Re-processing model: complex.models.Story

    complex_story_1.camera_center_place = complex_place_110
    complex_story_1 = importer.save_or_locate(complex_story_1)

    complex_story_2.camera_center_place = complex_place_103
    complex_story_2 = importer.save_or_locate(complex_story_2)

    complex_story_3.camera_center_place = complex_place_124
    complex_story_3 = importer.save_or_locate(complex_story_3)

    complex_story_4.camera_center_place = complex_place_400
    complex_story_4 = importer.save_or_locate(complex_story_4)

    complex_story_5.camera_center_place = complex_place_350
    complex_story_5 = importer.save_or_locate(complex_story_5)

    complex_story_6.camera_center_place = complex_place_151
    complex_story_6 = importer.save_or_locate(complex_story_6)

    complex_story_7.camera_center_place = complex_place_90
    complex_story_7 = importer.save_or_locate(complex_story_7)

    complex_story_8.camera_center_place = complex_place_386
    complex_story_8 = importer.save_or_locate(complex_story_8)

    complex_story_9.camera_center_place = complex_place_419
    complex_story_9 = importer.save_or_locate(complex_story_9)

    complex_story_10.camera_center_place = complex_place_411
    complex_story_10 = importer.save_or_locate(complex_story_10)

    complex_story_11.camera_center_place = complex_place_63
    complex_story_11 = importer.save_or_locate(complex_story_11)

    complex_story_12.camera_center_place = complex_place_479
    complex_story_12 = importer.save_or_locate(complex_story_12)

    complex_story_13.camera_center_place = complex_place_82
    complex_story_13 = importer.save_or_locate(complex_story_13)

    complex_story_14.camera_center_place = complex_place_330
    complex_story_14 = importer.save_or_locate(complex_story_14)

    complex_story_15.camera_center_place = complex_place_330
    complex_story_15 = importer.save_or_locate(complex_story_15)

    complex_story_16.camera_center_place = complex_place_218
    complex_story_16 = importer.save_or_locate(complex_story_16)

    complex_story_17.camera_center_place = complex_place_286
    complex_story_17 = importer.save_or_locate(complex_story_17)

    complex_story_18.camera_center_place = complex_place_169
    complex_story_18 = importer.save_or_locate(complex_story_18)

    complex_story_19.camera_center_place = complex_place_169
    complex_story_19 = importer.save_or_locate(complex_story_19)

    complex_story_20.camera_center_place = complex_place_482
    complex_story_20 = importer.save_or_locate(complex_story_20)

    complex_story_21.camera_center_place = complex_place_482
    complex_story_21 = importer.save_or_locate(complex_story_21)

    complex_story_22.camera_center_place = complex_place_238
    complex_story_22 = importer.save_or_locate(complex_story_22)

    complex_story_23.camera_center_place = complex_place_238
    complex_story_23 = importer.save_or_locate(complex_story_23)

    complex_story_24.camera_center_place = complex_place_171
    complex_story_24 = importer.save_or_locate(complex_story_24)

    complex_story_25.camera_center_place = complex_place_498
    complex_story_25 = importer.save_or_locate(complex_story_25)

    complex_story_26.camera_center_place = complex_place_495
    complex_story_26 = importer.save_or_locate(complex_story_26)

    complex_story_27.camera_center_place = complex_place_32
    complex_story_27 = importer.save_or_locate(complex_story_27)

    complex_story_28.camera_center_place = complex_place_32
    complex_story_28 = importer.save_or_locate(complex_story_28)

    complex_story_29.camera_center_place = complex_place_7
    complex_story_29 = importer.save_or_locate(complex_story_29)

    complex_story_30.camera_center_place = complex_place_10
    complex_story_30 = importer.save_or_locate(complex_story_30)

    complex_story_31.camera_center_place = complex_place_361
    complex_story_31 = importer.save_or_locate(complex_story_31)

    complex_story_32.camera_center_place = complex_place_273
    complex_story_32 = importer.save_or_locate(complex_story_32)

    complex_story_33.camera_center_place = complex_place_537
    complex_story_33 = importer.save_or_locate(complex_story_33)

    complex_story_34.camera_center_place = complex_place_470
    complex_story_34 = importer.save_or_locate(complex_story_34)

    complex_story_35.camera_center_place = complex_place_470
    complex_story_35 = importer.save_or_locate(complex_story_35)

    complex_story_36.camera_center_place = complex_place_444
    complex_story_36 = importer.save_or_locate(complex_story_36)

    complex_story_37.camera_center_place = complex_place_190
    complex_story_37 = importer.save_or_locate(complex_story_37)

    complex_story_38.camera_center_place = complex_place_179
    complex_story_38 = importer.save_or_locate(complex_story_38)

    # Re-processing model: complex.models.Route























































    # Re-processing model: complex.models.Venue




































































































    # Re-processing model: complex.models.Place

    # Re-processing model: complex.models.Step

