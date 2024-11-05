from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Autores"

class Livro(models.Model):
    titulo = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)
    capa = models.ImageField(blank=True, null=True, upload_to="capa/", default="capa/default.jpg") 
    isbn = models.CharField(max_length=13, unique=True)
    n_paginas = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo + " - " + self.autor.nome