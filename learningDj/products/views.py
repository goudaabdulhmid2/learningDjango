from django.shortcuts import render
from .models import Product
# Create your views here.

def product(request):
    
    return render(request,'products/product.html')

def products(request):
    
    pro = Product.objects.all()
    # data = {'pro':pro.filter(price__exact=99.99)}
    # data = {'pro':pro.filter(name__exact='Docker')}
    # data = {'pro':pro.filter(name__contains='A')}
    # data = {'pro':pro.filter(price__in=[333.99,99.99])}
    data = {'pro':pro.filter(price__range=(10,500))}
    
    return render(request,'products/products.html',data)