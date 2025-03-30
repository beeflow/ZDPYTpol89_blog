from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class User(AbstractUser):
    about_user = models.TextField(null=True, blank=True, verbose_name="About me")
    email = models.EmailField(blank=False, db_index=True, unique=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
