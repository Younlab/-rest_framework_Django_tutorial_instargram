from rest_framework import generics, viewsets

from ..serializers import PostSerializer, PostDetailSerializer
from ..models import Post


# class PostListAPI(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostListAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPI(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
