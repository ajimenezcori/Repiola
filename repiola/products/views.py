from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Product

def productos(request):
    productos = Product.objects.all()
    return render(request, 'products/productos_lista.html', {'products' : productos})
