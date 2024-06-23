from django.contrib import admin
from .models import Product, Category
# Register your models here.


class ListProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock']


admin.site.register(Product, ListProduct)
admin.site.register(Category)
