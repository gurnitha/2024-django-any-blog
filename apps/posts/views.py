# apps/posts/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.posts.models import Author, Category, Post, Tag, Gallery
from apps.marketing.models import Signup

# Create your views here.

def index(request):

	# Grab all the posts that has featured as true
	featured_posts = Post.objects.filter(featured=True)

	# Testing
	# print(featured_posts)

	# Grab 3 latest posts and render them based on LIFO
	latest_posts = Post.objects.order_by('-timestamp')[0:3]
	
	# Testing
	# print(latest_posts)

	# Subscribe Newsletter (without security)
	if request.method == "POST":
		email = request.POST["email"]
		new_signup = Signup()
		new_signup.email = email
		new_signup.save()
	
	# # Gallery
	# Grab 3 latest images and render them based on LIFO
	images_list = Gallery.objects.order_by('-timestamp')[0:4]

	context = {
		'object_list': featured_posts,
		'object_list': latest_posts,
		'images_list': images_list
	}

	return render(request, 'index.html', context)


def posts_list(request):
	return render(request, 'posts-list.html')


def post_single(request):
	return render(request, 'post-single.html')