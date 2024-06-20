from django.urls import path

from . import views

urlpatterns = [
    path("<int:product_id>/", views.get_product, name="get product"),
    path("<int:product_id>/edit", views.edit_product, name="edit product"),
    path("<int:product_id>/delete", views.delete_product, name="delete product"),
]
