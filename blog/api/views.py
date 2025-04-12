from rest_framework import viewsets

from api.serializers import PostListSerializer
from web.models import Post


# class PostsListView(generics.ListCreateAPIView):
#     serializer_class = PostListSerializer
#     queryset = Post.objects.all()
#
#
# class PostView(generics.RetrieveUpdateDestroyAPIView):
#     """Pojedynczy post może być: pobrany (get), zaktualizowany (put), usunięty (delete)"""
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
