# apps/posts/urls.py

# Django modules
from django.urls import path

# Locals
from apps.posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='home'),
]
