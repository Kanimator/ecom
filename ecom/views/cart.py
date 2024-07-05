from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from ecom.models.cart import Cart


class CartListView(ListView):
    model = Cart
    context_object_name = "cartitems"


class CartView(View):
    template_name = "ecom/cart.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        context = {"title": "Cart", "cart": cart}
        return render(request, self.template_name, context=context)

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        context = {"title": "Cart"}
        if request.htmx:
            return render(request, self.template_name, context=context)
        else:
            return render(request, self.template_name, context=context)
