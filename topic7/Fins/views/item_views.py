# Item
from django.contrib.auth.mixins import PermissionRequiredMixin, \
    LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, UpdateView, DetailView

from Fins.models import Item, Department


class ItemDetail(LoginRequiredMixin, DetailView):
    model = Item
    template_name = 'item/item_detail.html'
    context_object_name = 'item'


class ItemCreateView(PermissionRequiredMixin, CreateView):
    model = Item
    template_name = 'item/item_new.html'
    fields = ['name', 'description', 'price', 'is_sold', 'comments']
    permission_required = 'Fins.add_item'

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


class ItemUpdateView(PermissionRequiredMixin, UpdateView):
    model = Item
    template_name = 'item/item_update.html'
    fields = ['name', 'description', 'price', 'is_sold', 'comments']
    success_url = reverse_lazy('index')
    permission_required = 'Fins.change_item'


class ItemDeleteView(PermissionRequiredMixin, DeleteView):
    model = Item
    template_name = 'item/item_delete.html'
    success_url = reverse_lazy('index')
    permission_required = 'Fins.delete_item'
