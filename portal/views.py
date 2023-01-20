from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Category, Case

@login_required
def dashboard(request):
    template_name = "./dashboard.html"
    total = Case.objects.filter(user=request.user)
    active = total.filter(closed=False)
    resolved = total.filter(closed=True)
    # pending = total.filter(status="p")

    context = {
        "active":active.count(),
        "resolved":resolved.count(),
        "pending": active.count(),
        "total": total.count(),
        "latest": total.order_by("-pk")[:10],
    }
    return render(request, template_name, context)


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