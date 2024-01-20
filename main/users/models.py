from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length = 30,  blank=False)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False)

   

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

def Profile(request):
    user = models.oneTOoneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'self.user.username', Profile