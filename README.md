# Sistema Web de Gestão de Tarefas

Aplicação web de gestão de tarefas desenvolvida com Django. Esta versão utiliza os models `Categoria` e `Tarefa`, com persistência no SQLite.

## Tecnologias
- Python
- Django
- HTML e CSS
- SQLite

## Executar o projeto
No terminal, entre na pasta que contém `manage.py`, ative o ambiente virtual e execute:

```powershell
venv\\Scripts\\activate
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/admin/` para cadastrar categorias e tarefas. A listagem pública usa os dados persistidos no banco.

## Consultas ORM
```python
from tarefas.models import Categoria, Tarefa
Tarefa.objects.all()
Tarefa.objects.filter(situacao="PENDENTE")
Tarefa.objects.order_by("data_prevista")
tarefa = Tarefa.objects.filter(situacao="PENDENTE").first()
if tarefa:
    tarefa.situacao = "CONCLUIDA"
    tarefa.save()
```

## Registro da atividade
Dificuldade encontrada: a listagem e o cadastro usavam uma lista em memória, então os registros desapareciam ao reiniciar o servidor. A solução foi substituir essa lista por consultas e gravações com os models do Django, que persistem os dados no SQLite.

Antes de entregar, execute as migrações, cadastre pelo menos duas categorias e duas tarefas no Admin, valide as consultas no shell e registre o commit:
`git add .`
`git commit -m "Adiciona persistência de categorias e tarefas"`
