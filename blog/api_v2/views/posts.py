from rest_framework import viewsets

from api_v2.serializers import PostListSerializer
from web.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
