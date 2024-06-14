from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=1024)
    desc = models.TextField()
    source = models.ImageField(upload_to="categories/")
    products = models.ManyToManyField("Product")

    def __str__(self):
        return self.name

    def url(self):
        return self.source.url
