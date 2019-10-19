from django.shortcuts import render
from blog.models import Post
from blog.filters import PostFilter
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def anasayfa(request):
    context = {
            'posts': Post.objects.filter().order_by('-date_posted')[0:10]
            }
    return render(request,"blog/index.html", context)



