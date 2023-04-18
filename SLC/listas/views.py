from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import *
from django import forms
from django.db import transaction

# Create your views here.

def index(request):
    return render(request, "listas/index.html", {
        "listas": Lista.objects.all()
    })

def lista(request, lista_id):
    lista = Lista.objects.get(id=lista_id)
    produto = lista.nome.all()
    sem_lista = Produto.objects.exclude(id=lista_id).all()
    return render(request, "listas/lista.html", {
        "lista": lista,
        "produto": produto,
        "sem_lista": sem_lista
    })

def livro(request, lista_id):
    if request.method == "POST":
        lista = Lista.objects.get(pk=lista_id)
        produto_id = int(request.POST["produto"])
        produto = Produto.objects.get(pk=produto_id)
        produto.nome.add(lista)
        return HttpResponseRedirect(reverse("listas:lista", args=(lista.id,)))

def add_lista(request):
    if request.user.is_authenticated:
        formLista = NovaLista(request.POST or None)
        if formLista.is_valid():
            formLista.save()
        return render(request, 'listas/novalista.html', {
            'formLista': formLista
            })

def add_produto(request):
    if request.user.is_authenticated:
        formProduto = NovoProduto(request.POST or None)
        if formProduto.is_valid():
            formProduto.save()
        return render(request, 'listas/mercado.html', {
            'formProduto' : formProduto
            })