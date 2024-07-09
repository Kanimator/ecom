from django.views.generic import ListView

from ecom.models.cart import CartItem


class CartItemListView(ListView):
    model = CartItem
    template_name = "ecom/cartitems_list.html"
    partial_template_name = "ecom/partials/cartitems_list.html"

    def get_queryset(self, *args, **kwargs):
        return CartItem.objects.filter(cart__user=self.request.user.id)
