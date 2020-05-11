from django.db import models

# Create your models here.

from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children' ,on_delete=models.CASCADE)

    class Meta:
        #enforcing that there can not be two categories under a parent with same slug
        
        # __str__ method elaborated later in post.  use __unicode__ in place of
        
        # __str__ if you are using python 2

        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"  

    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    photo = models.ImageField(upload_to='images/', null = True, blank = True)
    text = RichTextField(blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True,editable=True, default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    
    


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_cat_list(self):
        k = self.category # for now ignore this instance method
        
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]