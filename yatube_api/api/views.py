from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import AllowAny
from rest_framework.pagination import LimitOffsetPagination

from .permissions import AuthorOrReadOnly
from .serializers import PostSerializer, GroupSerializer, CommentSerializer, \
    FollowSerializer
from posts.models import Group, Post, Follow


class ListCreateViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        pk = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=pk)
        return post.comments

    def perform_create(self, serializer):
        pk = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=pk)
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(ListCreateViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username',)

    def get_queryset(self):
        new_queryset = self.request.user.followers
        return new_queryset

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
