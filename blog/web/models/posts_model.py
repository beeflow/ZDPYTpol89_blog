"""copyright (c) 2014 - 2025 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-created_at']
