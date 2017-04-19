from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.translation import ungettext
from django.views.decorators.http import require_POST

from blog.posts.forms import PostForm, PostDeleteForm, EditPostForm, PostModelForm, FilterPostForm
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
    post = get_object_or_404(Post, id=id)
    author = post.author
    delete_form = PostDeleteForm(initial={'post': id})

    return render(request, 'posts/detail.html', {
        'post': post,
        'author': author,
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
    text = 'piblished' if post.status == 'd' else 'draft'
    return JsonResponse({
        'text': text,
    })

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


def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = EditPostForm(request.POST or None, initial={
        'post': post.id,
        'title': post.title,
        'description': post.description,
        'author': post.author,
    })

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Post has been updated')
            return redirect(reverse('posts-detail', args=[post.id]))
        else:
            messages.error(request, 'Could not update post', extra_tags='alert')

    return render(request, 'posts/update_post.html', locals())


def create_post_with_forms(request):
    message = None

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'New post has been created.')
            return redirect('posts-index')
        else:
            messages.error('There is an error in your form inputs')
    else:
        form = PostForm()

    context = {
        'form': form,
        'message': message,
    }

    return render(request, 'posts/create_post_form.html', context)

def create_post_with_modelforms(request):
    form = PostModelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'New post has been created.')
            return redirect('posts-index')
        else:
            messages.error(request, 'There is an error in your form inputs', extra_tags='alert')

    return render(request, 'posts/create_post_form.html', locals())


def filter_posts_view(request):
    form = FilterPostForm(request.GET or None)
    posts = Post.objects.all()
    if form.is_valid():
        posts = form.filter(posts)
    return render(request, 'posts/filter_posts.html', locals())


def count_posts(request):
    count = 53
    text = ungettext(
        'There is %(count)d post',
        'There are %(count)d posts',
        count
    ) % { 'count': count }
    return render(request, 'posts/count_posts.html', locals())
