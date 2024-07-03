from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from ecom.models import Cart, Product


class CartView(View):
    template_name = "ecom/cart.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        context = {"title": "Cart", "cart": cart}
        return render(request, self.template_name, context=context)

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        context = {"title": "Shop"}
        if request.htmx:
            return render(request, self.template_name, context=context)
        else:
            return render(request, self.template_name, context=context)


def clear_cart(request: HttpRequest) -> HttpResponse:
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart.clear_items().save()
    context = {
        "title": "Cart",
        "cart": cart,
    }
    return render(request, "ecom/cart.html", context=context)


def add_to_cart(request: HttpRequest, product_id: int, quantity: int) -> HttpResponse:
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart.add_product(product=product, quantity=quantity).save()
    context = {
        "title": "Cart",
        "cart": cart,
    }
    return render(request, "ecom/cart.html", context=context)
