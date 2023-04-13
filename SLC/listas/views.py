from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import *
from django import forms

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

def mercado(request):
    if request.method == "POST":
        form = NovoProduto(request.POST)
        if form.is_valid():
            mercado = form.cleaned_data["mercado"]
            request.session["mercado"] += [mercado]
            return HttpResponseRedirect(reverse("listas:mercado"))
        else:
            return render(request, "listas/mercado.html", {
                "mercado": form
            })

    return render(request, "listas/mercado.html", {
        "mercado": NovoProduto()
    })

def livro(request, lista_id):
    if request.method == "POST":
        lista = Lista.objects.get(pk=lista_id)
        produto_id = int(request.POST["produto"])
        produto = Produto.objects.get(pk=produto_id)
        produto.nome.add(lista)
        return HttpResponseRedirect(reverse("lista", args=(lista.id,)))