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


class Order(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField("Product", through="OrderItem")


class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.quantity} of {self.product.name} in Order #{self.order.id}"


class Cart(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s cart"


class CartItem(models.Model):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.quantity} of {self.product.name} in Cart #{self.cart.id}"
