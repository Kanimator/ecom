from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cart/", views.get_cart, name="cart"),
    path("part/<int:part_id>/", views.get_part, name="part"),
    path("category/<str:category>/", views.get_category, name="category"),
    path("build/<int:build_id>/", views.get_build, name="get build"),

    path("build/custom/<int:custom_build_id>/", views.ArkComputingCustomBuild.get, name="get custom build"),
    path("build/custom/create/", views.ArkComputingCustomBuild.create, name="create custom build"),
    path("build/custom/delete/", views.ArkComputingCustomBuild.delete, name="delete custom build"),
    path("build/custom/update/", views.ArkComputingCustomBuild.update, name="update custom build"),
]
