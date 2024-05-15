from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_all_builds, name="get all builds"),
    path("<str:build_slug>/", views.get_build, name="get build"),
]
