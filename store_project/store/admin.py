from django.contrib import admin
from .models import Product, Category, Order

admin.site.register(Product)
admin.site.register(Category)

class OrderAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'product']

admin.site.register(Order, OrderAdmin)