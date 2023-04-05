from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import Category, Case, Media

# A decorator to allow only logged in user to access the view
@login_required
def dashboard(request):

    # template
    template_name = "./dashboard.html"

    # If user is admin fetch all cases else fetch cases only for the particular user
    if request.user.is_superuser or request.user.is_staff:
        # Fetch all cases
        total = Case.objects.all()
    else:
        # Filter cases by user
        total = Case.objects.filter(user=request.user)
    
    # Filter active cases
    active = total.filter(closed=False)

    #Filter closed cases
    resolved = total.filter(closed=True)
    # pending = total.filter(status="p")

    # Information to be passed to the frontend
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

    # If user is admin fetch all cases else fetch cases only for the particular user
    if request.user.is_superuser:
        total = Case.objects.all()
    else:
        total = Case.objects.filter(user=request.user)
    
    # Filter active cases
    active = total.filter(closed=False)

    #Filter closed cases
    resolved = total.filter(closed=True)

    # Information to be passed to the frontend
    context = {
        "active":active.count(),
        "resolved":resolved.count(),
        "pending": active.count(),
        "total": total.count(),
        "categories": Category.objects.all(),
        "msg": False
    }

    # If a user report a case else just render the report page
    if request.method == "POST":
        category = request.POST.get("category")
        message = request.POST.get("message")
        address = request.POST.get("address")
        files = request.FILES.getlist("files")
        user = request.user
        categories = Category.objects.filter(name=category)
        if categories.exists():
            case = Case.objects.create(user=user, address=address, category=categories.last(), description=message)
            for file in files:
                media = Media.objects.create(file=file, case=case)
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
def update_case(request, case_id):
    template_name = "./update_case.html"

    # If user is admin fetch all cases else fetch cases only for the particular user
    if request.user.is_superuser:
        total = Case.objects.all()
    else:
        total = Case.objects.filter(user=request.user)
    
    # Filter active cases
    active = total.filter(closed=False)
    case = Case.objects.get(id=case_id)
    #Filter closed cases
    resolved = total.filter(closed=True)

    # Information to be passed to the frontend
    context = {
        "active":active.count(),
        "resolved":resolved.count(),
        "pending": active.count(),
        "total": total.count(),
        "categories": Category.objects.all(),
        "case": case,
        "msg": False
    }

    # If a user report a case else just render the report page
    if request.method == "POST":
        category = request.POST.get("category")
        message = request.POST.get("message")
        address = request.POST.get("address")
        files = request.FILES.getlist("files")
        categories = Category.objects.filter(name=category)
        if categories.exists():
            case.category = categories.last()
            case.description = message
            case.address = address
            case.save()
            for file in files:
                media = Media.objects.create(file=file, case=case)
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

    # Fetching all cases ordering from latest to oldest
    cases = Case.objects.all().order_by("-pk")
    context = {
        "cases":cases
    }
    return render(request, template_name, context)

@login_required
def closedcases(request):
    template_name = "./closedcases.html"

    # If user is admin fetch all closed cases else fetch closed cases only for the particular user
    if request.user.is_superuser:
        cases = Case.objects.all().filter(closed=True)
    else:
        cases = Case.objects.filter(user=request.user).filter(closed=True)
    context = {
        "cases":cases
    }
    return render(request, template_name, context)

@login_required
def casedetails(request, case_id):
    template_name = "./casedetails.html"

    # Fetch a specific case
    case = Case.objects.get(pk=int(case_id))

    # Updating the status
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

    # Getting a specific case
    case = Case.objects.get(id=case_id)

    #unresolve the case
    case.closed = False
    case.action = None
    case.save()

    # redirect to case details 
    return redirect("portal:casedetails", case_id=case.id)