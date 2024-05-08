from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cart/", views.get_cart, name="cart"),
    path("part/<int:part_id>/", views.get_part, name="part"),
    path("build/<int:build_id>/", views.get_build, name="build"),
]
