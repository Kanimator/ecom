from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("cart/", views.CartView.as_view(), name="cart"),
    path("<slug:slug>/detail/", views.ProductDetailView.as_view(), name="product detail"),
    path("all/", views.ProductListView.as_view(), name="product list"),
    path("orders/", views.OrderListView.as_view(), name="order list"),
]
