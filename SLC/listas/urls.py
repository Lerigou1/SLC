from django.urls import path
from . import views

app_name = "listas"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:lista_id>", views.lista, name="lista"),
    path("<int:lista_id>/livro", views.livro, name="livro"),
    path("mercado", views.mercado, name="mercado")
]