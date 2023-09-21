from django.contrib import admin
from django.urls import path
from controleTarefas.views.alunos import AlunosView
from controleTarefas.views.disciplinas import DisciplinaView
from controleTarefas.views.tarefas import TarefasView
from controleTarefas.views.tarefaAluno import TarefaAlunoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/alunos/',AlunosView.as_view()),
    path('api/alunos/<int:id>/',AlunosView.as_view()),
    path('api/disciplinas/', DisciplinaView.as_view()),
    path('api/disciplinas/<int:id>/',DisciplinaView.as_view()),
    path('api/tarefas/', TarefasView.as_view()),
    path('api/tarefas/<int:id>/',TarefasView.as_view()),
    path('api/alunos/<int:aluno_id>/tarefas/', TarefaAlunoView.as_view()),
]
