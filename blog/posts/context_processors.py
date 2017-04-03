# -*- coding: utf-8 -*-
from blog.categories.models import Category


def categories(request):
    return {
        'blog_categories': Category.objects.all()
    }