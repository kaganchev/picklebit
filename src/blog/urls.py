from django.contrib import admin
from django.urls import path, include
from .views import Blog, DetailedPost, About


urlpatterns = [
    path('', Blog.as_view(), name="home"),
    path('blog/', Blog.as_view(), name="blog"),
    path('blog/<uuid:pk>/', DetailedPost.as_view(), name='post'),
    path('about/', About.as_view(), name="about" ),
]