from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def post_list(request):
    return HttpResponse("Hello, blog! i'm a post list view")