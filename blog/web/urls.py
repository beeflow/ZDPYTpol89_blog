"""copyright (c) 2014 - 2025 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.urls import path
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from web.models import Post
from web.views import UserBlogView

urlpatterns = [
    path('', ListView.as_view(model=Post), name='index'),
    path('<int:pk>', UserBlogView.as_view(), name='user_blog'),
    path(
        'post/add',
        CreateView.as_view(
            model=Post, success_url="/post/{id}", fields=("title", "teaser", "content", "created_by", "header_image")
        ),
        name='post_add',
    ),
    path(
        'post/edit/<int:pk>',
        UpdateView.as_view(
            model=Post, fields=("title", "teaser", "content", "header_image"), success_url="/post/{id}"
        ),
        name='update_post'
    ),
    path('post/<int:pk>', DetailView.as_view(model=Post), name='user_post'),
]
