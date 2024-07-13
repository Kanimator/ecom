from django.contrib import admin

from ecom.models import (Cart, CartItem, Order, OrderItem, Product,
                         ProductCategory, ProductImage, ProductVideo)


class ProductCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {"fields": ["name", "cover_image"]},
        ),
        (
            "Products",
            {"fields": ["products"]},
        ),
    ]


class CartAdmin(admin.ModelAdmin):
    fieldsets = [(None, {"fields": ["user"]})]
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
admin.site.register(CartItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductVideo)
