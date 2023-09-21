from django.db import models

from controleTarefas.models.alunos import AlunosEntidade
from controleTarefas.models.disciplinas import DisciplinasEntidade

class TarefasEntidade(models.Model):
    #define campos titulo, descrição, data, completo
    titulo = models.CharField(max_length=70)
    descrição = models.TextField()
    data = models.DateTimeField()
    completo = models.BooleanField()

    # Define um relacionamento de chave estrangeira com 'AlunosEntidade'.
    #Se o aluno for excluído, as tarefas serão excluídas também.
    AlunosTarefas = models.ForeignKey(AlunosEntidade, on_delete=models.CASCADE, blank=False, null=False)

    # Define um relacionamento muitos-para-muitos com 'DisciplinasEntidade'.
    DisiplinasTarefas = models.ManyToManyField(DisciplinasEntidade)

    #construtor string
    def __str__(self) -> str:
        return "Tarefas [%i - %s]" % (self.id, self.titulo)
    