from django.urls import path

from .views import CalendarioPagoListar


urlpatterns = [
    path('<str:cuenta_id>/listar/', CalendarioPagoListar.as_view(), name="calendario-listar"),
]
