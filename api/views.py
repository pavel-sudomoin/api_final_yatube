from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from .models import User, Post, Comment, Group, Follow
from .serializers import PostSerializer, CommentSerializer
from .serializers import GroupSerializer, FollowSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Post.objects.all()
        group_pk = self.request.query_params.get('group', None)
        if group_pk is not None:
            queryset = queryset.filter(group__pk=group_pk)
        return queryset


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_post(self, pk):
        return get_object_or_404(Post, pk=pk)

    def get_queryset(self):
        post = self.get_post(self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = self.get_post(self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = Follow.objects.all()
        username = self.request.query_params.get('search', None)
        if username is not None:
            queryset = queryset.filter(
                Q(user__username=username) | Q(following__username=username)
            )
        return queryset
