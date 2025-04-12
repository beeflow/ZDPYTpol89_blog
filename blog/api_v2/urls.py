from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_v2.views import PostViewSet

app_name = "api_v2"

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
]
