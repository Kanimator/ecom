from django.contrib import admin

from ecom.models import ArkComputingPart
from ecom.models import ArkComputingBuild
from ecom.models import ArkComputingUser
from ecom.models import ArkComputingCustomBuild

admin.site.register(ArkComputingPart)
admin.site.register(ArkComputingBuild)
admin.site.register(ArkComputingUser)
admin.site.register(ArkComputingCustomBuild)
