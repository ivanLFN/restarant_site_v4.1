from django.views.generic import TemplateView
from django.urls import include, path
from reservation import views

urlpatterns = [
    path('', views.reserv, name='reservation'),
]
