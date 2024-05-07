from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cart/", views.cart, name="cart"),
    path("<int:product_id>/", views.detail, name="detail"),
]
