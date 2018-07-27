from django.urls import path, include
from rest_framework.routers import SimpleRouter
from posts.apis import PostListAPI
from user.apis import UserListAPI

router = SimpleRouter()
router.register(r'posts', PostListAPI)
router.register(r'users', UserListAPI)

urlpatterns = [
    path('', include(router.urls)),
]
