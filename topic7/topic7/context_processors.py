from django.db.models import Count, IntegerField, Q
from Fins.models import Item


def items_amount_processor(request):
    ITEMS_AMOUNT = Item.objects.aggregate(cnt_item=Count(
        'id',
        filter=Q(is_sold__iexact='false'),
        output_field=IntegerField(),
    )).get('cnt_item')
    return {'ITEMS_AMOUNT': ITEMS_AMOUNT}
