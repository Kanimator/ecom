from django.views.generic import DetailView, ListView

from ecom.models import Order

class OrderDetailView(DetailView):
    model = Order
    context_object_name = "order"

class OrderListView(ListView):
    model = Order
    context_object_name = "orders_list"
