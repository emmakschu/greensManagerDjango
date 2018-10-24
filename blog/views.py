from django.shortcuts import render, redirect
from django.utils.timezone import now

from .models import BlogPost

def curr_time():
    return now()

def index(request):
    posts = BlogPost.objects.all().order_by('-created_at')[:5]

    context = {
        'curr_time': curr_time(),
        'posts': posts,
    }

    return render(request, 'blog/index.html', context)
