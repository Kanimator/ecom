from django.db import models
from django.shortcuts import get_object_or_404


class Cart(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def add_product(self, product_id: int, quantity: int = 1) -> None:
        product = get_object_or_404("Product", id=product_id)
        cart_item, created = CartItem.objects.get_or_create(
            cart=self, product=product, quantity=quantity
        )
        if not created:
            cart_item.quantity += quantity
        cart_item.save()

        return None

    def __str__(self) -> str:
        return f"{self.user.username}'s cart"


class CartItem(models.Model):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.quantity} of {self.product.name} in Cart #{self.cart.id}"
