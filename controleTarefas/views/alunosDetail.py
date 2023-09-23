from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from controleTarefas.models.alunos import AlunosEntidade
from controleTarefas.serializers.alunos import AlunosSerializer

class AlunosDetailView (APIView):

    def get_object(self, pk):
        try:
            return AlunosEntidade.objects.get(pk=pk)
        except AlunosEntidade.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        alunos = self.get_object(pk)
        serializer = AlunosSerializer(alunos)
        return Response(serializer.data)

    # o método PUT atualiza um aluno existente
    def put(self, request, pk, format=None):
        alunos = self.get_object(pk)        
        serializer = AlunosSerializer(alunos,data=request.data)
         # salva as alterações se os dados forem válidos
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # o método DELETE exclui todos os alunos
    def delete(self, request, pk, format=None):
        alunos = self.get_object(pk)
        alunos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)