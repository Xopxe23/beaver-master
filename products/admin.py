from django.contrib import admin

from products.models import Product, ProductCategory

# Register your models here.


admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'article', 'category', 'car_brand', 'price', 'in_stock')
    search_fields = ('name', 'category')
    ordering = ('name',)
    list_display_links = ('name', 'article')
