from django.shortcuts import redirect
from decimal import Decimal

from rest_framework import generics

from api.serializers import TransaccionSerializer
from apps.transaccion.models import Transaccion
from apps.calendarioPago.models import CalendarioPago
from apps.cuenta.models import Cuenta


# Create your views here.
class TransaccionListar(generics.ListAPIView):
    serializer_class = TransaccionSerializer
    queryset = Transaccion.objects.all()


class TransaccionCreate(generics.CreateAPIView):
    serializer_class = TransaccionSerializer
    queryset = Transaccion.objects.all()

    def post(self, request):
        serializer = TransaccionSerializer(data=request.data)
        if serializer.is_valid():
            cuenta = Cuenta.objects.get(id=serializer.validated_data['cuenta_id'])
            calendarioPagos = CalendarioPago.objects.filter(cuenta_id=serializer.validated_data['cuenta_id'])

            print(serializer.validated_data)
            for pago in calendarioPagos:
                if pago.num_pago == 1 and Decimal(serializer.validated_data['monto']) > pago.monto:
                    print("El pago debe de ser exacto. Vuelve a intentarlo")
                elif pago.num_pago == 1 and Decimal(serializer.validated_data['monto']) < pago.monto:
                    pago.estatus = 'PARCIAL'
                    pago.save()
                else:
                    pago.estatus = 'PAGADO'
                    pago.save()
            serializer.save()
            # Si la transacción se crea correctamente, actualizamos el saldo de la cuenta
            cuenta.saldo = cuenta.monto - serializer.validated_data['monto']
            cuenta.save()
            return redirect('transaccion_listar')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
