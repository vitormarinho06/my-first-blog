from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import forms
#from blog_well.settings import EMAIL_HOST_USER



# Create your views here.


def category_detail(request, slug):
    some_category = Category.objects.get(slug=slug)
    categories_post = Post.objects.filter(category = some_category)

    return render(request, 'blog/category_list.html', {'categories_post': categories_post}) # in this template, you will have access to category and posts under that category by (category.post_set).

def post_list(request):
	#return render(request, 'blog/post_list.html', {'posts': posts})
	return render(request, 'blog/base.html')


def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})


def sobre(request):
	return render(request, 'blog/sobre.html')


def subscribe(request):
	if request.method =='GET':
		form = forms.Subscribe()
	else:
		form = forms.Subscribe(request.POST)
		if form.is_valid():
			sender_name = form.cleaned_data['name']
			subject = form.cleaned_data['subject']
			message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
			Email = form.cleaned_data['Email']
			try:
				

				send_mail(subject, message, Email, ['vitormarinho0610@gmail.com'], fail_silently=False)
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('success')
	return render(request, "blog/email.html", {'form': form})

def successView(request):
	return HttpResponse('Success! Thank you for your message.')