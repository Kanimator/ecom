from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from typing import Any
from ecom.models.product import Product

class ProductDetailView(DetailView):
    model = Product
    queryset = Product.objects.filter(visibility__exact="VIS")

class ProductListView(ListView):
    model = Product
    queryset = Product.objects.filter(visibility__exact="VIS").all()