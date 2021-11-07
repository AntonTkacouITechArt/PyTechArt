# Shop
from django.contrib.auth.mixins import PermissionRequiredMixin, \
    LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from Fins.models import Shop


class ShopListView(ListView):
    model = Shop
    template_name = 'index.html'
    context_object_name = 'shops'

    def post(self, request):
        print(self.request.user)
        return HttpResponseRedirect(f"{self.request.POST.get('value')}/")


class ShopDetailView(DetailView):
    model = Shop
    template_name = 'shop/shop_detail.html'
    context_object_name = 'shop'


class ShopDetailView2(LoginRequiredMixin, DetailView):
    model = Shop
    template_name = 'shop/shop_detail2.html'
    context_object_name = 'shop'


class ShopUpdateView(PermissionRequiredMixin, UpdateView):
    model = Shop
    template_name = 'shop/shop_update.html'
    fields = ['name', 'address', 'staff_amount']
    permission_required = 'Fins.change_shop'


class ShopDeleteView(PermissionRequiredMixin, DeleteView):
    model = Shop
    template_name = 'shop/shop_delete.html'
    success_url = reverse_lazy('index')
    permission_required = 'Fins.delete_shop'
