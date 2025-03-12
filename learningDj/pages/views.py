from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
                'name':'Abdulhamid Ahmed Gouda',
                'age':13435345664564
            }
    return render(request,'pages/index.html',context);

def about(request):
    return HttpResponse('About pages');