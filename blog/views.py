from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import forms
from django.core.mail import send_mail
from blog_well.settings import EMAIL_HOST_USER



# Create your views here.

def category_list(request):
    categories = Category.objects.all() # this will get all categories, you can do some filtering if you need (e.g. excluding categories without posts in it)

    return render (request, 'blog/category.html', {'categories': categories}) # blog/category_list.html should be the template that categories are listed.

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)

    return render(request, 'blog/category_detail.html', {'category': category}) # in this template, you will have access to category and posts under that category by (category.post_set).

def post_list(request):
	posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	page = request.GET.get('page', 1)
	paginator = Paginator(posts_list, 8)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	#return render(request, 'blog/post_list.html', {'posts': posts})
	return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_detail.html', {'post': post,'posts': posts})

def sobre(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/sobre.html', {'posts': posts})


def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = str(sub['subject'].value())
        message = str(sub['message'].value())
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'blog/success.html', {'recepient': recepient})
    return render(request, 'blog/email.html', {'form':sub})