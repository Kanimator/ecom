from django.core.exceptions import ValidationError
from django.core.files.storage import storages
from django.db import models
from django.utils.translation import gettext_lazy as _


def validate_positive(value: float) -> None:
    """Raises ValidationError if the value is zero or negative."""
    if value <= 0:
        raise ValidationError(_("Price cannot be less than or equal to zero."))


class Product(models.Model):
    """A purchasable item in the store."""

    class Visibility(models.TextChoices):
        """Visibility states of a product."""

        VISIBLE = "VIS", _("Visible")
        HIDDEN = "HID", _("Hidden")
        UNAVAILABLE = "UNA", _("Unavailable")

    name = models.CharField(max_length=64)
    desc = models.TextField(verbose_name="description", max_length=2048)
    date_added = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    visibility = models.CharField(
        max_length=3,
        choices=Visibility,
        default=Visibility.UNAVAILABLE,
    )
    price = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[validate_positive]
    )
    is_featured = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class ProductImage(models.Model):
    """Image for a :model:`ecom.Product`."""

    name = models.CharField(max_length=64)
    caption = models.CharField(max_length=256)
    product = models.ForeignKey(
        "Product",
        related_name="images",
        on_delete=models.CASCADE,
    )
    source = models.FileField(storage=storages["bucket"])

    @property
    def url(self) -> str:
        return self.source.url

    def __str__(self) -> str:
        return f"Image #{self.id} for {self.product.name}"


class ProductVideo(models.Model):
    """Video for a :model:`ecom.Product`."""

    name = models.CharField(max_length=64)
    caption = models.CharField(max_length=256)
    product = models.ForeignKey(
        "Product",
        related_name="videos",
        on_delete=models.CASCADE,
    )
    source = models.FileField(storage=storages["bucket"])

    @property
    def url(self) -> str:
        return self.source.url

    def __str__(self) -> str:
        return f"Video #{self.id} for {self.product.name}"


class ProductCategory(models.Model):
    """Intermediate class for organizing :model:`ecom.Product`s."""

    name = models.CharField(max_length=64)
    cover_image = models.FileField(storage=storages["bucket"], null=True, default=None)
    logo_image = models.FileField(storage=storages["bucket"], null=True, default=None)
    product = models.ForeignKey(
        "Product",
        related_name="categories",
        on_delete=models.CASCADE,
    )
