from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, \
    CreateView
from Fins.models import Shop, Item, Department
from django.urls import reverse_lazy


class ShopListView(ListView):
    model = Shop
    template_name = 'index.html'
    context_object_name = 'shops'

    def post(self, request):
        return HttpResponseRedirect(f"{self.request.POST.get('value')}/")


class ShopDetailView(DetailView):
    model = Shop
    template_name = 'shop_detail.html'
    context_object_name = 'shop'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department_detail.html'
    context_object_name = 'department'


class DepartmentCreateView(CreateView):
    model = Department
    template_name = 'department_new.html'
    fields = ['sphere', 'staff_amount', 'shop']


class DepartmentUpdateView(UpdateView):
    model = Department
    template_name = 'department_update.html'
    fields = ['sphere', 'staff_amount', 'shop']


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'department_delete.html'
    fields = ['sphere', 'staff_amount', 'shop']
    context_object_name = 'department'


class ItemDetail(DeleteView):
    model = Item
    template_name = 'item_detail.html'
    context_object_name = 'item'


class ItemCreateView(CreateView):
    model = Item
    template_name = 'item_new.html'
    fields = ['name', 'description', 'price', 'is_sold', 'comments']


class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'item_update.html'
    fields = ['name', 'description', 'price', 'is_sold', 'comments']


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_delete.html'
    success_url = reverse_lazy('index')
