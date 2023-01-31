
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "MyPlan Admin Site"
admin.site.site_title = "MyPlan Admin"
admin.site.index_title = "Welcome to Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include("main.urls", namespace="main")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("users/portal/", include("portal.urls", namespace="portal")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
