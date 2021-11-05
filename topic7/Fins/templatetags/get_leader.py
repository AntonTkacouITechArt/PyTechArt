from django import template
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def get_leader(dep1, dep2, field):

    return format_html()
