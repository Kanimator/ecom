from django.contrib import admin

from ecom.models import Cart, Category, Order, Product

admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Product)
