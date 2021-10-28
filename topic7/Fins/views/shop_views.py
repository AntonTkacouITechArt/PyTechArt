# Shop
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView

from Fins.models import Shop


class ShopListView(ListView):
    model = Shop
    template_name = 'index.html'
    context_object_name = 'shops'

    def post(self, request):
        return HttpResponseRedirect(f"{self.request.POST.get('value')}/")


class ShopDetailView(DetailView):
    model = Shop
    template_name = 'shop/shop_detail.html'
    context_object_name = 'shop'