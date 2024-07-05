from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView

from ecom.models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = "available_products"


class ProductView(View):
    template_name = "ecom/product.html"
    partial_template_name = "ecom/partials/product.html"

    def get(
        self, product_id: int, request: HttpRequest, *args, **kwargs
    ) -> HttpResponse:
        product = get_object_or_404(Product, id=product_id)
        context = {"title": product.name.title(), "product": product}
        return render(request, self.template_name, context)

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.htmx:
            context = {"title": ""}
            return render(request, self.partial_template_name, context)
        else:
            context = {"title": ""}
            return render(request, self.template_name, context)
