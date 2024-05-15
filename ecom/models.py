from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


class Part(models.Model):
    class Location(models.TextChoices):
        OFFICE = "OFF", _("Main Office")
        STORAGE = "STO", _("Self-Storage")

    class Category(models.TextChoices):
        CENTRAL_PROCESSOR = "CPU", _("CPU")
        CPU_COOLER = "CPC", _("Cpu Cooler")
        MOTHERBOARD = "MOB", _("Motherboard")
        MEMORY = "MEM", _("Memory")
        STORAGE = "STO", _("Storage")
        GRAPHICS_CARD = "GPU", _("Graphics card")
        CASE = "CAS", _("PC Case")
        POWER_SUPPLY_UNIT = "PSU", _("Power supply")
        OPERATING_SYSTEM = "OS", _("Operating System")

    name = models.CharField(max_length=256, unique=False)
    image = models.ImageField(upload_to="media/product")
    upload_date = models.DateTimeField("upload date", default=datetime.now)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    location = models.CharField(
        max_length=3,
        choices=Location,
        default=Location.OFFICE,
    )

    category = models.CharField(
        max_length=3,
        choices=Category,
        default=Category.CENTRAL_PROCESSOR,
    )

    def __str__(self):
        return self.name


class Build(models.Model):
    class BuildType(models.TextChoices):
        AIS = "AIS", _("Always in stock")
        RTS = "RTS", _("Ready to ship")

    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=64, unique=True)
    desc = models.TextField(max_length=2048)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    tok_link = models.URLField(null=True, blank=True)
    upload_date = models.DateTimeField("upload date", default=datetime.now)

    image = models.ImageField(upload_to="media/product", null=True, blank=True)
    alt_image = models.ImageField(upload_to="media/product", null=True, blank=True)
    video = models.FileField(null=True, blank=True)

    build_type = models.CharField(
        max_length=3,
        choices=BuildType,
        default=BuildType.RTS,
    )

    def __str__(self):
        return self.name
