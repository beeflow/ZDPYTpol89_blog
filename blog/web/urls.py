"""copyright (c) 2014 - 2025 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""

from utils.html_view_set import HtmlViewSet
from web.models import Post

urlpatterns = HtmlViewSet.as_viewset(
    model=Post,
    fields=("title", "teaser", "content", "created_by", "header_image", "created_by")
)
