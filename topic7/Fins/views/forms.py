from django import forms
from django.forms import Form, BooleanField

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


class CompareForm(Form):
    select_department_1 = forms.MultipleChoiceField(
        required=True,
        widget=forms.Select,
        choices=FAVORITE_COLORS_CHOICES,
    )
    select_department_2 = forms.MultipleChoiceField(
        required=True,
        widget=forms.Select,
        choices=FAVORITE_COLORS_CHOICES,
    )
    staff_amount = BooleanField(required=False)
    total_sold_goods = BooleanField(required=False)
    total_unsold_goods = BooleanField(required=False)
    total_cost_goods = BooleanField(required=False)
    total_sold_goods = BooleanField(required=False)
    total_unsold_goods = BooleanField(required=False)
    total_goods = BooleanField(required=False)
