from rest_framework import serializers
from controleTarefas.models.alunos import AlunosEntity

class AlunosSerializer(serializers.Serializer):
    class Meta:
        modelo = AlunosEntity
        fiels = '__all__'