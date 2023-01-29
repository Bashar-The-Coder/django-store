from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()[:10:2]
    context = {"products" : products}
    return render (request, "index.html" , context)