from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),

    path('users', include('users.urls')),

    path('menu/', include('menu.urls')),

]
