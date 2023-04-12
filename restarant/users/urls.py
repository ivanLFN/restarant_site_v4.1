from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import include, path
from users.views import Register 


urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', Register.as_view(), name='register'),
]