from django.shortcuts import redirect, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from api.serializers import ClienteSerializer
from apps.cliente.models import Cliente


# Create your views here.
class ClienteListar(generics.ListAPIView):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()


class ClienteCreate(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request, *args, **kwargs):
        queryset = Cliente.objects.all()
        serializer = ClienteSerializer(queryset, many=True)
        return Response({'serializer': serializer.data})

    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('cliente_listar')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteUpdate(generics.UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get(self, request, id):
        cliente = get_object_or_404(Cliente, pk=id)
        serializer = ClienteSerializer(cliente)
        return Response({'serializer': serializer.data})

    def post(self, request, id):
        cliente = get_object_or_404(Cliente, pk=pk)
        serializer = ClienteSerializer(cliente, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'cliente': cliente})
        serializer.save()
        return redirect('cliente_listar')
