from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post
from .forms import SharePostForm, CommentForm, CustomAuthenticationForm, CustomUserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .forms import AddPost
from django.contrib.postgres.search import SearchVector, SearchQuery

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

def view_myblog(request):
    owner = request.user
    posts = Post.objects.filter(owner=owner)
    context = {'posts': posts}
    return render(request, 'blog/view-myblog.html', context)


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

def create_post(request):
    owner = request.user
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = owner
            new_post.save()
            return redirect('blog:view-myblog')
    else:

        form = AddPost()
    context = {'form': form}
    return render(request, 'blog/create-post.html', context)



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
        
    
def user_login(request):
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('blog:post-list')
            
    else:
        form = CustomAuthenticationForm()
            
    context = {'form': form}
    return render(request, 'blog/user_login.html', context)


def user_logout(request):

    logout(request)
    return redirect('blog:post-list')


def create_user(request):
    
    if request.method == 'POST':
        print('enter in post')
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            print('save data')
            return redirect('blog:user-login')
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'blog/create_user.html', context)


def do_search(request):
    query = request.GET.get('query', '')
    search_vector = SearchVector('title', 'body')
    search_query = SearchQuery(query)
    results = Post.objects.annotate(search=search_vector).filter(search=search_query)
    context = {'results': results}
    print(results)
    return render(request, 'blog/post-list.html', context)




