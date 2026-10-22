# Generated for the Categoria and Tarefa models.
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tarefa",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=200)),
                ("descricao", models.TextField(blank=True)),
                ("prioridade", models.CharField(choices=[("BAIXA", "Baixa"), ("MEDIA", "Média"), ("ALTA", "Alta")], default="MEDIA", max_length=10)),
                ("data_prevista", models.DateField(blank=True, null=True)),
                ("situacao", models.CharField(choices=[("PENDENTE", "Pendente"), ("EM_ANDAMENTO", "Em andamento"), ("CONCLUIDA", "Concluída")], default="PENDENTE", max_length=15)),
                ("categoria", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="tarefas", to="tarefas.categoria")),
            ],
        ),
    ]
