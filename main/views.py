from django.shortcuts import render
from . models import Case, Category

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
    return render(request, template_name, context)
