from django.contrib import admin
from posts import views
from django.urls import path, include


urlpatterns = [
    path('', views.index),
]
