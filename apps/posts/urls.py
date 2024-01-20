# apps/posts/urls.py

# Django modules
from django.urls import path

# Locals
from apps.posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/', views.posts_list, name='posts_list'),
    path('post/1', views.post_single, name='post_single'),
]
