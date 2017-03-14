from django.shortcuts import render

from blog.posts.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {
        'posts': posts,
    })


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'posts/detail.html', {
        'post': post,
    })


def deleted_posts(request):
    return render(request, 'posts/deleted_posts.html')

