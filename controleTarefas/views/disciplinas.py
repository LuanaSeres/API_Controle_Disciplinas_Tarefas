from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from controleTarefas.models.disciplinas import DisciplinasEntidade
from controleTarefas.serializers.disciplinas import DisciplinasSerializer

class DisciplinaView(APIView):

    # o método GET busca informações sobre as disciplinas
    def get(self, request, pk=None):
         # verifica se o id foi passado como parâmetro na URL
        if pk is not None:
            # tenta buscar uma disciplina pelo ID especificado
            try:
                disciplina = DisciplinasEntidade.objects.get(pk=pk)
                serializer = DisciplinasSerializer(disciplina, many=False)
                return Response(serializer.data)
            except DisciplinasEntidade.DoesNotExist:
                # retorna uma resposta de erro se a disciplina não existir
                return Response({'detail': 'Disciplina não existente'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # se nenhuma pk for especificado, busca todos as disciplinas
            disciplina = DisciplinasEntidade.objects.all()
            serializer = DisciplinasSerializer(disciplina, many=True)
            return Response(serializer.data)

    # o método POST cria um nova disciplina
    def post(self, request, format=None):
        serializer = DisciplinasSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # o método PUT atualiza uma disciplina existente
    def put(self, request, pk=None):
        # tenta buscar pelo ID especificado na solicitação
        try:
            disciplina = DisciplinasEntidade.objects.get(pk=pk)
        except DisciplinasEntidade.DoesNotExist:
            return Response({'detail': 'Disciplina não encontrada'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = DisciplinasSerializer(data=request.data)
        # salva as alterações se os dados forem válidos
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # o método DELETE exclui todos as disciplinas
    def delete(self, request, format=None):
        disciplina = DisciplinasEntidade.objects.all()
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)