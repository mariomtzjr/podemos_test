from django.urls import path, include

urlpatterns = [
    path('calendario-pago/', include('apps.calendarioPago.urls')),
    path('clientes/', include('apps.cliente.urls')),
    path('grupos/', include('apps.grupo.urls')),
    path('miembros/', include('apps.miembro.urls')),
    path('cuentas/', include('apps.cuenta.urls')),
    path('transacciones/', include('apps.transaccion.urls')),
]
