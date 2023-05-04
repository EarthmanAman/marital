from django.contrib import admin
from . models import CustomUser, AdminPost
# Register your models here.

admin.site.register(AdminPost)
admin.site.register(CustomUser)
