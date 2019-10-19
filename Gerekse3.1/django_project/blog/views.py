from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from .filters import PostFilter
import operator
from functools import reduce
from django.contrib.auth.mixins import LoginRequiredMixin
from .config import pagination
from django.db.models import Q

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/ilan.html', context)

def post_list(request):
    template_name = 'blog/ilan.html'  # <app>/<model>_<viewtype>.html
    object_list = Post.objects.all()
    
    pages = pagination(request, object_list)
    
    context = {
            'items': pages[0],
            'page_range': pages[1],
            }   
    return render(request, 'blog/ilan.html', context)

def search(request):
    template = 'blog/ilan.html'
    query = request.GET.get('q')
    
    if query:
        results = Post.objects.filter(Q(title__icontains=query) | Q(author__username=query))
    else:
        results = Post.objects.all()
    pages = pagination(request, results, num=10)
    
    context = {
            'items': pages[0],
            'page_range': pages[1],
            'query': query,
            }
    return render(request, template, context)
    
class PostDetailView(DetailView):
    model = Post

    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['Aktiflik', 'title', 'mini_content', 'content', 'image', 'iletisim', 'Kategori_1', 'Kategori_2']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['Aktiflik', 'title', 'mini_content', 'content', 'image', 'iletisim', 'Kategori_1', 'Kategori_2']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/misyonvizyon.html', {'title': 'About'})

def sozlesme(request):
    return render(request, 'blog/sozlesme.html')
