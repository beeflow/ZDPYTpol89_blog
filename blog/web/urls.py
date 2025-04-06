"""copyright (c) 2014 - 2025 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""

from utils.html_view_set import HtmlViewSet
from web.models import Post

urlpatterns = HtmlViewSet.as_viewset(
    model=Post,
    # lista pól wspólnych dla widoków create i update
    fields=("title", "teaser", "content", "header_image"),
    # lista pól dla specyficznych widoków, które nie powinny znaleźć się w innych
    fields_by_view={'create': ("created_by",)}
)
