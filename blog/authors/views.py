from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from blog.authors.forms import AddAuthorForm, EditAuthorEmailForm, AddAuthorModelForm, EditAuthorEmailModelForm
from blog.authors.models import Author


def authors_list(request):
    category_name = request.GET.get('name')
    authors = Author.objects.all()

    if category_name:
        authors = authors.filter(post__categories__name__istartswith=category_name).distinct()

    return render(request, 'authors/list.html', locals())


def authors_add(request):
    form = AddAuthorModelForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            author = form.save()

            messages.success(request, 'New author has been added: {}.'.format(author))

            return redirect(reverse('authors-list'))
        else:
            # print form.errors
            # {
            #   'email': ['error1', 'error2'],
            #   'date_of_birth': ['error message'],
            #   '__all__': ['errors',]
            # }
            default_error = 'Something went wrong. Please try again.'
            error_message = form.errors['__all__'] if '__all__' in form.errors else default_error

        messages.error(request, error_message, extra_tags='alert')

    return render(request, 'authors/add.html', locals())


def authors_details(request, author_id):
    author = Author.objects.get(id=author_id)
    posts = author.post_set.all()
    # posts = Post.objects.filter(author=author)
    return render(request, 'authors/details.html', locals())


def author_edit_email(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    form = EditAuthorEmailModelForm(request.POST or None, instance=author)

    # form = EditAuthorEmailForm(request.POST or None, initial={
    #     'author': author_id,
    # })

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Email has been changed.', extra_tags='primary')
            return redirect(reverse('authors-details', args=[author_id]))
        else:
            messages.error(request, 'Something went wrong. Please try again.', extra_tags='alert')
    return render(request, 'authors/edit-email.html', locals())
