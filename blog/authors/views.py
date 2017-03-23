from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from blog.authors.forms import AddAuthorForm, EditAuthorEmailForm
from blog.authors.models import Author


def authors_list(request):
    authors = Author.objects.all()

    return render(request, 'authors/list.html', locals())


def authors_add(request):
    form = AddAuthorForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            messages.success(request, 'New author has been added.')

            return redirect(reverse('authors-list'))

        messages.error(request, 'Something went wrong. Please try again.')

    return render(request, 'authors/add.html', locals())


def authors_details(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'authors/details.html', locals())


def author_edit_email(request, author_id):
    form = EditAuthorEmailForm(request.POST or None, initial={
        'author': author_id,
    })

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('authors-details', args=[author_id]))
        else:
            messages.error / (request, 'Something went wrong. Please try again.')
    return render(request, 'authors/edit-email.html', locals())
