# unsold item
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView
from Fins.models import Item


class UnSoldItemView(PermissionRequiredMixin, TemplateView):
    template_name = 'unsold_items/unsold_items.html'
    context_object_name = 'data'
    permission_required = 'Fins.delete_shop'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.filter(is_sold__exact=False).all()
        return context

    def post(self, *args, **kwargs):
        if self.request.POST.get('Delete'):
            Item.objects.filter(is_sold__exact=False).delete()
        return redirect('fins/index')
