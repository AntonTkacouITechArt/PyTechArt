from django.urls import path

from Fins.views.department_views import DepartmentDetailView, \
    DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView
from Fins.views.filter_views import FilterShopView, FilterItemView
from Fins.views.item_views import ItemDetail, ItemCreateView, ItemUpdateView, \
    ItemDeleteView
from Fins.views.shop_views import ShopListView, ShopDetailView

urlpatterns = [
    # shop
    path('index/',
         ShopListView.as_view(), name='index'),
    path('index/<int:pk>/',
         ShopDetailView.as_view(), name='shop_detail'),

    # ???????
    # path('index/<int:pk>/detail/',
    #      ShopDetailView.as_view(), name='shop_detail2'),

    # department
    path('index/<int:shop_pk>/<int:pk>/',
         DepartmentDetailView.as_view(), name='department_detail'),
    path('index/<int:shop_pk>/department/new/',
         DepartmentCreateView.as_view(), name='department_create'),
    path('index/<int:shop_pk>/<int:pk>/update/',
         DepartmentUpdateView.as_view(), name='department_update'),
    path('index/<int:shop_pk>/<int:pk>/delete/',
         DepartmentDeleteView.as_view(), name='department_delete'),

    # item
    path('index/<int:shop_pk>/<int:dep_pk>/<int:pk>/',
         ItemDetail.as_view(), name='item_detail'),
    path('index/<int:shop_pk>/<int:dep_pk>/item/new/',
         ItemCreateView.as_view(), name='create_item_into_department'),
    path('index/<int:shop_pk>/<int:dep_pk>/<int:pk>/update/',
         ItemUpdateView.as_view(), name='update_item_into_department'),
    path('index/<int:shop_pk>/<int:dep_pk>/<int:pk>/delete/',
         ItemDeleteView.as_view(), name='delete_item_into_department'),

    # filter
    path('filter/item/<int:number>/',
         FilterItemView.as_view(), name='filter_item'),
    path('filter/shop/<int:number>/',
         FilterShopView.as_view(), name='filter_shop'),

]