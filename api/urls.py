from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('calendario-pago/', include('apps.calendarioPago.urls')),
    path('clientes/', include('apps.cliente.urls')),
    path('grupos/', include('apps.grupo.urls')),
    path('miembros/', include('apps.miembro.urls')),
    path('cuentas/', include('apps.cuenta.urls')),
    path('transacciones/', include('apps.transaccion.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
