from django.db import models, transaction

from ecom.models.product import Product


class Cart(models.Model):
    """Holds :model:`ecom.Product`s that a user can purchase all at once."""

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField("Product", through="CartItem", null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f"{self.user.username}'s cart"

    def get_product_by_id(self, product_id: int) -> Product:
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValueError(f"No product with {id = } exists.")

    def get_cartitem_by_product(self, product: Product) -> "CartItem":
        try:
            return CartItem.objects.get(cart=self, product=product)
        except CartItem.DoesNotExist:
            raise ValueError(f"No product with id `{product.id}` present in this cart.")

    @transaction.atomic
    def create_order(self) -> None:
        """Creates an :model:`ecom.Order` based on this cart's items list."""
        if not self.items.exists():
            raise ValueError("Cannot create order without items.")

        return None

    @transaction.atomic
    def clear_items(self) -> None:
        """Removes all instances of :model:`ecom.CartItem` from this cart."""
        self.items.all().delete()

        return None

    @transaction.atomic
    def add_product(self, product_id: int, quantity: int = 1) -> None:
        """Add any quantity of :model:`ecom.Product`s (by id) to this cart."""
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        product = self.get_product_by_id(product_id)
        cartitem, created = CartItem.objects.get_or_create(cart=self, product=product)
        if created:
            cartitem.quantity = quantity
            cartitem.save()
        else:
            cartitem.quantity += quantity
            cartitem.save()

        return None

    @transaction.atomic
    def rm_product(self, product_id: int, quantity: int = 1) -> None:
        """Remove any quantity of :model:`ecom.Product`s (by id) from this cart."""
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        product = self.get_product_by_id(product_id)
        cartitem = self.get_cartitem_by_product(product=product)

        if quantity > cartitem.quantity:
            raise ValueError(
                f"Invalid quantity '{quantity}'. Quantity cannot be greater than {cartitem.quantity}."
            )
        elif quantity == cartitem.quantity:
            cartitem.delete()
        else:
            cartitem.quantity -= quantity
            cartitem.save()

        return None


class CartItem(models.Model):
    """Intermediate model to represent a product in a :model:`ecom.Cart`."""

    cart = models.ForeignKey("Cart", related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.quantity} of {self.product.name} in Cart #{self.cart.id}"
