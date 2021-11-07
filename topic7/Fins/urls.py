from django.urls import path
from Fins.views.AuthViews import AuthLoginView, AuthLogoutView
from Fins.views.department_views import DepartmentDetailView, \
    DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView
from Fins.views.filter_views import FilterShopView, FilterItemView
from Fins.views.forms_view import CompareFormView
from Fins.views.item_views import ItemDetail, ItemCreateView, ItemUpdateView, \
    ItemDeleteView
from Fins.views.no_goods_views import NoGoodsView
from Fins.views.shop_views import ShopListView, ShopDetailView, \
    ShopDetailView2, ShopUpdateView, ShopDeleteView
from Fins.views.unsold_item import UnSoldItemView

urlpatterns = [
    # shop
    path('index/',
         ShopListView.as_view(), name='index'),
    path('index/<int:pk>/',
         ShopDetailView.as_view(), name='shop_detail'),
    path('index/<int:pk>/detail/',
         ShopDetailView2.as_view(), name='shop_detail2'),
    path('index/<int:pk>/update/',
         ShopUpdateView.as_view(), name='shop_update'),
    path('index/<int:pk>/delete/',
         ShopDeleteView.as_view(), name='shop_delete'),

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

    # login
    path('login/',
         AuthLoginView.as_view(), name='login'),
    path('logout/',
         AuthLogoutView.as_view(), name='logout'),

    # filter
    path('filter/item/<int:number>/',
         FilterItemView.as_view(), name='filter_item'),
    path('filter/shop/<int:number>/',
         FilterShopView.as_view(), name='filter_shop'),

    # compare
    path('index/<int:shop_pk>/compare/',
         CompareFormView.as_view(), name='compare_form'),

    # no goods
    path('nogoods/',
         NoGoodsView.as_view(), name='no_goods'),

    # unsold_items
    path('unsold_items/',
         UnSoldItemView.as_view(), name="unsold_items")

]
