from .models import Post, Category
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
	categories = Category.objects.all()

	#return render(request, 'blog/post_list.html', {'posts': posts})
	return {'posts': posts,'categories': categories}