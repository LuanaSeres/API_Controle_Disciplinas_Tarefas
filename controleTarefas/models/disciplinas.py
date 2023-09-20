from django.db import models

class DisciplinasEntidade(models.Model):
    nome = models.CharField(max=70)
    descrição = models.TextField()

    #construtor string
    def __str__(self) -> str:
        return "Dispiplina [i% - s%]" % (self.id, self.nome)