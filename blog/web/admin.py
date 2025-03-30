"""copyright (c) 2014 - 2025 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.contrib import admin

from web.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by']
