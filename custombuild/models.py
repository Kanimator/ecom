from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime

class CustomPart(models.Model):
    class CustomPartCategory(models.TextChoices):
        CENTRAL_PROCESSOR = "CPU", _("CPU")
        CPU_COOLER = "CPC", _("Cpu Cooler")
        MOTHERBOARD = "MOB", _("Motherboard")
        MEMORY = "MEM", _("Memory")
        STORAGE = "STO", _("Storage")
        GRAPHICS_CARD = "GPU", _("Graphics card")
        CASE = "CAS", _("PC Case")
        POWER_SUPPLY_UNIT = "PSU", _("Power supply")
        OPERATING_SYSTEM = "OPS", _("Operating System")

    name = models.CharField("name", max_length=256)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=9999.99)
    category = models.CharField(
        max_length=3,
        choices=CustomPartCategory,
        default=CustomPartCategory.CENTRAL_PROCESSOR,
    )

    def __str__(self) -> str:
        return self.name

class CustomBuild(models.Model):
    name = models.CharField("name", max_length=256)
    parts = models.ManyToManyField("CustomPart")
    created_on = models.DateTimeField("created on", default=datetime.now)

    def __str__(self) -> str:
        return self.name
    
    def price(self) -> float:
        return sum([
            part.price
            for part in self.parts
        ])
