from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    class Prioridade(models.TextChoices):
        BAIXA = "BAIXA", "Baixa"
        MEDIA = "MEDIA", "Média"
        ALTA = "ALTA", "Alta"

    class Situacao(models.TextChoices):
        PENDENTE = "PENDENTE", "Pendente"
        EM_ANDAMENTO = "EM_ANDAMENTO", "Em andamento"
        CONCLUIDA = "CONCLUIDA", "Concluída"

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    prioridade = models.CharField(
        max_length=10, choices=Prioridade.choices, default=Prioridade.MEDIA
    )
    data_prevista = models.DateField(null=True, blank=True)
    situacao = models.CharField(
        max_length=15, choices=Situacao.choices, default=Situacao.PENDENTE
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="tarefas"
    )

    def __str__(self):
        return self.titulo
