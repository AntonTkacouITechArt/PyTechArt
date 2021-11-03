from django import forms
from django.forms import Form, BooleanField, ChoiceField, ModelChoiceField

from Fins.models import Shop, Department

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


class CompareForm(Form):
    # def __init__(self, shop_pk, *args, **kwargs):
    #     super(CompareForm, self).__init__(*args, **kwargs)
    #     res = Department.objects.filter(
    #         shop__exact=kwargs.get('shop_pk')).all()
    #     print(res)
    #     self.fields['department_1'].__choices = res
    #     print(self.fields['department_1'].__dict__)
    #     print(shop_pk)

    department_1 = ChoiceField(
        required=True,
        widget=forms.Select, )
    department_2 = ChoiceField(
        required=True,
        widget=forms.Select,
    )
    staff_amount = BooleanField(required=False)
    total_sold_goods = BooleanField(required=False)
    total_unsold_goods = BooleanField(required=False)
    total_cost_goods = BooleanField(required=False)
    total_sold_goods = BooleanField(required=False)
    total_unsold_goods = BooleanField(required=False)
    total_goods = BooleanField(required=False)
