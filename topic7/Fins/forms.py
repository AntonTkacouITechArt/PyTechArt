from django import forms
from django.forms import Form, BooleanField, ChoiceField, ModelChoiceField

from Fins.models import Shop, Department


class CompareForm(Form):
    # department_1 = ChoiceField(
    #     required=True,
    #     widget=forms.Select, )
    # department_2 = ChoiceField(
    #     required=True,
    #     widget=forms.Select,
    # )
    department_1 = ModelChoiceField(queryset=Department.objects.all(),
                                    empty_label="Selected value")
    department_2 = ModelChoiceField(queryset=Department.objects.all(),
                                    empty_label="Selected value")
    staff_amount = BooleanField(required=False)
    total_sold_goods = BooleanField(required=False)
    total_unsold_goods = BooleanField(required=False)
    total_cost_goods = BooleanField(required=False)
    count_sold_goods = BooleanField(required=False)
    count_unsold_goods = BooleanField(required=False)
    count_goods = BooleanField(required=False)
