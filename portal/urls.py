from django.urls import path

from . views import dashboard, report, allcases

app_name = "portal"

urlpatterns = [
    path('dashboard', dashboard, name="dashboard"),
    path('report', report, name="report"),
    path('allcases', allcases, name="allcases"),
]