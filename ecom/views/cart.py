from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from ecom.models.cart import Cart
from ecom.models.product import Product

from typing import Any

class CartView(View):
    template_name = "ecom/cart.html"
    partial_template_name = "ecom/partials/cart.html"

    def get_context_data(self, request: HttpRequest, *args, **kwargs) -> Any:
        context = super().get_context_data(*args, **kwargs)
        context["cart"] = Cart.objects.get_or_create(user=request.user)
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, self.template_name)