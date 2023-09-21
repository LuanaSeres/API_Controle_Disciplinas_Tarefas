from django.contrib import admin
from django.urls import path
from controleTarefas.views.alunos import AlunosView
from controleTarefas.views.disciplinas import DisciplinaView
from controleTarefas.views.tarefas import TarefasView
from controleTarefas.views.tarefaAluno import TarefaAlunoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/',AlunosView.as_view()),
    path('alunos/<int:pk>/',AlunosView.as_view()),
    path('disciplinas/', DisciplinaView.as_view()),
    path('disciplinas/<int:pk>/',DisciplinaView.as_view()),
    path('tarefas/', TarefasView.as_view()),
    path('tarefas/<int:pk>/',TarefasView.as_view()),
    path('alunos/<int:pk>/tarefas/', TarefaAlunoView.as_view()),
]
