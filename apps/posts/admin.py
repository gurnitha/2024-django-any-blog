# apps/posts/admin.py

# Django modules
from django.contrib import admin

# Django locals
from apps.posts.models import Author, Category, Post, Tag

# PostAdmin class
class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)