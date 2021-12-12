from django import template
from django.urls import reverse_lazy
from django.utils.html import format_html

from testappdjango.models import Student, Teacher

register = template.Library()


@register.filter(needs_autoescape=True)
def url(value, autoescape=True):
    result = ''
    if isinstance(value, Student):
        link = reverse_lazy('student_detail', kwargs={'pk': value.pk})
        result = f'<a href="{link}">{value.name} {value.surname}</a>'
    if isinstance(value, Teacher):
        link = reverse_lazy('teacher_detail', kwargs={'pk': value.pk})
        result = f'<a href="{link}">{value.name} {value.surname}</a>'
    return format_html(result)