from django.shortcuts import redirect

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
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer

    def post(self, request):
        serializer = TransaccionSerializer(data=request.data)
        if serializer.is_valid():
            calendarioPagos = CalendarioPago.objects.filter(cuenta_id=serializer.data['cuenta_id'])
            cuenta = Cuenta.objects.get(id=serializer.data['cuenta_id'])
            print("# calendario pagos #")
            print(calendarioPagos)
            print("# cuenta #")
            print(cuenta)
            return redirect('transaccion_listar')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
