from django.db.models import Q, F, Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from Fins.models import Item, Shop


class FilterItemView(View):
    def get(self, request, *args, **kwargs):
        query = [
            # 1 (0)
            Item.objects.filter(
                department__shop__name__istartswith='i'),
            # 2 (1)
            Item.objects.filter(
                price__gt=10,
                department__staff_amount__lt=50
            ),
            # 3 (2)
            Item.objects.filter(
                Q(price__gt=20) | Q(department__shop__staff_amount__gt=50),
            ),
            # 4 (3)
            Item.objects.filter(
                department_id__in=[1, 3, 5, 6]
            ),
            # 5 (4)
            Item.objects.filter(
                Q(
                    price__gt=10,
                    name__icontains='a'
                ) | Q(
                    price__lt=20,
                    name__icontains='o'
                )),
            # 6 (5)
            Item.objects.filter(
                Q(price__exact=F('department__staff_amount') + 10)
            )

        ]
        if kwargs['number'] in range(1, 7):
            context = {'data': query[kwargs['number'] - 1].all()}
            return render(request, 'filter/filter_item.html', context=context)
        else:
            return HttpResponse('<h1>No such query</h1>')


class FilterShopView(View):
    def get(self, request, *args, **kwargs):
        query = [
            # 1 (0)
            Shop.objects.annotate(
                department_staff=Sum(
                    'department_filter__staff_amount')).filter(
                ~Q(staff_amount__exact=F('department_staff'))
            ).order_by('pk'),
            # 2 (1)
            Shop.objects.filter(
                Q(department_filter__item_filter__price__lt=5)
            ).order_by('pk').distinct(),
            # 3 (2)
            Shop.objects.raw(
                """
                SELECT 
                    "Fins_shop"."id",
                    "Fins_shop"."name",
                    COUNT("Fins_shop"."name") as count_goods,
                    MAX("Fins_item"."price") as max_price,
                    Count("Fins_shop"."name") as count_department,
                    SUM("Fins_department"."staff_amount")
                FROM "Fins_shop" 
                INNER JOIN "Fins_department" 
                ON "Fins_department"."shop_id" = "Fins_shop"."id"
                INNER JOIN "Fins_item" 
                ON "Fins_item"."department_id" = "Fins_department"."id"
                GROUP BY "Fins_shop"."id"
                """
            ),
            # 4 (3)
            Item.objects.raw(
                """
                SELECT
                    "Fins_shop".id,
                    "Fins_shop".name,
                   COUNT(*) as count_goods
                FROM "Fins_item" i
                INNER JOIN "Fins_department" ON "Fins_department"."id" = i."department_id"
                INNER JOIN "Fins_shop" ON "Fins_shop"."id" = "Fins_department"."shop_id"
                WHERE i."price" <= 10 OR i."name" LIKE '%%a%%'
                GROUP BY "Fins_shop"."id";
                """
            )
        ]
        if kwargs['number'] in range(1, 5):
            if kwargs['number'] in [3, 4]:
                context = {'data': query[kwargs['number'] - 1]}
            else:
                context = {'data': query[kwargs['number'] - 1].all()}
            return render(request, 'filter/filter_shop.html', context=context)
        else:
            return HttpResponse('<h1>No such query</h1>')
