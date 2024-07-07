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