from django.shortcuts import render, redirect
from . models import Case, Category, Media

def index(request):
    template_name = "./index.html"
    total = Case.objects.filter()
    active = total.filter(closed=False)
    resolved = total.filter(closed=True)
    # pending = total.filter(status="p")
    categories = Category.objects.all()

    context = {
        "active":active.count(),
        "resolved":resolved.count(),
        "pending": active.count(),
        "total": total.count(),
        "latest": total.order_by("-pk")[:10],
        "categories": categories
    }

    if request.method == "POST":
        category = request.POST.get("category")
        category = categories.filter(name=category)
        
        if category.exists():
            address = request.POST.get("address")
            message = request.POST.get("message")
            files = request.FILES.getlist("files")
            incident = Case.objects.create(category=category.last(), address=address, description=message, media=files)
            for file in files:
                media = Media.objects.create(file=file, case=incident)

            context["active"] += 1
            context["total"] += 1
            context["pending"] += 1

    return render(request, template_name, context)
