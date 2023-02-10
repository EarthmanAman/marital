from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Creating a user model by inheriting the Django standard user and adding 
    Phone number and address as required field during user login
    """
    phone_number = models.CharField(max_length=15, blank=True)
    address  = models.CharField(max_length=100, blank=True)