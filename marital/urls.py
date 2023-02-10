
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Customizing the djanfo admin portal
admin.site.site_header = "MyPlan Admin Site"
admin.site.site_title = "MyPlan Admin"
admin.site.index_title = "Welcome to Admin Panel"

# Main urls
urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include("main.urls", namespace="main")), # To main app urls
    path("accounts/", include("accounts.urls", namespace="accounts")), # To account app urls
    path("users/portal/", include("portal.urls", namespace="portal")), # To portal app urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Linking static and media files
