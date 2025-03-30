"""copyright (c) 2014 - 2025 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.urls import path

from web.views import WebView, UserBlogView

urlpatterns = [
    path('', WebView.as_view(), name='index'),
    path('<int:pk>', UserBlogView.as_view(), name='user_blog'),
]
