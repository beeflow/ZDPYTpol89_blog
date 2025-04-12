from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet

app_name = "api"

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path("posts", PostsListView.as_view(), name="posts-list"),
#     path("posts/<int:pk>", PostView.as_view(), name="posts-detail"),
# ]