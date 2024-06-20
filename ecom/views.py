from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from ecom.models import Cart, Product


def get_product(request: HttpRequest, product_id: int) -> HttpResponse:
    product = Product.objects.get(pk=product_id)
    context = {
        "title": product.name,
        "product": product,
    }
    return render(request, "ecom/product.html", context=context)


def edit_product(request: HttpRequest, product_id: int) -> HttpResponse:
    if not request.user.is_authenticated:
        return get_product(request, product_id)

    product = Product.objects.get(pk=product_id)
    context = {
        "title": f"Edit {product.name}",
        "product": product,
    }
    return render(request, "ecom/edit_product.html", context=context)


def delete_product(request: HttpRequest, product_id: int) -> HttpResponse:
    if not request.user.is_authenticated:
        return get_product(request, product_id)

    product = Product.objects.get(pk=product_id)
    context = {
        "title": f"Delete {product.name}",
        "product": product,
    }
    return render(request, "ecom/delete_product.html", context=context)


def get_cart(request: HttpRequest) -> HttpResponse:
    cart, created = Cart.objects.get_or_create(user=request.user)
    context = {
        "title": "Cart",
        "cart": cart,
        "cart_is_new": created,
    }
    return render(request, "ecom/cart.html", context=context)
