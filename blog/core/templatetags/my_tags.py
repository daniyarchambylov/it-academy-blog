from django.template import Library
from django.templatetags.static import static
from django.urls import reverse
from django.utils.safestring import mark_safe

register = Library()


@register.filter
def get_image(value, fallback='http://placehold.it/350x150'):
    if value:
        return value.url
    return fallback


@register.filter
def get_image2(value):
    if value:
        return value.url
    return static('no-image.png')


@register.filter
def make_link(obj, url):
    url = reverse(url, args=[obj.id])
    return '<a href="{0}">{1}</a>'.format(url, obj.title)