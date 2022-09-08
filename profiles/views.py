# from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import DetailView

from .models import Profile


# DetailView should be used when you want to present detail of a single model instance.
class ProfileDetailView(DetailView):
    http_method_names = ['get']
    template_name = 'profiles/detail.html'
    model = User
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'
