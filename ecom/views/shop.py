from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import RequestContext, Context
from django.views import View

from typing import Any

from ecom.models.cart import Cart
from ecom.models.product import Product

def cartitems_processor(request: HttpRequest) -> dict[str, Any]:
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cartitems = cart.items.all()
    return {
        "cart": cart,
        "cartitems": cartitems,
    }


class ShopView(View):
    template_name = "ecom/shop.html"
    partial_template_name = "ecom/partials/shop.html"
    http_method_names = ["get"]
    object = None
    
    def get_queryset(self, *args, **kwargs):
        return Product.objects.filter(visibility__exact="VIS")

    def get_context_data(self, request: HttpRequest, *args, **kwargs) -> dict:
        context = RequestContext(
            request,
            {
                "title": "Shop",
                "featured_product": self.get_queryset().last(),
            },
            [cartitems_processor],
        )
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if not request.htmx:
            return render(
                request,
                self.template_name,
            )
        else:
            return render(
                request,
                self.partial_template_name,
            )

class ShopAllView(ShopView):
    template_name = "ecom/shop_all.html"
    partial_template_name = "ecom/partials/shop_all.html"