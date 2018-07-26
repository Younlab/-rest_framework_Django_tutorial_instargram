from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostCreate


def post_list(request):
    post = Post.objects.all()
    context = {
        'posts': post,
    }
    return render(request, 'posts/post_list.html', context)


def post_create(request):
    form = PostCreate()
    if request.method == 'POST':
        form = PostCreate(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post:post_list')

    context = {
        'forms': form
    }
    return render(request, 'posts/post_create.html', context)


def comment_create(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_pk)
        content = request.POST['content']
        if not content:
            raise PermissionDenied('내용을 입력하세요')
        elif not request.user.username:
            return redirect('index')
        Comment.objects.create(
            post=post,
            author=request.user,
            content=content,
        )
    return redirect('post:post_list')
