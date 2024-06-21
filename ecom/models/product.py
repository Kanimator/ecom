from django.core.files.storage import storages
from django.db import models


class Product(models.Model):
    """A purchasable item in the store."""

    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=420.69)

    def __str__(self) -> str:
        return self.name


class ProductImage(models.Model):
    """Image for a Product."""

    name = models.CharField(max_length=64)
    caption = models.CharField(max_length=256)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    source = models.FileField(storage=storages["bucket"])

    @property
    def url(self) -> str:
        return self.source.url

    def __str__(self) -> str:
        return f"Image #{self.id} for {self.product.name}"


class ProductVideo(models.Model):
    """Video for a Product."""

    name = models.CharField(max_length=64)
    caption = models.CharField(max_length=256)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    source = models.FileField(storage=storages["bucket"])

    @property
    def url(self) -> str:
        return self.source.url

    def __str__(self) -> str:
        return f"Video #{self.id} for {self.product.name}"
