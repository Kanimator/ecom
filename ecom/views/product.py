from django.views.generic import ListView
from django.views.generic.detail import DetailView
from ecom.models.product import Product

class ProductDetailView(DetailView):
    model = Product
    queryset = Product.objects.filter(visibility__exact="VIS")

class ProductListView(ListView):
    model = Product
    queryset = Product.objects.filter(visibility__exact="VIS")