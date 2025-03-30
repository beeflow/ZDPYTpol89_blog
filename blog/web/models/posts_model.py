"""copyright (c) 2014 - 2025 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.conf import settings
from django.db import models
from django_resized import ResizedImageField

from utils.photo_path import get_photo_path_name


class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    header_image = ResizedImageField(
        null=True, blank=True,
        size=[700, 220],
        quality=100,
        upload_to=get_photo_path_name,
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-created_at']
