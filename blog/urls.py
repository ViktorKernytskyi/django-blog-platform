from django.urls import path

from . import views

urlpatterns = [

    path('', views.post_list, name='post_list'),
    path('post_list_blog/', views.post_list_blog, name='post_list_blog'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]