# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path("", include("complex.urls")),
    path(
        "admin_password_reset/",
        auth_views.PasswordResetView.as_view(),
        name="admin_password_reset",
    ),
    path(
        "admin_password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
