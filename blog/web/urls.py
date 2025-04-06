"""copyright (c) 2014 - 2025 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""

from django.urls import path

from utils.html_view_set import HtmlViewSet
from web.models import Post
from web.views.comments import CommentCreateView

urlpatterns = HtmlViewSet.as_viewset(
    model=Post,
    # lista pól wspólnych dla widoków create i update
    fields=("title", "teaser", "content", "header_image"),
    # lista pól dla specyficznych widoków, które nie powinny znaleźć się w innych
    fields_by_view={'create': ("created_by",)}
) + [path('<post_id>/comment/create', CommentCreateView.as_view(), name='comment-create'), ]
