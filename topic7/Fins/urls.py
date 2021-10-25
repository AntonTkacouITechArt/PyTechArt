from django.urls import path

from Fins.views import IndexView, ShopDetailView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('index/<int:pk>', ShopDetailView.as_view(), name='shop_detail'),
]