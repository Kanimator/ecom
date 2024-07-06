from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from typing import Any
from ecom.models.product import Product

class ProductDetailView(DetailView):
    context_object_name = "product"
    queryset = Product.objects.filter(visibility__exact="VIS")

class ProductListView(ListView):
    context_object_name = "products"
    queryset = Product.objects.filter(visibility__exact="VIS").all()


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
