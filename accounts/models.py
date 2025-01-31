from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# auth --> 認証
class CustomUser(AbstractUser):
    pass