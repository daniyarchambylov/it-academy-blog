from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST

from blog.posts.forms import PostForm, PostDeleteForm
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

    delete_form = PostDeleteForm(initial={'post': id})

    return render(request, 'posts/detail.html', {
        'post': post,
        'delete_form': delete_form,
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


@require_POST
def change_status(request, id):
    post = Post.objects.get(id=id)
    post.change_status()
    return redirect(reverse('posts-detail', args=[id, ]))

# from django.views.decorators.http import require_POST, require_GET, require_http_methods,
# @require_POST
# @require_GET
# validate methods DELETE or PUT @require_http_methods(['DELETE', 'PUT'])

@require_POST
def delete_post(request, id):
    form = PostDeleteForm(request.POST)
    if form.is_valid():
        form.delete()
        messages.success(request, 'Post %s has been deleted.' % id)
        return redirect(reverse('posts-index'))

    messages.error(request, 'Could not delete post %s' % id, extra_tags='alert')
    return redirect(reverse('posts-detail', args=[id, ]))


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
