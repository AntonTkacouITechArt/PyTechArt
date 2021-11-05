from django import template
from django.db.models import Sum, Count, QuerySet
from django.utils.html import format_html

COMPARE_FIELDS = ['staff_amount', 'total_sold_goods', 'total_unsold_goods',
                  'total_cost_goods', 'count_sold_goods', 'count_unsold_goods',
                  'count_goods']

COMPARE_QUERY = {
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

register = template.Library()


@register.simple_tag
def get_leader(dep1, dep2, field: str):
    result = '<tr><td>NO SUCH FIELD TO COMPARE</td></tr>'
    if field in COMPARE_FIELDS:
        d1 = COMPARE_QUERY.get(field)(dep1) or 0
        d2 = COMPARE_QUERY.get(field)(dep2) or 0
        if d1 > d2:
            result = f'<tr><td>{field}</td><td class="more_than_another">{d1}</td><td>{d2}</td></tr>'
        else:
            result = f'<tr><td>{field}</td><td>{d1}</td><td class="more_than_another">{d2}</td></tr>'
    return format_html(result)
