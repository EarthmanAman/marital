
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include("main.urls", namespace="main")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("users/portal/", include("portal.urls", namespace="portal")),
]
