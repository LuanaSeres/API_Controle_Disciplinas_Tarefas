from rest_framework.views import APIView
from rest_framework. response import Response
from rest_framework import status
from controleTarefas.models.alunos import AlunosEntidade
from controleTarefas.models.tarefas import TarefasEntidade
from controleTarefas.serializers.tarefas import TarefasSerializer

class TarefaAlunoView(APIView):
    def get (self, request, aluno_id):
        #Busca o aluno pelo ID 
        try:
            aluno = AlunosEntidade.objects. get (pk=aluno_id)
        except AlunosEntidade.DoesNotExist:
            return Response({'detail': 'Aluno não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        #Retorna todas tarefa com esse ID associado
        tarefas = TarefasEntidade.objects.filter(aluno_delegado=aluno)
        serializer = TarefasSerializer (tarefas, many=True)
        return Response(serializer.data)