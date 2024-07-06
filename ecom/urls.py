from django.urls import path

from . import views

urlpatterns = [
    path("", views.ShopView.as_view(), name="shop"),
    path("contact/", views.contact_view, name="contact"),
    path("privacy/", views.privacy_view, name="privacy"),
    path("source/", views.source_view, name="source"),
    path("cart/", views.CartView.as_view(), name="cart"),
    path("<slug:slug>/detail/", views.ProductDetailView.as_view(), name="product detail"),
    path("all/", views.ProductListView.as_view(), name="product list"),
    path("orders/", views.OrderListView.as_view(), name="order list"),
]
