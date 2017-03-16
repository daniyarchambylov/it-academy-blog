from django.shortcuts import render

from blog.posts.models import Post


def index(request):
    status = request.GET.get('status')

    if status in ['d', 'p']:
        posts = Post.objects.filter(status=status)
    else:
        posts = Post.objects.all()

    return render(request, 'posts/index.html', {
        'posts': posts,
    })


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'posts/detail.html', {
        'post': post,
    })


def draft_posts(request):
    posts = Post.objects.filter(status='d')
    return render(request, 'posts/draft_posts.html', {
        'posts': posts,
    })


def published_posts(request):
    posts = Post.objects.filter(status='p')

    return render(request, 'posts/published_posts.html', {
        'posts': posts,
    })


def change_status(request, id):
    post = Post.objects.get(id=id)
    post.change_status()

    return render(request, 'posts/status_changed.html', {
        'post': post,
    })


def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return render(request, 'posts/has_been_deleted.html', {
        'post': post,
    })


def create_post(request):
    if request.method == 'POST':
        post = Post(title=request.POST['post_title'], description=request.POST['post_text'])
        post.save()
        is_created = True
    else:
        is_created = False

    context = {
        'post_created': is_created,
    }

    return render(request, 'posts/create_post.html', context)
