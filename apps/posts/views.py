# apps/posts/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.posts.models import Author, Category, Post, Tag
from apps.marketing.models import Signup

# Create your views here.

def index(request):

	# SELECT * FROM post WHERE post = featured
	featured_posts = Post.objects.filter(featured=True)

	# Grab 3 latest posts and render them based on LIFO
	latest_posts = Post.objects.order_by('-timestamp')[0:3]

	# Testing
	# print(featured_posts)

	# Subscribe Newsletter (without security)
	if request.method == "POST":
		# Get the email
		email = request.POST["email"]
		# Use the signup method
		new_signup = Signup()
		# Signup with email
		new_signup.email = email
		# save its email
		new_signup.save()

	context = {
		'object_list': featured_posts,
		'latest_posts': latest_posts
	}

	return render(request, 'index.html', context)


def posts_list(request):
	return render(request, 'posts-list.html')


def post_single(request):
	return render(request, 'post-single.html')