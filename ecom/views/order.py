from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import ListView

from ecom.models.order import Order


class OrderListView(ListView):
    model = Order


class OrderView(View):
    template_name = "ecom/order.html"
    partial_template_name = "ecom/partials/order.html"

    def get(self, request: HttpRequest, order_id: int, *args, **kwargs) -> HttpResponse:
        order = get_object_or_404(Order, id=order_id)
        context = {"title": f"Order #{order.id}", "order": order}
        if not request.htmx:
            return render(request, self.template_name, context=context)
        else:
            return render(request, self.partial_template_name, context=context)
