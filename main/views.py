from django.shortcuts import render, redirect
import uuid
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from . models import Case, Category, Media
from accounts.models import AdminPost, CustomUser

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
    admin_posts = AdminPost.objects.all()

    # Information to be passed to the frontend
    context = {
        "active":active.count(),
        "resolved":resolved.count(),
        "pending": active.count(),
        "total": total.count(),
        "latest": total.order_by("-pk")[:10],
        "categories": categories,
        "admin_posts":admin_posts,
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
            admin_post = request.POST.get("admin_post")

            # Creating a case
            admin_post = AdminPost.objects.get(id=int(admin_post))

            # Get the first 7 characters of UUID - Case code
            uuid_str = str(uuid.uuid4())[:7]
            incident = Case.objects.create(admin_post=admin_post, uuid=uuid_str, category=category.last(), address=address, description=message)
            
            # Attach case files
            for file in files:
                media = Media.objects.create(file=file, case=incident)

            # Update information passed to frontend
            context["active"] += 1
            context["total"] += 1
            context["pending"] += 1
            context["success"] = True
            context["uuid"] = uuid_str

            # Fetching all admin in the nearest admin post
            users = CustomUser.objects.filter(admin_post=admin_post)
            email_list = []

            #Adding their emails into a list
            for user in users:
                email_list.append(user.email)

            if len(email_list) > 0:

                #Formulating an email and sending it
                current_site = get_current_site(request)
                domain = current_site.domain
                url = f"http://{domain}/users/portal/casedetails/{incident.id}"
                subject = f"CASE {incident.id} - {incident.category.name} : SUBMITTED"
                message = f"\nDear Admin\n\nA case has been registered in your jurisdiction. Kindly log into the system and take the necessary actions\n\nFollow link below to view the case\n\n{url}\n\nThank you,\nKind Regards."
                send_mail(
                    subject= subject,
                    from_email="hashimathman.info@gmail.com",
                    message=message,
                    recipient_list=email_list,
                    fail_silently=False,
                )
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