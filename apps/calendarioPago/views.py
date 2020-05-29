from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import generics

from api.serializers import CalendarioPagoSerializer
from apps.calendarioPago.models import CalendarioPago


# Create your views here.
class CalendarioPagoListar(generics.ListAPIView):
    serializer_class = CalendarioPagoSerializer
    queryset = CalendarioPago.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = CalendarioPago.objects.filter(cuenta_id=kwargs.get('cuenta_id'))
        serializer = CalendarioPagoSerializer(queryset, many=True)

        return Response({'CalendarioPago': serializer.data})
