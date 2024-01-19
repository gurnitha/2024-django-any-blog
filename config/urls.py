# config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
]
