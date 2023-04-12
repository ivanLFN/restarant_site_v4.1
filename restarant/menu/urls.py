from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', TemplateView.as_view(template_name='menu.html'), name='menu'),
]
