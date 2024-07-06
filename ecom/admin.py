from django.contrib import admin

from ecom.models.order import Order
from ecom.models.product import Product, ProductImage, ProductVideo
from ecom.models.cart import Cart

class CartAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": ["user"]
            }
        )
    ]
    readonly_fields = ["date_created"]

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "price", "desc", "visibility"],
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
    list_display_links = ["name", "price"]
    list_editable = ["visibility"]

class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": ["user", "status"],
            },
        ),
    ]
    readonly_fields = ["date_created", "date_last_modified"]
    list_display = ["id", "user", "date_created", "date_last_modified"]
    list_per_page = 50
        
    


admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductVideo)