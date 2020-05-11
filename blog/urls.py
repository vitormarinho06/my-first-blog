from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('sobre/',views.sobre, name='sobre'),
    path('categorias/', views.category_list, name='categorias'),
    path('email/', views.subscribe, name='email'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
