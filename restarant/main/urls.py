from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import include, path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
