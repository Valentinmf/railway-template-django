from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post

class BlogHome(ListView):
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)

class BlogPostDetail(DetailView):
    model = Post
    context_object_name = "post"