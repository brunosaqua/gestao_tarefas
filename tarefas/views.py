from django.shortcuts import render, redirect
from .models import Categoria, Tarefa


def inicio(request):
    return render(request, "tarefas/inicio.html")


def lista_tarefas(request):
    tarefas = Tarefa.objects.select_related("categoria").all().order_by("data_prevista", "titulo")
    return render(request, "tarefas/lista.html", {"tarefas": tarefas})


def cadastrar_tarefa(request):
    categorias = Categoria.objects.all().order_by("nome")

    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        descricao = request.POST.get("descricao", "").strip()
        prioridade = request.POST.get("prioridade", Tarefa.Prioridade.MEDIA)
        situacao = request.POST.get("situacao", Tarefa.Situacao.PENDENTE)
        categoria_id = request.POST.get("categoria")
        data_prevista = request.POST.get("data_prevista") or None

        if titulo and categoria_id:
            Tarefa.objects.create(
                titulo=titulo,
                descricao=descricao,
                prioridade=prioridade,
                situacao=situacao,
                categoria_id=categoria_id,
                data_prevista=data_prevista,
            )
            return redirect("lista_tarefas")

        return render(request, "tarefas/cadastrar.html", {
            "categorias": categorias,
            "erro": "Informe o título e selecione uma categoria.",
        })

    return render(request, "tarefas/cadastrar.html", {"categorias": categorias})
