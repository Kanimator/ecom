from django.contrib import admin

from ecom.models import Order, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]


admin.site.register(Order)
admin.site.register(Product)
