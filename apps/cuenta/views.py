import json
from datetime import datetime, timedelta
from collections import defaultdict
from django.shortcuts import redirect

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from api.serializers import CuentaSerializer
from apps.cuenta.models import Cuenta
from apps.grupo.models import Grupo
from apps.calendarioPago.models import CalendarioPago
from apps.transaccion.models import Transaccion


# Create your views here.
class CuentaListar(generics.ListAPIView):
    serializer_class = CuentaSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cuenta/cuenta_listar.html'

    def get(self, request, *args, **kwargs):
        grupos = Grupo.objects.all()

        groups = {
        }

        groups['grupos'] = [{
            "grupo_id": g.id,
        } for g in grupos]

        for c in groups['grupos']:
            counts = Cuenta.objects.filter(grupo_id=c['grupo_id'])
            for c2 in counts:
                c['cuentas'] = counts.values()

        for cuentas in groups['grupos']:
            for cuenta in cuentas['cuentas']:
                calendario = CalendarioPago.objects.filter(cuenta_id=cuenta['id'])
                cuenta['calendarioPagos'] = calendario.values()

                pagos = Transaccion.objects.filter(cuenta_id=cuenta['id'])
                cuenta['pagos'] = pagos.values()

        return Response({'groups': groups})


class CuentaCreate(generics.CreateAPIView):
    serializer_class = CuentaSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cuenta/cuenta_crear.html'

    def get(self, request):
        queryset = Cuenta.objects.all()
        serializer = CuentaSerializer(queryset, many=True)
        grupos = Grupo.objects.all()

        return Response({'serializer': serializer.data, 'grupos': grupos})

    def post(self, request):
        serializer = CuentaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            fecha_inicio = datetime.now()
            num_pagos = 4

            fecha_siguiente = fecha_inicio
            for pago in range(1, num_pagos + 1, 1):
                fecha_siguiente += timedelta(days=7)

                if fecha_siguiente.weekday() == 5:
                    fecha_siguiente += timedelta(days=2)
                if fecha_siguiente.weekday() == 6:
                    fecha_siguiente += timedelta(days=1)

                CalendarioPago.objects.create(
                    cuenta_id=Cuenta.objects.get(id=request.data['id']),
                    num_pago=pago,
                    monto=float(request.data['monto']) / num_pagos,
                    fecha_pago=fecha_siguiente,
                    estatus='PENDIENTE'
                )
            return redirect('cuenta_listar')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
