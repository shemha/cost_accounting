from django.contrib import admin
from .models import Vender, Material, Product, Cost, Warehousing, Stock, Client, Sale

# Register your models here.
class VenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'name',)
    list_display_links = ('id', 'name',)

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'division',)
    list_display_links = ('id', 'name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)

class CostAdmin(admin.ModelAdmin):
    list_display = ('id', 'product',)
    list_display_links = ('id',)

class WarehousingAdmin(admin.ModelAdmin):
    list_display = ('id', 'cost', 'date',)
    list_display_links = ('id', 'date',)

class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'warehousing',)
    list_display_links = ('id',)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'name',)
    list_display_links = ('id', 'name',)

class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'order_date',)
    list_display_links = ('id', 'client', 'order_date',)


admin.site.register(Vender, VenderAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cost, CostAdmin)
admin.site.register(Warehousing, WarehousingAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Sale, SaleAdmin)