from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.
from django.utils.translation import pgettext_lazy


class User(AbstractUser):
    user_type = models.CharField(max_length=255,unique=False,verbose_name=pgettext_lazy('User','user_type'))
