from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.post_list, name='post_list'),
    #path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('sobre/',views.sobre, name='sobre'),
    path('categorias/<slug>/', views.category_detail, name='category_detail'),
    path('email/', views.subscribe, name='email'),
    path('success/', views.successView, name='success'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
