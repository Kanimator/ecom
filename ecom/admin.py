from django.contrib import admin

from ecom.models import ArkComputingBuild, ArkComputingPart, ArkComputingUser, ArkComputingCustomBuild

admin.site.register(ArkComputingPart)
admin.site.register(ArkComputingBuild)
admin.site.register(ArkComputingUser)
admin.site.register(ArkComputingCustomBuild)
