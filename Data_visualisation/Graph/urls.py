from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('app/',views.app,name = 'app'),
    path('app/graph/',views.app_page,name = 'app_page'),
    path('app/read/',views.ReadDoc,name = 'read_file'),
    path('suggestion/',views.suggestion,name = 'suggestion'),
    path('networkx/',views.networkx,name = 'networkx'),
    # path('about-me/',views.aboutme,name='about-me'),
]
