from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 6)

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {
        'posts': posts,
    }

    return render(request, 'posts/index.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'posts/form.html', context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    context = {
        'post': post,
    }

    return render(request, 'posts/detail.html', context)


def update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm(instance=post)
    
    context = {
        'form': form,
    }

    return render(request, 'posts/form.html', context)


def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('posts:index')
