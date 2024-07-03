from django.urls import path

from .views import CartView, product_view

urlpatterns = [
    path("", CartView.as_view(), name="get shop"),
    path("<int:product_id>/", product_view, name="get product"),
    path("cart/", CartView.as_view(), name="get cart"),
    path("cart/clear/", CartView.as_view(), name="clear cart"),
    path("cart/add/", CartView.as_view(), name="add to cart"),
]
