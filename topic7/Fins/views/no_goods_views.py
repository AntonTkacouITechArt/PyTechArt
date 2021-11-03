from django.views.generic import TemplateView


class NoGoodsView(TemplateView):
    template_name = 'no_goods/no_goods.html'
