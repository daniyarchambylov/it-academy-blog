from django.template import Library
from django.templatetags.static import static

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
