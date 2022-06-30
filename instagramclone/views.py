from django.shortcuts import render
from django.utils import timezone
from .models import Instapost
from django.shortcuts import redirect

from .forms import PostForm


def instapost_list(request):
    posts = Instapost.objects.filter(
        created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'instagramclone/home.html', {'posts': posts})


def post_new(request):
    form = PostForm()
    return render(request, 'instagramclone/post_new.html', {'form': form})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('instapost_list')
    else:
        form = PostForm()
    return render(request, 'instagramclone/post_new.html', {'form': form})
