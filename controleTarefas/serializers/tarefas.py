from rest_framework import serializers
from controleTarefas.models.tarefas import TarefasEntity

class AlunosSerializer(serializers.Serializer):
    class Meta:
        modelo = TarefasEntity
        fiels = '__all__'