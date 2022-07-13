from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newpage", views.newpage, name="newpage"),
    path("editpage/<str:entry>", views.editpage, name="editpage"),
    path("randompage", views.randompage, name="randompage"),
    path("wiki/<str:name>", views.entrada, name="entrada"),
]
