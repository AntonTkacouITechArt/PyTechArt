from django.urls import path

from Fins.views import ShopListView, ShopDetailView, ItemCreateView,\
    ItemUpdateView, ItemDeleteView, ItemDetail

urlpatterns = [
    path('index/', ShopListView.as_view(),
         name='index'),
    path('index/<shop_pk>/', ShopDetailView.as_view(),
         name='shop_detail'),

    path('index/<int:shop_pk>/<int:dep_pk>/<int:item_pk>',
         ItemDetail.as_view(), name='detail_item'),
    path('index/<int:shop_pk>/<int:dep_pk>/item/new/',
         ItemCreateView.as_view(), name='create_item_into_department'),
    path('index/<int:shop_pk>/<int:dep_pk>/<int:item_pk>/update/',
         ItemUpdateView.as_view(), name='update_item_into_department'),
    path('index/<int:shop_pk>/<int:dep_pk>/<int:item_pk>/delete/',
         ItemDeleteView.as_view(), name='delete_item_into_department'),
]