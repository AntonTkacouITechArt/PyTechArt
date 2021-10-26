from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView,\
    CreateView
from Fins.models import Shop, Item
from django.urls import reverse_lazy

# Create your views here.



class IndexView(ListView):
    model = Shop
    template_name = 'index.html'
    context_object_name = 'shops'

    def post(self, request):
        return HttpResponseRedirect(f"{self.request.POST.get('value')}/")


class ShopDetailView(DetailView):
    model = Shop
    template_name = 'shop_detail.html'
    context_object_name = 'shop'

class ItemCreateView(CreateView):
    model = Item
    template_name = 'item_new.html'
    fields = ['name', 'description', 'is_sold', 'comments']
    # 'price',


class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'item_update.html'
    fields = ['name', 'description', 'is_sold', 'comments']
    #  'price'

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_delete.html'
    success_url = reverse_lazy('index')


