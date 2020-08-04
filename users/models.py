from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    avatar = models.ImageField(upload_to='profile', null=True, default='/profile/avatar.png')
    AboutYou = models.TextField(null=True, blank=True)
    
