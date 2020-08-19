from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import PostViewSet, CommentViewSet
from .views import FollowViewSet, GroupViewSet


v1_router = DefaultRouter()
v1_router.register(
    'posts',
    PostViewSet,
    basename='Posts'
)
v1_router.register(
    r'posts/(?P<post_id>[^/.]+)/comments',
    CommentViewSet,
    basename='Comments'
)
v1_router.register(
    'follow',
    FollowViewSet,
    basename='Follow'
)
v1_router.register('group', GroupViewSet)

urlpatterns = [
    path('', include(v1_router.urls)),
]
