from django.shortcuts import get_object_or_404, render

from ecom.models import Build


def get_all_builds(request):
    latest_builds_list = Build.objects.all().order_by("?")
    context = {"title": "Home", "latest_builds_list": latest_builds_list}
    return render(request, "ecom/home.html", context=context)


def get_build(request, build_slug):
    build = Build.objects.get(f"{build_slug}")
    context = {
        "title": f"{build.name}",
        "build": build,
    }
    return render(request, "ecom/build.html", context=context)
