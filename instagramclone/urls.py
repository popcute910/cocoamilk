from django.urls import path
from . import views

urlpatterns = [
    path('', views.instapost_list, name='instapost_list'),
    path('post/new/', views.post_new, name='post_new'),
]