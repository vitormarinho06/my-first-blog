from django.db import models

# Create your models here.

from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    

    class Meta:
        #enforcing that there can not be two categories under a parent with same slug
        
        # __str__ method elaborated later in post.  use __unicode__ in place of
        
        # __str__ if you are using python 2
  
        verbose_name_plural = "categories"  

    def __str__(self):                           
        return self.name                  
        

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    categories = models.ManyToManyField('Category', null=True, blank=True)
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

    