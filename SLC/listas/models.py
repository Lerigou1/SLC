from django.db import models
from django import forms
from django.forms import ModelForm

# Create your models here.

class Lista(models.Model):
    nome_lista = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.nome_lista}"

class Produto(models.Model):
    produto = models.CharField(max_length=64)
    preco = models.FloatField()
    nome = models.ManyToManyField(Lista, blank=True, related_name="nome")

    def __str__(self):
        return f"{self.produto} - R$  {self.preco}"


class NovaLista(ModelForm):
    class Meta:
        model = Lista
        fields = ['nome_lista']

class NovoProduto(ModelForm):
    class Meta:
        model = Produto
        fields = ['produto', 'preco']