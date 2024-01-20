# apps/posts/admin.py

# Django modules
from django.contrib import admin

# Django locals
from apps.posts.models import Author, Category, Post, Tag

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)