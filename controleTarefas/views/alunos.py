from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from controleTarefas.models.alunos import AlunosEntidade
from controleTarefas.serializers.alunos import AlunosSerializer

class AlunosView(APIView):

    # o método GET busca informações sobre os alunos
    def get(self, request, pk=None):
        # verifica se o id foi passado como parâmetro na URL
        if pk is not None:
            # tenta buscar um aluno pelo ID especificado
            try:
                alunos = AlunosEntidade.objects.get(pk=pk)
                serializer = AlunosSerializer(alunos, many=False)
                return Response(serializer.data)
            except AlunosEntidade.DoesNotExist:
                # retorna uma resposta de erro se o aluno não existir
                return Response({'detail': 'Aluno não existente'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # se nenhuma pk for especificado, busca todos os alunos
            alunos = AlunosEntidade.objects.all()
            serializer = AlunosSerializer(alunos, many=True)
            return Response(serializer.data)

    # o método POST cria um novo aluno
    def post(self, request, format=None):
        serializer = AlunosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # o método PUT atualiza um aluno existente
    def put(self, request, pk):
        # tenta buscar pelo ID especificado na solicitação
        try:
            alunos = AlunosEntidade.objects.get(pk=pk)
        except AlunosEntidade.DoesNotExist:
            return Response({'detail': 'Aluno não encontrado'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = AlunosSerializer(data=request.data)
         # salva as alterações se os dados forem válidos
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # o método DELETE exclui todos os alunos
    def delete(self, request, format=None):
        alunos = AlunosEntidade.objects.all()
        alunos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)