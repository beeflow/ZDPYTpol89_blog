from django.contrib.auth.models import AbstractUser
from django.db import models
from django_resized import ResizedImageField

from users.user_manager import UserManager
from utils.photo_path import get_photo_path_name


class User(AbstractUser):
    about_user = models.TextField(null=True, blank=True, verbose_name="About me")
    email = models.EmailField(blank=False, db_index=True, unique=True)
    photo = ResizedImageField(
        null=True,
        blank=True,
        size=[200, 200],
        quality=75,
        upload_to=get_photo_path_name,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
