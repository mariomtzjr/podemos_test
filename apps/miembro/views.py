from django.shortcuts import redirect, get_object_or_404

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from api.serializers import MiembrosSerializer
from apps.miembro.models import Miembro
from apps.grupo.models import Grupo
from apps.cliente.models import Cliente


# Create your views here.
class MiembrosListar(generics.ListAPIView):
    serializer_class = MiembrosSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'miembro/miembro_listar.html'

    def get(self, request):
        queryset = Miembro.objects.all()
        serializer = MiembrosSerializer(queryset, many=True)

        return Response({'miembros': serializer.data})


class MiembroCreate(generics.CreateAPIView):
    serializer_class = MiembrosSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'miembro/miembro_crear.html'

    def get(self, request, *args, **kwargs):
        queryset = Miembro.objects.all()
        grupos = Grupo.objects.all()
        clientes = Cliente.objects.all()
        serializer = MiembrosSerializer(queryset, many=True)
        return Response({'serializer': serializer.data, 'grupos': grupos, 'clientes': clientes})

    def post(self, request):
        serializer = MiembrosSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return redirect('miembros_listar')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MiembroUpdate(generics.UpdateAPIView):
    serializer_class = MiembrosSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'miembro/miembro_editar.html'

    def get(self, request, id):
        miembro = get_object_or_404(Miembro, pk=id)
        serializer = MiembrosSerializer(miembro)

        return Response({'serializer': serializer, 'miembro': miembro})

    def post(self, request, id):
        miembro = get_object_or_404(Miembro, pk=id)

        serializer = MiembrosSerializer(miembro, data=request.data)
        if not serializer.is_valid():
            return Response({"serializer": serializer, "miembro": miembro})
        serializer.save()
        return redirect('miembros_listar')


class MiembroDelete(generics.DestroyAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'miembro/miembro_delete.html'
    serializer_class = MiembrosSerializer

    def get(self, request, id):
        miembro = get_object_or_404(Miembro, pk=id)
        serializer = MiembrosSerializer(miembro)

        return Response({'serializer': serializer.data, 'miembro': miembro})

    def post(self, request, id):
        miembro = get_object_or_404(Miembro, pk=id)

        serializer = MiembrosSerializer(miembro, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'miembro': miembro})
        miembro.delete()
        return redirect('miembros_listar')

    def delete(self, request, id):
        miembro = get_object_or_404(Miembro, pk=id)
        miembro.delete()
        return redirect('miembros_listar')
