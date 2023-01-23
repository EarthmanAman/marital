from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Case(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    closed = models.BooleanField(default=False)
    address = models.CharField(max_length=100, blank=True, null=True)

    action = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.description

class Media(models.Model):
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='images/')

    def __str__(self):
        return self.case.description

