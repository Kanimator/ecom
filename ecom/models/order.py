from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    """A single purchase."""

    class Status(models.TextChoices):
        CREATED = "CRE", _("Order was created.")
        CANCELED = "CAL", _("Order was canceled.")
        FULFILLED = "FUL", _("Products were delivered to customer.")
        SHIPPING = "SHP", _("Order is being shipped.")

    user = models.ForeignKey("auth.User", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=3,
        choices=Status,
        default=Status.CREATED,
    )
    products = models.ManyToManyField("Product", through="OrderItem")


class OrderItem(models.Model):
    """Intermediate model to represent a product and its quantity in an :model:`ecom.Order`."""

    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.quantity} of {self.product.name} in Order #{self.order.id}"
