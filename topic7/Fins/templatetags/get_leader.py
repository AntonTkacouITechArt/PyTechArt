from django import template
from django.db.models import Q, Sum, Count, QuerySet
from django.http import HttpResponse
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def get_leader(dep1, dep2, field: str):
    query = {
        'staff_amount': lambda x: x.staff_amount,

        'total_sold_goods': lambda x: QuerySet(x).filter(
            id__exact=x.id,
            item_filter__is_sold__exact=True,
        ).aggregate(
            sum=Sum('item_filter__price')).get('sum'),

        'total_unsold_goods': lambda x: QuerySet(x).filter(
            id__exact=x.id,
            item_filter__is_sold__exact=False,
        ).aggregate(
            sum=Sum('item_filter__price')).get('sum'),

        'total_cost_goods': lambda x: QuerySet(x).filter(
            id__exact=x.id,
        ).aggregate(
            sum=Sum('item_filter__price')).get('sum'),

        'count_sold_goods': lambda x: QuerySet(x).filter(
            id__exact=x.id,
            item_filter__is_sold__exact=True,
        ).aggregate(
            cnt=Count('item_filter__id')).get('cnt'),

        'count_unsold_goods': lambda x: QuerySet(x).filter(
            id__exact=x.id,
            item_filter__is_sold__exact=False,
        ).aggregate(
            cnt=Count('item_filter__id')).get('cnt'),

        'count_goods': lambda x: QuerySet(x).filter(
            id__exact=x.id,
        ).aggregate(
            cnt=Count('item_filter__id')
        ).get('cnt'),
    }

    d1 = ''
    d2 = ''
    result = ''

    if field == 'staff_amount':
        d1 = query.get('staff_amount')(dep1)
        d2 = query.get('staff_amount')(dep2)
    elif field == 'total_sold_goods':
        d1 = query.get('total_sold_goods')(dep1)
        d2 = query.get('total_sold_goods')(dep2)
    elif field == 'total_unsold_goods':
        d1 = query.get('total_unsold_goods')(dep1)
        d2 = query.get('total_unsold_goods')(dep2)
    elif field == 'total_cost_goods':
        d1 = query.get('total_cost_goods')(dep1)
        d2 = query.get('total_cost_goods')(dep2)
    elif field == 'count_sold_goods':
        d1 = query.get('count_sold_goods')(dep1)
        d2 = query.get('count_sold_goods')(dep2)
    elif field == 'count_unsold_goods':
        d1 = query.get('count_unsold_goods')(dep1)
        d2 = query.get('count_unsold_goods')(dep2)
    elif field == 'count_goods':
        d1 = query.get('count_goods')(dep1)
        d2 = query.get('count_goods')(dep2)

    d1 = d1 or 0
    d2 = d2 or 0
    if d1 > d2:
        result = f'<tr><td>{field}</td><td class="more_than_another">{d1}</td><td>{d2}</td></tr>'
    else:
        result = f'<tr><td>{field}</td><td>{d1}</td><td class="more_than_another">{d2}</td></tr>'
    return format_html(result)
