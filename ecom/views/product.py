from django.views.generic import DetailView, ListView

from ecom.models import Product

class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    queryset = Product.objects.filter(visibility__exact="VIS").all()

class ProductListView(ListView):
    model = Product
    context_object_name = "available_products"
    queryset = Product.objects.filter(visibility__exact="VIS").all()
