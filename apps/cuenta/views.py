import json
from collections import defaultdict

from rest_framework import generics
from rest_framework.response import Response

from api.serializers import CuentaSerializer
from apps.cuenta.models import Cuenta
from apps.grupo.models import Grupo
from apps.calendarioPago.models import CalendarioPago


# Create your views here.
class CuentaListar(generics.ListAPIView):
    serializer_class = CuentaSerializer
    queryset = Cuenta.objects.all()

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

        return Response(groups)
