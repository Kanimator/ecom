from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


class ProductView(View):
    template_name = "ecom/product.html"
    partial_template_name = "ecom/partials/product.html"
    context = {"title": "Home"}

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, self.template_name, self.context)

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.htmx:
            return render(request, self.partial_template_name, self.context)
        else:
            return render(request, self.template, self.context)
