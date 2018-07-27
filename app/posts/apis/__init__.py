from rest_framework import generics, viewsets

from ..serializers import PostSerializer
from ..models import Post


class PostListAPI(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class PostListAPI(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
