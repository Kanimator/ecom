from django.db import models


class Order(models.Model):
    """A single purchase."""

    user = models.ForeignKey("auth.User", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField("Product", through="OrderItem")


class OrderItem(models.Model):
    """Intermediate model to represent a product and its quantity in an Order."""

    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.quantity} of {self.product.name} in Order #{self.order.id}"
