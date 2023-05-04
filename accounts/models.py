from django.db import models
from django.contrib.auth.models import AbstractUser

class AdminPost(models.Model):
    name    = models.CharField(max_length=50)
    area    = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name + " :- " + self.area
    
class CustomUser(AbstractUser):
    """
    Creating a user model by inheriting the Django standard user and adding 
    Phone number and address as required field during user login
    """
    phone_number = models.CharField(max_length=15, blank=True)
    address  = models.CharField(max_length=100, blank=True)
    admin_post  = models.ForeignKey(AdminPost, on_delete=models.SET_NULL, null=True, blank=True)