from django.urls import path, include
from . import views, apis

# include mode
urlpatterns = [
    # Templates
    path('', include(views)),
    # API
    path('api/', include(apis)),
]
