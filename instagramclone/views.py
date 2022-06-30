from django.shortcuts import render
from django.utils import timezone
from .models import Instapost

def instapost_list(request):
    posts = Instapost.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'instaclone/home.html', {'posts': posts})