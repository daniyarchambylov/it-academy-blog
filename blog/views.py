from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _


def test_messages(request):
    messages.success(request, _('This is success message'))
    messages.error(request, _('This is error message'), extra_tags='alert')
    messages.info(request, _('This is information message'), extra_tags='primary')
    messages.warning(request, _('This is warning message'), extra_tags='warn')

    return render(request, 'blog/test-messages.html')
