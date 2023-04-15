from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('<int:post_id>/', views.detail_post, name='detail_post'),
    path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
]