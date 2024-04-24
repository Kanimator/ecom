from django.urls import path

from . import views

urlpatterns = [
    path("", views.discord_info, name="discord info"),
]
