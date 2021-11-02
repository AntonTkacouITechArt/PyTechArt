# Item
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, UpdateView

from Fins.models import Item, Department


class ItemDetail(DeleteView):
    model = Item
    template_name = 'item/item_detail.html'
    context_object_name = 'item'


class ItemCreateView(CreateView):
    model = Item
    template_name = 'item/item_new.html'
    fields = ['name', 'description', 'price', 'is_sold', 'comments']

    def post(self, request, *args, **kwargs):
        new_item = Item.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            price=request.POST.get('price'),
            is_sold=True if request.POST.get('is_sold') == "on" else False,
            comments=request.POST.get('comments').split(','),
            department=Department.objects.get(id=kwargs.get('dep_pk'))
        ).save()
        return HttpResponseRedirect(f"/fins/index/{kwargs['shop_pk']}/")


class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'item/item_update.html'
    fields = ['name', 'description', 'price', 'is_sold', 'comments']
    success_url = reverse_lazy('index')


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item/item_delete.html'
    success_url = reverse_lazy('index')
