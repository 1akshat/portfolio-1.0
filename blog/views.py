from django.shortcuts import render_to_response, get_object_or_404
from .models import Blog, Category

def index(request):
	return render_to_response('blog.html', {
		'categories': Category.objects.all(),
		'posts': Blog.objects.all()[:5]
		})

def view_post(request, slug):
	return render_to_response('blog-item.html', {
		'post': get_object_or_404(Blog, slug=slug),
		'categories': Category.objects.all()
		})

def view_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	return render_to_response('view_category.html', {
		'category': category,
		'posts': Blog.objects.filter(category=category)[:5]
		})
