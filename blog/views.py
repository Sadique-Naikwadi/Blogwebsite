from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post
from .forms import SharePostForm, CommentForm
from django.core.mail import send_mail
from django.conf import settings
from django.db import IntegrityError

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
    form =  CommentForm()
    comments = post.comments.filter(active=True)
    context = {'post': post, 'form': form, 'comments': comments}
    return render(request, 'blog/post-details.html', context)


def share_post(request, pk):
    form = SharePostForm()
    post = get_object_or_404(Post, id=pk, status='PB')
    if request.method == 'POST':
        form = SharePostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['Name']} recommends you to read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                    f"{cd['Name']}\'s comments: {cd['comment']}"
            

            send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [cd['to']],
            fail_silently=False,
        )
        return redirect('blog:post-list')

    context = {'form': form}
    return render(request, 'blog/share-post.html', context)


def create_comment(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            try:
                new_comment.post = post
                new_comment.save()
            except IntegrityError:
                print(' You have already given the comment.')

            return redirect('blog:post-details', slug=post.slug)
        else:
            print('Error in saving comment.')
        
    


