from django.db.models import Count, IntegerField, Q

from testappdjango.models import Mark


def mark_amount_processor(request) -> dict:
    MARK_AMOUNT = Mark.objects.aggregate(cnt_mark=Count(
        'id',
        output_field=IntegerField(),
    )).get('cnt_mark')
    return {'MARK_AMOUNT': MARK_AMOUNT}
