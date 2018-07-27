from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('posts/', include('posts.urls.views')),
    path('user/', include('user.urls.views')),
    path('api/posts/', include('posts.urls.apis')),
    path('api/user/', include('user.urls.apis')),
]

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
