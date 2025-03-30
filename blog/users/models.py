from django.contrib.auth.models import AbstractUser
from django.db import models

from users.user_manager import UserManager


class User(AbstractUser):
    about_user = models.TextField(null=True, blank=True, verbose_name="About me")
    email = models.EmailField(blank=False, db_index=True, unique=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
