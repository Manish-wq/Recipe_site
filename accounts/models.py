from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# # Create your models here.

class CustomUser(AbstractUser):
    username = None
    phone_no = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    user_bio = models.CharField(max_length=50)
    user_profile_img = models.ImageField(upload_to='profile')

    USERNAME_FIELD = 'phone_no'
    REQUIRED_FIELDS = []
    objects = UserManager()

    









