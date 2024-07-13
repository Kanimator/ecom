<<<<<<< HEAD
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from ecom.models.cart import Cart


class CartListView(ListView):
    model = Cart
    context_object_name = "cartitems"
=======
from django.views.generic import ListView

from ecom.models.cart import CartItem
>>>>>>> refs/remotes/origin/main


class CartItemListView(ListView):
    model = CartItem
    template_name = "ecom/cartitems_list.html"
    partial_template_name = "ecom/partials/cartitems_list.html"

<<<<<<< HEAD
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
=======
    def get_queryset(self, *args, **kwargs):
        return CartItem.objects.filter(cart__user=self.request.user.id)
>>>>>>> refs/remotes/origin/main
