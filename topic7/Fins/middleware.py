from django.db.models import Count, Q
from django.shortcuts import render
from Fins.models import Item, Statistics


class NoItemsMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        item = Item.objects.aggregate(
            cnt=Count(
                'id',
                filter=Q(is_sold__exact=False),
            )
        )
        if 'admin' not in request.path and item.get('cnt') == 0:
            return render(request, 'no_goods/no_goods.html')
        response = self._get_response(request)
        print('>Work no_items_middleware')
        return response


class CountURLMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        if 'admin' not in request.path:
            try:
                obj = Statistics.objects.get(url=request.path)
                obj.amount += 1
            except Statistics.DoesNotExist:
                obj = Statistics.objects.create(url=request.path)
            obj.save()
        response = self._get_response(request)
        return response
