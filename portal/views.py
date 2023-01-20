from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    template_name = "./dashboard.html"
    return render(request, template_name)


@login_required
def report(request):
    template_name = "./report.html"
    return render(request, template_name)

@login_required
def allcases(request):
    template_name = "./allcases.html"
    return render(request, template_name)

@login_required
def closedcases(request):
    template_name = "./closedcases.html"
    return render(request, template_name)