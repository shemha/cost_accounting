from django.contrib import admin
from .models import Vender, Material, Category, Item, Product, Cost, Warehousing, Stock, Customer, Orderer, Sale

# Register your models here.
class VenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'name',)
    list_display_links = ('id', 'company', 'name',)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vender',)
    list_display_links = ('id', 'name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'amount', 'unit',)
    list_display_links = ('id', 'item', 'amount', 'unit',)


class CostAdmin(admin.ModelAdmin):
    list_display = ('id', 'product',)
    list_display_links = ('id',)


class WarehousingAdmin(admin.ModelAdmin):
    list_display = ('id', 'material', 'date',)
    list_display_links = ('id', 'material', 'date',)


class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'warehousing',)
    list_display_links = ('id',)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'company',)
    list_display_links = ('id', 'company',)


class OrdererAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'name',)
    list_display_links = ('id', 'company', 'name',)


class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order_date',)
    list_display_links = ('id', 'customer', 'order_date',)


admin.site.register(Vender, VenderAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cost, CostAdmin)
admin.site.register(Warehousing, WarehousingAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Orderer, OrdererAdmin)
admin.site.register(Sale, SaleAdmin)