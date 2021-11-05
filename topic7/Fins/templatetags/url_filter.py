from django import template
from django.urls import reverse_lazy
from django.utils.html import format_html
from Fins.models import Shop, Department, Item

register = template.Library()


@register.filter(needs_autoescape=True)
def url(value, autoescape=True):
    result = ''
    if isinstance(value, Shop):
        link = reverse_lazy('shop_detail2', kwargs={'pk': value.id})
        result = f'<a href="{link}">{value.name}</a>'
    if isinstance(value, Department):
        link = reverse_lazy('department_detail',
                            kwargs={
                                'shop_pk': value.shop.id,
                                'pk': value.id,
                            })
        result = f'<a href="{link}">{value.sphere}</a>'
    if isinstance(value, Item):
        link = reverse_lazy("item_detail",
                            kwargs={
                                'pk': value.id,
                                'shop_pk': value.department.shop.id,
                                'dep_pk': value.department.id,
                            })
        result = f'<a href="{link}">{value.name}</a>'
    return format_html(result)
