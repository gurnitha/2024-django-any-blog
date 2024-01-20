# apps/posts/views.py

# Django modules
from django.shortcuts import render
from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Locals
from apps.posts.models import Author, Category, Post, Tag, Gallery
from apps.marketing.models import Signup

# Create your views here.

def search(request):

	# Load all post objects
    queryset = Post.objects.all()
    # Get and query all post objects
    query = request.GET.get('q')

    # If there is query, filter them
    # by title or overview and if there are
    # the same objects showed by title and overview,
    # use distinct to distinguished them.
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()

    context = {
        'queryset': queryset
    }
    return render(request, 'search_results.html', context)

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

	# Pagination
	# Set number of post to view per page
	paginator = Paginator(posts_list, 3)
	# Page request pariable
	# -> 127.0.0.1:8000/blog/?page=3	
	page_request_var = 'page' # <-- page=3
	page = request.GET.get(page_request_var)  # <-- page=3
	# Do some check
	try:
		paginated_queryset = paginator.page(page)
	# if request was not integer: 
	# --> 127.0.0.1:8000/blog/?page=fdfkdfkdfk
	# then return to page 1 or home page		
	except PageNotAnInteger: 
		paginated_queryset = paginator.page(1)
	# if request was empty page: 
	# --> 127.0.0.1:8000/blog/?page=
	# then return number of pages in queryset
	except EmptyPage:
		paginated_queryset = paginator.page(paginator.num_pages)

	context = {
		# 'posts_list':posts_list, # see line 102 ---> 'posts_list':paginated_queryset,
		'posts_latest':posts_latest,
		'category_count':category_count,
		'tag_count':tag_count,

		# Pagination
		'posts_list':paginated_queryset,
		'page_request_var':page_request_var,
	} 
	
	return render(request, 'posts/posts-list.html', context)


def post_single(request):
	return render(request, 'post-single.html')