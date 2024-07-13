from django.views import View
from django.views.generic import ListView

from ecom.models import Cart, CartItem

class CartView(View):
    model = Cart

class CartItemListView(ListView):
    model = CartItem

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs
