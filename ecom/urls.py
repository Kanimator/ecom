from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("cart/", views.CartListView.as_view(), name="cart"),
    path("<int:product_id>/", views.ProductView.as_view(), name="product"),
    path("all/", views.ProductListView.as_view(), name="product list"),
    path("orders/", views.OrderListView.as_view(), name="order list"),
]
