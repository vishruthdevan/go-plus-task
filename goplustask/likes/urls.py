from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('like/', views.like, name='like'),
    path('dislike/', views.dislike, name='dislike')
]
