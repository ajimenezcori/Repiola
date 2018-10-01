from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Product

def productos(request):
    productos = Product.objects.all()
    return render(request, 'products/productos_lista.html', {'products' : productos})

def addp(request):
    Product.objects.all()
    productos = Product()
    productos.producto_nombre = request.GET['producto']
    productos.producto_precio = request.GET['valor']
    productos.save()
    return render(request, 'products/addp.html', { 'xx' : productos})
