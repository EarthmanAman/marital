from django.urls import path

from . views import dashboard, report, allcases, closedcases, casedetails, unresolved

app_name = "portal"

urlpatterns = [
    path('dashboard', dashboard, name="dashboard"),
    path('report', report, name="report"),
    path('allcases', allcases, name="allcases"),
    path('closedcases', closedcases, name="closedcases"),
    path('casedetails/<int:case_id>', casedetails, name="casedetails"),
    path('unresolved/<int:case_id>', unresolved, name="unresolved"),
]