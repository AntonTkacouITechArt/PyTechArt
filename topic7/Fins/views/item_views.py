# Item
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, UpdateView

from Fins.models import Item


class ItemDetail(DeleteView):
    model = Item
    template_name = 'item/item_detail.html'
    context_object_name = 'item'


class ItemCreateView(CreateView):
    model = Item
    template_name = 'item/item_new.html'
    fields = ['name', 'description', 'price', 'is_sold', 'comments']


class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'item/item_update.html'
    fields = ['name', 'description', 'price', 'is_sold', 'comments']


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item/item_delete.html'
    success_url = reverse_lazy('index')