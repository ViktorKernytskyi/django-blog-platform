from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
       return HttpResponse("Привіт, Віктор! Це твоя перша сторінка на Django 🚀")
def hello_1(request):
    return render(request, 'main/hello.html')