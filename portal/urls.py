from django.urls import path

from . views import dashboard, report, allcases, closedcases, casedetails, unresolved, update_case

app_name = "portal"

urlpatterns = [
    # dashboard url it calls the dashboard view
    # http://127.0.0.1:8000/portal/dashboard
    path('dashboard', dashboard, name="dashboard"),

    # report url it calls the report view
    # http://127.0.0.1:8000/portal/report
    path('report', report, name="report"),

    # report url it calls the update case view
    # http://127.0.0.1:8000/portal/report
    path('update/<int:case_id>/', update_case, name="update_case"),
    # allcases url it calls the allcases view
    # http://127.0.0.1:8000/portal/allcases
    path('allcases', allcases, name="allcases"),

    # closedcases url it calls the dashboard view
    # http://127.0.0.1:8000/portal/closedcases
    path('closedcases', closedcases, name="closedcases"),

    # casedetails url it calls the casedetails view
    # http://127.0.0.1:8000/portal/casedetails/1
    path('casedetails/<int:case_id>', casedetails, name="casedetails"),

    # unresolved url it calls the unresolved view
    # http://127.0.0.1:8000/portal/unresolved/1
    path('unresolved/<int:case_id>', unresolved, name="unresolved"),
]