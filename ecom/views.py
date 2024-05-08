from django.shortcuts import render
from django.shortcuts import get_object_or_404

from ecom.models import ArkComputingPart, ArkComputingBuild

def home(request):
    latest_builds_list = ArkComputingBuild.objects.order_by("-upload_date")[:5]
    context = { "title": "Home", "latest_builds_list": latest_builds_list }
    return render(request, "ecom/home.html", context=context)

def get_build(request, build_id):
    build = ArkComputingBuild.objects.get(build_id)
    context = {
        "title": f"{build.name}",
        "build": build,
    }
    return render(request, "ecom/build.html", context=context)

def get_cart(request):
    context = { "title": "Your Cart" }
    return render(request, "ecom/cart.html", context=context)

def get_part(request, part_id):
    part = get_object_or_404(ArkComputingPart, id=part_id)
    context = {
        "title": f"{part.name}",
        "part": part,
    }
    return render(request, "ecom/part.html", context=context)
