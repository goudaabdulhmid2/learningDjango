from django.shortcuts import render
from .models import Product
# Create your views here.

def product(request):
    
    return render(request,'products/product.html')

def products(request):
    # data = {'pro': Product.objects.get(id = 1)}
    pro = Product.objects.all()
    # data = {'pro': pro.order_by('price')}
    # data = {'pro': str(pro.count())}
    data = {'pro': pro.exclude(price=99.99)}

    

    return render(request,'products/products.html',data)