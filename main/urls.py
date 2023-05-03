
from django.urls import path

# Importing views
from . views import index, track_case

app_name = "main"

urlpatterns = [

    # Url to homepage calls the index view
    # http://127.0.0.1:8000
    path('', index, name="index"),
    path('track', track_case, name="track_case"),
]
