from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:lista_id>", views.lista, name="lista")
]