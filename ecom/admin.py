from django.contrib import admin

from .models import ArkComputingBuild, ArkComputingPart

admin.site.register(ArkComputingPart)
admin.site.register(ArkComputingBuild)
