from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _

class ArkComputingPart(models.Model):
    class Location(models.TextChoices):
        OFFICE = "OFF", _("Ark Computing Main Office")
        STORAGE = "STO", _("Ark Computing Self-Storage")

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
    cost = models.DecimalField(max_digits=7, decimal_places=2, default=9999.99)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=9999.99)
    build = models.ManyToManyField("ArkComputingBuild")

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

class ArkComputingBuild(models.Model):
    class Type(models.TextChoices):
        AIS = "AIS", _("Always in stock")
        RTS = "RTS", _("Ready to ship")

    name = models.CharField(max_length=256, unique=True)
    upload_date = models.DateTimeField("upload date", default=datetime.now)
    build_type = models.CharField(
        max_length=3,
        choices=Type,
        default=Type.RTS,
    )

    def __str__(self):
        return self.name
