from django.conf import settings

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from blog.core.decorators import is_anonymous


@is_anonymous
def signup(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            messages.success(request, 'New user has been created %s.' % user.phone)
        else:
            messages.error(request, 'Error', extra_tags='alert')
    return render(request, 'core/signup.html', locals())


@is_anonymous
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


@login_required
# @require_POST
def signout(request):
    logout(request)
    return redirect(settings.LOGIN_URL)
