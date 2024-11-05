from django.contrib import admin

from .models import Livro, Autor


admin.site.register(Autor)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'autor', 'n_paginas')
