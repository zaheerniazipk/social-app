# from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.
# Note: ListView should be used when to present a list of objects in a html page.
class HomePage(ListView):
    http_method_names = ['get']
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'  # by default, it is objects
    queryset = Post.objects.all().order_by('-id')[0:30]


# DetailView should be used when you want to present detail of a single model instance.
class PostDetailView(DetailView):
    http_method_names = ['get']
    template_name = 'detail.html'
    model = Post
    context_object_name = 'post'
