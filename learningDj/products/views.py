from django.shortcuts import render
from .models import Product
# Create your views here.

def product(request):
    
    return render(request,'products/product.html')

def products(request):
    data = {'pro': Product.objects.all()}
    return render(request,'products/products.html',data)