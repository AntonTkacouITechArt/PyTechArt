from django.urls import path

from rest_api.views import ShopAPIListView, ShopAPIDetailView, DepartmentAPIListView, \
    DepartmentAPIDetailView, ItemAPIListView, ItemAPIDetailView, ItemUnsoldDeleteView

urlpatterns = [
    # API
    # ITEM
    path('items/', ItemAPIListView.as_view()),
    path('items/<int:pk>/', ItemAPIDetailView.as_view()),
    path('unsold_items/', ItemUnsoldDeleteView.as_view()),
    # DEPARTMENTS
    path('departments/', DepartmentAPIListView.as_view()),
    path('departments/<int:pk>/', DepartmentAPIDetailView.as_view()),
    # SHOPS
    path('shops/', ShopAPIListView.as_view()),
    path('shops/<int:pk>/', ShopAPIDetailView.as_view()),
]
