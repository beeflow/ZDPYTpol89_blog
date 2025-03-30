"""copyright (c) 2014 - 2025 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.contrib.auth.models import UserManager as BaseUserManager


class UserManager(BaseUserManager):
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        return super().create_superuser(email, email, password, **extra_fields)

    def create_user(self, username=None, email=..., password=..., **extra_fields):
        return super().create_user(email, email, password, **extra_fields)
