from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets

from ..serializers import UserSerializer

User = get_user_model()


class UserListAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserListAPI(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
