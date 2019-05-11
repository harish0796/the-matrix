from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_posts),
    path('createposts/',views.create_posts)
]