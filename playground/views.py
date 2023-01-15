from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calculate():
    x = 12
    y = 13
    return x+y

def say_hello (request):
    x = calculate()
    y = 2
    context = {'content' : 'hello world'}
    return render (request, 'index.html', {'context': context})