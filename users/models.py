from django.db import models
from django.contrib.auth.models import AbstractUser
from users.manager import CustomUserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    membership_date = models.DateTimeField(null=True)
    phone_number = models.CharField(blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
