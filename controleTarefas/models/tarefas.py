from django.db import models

from models.alunos import AlunosEntity
from models.disciplinas import DisciplinasEntity

class TarefasEntidade(models.Model):
    titulo = models.CharField(max=70)
    descrição = models.TextField()
    data = models.DateTimeField()
    completo = models.BooleanField()

    AlunosTarefas = models.ForeignKey(AlunosEntity, on_delete=models.CASCADE, blank=False, null=False)

    DisiplinasTarefas = models.ManyToManyField(DisciplinasEntity)

    #construtor string
    def __str__(self) -> str:
        return "Tarefas [i% - s%]" % (self.id, self.title)
    