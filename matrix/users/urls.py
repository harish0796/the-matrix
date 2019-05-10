from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/',views.signin ),
    path('logout/',views.signout),
    path('register/', views.register),
    path('dashboard/',views.dashboard),
]