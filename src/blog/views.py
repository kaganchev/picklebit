from blog.models import Post
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView

# Create your views here.

class Blog(ListView):
    model = Post
    template_name = "blog_content.html"

class DetailedPost(DetailView):
    template_name = "post_detailed.html"
    
    def get_queryset(self):
        return Post.objects.filter(id=self.kwargs["pk"])

class About(TemplateView):
    template_name = "about.html"
