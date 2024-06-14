from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=1024)
    desc = models.TextField()
    sku = models.CharField(max_length=12, unique=True, blank=False, null=False)
    source = models.ImageField(upload_to="products/")
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cat = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True)
    amazon_link = models.URLField(null=True, blank=True)
    amazon_rating = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)

    def __str__(self):
        return self.name

    def img(self):
        return self.source.url

    def rating(self):
        return int(self.amazon_rating * 20)
