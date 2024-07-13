from django.http import HttpRequest, HttpResponse
from django.views import View


class SearchView(View):
    template_name = "ecom/search.html"
    initial = {"query": "*"}
