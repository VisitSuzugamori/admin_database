from django.urls import path

from . import views

app_name = "complex"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<page>", views.PageView.as_view(), name="page"),
]
