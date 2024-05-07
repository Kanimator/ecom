from django.db import models
from datetime import datetime

from django.utils.translation import gettext_lazy as _

class ArkComputingPart(models.Model):
    class ArkComputingPartLocation(models.TextChoices):
        OFFICE = "OFF", _("Ark Computing Main Office")
        STORAGE = "STO", _("Ark Computing Self-Storage")

    class ArkComputingPartCategory(models.TextChoices):
        CPU = "CPU", _("CPU")
        CPU_COOLER = "CPC", _("CPU Cooler")
        MOTHERBOARD = "MOB", _("Motherboard")
        MEMORY = "MEM", _("Memory")
        STORAGE = "STO", _("Storage")
        GPU = "GPU", _("GPU")
        CASE = "CAS", _("PC Case")
        PSU = "PSU", _("Power supply")
        OS = "OPS", _("Operating System")

    name = models.CharField(max_length=256, unique=False)
    image = models.ImageField(upload_to="media/product")
    upload_date = models.DateTimeField("upload date", default=datetime.now())
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    location = models.CharField(
        max_length=3,
        choices=ArkComputingPartLocation,
        default=ArkComputingPartLocation.OFFICE,
    )
    category = models.CharField(
        max_length=3,
        choices=ArkComputingPartCategory,
        default=ArkComputingPartCategory.CPU,
    )

    def __str__(self):
        return self.name

class ArkComputingBuild(models.Model):
    class ArkComputingBuildType(models.TextChoices):
        AIS = "AIS", _("Always in stock")
        RTS = "RTS", _("Ready to ship")

    name = models.CharField(max_length=256, unique=True)
    upload_date = models.DateTimeField("upload date", default=datetime.now())
    parts = models.ForeignKey(ArkComputingPart, on_delete=models.CASCADE)
    build_type = models.CharField(
        max_length=3,
        choices=ArkComputingBuildType,
        default=ArkComputingBuildType.RTS,
    )

    def __str__(self):
        return self.name
