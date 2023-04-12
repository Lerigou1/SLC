from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Lista, Produto
from django import forms

# Create your views here.

def index(request):
    return render(request, "listas/index.html", {
        "listas": Lista.objects.all()
    })

def lista(request, lista_id):
    lista = Lista.objects.get(id=lista_id)
    produto = lista.produto.all()
    sem_lista = Produto.objects.exclude(id=lista_id).all()
    return render(request, "listas/lista.html", {
        "lista": lista,
        "produto": produto,
        "sem_lista": sem_lista
    })

#def add(request):
#    if request.method == "POST":
#        form = Produto(request.POST)
#        if form.is_valid():
#            task = form.cleaned_data["task"]
#            request.session["tasks"] += [task]
#            return HttpResponseRedirect(reverse("listas:index"))
#        else:
#            return render(request, "listas/lista.html", {
#                "form": form
#            })
#
#    return render(request, "tasks/lista.html", {
#        "form": Produto()
#    })