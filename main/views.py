from django.shortcuts import render, redirect
import uuid
from . models import Case, Category, Media

def index(request):
    """
    index view.
    It accept an http request as a parameter and renders the ./admin_login.html
    """

    # Template
    template_name = "./index.html"

    # Fetch all cases from the database
    total = Case.objects.all()

    # Filtering cases which are still active from the list of all cases
    active = total.filter(closed=False)

    # Filtering cases which are closed from the list of all cases
    resolved = total.filter(closed=True)
    
    # Fetching all categories from database to be used during reporting
    categories = Category.objects.all()

    # Information to be passed to the frontend
    context = {
        "active":active.count(),
        "resolved":resolved.count(),
        "pending": active.count(),
        "total": total.count(),
        "latest": total.order_by("-pk")[:10],
        "categories": categories,
        "success": False,
        "error": False,
        "uuid": None,
    }

    # If user post a incident handle it else display the home page
    if request.method == "POST":
        category = request.POST.get("category")

        # Check if the user passed category exist
        category = categories.filter(name=category)
        
        # If it exist continue creation of case else stop
        if category.exists():
            address = request.POST.get("address")
            message = request.POST.get("message")
            files = request.FILES.getlist("files")

            # Creating a case
            uuid_str = str(uuid.uuid4())[:7]
            incident = Case.objects.create(uuid=uuid_str, category=category.last(), address=address, description=message, media=files)
            
            # Attach case files
            for file in files:
                media = Media.objects.create(file=file, case=incident)

            # Update information passed to frontend
            context["active"] += 1
            context["total"] += 1
            context["pending"] += 1
            context["success"] = True
            context["uuid"] = uuid_str
        else:
            context["error"] = True

    return render(request, template_name, context)


def track_case(request):
    template_name = "./track.html"
    context = {
        "case": None,
        "uuid": "",
        "error": None,
    }

    if request.method == "POST":
        code = request.POST.get("code", None)
        if code != None:
            case = Case.objects.filter(uuid=code)
            if case.exists():
                context["case"] = case.last()
            else:
                context["error"] = True            
        context["uuid"] = code            

    return render(request, template_name, context)