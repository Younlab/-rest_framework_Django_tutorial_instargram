from django.urls import path, include

# API URL
urlpatterns = [
    path('', include([
        path('posts/', include('posts.urls.apis')),
        path('user/', include('user.urls.apis')),
    ])),
]
