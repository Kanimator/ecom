from django.contrib.auth.models import User
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _

from ecom.models.product import Product


class Order(models.Model):
    """A single purchase."""

    class Status(models.TextChoices):
        CREATED = "CRE", _("Order was created.")
        CANCELED = "CAL", _("Order was canceled.")
        FULFILLED = "FUL", _("Products were delivered to customer.")
        SHIPPING = "SHP", _("Order is being shipped.")

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    note = models.TextField(max_length=2048, blank=True, default="")
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=3,
        choices=Status,
        default=Status.CREATED,
    )
    products = models.ManyToManyField(Product, through="OrderItem")

    def get_product_by_id(self, product_id: int) -> Product:
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValueError(f"No product with {id = } exists.")

    def update_status(self, new_status: str) -> None:
        self.update(status=new_status)
        self.save()

    @transaction.atomic
    def add_product(self, product_id: int, quantity: int = 1) -> None:
        """Add any quantity of :model:`ecom.Product`s (by id) to this cart."""
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        product = self.get_product_by_id(product_id)
        orderitem, created = OrderItem.objects.get_or_create(cart=self, product=product)
        if created:
            orderitem.quantity = quantity
            orderitem.save()
        else:
            orderitem.quantity += quantity
            orderitem.save()

        return None

    def __str__(self) -> str:
        return f"#{self.id} - {self.date_created:%c} - {self.user.username}"


class OrderItem(models.Model):
    """Intermediate model to represent a product and its quantity in an :model:`ecom.Order`."""

    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.quantity} of {self.product.name}"
