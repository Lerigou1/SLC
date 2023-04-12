from django.db import models

# Create your models here.

class Lista(models.Model):
    nome_lista = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.id}: {self.nome_lista}"

class Produto(models.Model):
    produto = models.CharField(max_length=64)
    preco = models.IntegerField()
    nome = models.ForeignKey(Lista, on_delete=models.CASCADE, related_name="nome")

    def __str__(self):
        return f"{self.id}: {self.produto}"

#class Produto(models.Model):
#    produto = models.CharField(max_length=64)
#    preco = models.IntegerField()
#    lista = models.ManyToManyField(Lista, blank=True, related_name="produto")
#
#    def __str__(self):
#        return f"{self.id}: {self.produto}"