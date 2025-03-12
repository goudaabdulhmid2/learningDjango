from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
                'name':'abdulhmid',
                'age':14
            }
    return render(request,'pages/index.html',context);

def about(request):
    return HttpResponse('About pages');