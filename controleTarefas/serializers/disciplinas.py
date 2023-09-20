from rest_framework import serializers
from controleTarefas.models.disciplinas import DisciplinasEntity

class DisciplinasSerializer(serializers.Serializer):
    class Meta:
        modelo = DisciplinasEntity
        fiels = '__all__'