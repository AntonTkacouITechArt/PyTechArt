from django import template
from django.utils.html import format_html

register = template.Library()


@register.filter(needs_autoescape=True)
def pluralize_rus(value, autoescape=True):
    result = ''
    if value in [0, 5, 6, 7, 8, 9, 10]:
        result = "ов"
    elif value in [2, 3, 4]:
        result = 'а'
    else:
        result = ''
    return format_html(result)
