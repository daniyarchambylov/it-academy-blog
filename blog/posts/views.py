from django.contrib import messages
from django.shortcuts import render

from blog.posts.forms import PostForm
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
    error_message = None
    is_created = False

    if request.method == 'POST':
        title = request.POST['post_title']
        description = request.POST['post_text']

        if len(title) > 0 and len(description) > 0:
            post = Post(title=title, description=description)
            post.save()
            is_created = True
        else:
            error_message = 'title or description is empty'

    context = {
        'post_created': is_created,
        'errors': error_message,
    }

    return render(request, 'posts/create_post.html', context)


def create_post_with_forms(request):
    message = None

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']

            post = Post(title=title, description=description)
            post.save()

            messages.success(request, 'New post has been created.')
        else:
            messages.error('There is an error in your form inputs')
    else:
        form = PostForm()

    context = {
        'form': form,
        'message': message,
    }

    return render(request, 'posts/create_post_form.html', context)
