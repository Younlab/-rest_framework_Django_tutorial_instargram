from rest_framework import serializers

from user.serializers import UserSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'author',
            'content',
            'image',
            'created_at',
        )
class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'author',
            'content',
            'image',
            'created_at',
        )
        read_only_fields = (
            'author',
        )