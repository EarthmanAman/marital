from django.contrib import admin

from . models import Category, Case, Media

admin.site.register(Category)
admin.site.register(Case)
admin.site.register(Media)

