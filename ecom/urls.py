from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.HomeView.as_view(), name="home"),
    path("cart/", views.CartListView.as_view(), name="cart"),
    path("<int:product_id>/", views.ProductView.as_view(), name="product"),
    path("all/", views.ProductListView.as_view(), name="product list"),
=======
    path("", views.ProductListView.as_view(), name="shop"),
    path("all/", views.ProductListView.as_view(), name="shop all"),
    path("contact/", views.contact_view, name="contact"),
    path("privacy/", views.privacy_view, name="privacy"),
    path("source/", views.source_view, name="source"),
    path("cart/", views.CartItemListView.as_view(), name="cart"),
    path("items/", views.ProductListView.as_view(), name="product list"),
    path(
        "items/<slug:slug>/", views.ProductDetailView.as_view(), name="product detail"
    ),
>>>>>>> refs/remotes/origin/main
    path("orders/", views.OrderListView.as_view(), name="order list"),
    path("orders/<int:pk>/", views.OrderDetailView.as_view(), name="order detail"),
]
