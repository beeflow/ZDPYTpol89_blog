"""copyright (c) 2014 - 2025 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.db import models

from web.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    # Nie będziemy wyświetlać komentarzy, które nie zostały zmoderowane
    is_approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.content[:30]
