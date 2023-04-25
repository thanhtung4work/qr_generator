from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_qr", views.get_qr, name="get_qr")
]