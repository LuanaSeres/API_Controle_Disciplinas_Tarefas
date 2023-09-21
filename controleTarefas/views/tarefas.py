from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from controleTarefas.models.tarefas import TarefasEntidade
from controleTarefas.serializers.tarefas import TarefasSerializer

class TarefasView(APIView):

    # o método GET busca informações sobre as tarefas
    def get(self, request, pk=None):
        # verifica se o id foi passado como parâmetro na URL
        if pk is not None:
            # tenta buscar uma tarefa pelo ID especificado
            try:
                tarefas = TarefasEntidade.objects.get(pk=pk)
                serializer = TarefasSerializer(tarefas, many=False)
                return Response(serializer.data)
            except TarefasEntidade.DoesNotExist:
                # retorna uma resposta de erro se a tarefa não existir
                return Response({'detail': 'Tarefa não existente'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # se nenhum 'id' for especificado, busca todos as tarefas
            tarefas = TarefasEntidade.objects.all()
            serializer = TarefasSerializer(tarefas, many=True)
            return Response(serializer.data)

    # o método POST cria um nova tarefa
    def post(self, request, format=None):
        serializer = TarefasSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # o método PUT atualiza uma tarefa existente
    def put(self, request, pk=None):
        # tenta buscar pelo ID especificado na solicitação
        try:
            tarefas = TarefasEntidade.objects.get(pk=pk)
        except TarefasEntidade.DoesNotExist:
            return Response({'detail': 'Tarefa não encontrada'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = TarefasSerializer(data=request.data)
        # salva as alterações se os dados forem válidos
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # o método DELETE exclui todos as tarefas
    def delete(self, request, format=None):
        tarefas = TarefasEntidade.objects.all()
        tarefas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    