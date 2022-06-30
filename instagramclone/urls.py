from django.urls import path
from . import views

urlpatterns = [
    path('', views.instapost_list, name='instapost_list'),
]