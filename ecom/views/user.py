from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic import ListView

from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

class UserView(View):
    template_name = "ecom/user.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        context = {
            "title": f"{request.user.username}",
            "user": request.user,
        }
        return render(request, self.template_name, context)

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if not request.htmx:
            return HttpResponse(status=400)
        context = {
            "title": f"{request.user.username}",
            "user": request.user,
        }
        return render(request, self.template_name, context)

class UserListView(View):
    template_name = "ecom/user_list.html"

class UserDetailView(View):
    template_name = "ecom/user_detail.html"