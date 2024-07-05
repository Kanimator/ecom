from django.contrib import admin

from ecom.models.order import Order
from ecom.models.product import Product


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "price", "visibility"],
            },
        ),
        (
            "Advanced",
            {
                "fields": ["slug"],
            },
        ),
    ]
    readonly_fields = ["slug"]
    list_display = ["name", "price", "visibility"]


admin.site.register(Order)
admin.site.register(Product, ProductAdmin)
