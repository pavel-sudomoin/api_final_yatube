from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import PostViewSet, CommentViewSet
from .views import FollowViewSet, GroupViewSet


v1_router = DefaultRouter()
v1_router.register(
    'posts',
    PostViewSet,
    basename='Posts'
)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
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
    path('v1/', include(v1_router.urls)),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
