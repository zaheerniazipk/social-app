from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from feed.models import Post
from followers.models import Follower


# Create your views here.
# Note: ListView should be used when to present a list of objects in a html page.
# class HomePage(ListView):
#     http_method_names = ['get']
#     template_name = 'index.html'
#     model = Post
#     context_object_name = 'posts'  # by default, it is objects
#     queryset = Post.objects.all().order_by('-id')[0:30]


# TemplateView should be used when you want to present some information in a html page
# Show Posts by following
class HomePage(TemplateView):
    http_method_names = ["get"]
    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            following = list(
                Follower.objects.filter(followed_by=self.request.user).values_list(
                    'following', flat=True)
            )
            if not following:
                # Show the default 30
                posts = Post.objects.all().order_by('-id')[0:30]
            else:
                posts = Post.objects.filter(
                    author__in=following).order_by('-id')[0:60]
        else:
            posts = Post.objects.all().order_by('-id')[0:30]
        context['posts'] = posts
        return context


# DetailView should be used when to present detail of a single model instance.
class PostDetailView(DetailView):
    http_method_names = ['get']
    template_name = 'detail.html'
    model = Post
    context_object_name = 'post'


# A view that displays a form for creating an object, re-displaying the form with validation errors (if there are any) and saving the object.
class CreateNewPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['text']

    # How to tackle Integrity Error
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

    # post request
    def post(self, request, *args, **kwargs):

        post = Post.objects.create(
            text=request.POST.get("text"),
            author=request.user,
        )

        return render(
            request,
            "includes/post.html",   # template
            {
                "post": post,
                "show_detail_link": True,
            },
            content_type="application/html"
        )
