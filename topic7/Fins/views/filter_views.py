from django.db.models import Q
from django.shortcuts import render
from django.views import View

from Fins.models import Item


class FilterItemView(View):
    def get(self, request, *args, **kwargs):
        query = [
            # 1 (0)
            lambda x: x.objects.filter(
                department__shop__name__istartswith='i').all(),
            # 2 (1)
            lambda x: x.objects.filter(
                price__gt=10,
                department__staff_amount__lt=50
            ).all(),
            # 3 (2)
            lambda x: x.objects.filter(
                Q(price__gt=20) | Q(department__shop__staff_amount__gt=50),
            ).all(),
            # 4 (3)
            lambda x: x.objects.filter(
                department_id__in=[1, 3, 5, 6]
            ).all(),
            # 5 (4)
            lambda x: x.objects.filter(
                Q(
                    price__gt=10,
                    name__icontains='a'
                ) | Q(
                    price__lt=20,
                    name__icontains='o'
                )),
            # 6 (5)
            lambda x: x.objects.filter(
                price_exact=department_staff_amount + 10
            )
        ]
        print(kwargs)
        context = {'data': query[kwargs['number']](Item)}
        return render(request, 'filter/filter_item.html', context=context)


class FilterShopView(View):
    def get(self, request, *args, **kwargs):
        query = [
            # 1 (0)
            lambda x: x.objects.filter(
                department__shop__name__istartswith='i').all(),
            # 2 (1)
            lambda x: x.objects.filter(
                price__gt=10,
                department__staff_amount__lt=50
            ).all(),
            # 3 (2)
            lambda x: x.objects.filter(
                Q(price__gt=20) | Q(department__shop__staff_amount__gt=50),
            ).all(),
            # 4 (3)
            lambda x: x.objects.filter(
                department_id__in=[1, 3, 5, 6]
            ).all(),
            # 5 (4)
            lambda x: x.objects.filter(
                Q(
                    price__gt=10,
                    name__icontains='a'
                ) | Q(
                    price__lt=20,
                    name__icontains='o'
                )),
            # 6 (5)
            lambda x: x.objects.filter(
                price_exact=department_staff_amount + 10
            )
        ]
        print(kwargs)
        context = {'data': query[kwargs['number']](Item)}
        return render(request, 'filter/filter_shop.html', context=context)
