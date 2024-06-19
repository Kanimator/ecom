from django.core.files.storage import storages
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=420.69)

    def __str__(self) -> str:
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=64)
    caption = models.CharField(max_length=256)
    product = models.ForeignKey(
        "Product", related_name="images", on_delete=models.CASCADE
    )
    source = models.FileField(storage=storages["bucket"])

    def __str__(self) -> str:
        return f"Image #{self.id} for {self.product.name}"


class Video(models.Model):
    name = models.CharField(max_length=64)
    caption = models.CharField(max_length=256)
    product = models.ForeignKey(
        "Product", related_name="videos", on_delete=models.CASCADE
    )
    source = models.FileField(storage=storages["bucket"])

    def __str__(self) -> str:
        return f"Video #{self.id} for {self.product.name}"
