from django.contrib import admin

from ecom.models import Cart, Order, Product, ProductImage, ProductVideo

admin.site.register(Cart)
admin.site.register(ProductImage)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(ProductVideo)
