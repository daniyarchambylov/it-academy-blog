from django.shortcuts import render


def index(request):
    return render(request, 'posts/index.html')


def post_detail(request):
    return render(request, 'posts/detail.html')


def deleted_posts(request):
    return render(request, 'posts/deleted_posts.html')

