from django.shortcuts import render
from django.shortcuts import get_object_or_404

from ecom.models import ClientPart, ClientBuild

"""
class ArkComputingCustomBuild:
    def get(request, custom_build_id):
        build = ArkComputingCustomBuild.objects.get(custom_build_id)
        context = { "title": custom_build_id, "build": build }

    def create(request, custom_build_data):
        context = { "title": "New Custom Build", "custom_build_data": custom_build_data }
        return render(request, "ecom/custom.html", context=context)

    def delete(request, custom_build_id):
        context = { "title": f"Delete Build #{custom_build_id}", "custom_build": custom_build_id }
        return render(request, "ecom/delete_custom.html", context=context)
"""

def home(request):
    latest_builds_list = ClientBuild.objects.order_by("-upload_date")[:5]
    context = { "title": "Home", "latest_builds_list": latest_builds_list }
    return render(request, "ecom/home.html", context=context)

def get_build(request, build_id):
    build = ClientBuild.objects.get(build_id)
    context = {
        "title": f"{build.name}",
        "build": build,
    }
    return render(request, "ecom/build.html", context=context)

def get_cart(request):
    context = { "title": "Your Cart" }
    return render(request, "ecom/cart.html", context=context)

def get_part(request, part_id):
    part = get_object_or_404(ClientPart, id=part_id)
    context = {
        "title": f"{part.name}",
        "part": part,
    }
    return render(request, "ecom/part.html", context=context)
