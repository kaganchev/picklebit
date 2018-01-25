from blog.models import Post
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

# Create your views here.

class Home(ListView):
    model = Post
    template_name = "base.html"