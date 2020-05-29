from rest_framework import serializers

from apps.calendarioPago.models import CalendarioPago
from apps.cliente.models import Cliente
from apps.cuenta.models import Cuenta
from apps.grupo.models import Grupo
from apps.miembro.models import Miembro
from apps.transaccion.models import Transaccion


# Serializers define the API representation.
class CalendarioPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarioPago
        fields = ['id', 'cuenta_id', 'num_pago', 'monto', 'fecha_pago', 'estatus', ]


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', ]


class MiembroSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(source='cliente_id', read_only=True)

    class Meta:
        model = Miembro
        fields = ['cliente']


class MiembrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = ['id', 'grupo_id', 'cliente_id']


class GrupoSerializer(serializers.ModelSerializer):
    miembros = MiembroSerializer(many=True)

    class Meta:
        model = Grupo
        fields = ['id', 'nombre', 'miembros']


class GruposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = ['id', 'nombre', ]


class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = ['id', 'cuenta_id', 'fecha', 'monto', ]


class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ['id', 'grupo_id', 'estatus', 'monto', 'saldo']
