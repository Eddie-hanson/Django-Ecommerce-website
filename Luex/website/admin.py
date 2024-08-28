from django.contrib import admin
from .models import Product, Category, Cart, Cart_Item, User_FeedBack
# Register your models here.


class ListProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'category']


admin.site.register(Product, ListProduct)
admin.site.register(Category)
admin.site.register(Cart_Item)
admin.site.register(Cart)
admin.site.register(User_FeedBack)
