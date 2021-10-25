from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from Fins.models import Shop
import typing


class IndexView(ListView):
    model = Shop
    template_name = 'index.html'
    context_object_name = 'shops'

    def post(self, pk: typing.Union[str, int]):
        return HttpResponseRedirect(f'index/{pk}/')


class ShopDetailView(DetailView):
    model = Shop
    template_name = 'shop_detail.html'
    context_object_name = 'shop'
