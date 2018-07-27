from django.urls import path
from .. import apis

urlpatterns = [
    path('', apis.UserListAPI.as_view()),
]
