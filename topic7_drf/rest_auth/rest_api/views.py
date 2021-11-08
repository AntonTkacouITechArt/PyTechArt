from typing import Type

from django.db.models import Q, QuerySet
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_api.models import Item, Department, Shop
from rest_api.serializers import AdminShopSerializer, UserShopSerializer, \
    NamelessShopSerializer, AdminDepartmentSerializer, \
    UserDepartmentSerializer, NamelessDepartmentSerializer, AdminItemSerializer, \
    UserItemSerializer, NamelessItemSerializer, AnonymousItemSerializer
from rest_api.permissions import IsAnonymous, IsAuthenticated, IsStaff, \
    IsStaffReadOnly, IsSuperUser
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer


# SHOPS

class ShopAPIListView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticated | IsStaff | IsSuperUser,
    ]

    def get_serializer_class(self) -> Type[BaseSerializer]:
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return AdminShopSerializer
            elif self.request.user.get_full_name():
                return UserShopSerializer
            return NamelessShopSerializer

    def get_queryset(self) -> Type[QuerySet]:
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return Shop.objects.all()
            else:
                return Shop.objects.filter(
                    Q(department_filter__item_filter__isnull=False) |
                    Q(department_filter__item_filter__is_sold=False)
                ).distinct().order_by('pk').all()


class ShopAPIDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsSuperUser | IsStaff | IsAuthenticated,
    ]

    def get_serializer_class(self) -> Type[BaseSerializer]:
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return AdminShopSerializer
            elif self.request.user.get_full_name():
                return UserShopSerializer
            return NamelessShopSerializer

    def get_queryset(self) -> Type[QuerySet]:
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return Shop.objects.all()
            else:
                return Shop.objects.filter(
                    Q(department_filter__item_filter__isnull=False) |
                    Q(department_filter__item_filter__is_sold=False)
                ).distinct().order_by('pk').all()


# DEPARTMENTS

class DepartmentAPIListView(ListCreateAPIView):
    permission_classes = [
        IsSuperUser | IsStaff | IsAuthenticated
    ]

    def get_serializer_class(self) -> Type[BaseSerializer]:
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return AdminDepartmentSerializer
            elif self.request.user.get_full_name():
                return UserDepartmentSerializer
            return NamelessDepartmentSerializer

    def get_queryset(self) -> Type[QuerySet]:
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return Department.objects.all()
            else:
                return Department.objects.filter(
                    Q(item_filter__isnull=False) |
                    Q(item_filter__is_sold=False)
                ).distinct().order_by('pk').all()


class DepartmentAPIDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsSuperUser | IsStaff | IsAuthenticated,
    ]

    def get_serializer_class(self) -> Type[BaseSerializer]:
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return AdminDepartmentSerializer
            elif self.request.user.get_full_name():
                return UserDepartmentSerializer
            return NamelessDepartmentSerializer

    def get_queryset(self) -> Type[QuerySet]:
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return Department.objects.all()
            else:
                return Department.objects.filter(
                    Q(item_filter__isnull=False) |
                    Q(item_filter__is_sold=False)
                ).distinct().order_by('pk').all()


# ITEMS

class ItemAPIListView(ListCreateAPIView):
    permission_classes = [
        IsSuperUser | IsStaff | IsAuthenticated | IsAnonymous,
    ]

    def get_serializer_class(self) -> Type[BaseSerializer]:
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return AdminItemSerializer
            elif self.request.user.get_full_name():
                return UserItemSerializer
            else:
                return NamelessItemSerializer
        else:
            return AnonymousItemSerializer

    def get_queryset(self) -> Type[QuerySet]:
        if self.request.user.is_staff:
            return Item.objects.all()
        else:
            return Item.objects.filter(is_sold__exact=False).all()


class ItemAPIDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsSuperUser | IsStaff | IsAuthenticated, IsAnonymous
    ]

    def get_serializer_class(self) -> Type[BaseSerializer]:
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return AdminItemSerializer
            elif self.request.user.get_full_name():
                return UserItemSerializer
            else:
                return NamelessItemSerializer
        else:
            return AnonymousItemSerializer

    def get_queryset(self) -> Type[QuerySet]:
        if self.request.user.is_staff:
            return Item.objects.all()
        else:
            return Item.objects.filter(is_sold__exact=False).all()


class ItemUnsoldDeleteView(ListAPIView):
    queryset = Item.objects.filter(is_sold__exact=False).all()
    serializer_class = AdminItemSerializer
    permission_classes = [IsSuperUser, ]

    def delete(self, request) -> Response:
        data = Item.objects.filter(is_sold__exact=False).all()
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#
