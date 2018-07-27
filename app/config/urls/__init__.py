from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .. import views
from . import api_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('posts/', include('posts.urls')),
    path('user/', include('user.urls')),
    path('api/', include(api_router)),
]

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
