# from django.contrib.admin.sites import AdminSite
from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    site_header = "「VSDB」コンテンツ管理用サイト"
    site_title = "「VSDB」プロジェクト"
    index_title = "ホーム"
