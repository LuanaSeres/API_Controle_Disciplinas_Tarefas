from rest_framework import serializers
from controleTarefas.models.disciplinas import DisciplinasEntidade

class DisciplinasSerializer(serializers.Serializer):
    class Meta:
        model = DisciplinasEntidade
        fields = '__all__'