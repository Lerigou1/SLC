from django.db import models
from django import forms

# Create your models here.

class Lista(models.Model):
    nome_lista = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.id}. {self.nome_lista}"

class Produto(models.Model):
    produto = models.CharField(max_length=64)
    preco = models.FloatField()
    nome = models.ManyToManyField(Lista, blank=True, related_name="nome")

    def __str__(self):
        return f"{self.produto} - R$  {self.preco}"

#