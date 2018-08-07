import json

from django.contrib.auth import get_user_model
from rest_framework.parsers import JSONParser

# from ..models import User
User = get_user_model()
from ..serializers import UserSerializer

from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.compat import authenticate
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class UserListAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthToken(APIView):

    def post(self, request):
        username = request.data.get('username')
        print(username)
        password = request.data.get('password')

        print(password)

        user = authenticate(username=username, password=password)
        print(user)

        if user:
            token, __ = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
            }
            return Response(data)
        raise AuthenticationFailed('인증 정보가 올바르지 않습니다.')


class AuthenticationTest(APIView):
    def get(self, request):
        # request.user 가 인증된 상태일 경우, UserSerializer 를 사영해 렌더링한 데이트를 보내줌
        # 인증되지 않았을 경우 NotAuthenticated Exception 을 raise
        if request.user.is_authenticated:
            return Response(UserSerializer(request.user).data)
        raise NotAuthenticated('로그인 되어있지 않습니다.')


class FacebookAuthToken(APIView):
    def post(self, request):
        print(request.data)
        # request.data 에 'facebook_id' 와 'name'이 올것을 예상
        # 전달받은 facebook_id 에 해당하는 유저가 있을 경우 해당 User 의 token값을 전달
        facebook_id = request.data.get('id')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        user, __ = User.objects.get_or_create(
            username=facebook_id,
            defaults={
                'last_name': last_name,
                'first_name': first_name,
            }
        )
        token, __ = Token.objects.get_or_create(user=user)
        data = {
            'token': token.key,
        }
        return Response(data)


class Profile(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return Response(UserSerializer(request.user).data)

        raise NotAuthenticated('인증안됨')
