from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.entrada, name="entrada"),
    path("newpage", views.newpage, name="newpage"),
    path("randompage", views.randompage, name="randompage"),
]
