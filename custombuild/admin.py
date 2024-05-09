from django.contrib import admin

from .models import CustomPart
from .models import CustomBuild

admin.site.register(CustomPart)
admin.site.register(CustomBuild)
