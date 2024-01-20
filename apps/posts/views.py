from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'index.html')


def posts_list(request):
	return render(request, 'posts-list.html')


def post_single(request):
	return render(request, 'post-single.html')