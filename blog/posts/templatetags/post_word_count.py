from django.template import Library

register = Library()


@register.filter
def my_word_count(value):
    return len(value.split())