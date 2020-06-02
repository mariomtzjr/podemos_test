from django.shortcuts import redirect, get_object_or_404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from api.serializers import MiembrosSerializer
from apps.miembro.models import Miembro


# Create your views here.
class MiembrosListar(generics.ListAPIView):
    serializer_class = MiembrosSerializer
    queryset = Miembro.objects.all()


class MiembroCreate(generics.CreateAPIView):
    serializer_class = MiembrosSerializer

    def post(self, request):
        serializer = MiembrosSerializer(data=(request.data))

        if serializer.is_valid():
            serializer.save()
            return redirect('miembros_listar')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MiembroUpdate(generics.UpdateAPIView):
    serializer_class = MiembrosSerializer
    queryset = Miembro.objects.all()

    def get(self, request, id):
        miembro = get_object_or_404(Miembro, pk=id)
        serializer = MiembrosSerializer(miembro)

        return Response({'serializer': serializer.data})

    def post(self, request, id):
        miembro = get_object_or_404(Miembro, pk=id)

        serializer = MiembrosSerializer(miembro, data=request.data)
        if not serializer.is_valid():
            return Response({serializer})
        serializer.save()
        return redirect('miembros_listar')


class MiembroDelete(generics.DestroyAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembrosSerializer

    def get(self, request, id):
        miembro = get_object_or_404(Miembro, pk=id)
        serializer = MiembrosSerializer(miembro)

        return Response({'serializer': serializer.data})

    def post(self, request, id):
        miembro = get_object_or_404(Miembro, pk=id)

        serializer = MiembrosSerializer(miembro, data=request.data)
        if not serializer.is_valid():
            return Response({serializer})
        miembro.delete()
        return redirect('miembros_listar')
    
    def delete(self, request, id):
        miembro = get_object_or_404(Miembro, pk=id)
        miembro.delete()
        return redirect('miembros_listar')
