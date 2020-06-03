from django.shortcuts import redirect, get_object_or_404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer

from api.serializers import GrupoSerializer, GruposSerializer
from apps.grupo.models import Grupo


# Create your views here.
class GrupoListar(generics.ListAPIView):
    serializer_class = GrupoSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'grupo/grupo_listar.html'

    def get(self, request, *args, **kwargs):
        queryset = Grupo.objects.all()
        serializer = GrupoSerializer(queryset, many=True)
        return Response({'grupos': serializer.data})


class GrupoCreate(generics.CreateAPIView):
    serializer_class = GruposSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'grupo/grupo_crear.html'

    def get(self, request):
        queryset = Grupo.objects.all()
        serializer = GruposSerializer(queryset, many=True)

        return Response({'serializer': serializer.data})

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
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'grupo/grupo_delete.html'

    def get(self, request, id):
        grupo = get_object_or_404(Grupo, pk=id)
        serializer = GruposSerializer(grupo)

        return Response({'serializer': serializer, 'grupo': grupo})

    def post(self, request, id):
        grupo = Grupo.objects.get(pk=id)
        grupo.delete()
        return redirect('grupo_listar')
