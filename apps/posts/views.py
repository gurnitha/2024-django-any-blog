# apps/posts/views.py

# Django modules
from django.shortcuts import render
from django.db.models import Count

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
		'featured_posts': featured_posts,
		'latest_posts': latest_posts,
		'images_list': images_list
	}

	return render(request, 'index.html', context)


# Category count view
def get_category_count():
	queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))
	return queryset

# Tag count view
def get_tag_count():
	queryset = Post.objects.values('tags__title').annotate(Count('tags__title'))
	return queryset


def posts_list(request):

	# Grab all posts
	posts_list = Post.objects.all()

	# Grab 3 posts based on LIFO
	posts_latest = Post.objects.order_by('-timestamp')[0:3]

	# Count the category
	category_count = get_category_count()

	# Count the tag
	tag_count = get_tag_count()

	context = {
		'posts_list':posts_list,
		'posts_latest':posts_latest,
		'category_count':category_count,
		'tag_count':tag_count
	} 
	
	return render(request, 'posts/posts-list.html', context)


def post_single(request):
	return render(request, 'post-single.html')