from django.db import models

class AlunosEntidade(models.Model):
    #define campos nome e email
    nome = models.CharField(max=100)
    email = models.CharField(max=200)

    #construtor string
    def __str__(self) -> str:
        return "Alunos [%i- %s]" % (self.id, self.nome)