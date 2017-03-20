from django.shortcuts import render

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
        else:
            print 'error'

    return render(request, 'authors/add.html', locals())


def author_detail(request, author_id):
    author = Author.objects(id=author_id)
    return render(request, 'authors/add.html', locals())


def author_edit_email(request, author_id):
    form = EditAuthorEmailForm(request.POST or None, initial={
        'author': author_id,
    })

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        else:
            print 'error'
    return render(request, 'authors/add.html', locals())



