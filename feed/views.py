# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post


# Create your views here.
# Note: ListView should be used when to present a list of objects in a html page.
class HomePage(ListView):
    http_method_names = ['get']
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'  # by default, it is objects
    queryset = Post.objects.all().order_by('-id')[0:30]


# DetailView should be used when to present detail of a single model instance.
class PostDetailView(DetailView):
    http_method_names = ['get']
    template_name = 'detail.html'
    model = Post
    context_object_name = 'post'


# A view that displays a form for creating an object, re-displaying the form with validation errors (if there are any) and saving the object.
class CreateNewPost(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['text']
