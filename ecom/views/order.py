from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from ecom.models.order import Order


class OrderListView(ListView):
    model = Order
    context_object_name = "orders"


class OrderDetailView(DetailView):
    model = Order

