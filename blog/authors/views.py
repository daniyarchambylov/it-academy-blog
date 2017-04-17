from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST

from blog.authors.forms import AddAuthorModelForm, EditAuthorEmailModelForm, UserModelForm
from blog.authors.models import Author


def authors_list(request):
    category_name = request.GET.get('name')
    authors = Author.objects.all()

    if category_name:
        authors = authors.filter(post__categories__name__istartswith=category_name).distinct()

    return render(request, 'authors/list.html', locals())


def authors_add(request):
    author_form = AddAuthorModelForm(request.POST or None, request.FILES or None)
    user_form = UserModelForm(request.POST or None)

    if request.method == 'POST':
        if author_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            author = author_form.save(commit=False)
            author.user = user
            author.save()
            messages.success(request, 'New author has been added: {}.'.format(author))

            return redirect(reverse('authors-list'))
        messages.error(request, 'Something went wrong. Please try again.', extra_tags='alert')

    return render(request, 'authors/add.html', locals())


@require_POST
def create_author_ajax(request):
    res = {}

    form = AddAuthorModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user = form.save()
        res['status'] = 'success'
        res['data'] = {
            'id': user.id,
            'gender': user.gender,
        }
    else:
        res['status'] = 'error'
        res['errors'] = form.errors

    return JsonResponse(res)


def authors_details(request, author_id):
    author = Author.objects.get(id=author_id)
    posts = author.post_set.all()
    # posts = Post.objects.filter(author=author)
    return render(request, 'authors/details.html', locals())


def author_edit_email(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    form = EditAuthorEmailModelForm(request.POST or None, instance=author.user)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Email has been changed.', extra_tags='primary')
            return redirect(reverse('authors-details', args=[author_id]))
        else:
            messages.error(request, 'Something went wrong. Please try again.', extra_tags='alert')
    return render(request, 'authors/edit-email.html', locals())


def get_username(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return JsonResponse({
        'username': author.user.phone,
    })
