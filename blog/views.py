from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(status='PB')
    upcoming = Post.objects.filter(status='DF')[:3]
    pages = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)
    page = pages.get_page(page_number)
    posts = page.object_list

    start_index = page.number - 1
    if start_index < 1:
        start_index = 1
    
    end_index = page.number + 3
    if end_index > pages.num_pages:
        end_index = (pages.num_pages) + 1
    
    custom_range = range(start_index,end_index)    
    
    context = {'posts': posts, 'upcoming': upcoming, 'pages': pages, 'page': page, 'custom_range': custom_range}
    return render(request, 'blog/post-list.html', context)

def post_details(request, slug):
    # post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    return render(request, 'blog/post-details.html', context)



