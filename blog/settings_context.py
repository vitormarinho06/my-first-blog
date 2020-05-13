from .models import Post, Category
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag


def post_list(request):
	posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	page = request.GET.get('page', 1)
	paginator = Paginator(posts_list, 8)
	common_tags = Post.tags.most_common()[:4]

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	categories = Category.objects.all()

	#return render(request, 'blog/post_list.html', {'posts': posts})
	return {'posts': posts,'categories': categories,'common_tags':common_tags}

def tagged(request, slug):
	tag = get_object_or_404(Tag, slug=slug)
	# Filter posts by tag name  
	posts = Post.objects.filter(tags=tag)
	context = {
	'tag':tag,
	'posts':posts,
	}

	return context