from django.urls import path

from Fins.views import IndexView, ShopDetailView, ItemCreateView,\
    ItemUpdateView, ItemDeleteView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('index/<int:pk>/', ShopDetailView.as_view(), name='shop_detail'),
    path('index/<int:pk>/<int:dep>/new/',
         ItemCreateView.as_view(), name='add_item_into_department'),
    path('index/<int:pk>/<int:dep>/<int:item>/update/',
         ItemUpdateView.as_view(), name='update_item_into_department'),
    path('index/<int:pk>/<int:dep>/<int:item>/delete/',
         ItemDeleteView.as_view(), name='delete_item_into_department'),
]