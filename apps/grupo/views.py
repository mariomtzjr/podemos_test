from django.shortcuts import redirect, get_object_or_404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from api.serializers import GrupoSerializer, GruposSerializer
from apps.grupo.models import Grupo


# Create your views here.
class GrupoListar(generics.ListAPIView):
    serializer_class = GrupoSerializer
    queryset = Grupo.objects.all()


class GrupoCreate(generics.CreateAPIView):
    serializer_class = GrupoSerializer

    def post(self, request):
        # Llamamos a GruposSerializer para que no exija miembros
        serializer = GruposSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('grupo_listar')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GrupoDelete(generics.DestroyAPIView):
    serializer_class = GruposSerializer

    def get(self, request, id):
        grupo = get_object_or_404(Grupo, pk=id)
        serializer = GruposSerializer(grupo)

        return Response({'serializer': serializer.data})

    def post(self, request, id):
        grupo = get_object_or_404(Grupo, pk=id)
        serializer = GruposSerializer(grupo, data=request.data)

        if not serializer.is_valid():
            return Response({serializer})
        grupo.delete()

        return redirect('grupo_listar')
