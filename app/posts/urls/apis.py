from django.urls import path
from .. import apis

urlpatterns = [
    path('', apis.PostListAPI.as_view()),
    path('<int:pk>/', apis.PostDetailAPI.as_view()),

]
