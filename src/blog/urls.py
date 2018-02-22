from django.contrib import admin
from django.urls import path, include
from .views import Blog, DetailedPost


urlpatterns = [
    path('', Blog.as_view(), name="home"),
    path('blog/', Blog.as_view(), name="blog"),
    path('blog/<uuid:pk>/', DetailedPost.as_view(), name='post')
]