from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.create_build, name="create build"),
    path("<int:custom_build_id>/", views.get_build, name="get build"),
    path("<int:custom_build_id>/submit", views.submit_build, name="submit build"),

    path("gallery/", views.gallery, name="build gallery"),
]
