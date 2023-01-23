from django.shortcuts import render, redirect
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
    total = Case.objects.filter(user=request.user)
    active = total.filter(closed=False)
    resolved = total.filter(closed=True)
    # pending = total.filter(status="p")

    context = {
        "active":active.count(),
        "resolved":resolved.count(),
        "pending": active.count(),
        "total": total.count(),
        "categories": Category.objects.all(),
        "msg": False
    }
    if request.method == "POST":
        category = request.POST.get("category")
        message = request.POST.get("message")
        address = request.POST.get("address")
        user = request.user
        categories = Category.objects.filter(name=category)
        if categories.exists():
            case = Case.objects.create(user=user, address=address, category=categories.last(), description=message)
            context["active"] += 1
            context["total"] += 1
            context["success"] = True
        else:
            context["success"] = False
            context["error"] = "Please select category"
        context["msg"] = True
        return render(request, template_name, context)
    return render(request, template_name, context)

@login_required
def allcases(request):
    template_name = "./allcases.html"
    cases = Case.objects.filter(user=request.user).order_by("-pk")
    context = {
        "cases":cases
    }
    return render(request, template_name, context)

@login_required
def closedcases(request):
    template_name = "./closedcases.html"
    cases = Case.objects.filter(user=request.user).filter(closed=True)
    context = {
        "cases":cases
    }
    return render(request, template_name, context)

@login_required
def casedetails(request, case_id):
    template_name = "./casedetails.html"
    case = Case.objects.get(pk=int(case_id))
    if request.method == "POST":
        case.action = request.POST.get("action")
        case.closed = True
        case.save()
    context = {
        "case":case
    }
    return render(request, template_name, context)

@login_required
def unresolved(request, case_id):
    case = Case.objects.get(id=case_id)
    case.closed = False
    case.action = None
    case.save()
    return redirect("portal:casedetails", case_id=case.id)