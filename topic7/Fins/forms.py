from django import forms
from django.forms import Form, BooleanField, ChoiceField


class CompareForm(Form):
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
    count_sold_goods = BooleanField(required=False)
    count_unsold_goods = BooleanField(required=False)
    count_goods = BooleanField(required=False)
