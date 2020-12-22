from django.shortcuts import render
from .models import Post
import datetime


# Create your views here.

def Index(request):

    week_ago = datetime.date.today() - datetime.timedelta(days= 7)
    trends = Post.objects.filter(time_upload__gte = week_ago).order_by('-read_time')

    parms = {
        'post':Post.objects.filter(publish=True),
        'trends' : trends,



        
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
