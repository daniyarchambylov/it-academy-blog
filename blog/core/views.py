from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def signup(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            messages.success(request, 'New user has been created %s.'% user.username)
        else:
            messages.error(request, 'Error', extra_tags='alert')
    return render(request, 'core/signup.html', locals())


def signin(request):
    form = AuthenticationForm(request, request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('posts-index')
        else:
            messages.error(request, 'Error: %s' % form.errors, extra_tags='alert')
    return render(request, 'core/signin.html', locals())
