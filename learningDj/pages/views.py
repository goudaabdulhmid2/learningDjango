from django.shortcuts import render
from django.http import HttpResponse
from .models import Login

# Create your views here.

def index(request):
    context = {
                'name':'mdo',
                'age':13435345664564
            }
    return render(request,'pages/index.html',context);

def about(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    data = Login(username=username,password=password)
    data.save();

    return render(request,'pages/about.html');