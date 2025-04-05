"""copyright (c) 2014 - 2025 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django import forms

from utils.bootstrap_form import BootstrapFormMixin
from web.models import Post


class PostEditForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'teaser', 'content', 'header_image']


class PostCreateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'teaser', 'content', 'header_image', 'created_by']
