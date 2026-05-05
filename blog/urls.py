from django.urls import path

from . import views

urlpatterns = [

    path('', views.post_list, name='post_list'),
    path('post_list_blog/', views.post_list_blog, name='post_list_blog'),
    
]