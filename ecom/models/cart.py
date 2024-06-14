from django.db import models


class Cart(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    products = models.ManyToManyField("Product")

    def total(self):
        return sum([p.price for p in self.products.all()])

    def __str__(self):
        return f"{self.user.username}'s Cart"
