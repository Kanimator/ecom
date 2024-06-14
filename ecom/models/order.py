from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        APPROVED = "AP", _("Order was approved by admin")
        CANCELED = "CL", _("Order was canceled by user")
        CANCELED_ADMIN = "CA", _("Order was canceled by admin")
        CREATED = "PD", _("Order was created")
        DECLINED = "DP", _("Order payment was declined")
        DECLINED_ADMIN = "DA", _("Order payment was declined by admin")
        DISPUTED = "DS", _("Order was disputed by user")
        FULFILLED = "FL", _("Order was fulfilled/received by customer")
        REFUNDED_FULL = "RF", _("Order was refunded in full")
        REFUNDED_PARTIAL = "RP", _("Order was refunded in part")
        SHIPPED = "SP", _("Order was shipped but not received")

    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2, default=OrderStatus.CREATED, choices=OrderStatus.choices
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_fulfilled = models.DateTimeField(blank=True, null=True, default=datetime.now)

    def __str__(self):
        return f"{self.cart.user.username}'s Order"
