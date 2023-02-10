from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from django.shortcuts import get_object_or_404


from posts.models import Comment, Post, Group, Follow, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title", "description", "slug")
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field="username")

    class Meta:
        fields = "__all__"
        model = Comment
        read_only_fields = ("post",)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username", read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    def validate_following(self, value):
        user = self.context["request"].user
        following = get_object_or_404(User, username=value)
        if user == following:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя")
        return super().validate(value)

    class Meta:
        fields = "__all__"
        model = Follow
        validators = (
            UniqueTogetherValidator(
                queryset=Follow.objects.all(), fields=("following", "user")
            ),
        )
