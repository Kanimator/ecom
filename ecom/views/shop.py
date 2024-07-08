from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect

from ecom.models.product import Product



class ShopView(View):
    template_name = "ecom/shop.html"
    partial_template_name = "ecom/partials/shop.html"