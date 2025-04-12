from django.http import JsonResponse
from django.utils.timezone import now
from rest_framework import viewsets
from rest_framework.decorators import action

from api_v2.serializers import PostListSerializer
from web.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    @action(detail=True, methods=['post'], url_path='publish', url_name='publish_now')
    def publish(self, *args, **kwargs):
        post = self.get_object()

        if post.published_at is None:
            post.published_at = now()
            post.save()

        return JsonResponse(self.get_serializer(post).data)