from rest_framework import serializers
from rest_api.models import Item, Department, Shop


# SHOP SERIALIZERS
class AdminShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'address', 'staff_amount']


class UserShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'address', 'staff_amount']


class NamelessShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'address']


# DEPARTMENTS SERIALIZERS
class AdminDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'sphere', 'staff_amount', 'shop']


class UserDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'sphere', 'staff_amount', 'shop']


class NamelessDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'sphere', 'shop']


# ITEMS SERIALIZERS
class AdminItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'is_sold', 'comments',
                  'department']


class UserItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'is_sold', 'comments',
                  'department']


class NamelessItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'is_sold', 'comments',
                  'department']


class AnonymousItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'is_sold']

# class DynamicFieldsModelSerializer(serializers.ModelSerializer):
#     """
#     A ModelSerializer that takes an additional `fields` argument that
#     controls which fields should be displayed.
#     """
#
#     def __init__(self, *args, **kwargs):
#         # Don't pass the 'fields' arg up to the superclass
#         fields = kwargs.pop('fields', None)
#
#         # Instantiate the superclass normally
#         super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)
#
#         if fields is not None:
#             # Drop any fields that are not specified in the `fields` argument.
#             allowed = set(fields)
#             existing = set(self.fields.keys())
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)
#
#
# class ItemSerializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = Item
#         fields = '__all__'
#
#
# class DepartmentSerializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = Department
#         fields = '__all__'
#
#
# class ShopSerializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = Shop
#         fields = '__all__'
