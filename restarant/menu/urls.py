
from django.urls import include, path
from menu.views import menu_home

urlpatterns = [
    path('', menu_home, name='menu_home'),
]
