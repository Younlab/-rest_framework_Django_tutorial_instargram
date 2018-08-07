from rest_framework import serializers

from user.serializers import UserSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'content',
            'image',
            'created_at',
        )

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'content',
            'image',
            'created_at',
        )
        read_only_fields = (
            'author',
        )