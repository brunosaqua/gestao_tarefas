from django.contrib import admin
from .models import Categoria, Tarefa


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome",)


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "prioridade", "situacao", "data_prevista")
    list_filter = ("prioridade", "situacao", "categoria")
    search_fields = ("titulo", "descricao")
    ordering = ("data_prevista", "titulo")
