from django.contrib import messages
from django.shortcuts import render


def test_messages(request):
    messages.success(request, 'This is success message')
    messages.error(request, 'This is error message', extra_tags='alert')
    messages.info(request, 'This is information message', extra_tags='primary')
    messages.warning(request, 'This is warning message', extra_tags='warn')

    return render(request, 'blog/test-messages.html')
