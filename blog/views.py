from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(status='PB')
    context = {'posts': posts}
    return render(request, 'blog/post-list.html', context)

def post_details(request, slug):
    # post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    return render(request, 'blog/post-details.html', context)



