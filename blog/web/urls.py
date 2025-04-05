"""copyright (c) 2014 - 2025 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.urls import path
from django.views.generic import DetailView, ListView

from web.models import Post
from web.views import UserBlogView

urlpatterns = [
    path('', ListView.as_view(model=Post), name='index'),
    path('<int:pk>', UserBlogView.as_view(), name='user_blog'),
    path('post/<int:pk>', DetailView.as_view(model=Post), name='user_post'),
]
