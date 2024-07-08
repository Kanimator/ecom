from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from ecom.models.cart import Cart

from typing import Any

class CartView(TemplateView):
    template_name = "ecom/cart.html"
    partial_template_name = "ecom/partials/cart.html"
    http_method_names = ["get", "post"]

    def get_context_data(self, *args, **kwargs) -> Any:
        context = super().get_context_data(*args, **kwargs)
        user = context["user"]
        cart, _ = Cart.objects.get_or_create(user=user)
        cartitems = cart.items.all()
        context["cart"] = cart
        context["cartitems"] = cartitems
        return context