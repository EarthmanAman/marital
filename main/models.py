from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Category(models.Model):

    """
    A model to map the category table in database

    Attributes:
        name = str
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Case(models.Model):
    """
    A model to map the Case table in database

    Attributes:
        user = ForeignKey (user who reported the incident)
        category = foreignkey (the category the case belongs)
        date = date
        description = str
        closed = bool
        address = str
        action = str
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    uuid     = models.CharField(max_length=10, null=True)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    closed = models.BooleanField(default=False)
    address = models.CharField(max_length=100, blank=True, null=True)

    action = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.description

class Media(models.Model):
    """
    A model to map the Media table in database

    Attributes:
        case = ForeignKey (the case which the media belong)
        file 
    """
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='images/')

    def __str__(self):
        return self.case.description

