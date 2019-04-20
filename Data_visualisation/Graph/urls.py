from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('app/',views.app,name = 'app'),
    # path('about-me/',views.aboutme,name='about-me'),
]
