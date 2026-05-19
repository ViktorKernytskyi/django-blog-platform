from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.http import HttpResponse


def post_list(request):
    return HttpResponse("Hello, blog! i'm a post list view")


def post_list_blog(request):
    posts = (Post.objects
             .filter(published_date__lte=timezone.now())
             .order_by('-published_date'))

    return render(
        request,
        'blog/post_list_blog.html',
        {'posts': posts
         })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(
        request,
        'blog/post_detail.html',
        {'post': post}
    )
