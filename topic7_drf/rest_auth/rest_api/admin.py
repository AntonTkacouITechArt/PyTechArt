from django.contrib import admin

from rest_api.models import Shop, Department, Item, Statistics


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'staff_amount')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'address')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'sphere', 'staff_amount', 'shop')
    list_display_links = ('id',)
    search_fields = ('sphere', 'shop')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'is_sold',
                    'comments', 'department')
    list_display_links = ('id',)
    search_fields = ('description', 'department', 'comments')


class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'amount')
    list_display_links = ('id', 'url')
    search_fields = ('url',)


admin.site.register(Shop, ShopAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Statistics, StatisticsAdmin)
