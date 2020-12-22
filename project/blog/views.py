from django.shortcuts import render
from .models import Post,Categories,Author

# Create your views here.

def Index(request):

    parms = {
        'post':Post.objects.all(),
    }
    return render(request,'index.html',parms)

def About(request):
    parms = {
        'title':'About | Title',
    }
    return render(request,'about.html',parms)

def Contact(request):
    return render(request,'contact.html')

def Categories(request):
    return render(request,'categories.html')

def Blog_Single(request):
    return render(request,'blog-single.html')
