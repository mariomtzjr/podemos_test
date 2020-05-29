from django.urls import path

from .views import CuentaListar


urlpatterns = [
    path('listar/', CuentaListar.as_view(), name="cuenta_listar"),
]
