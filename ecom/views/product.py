from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from ecom.models import Product


def product_view(request: HttpRequest, product_id: int) -> HttpResponse:
    product = Product.objects.get(pk=product_id)
    context = {
        "title": product.name,
        "product": product,
    }
    return render(request, "ecom/product.html", context=context)
