from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from ecom.models.order import Order


class OrderListView(ListView):
    context_object_name = "orders"
    queryset = Order.objects.all()
    template_name = "ecom/order_list.html"
    partial_template_name = "ecom/partials/order_list.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return HttpResponse(status=403)

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, self.partial_template_name)

class OrderDetailView(DetailView):
    context_object_name = "order"
    queryset = Order.objects.all()
    template_name = "ecom/order_detail.html"
    partial_template_name = "ecom/partials/order_detail.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return HttpResponse(status=403)

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, self.partial_template_name)