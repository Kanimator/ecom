from django.http import HttpRequest, HttpResponse
from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User

def source_view(request: HttpRequest) -> HttpResponse:
    if not request.method == "GET":
        return HttpResponse(status=403)
    repo_link = settings.ECOM_USERDATA.get("LINKS", {}).get("REPOSITORY", "")
    return redirect(repo_link)

def contact_view(request: HttpRequest) -> HttpResponse:
    if not request.method == "GET":
        return HttpResponse(status=403)
    context = {
        "title": "Contact",
        "userdata": settings.ECOM_USERDATA,
        "user": User.objects.get(username=request.username)
    }
    return render(request, "ecom/contact.html", context=context)

def privacy_view(request: HttpRequest) -> HttpResponse:
    if not request.method == "GET":
        return HttpResponse(status=403)
    context = {
        "title": "Contact",
        "userdata": settings.ECOM_USERDATA,
        "user": User.objects.get(username=request.user.username)
    }
    return render(request, "ecom/privacy.html", context=context)