# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views import View

from blog.posts.forms import PostModelForm


class ViewMixin(object):
    ping = 'pong'

class CustomTemplateView(ViewMixin, TemplateView):
    template_name = 'cbv/second_view.html'

    def get_id(self, obj):
        return obj.id

    def get_context_data(self, **kwargs):
        ctx = super(CustomTemplateView, self).get_context_data(**kwargs)
        ctx['ping'] = self.ping
        return ctx


class CustomTemplateView2(ViewMixin, TemplateView):
    template_name = 'cbv/third_view.html'

    def get_context_data(self, **kwargs):
        ctx = super(CustomTemplateView2, self).get_context_data(**kwargs)
        ctx['ping'] = self.ping
        return ctx


@method_decorator([login_required, ], name='dispatch')
class PostCBV(View):
    template_name = 'cbv/posts.html'
    form_class = PostModelForm
    #
    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(PostCBV, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'form': self.form_class(),
        })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            return redirect('posts-index')

        return render(request, self.template_name, {
            'form': form,
        })
