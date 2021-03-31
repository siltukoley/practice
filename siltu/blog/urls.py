from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blogHome, name="bloghome"),
    path('blogpost', views.blogPost, name="blogPost"),
]
