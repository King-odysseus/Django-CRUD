from django.shortcuts import render
from django.db import models
from blog.models import Post
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView


# Create your views here.
class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")


class PostDetailview(DetailView):
    model = Post


class PostUdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")


class PostDeleteView(UpdateView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")
