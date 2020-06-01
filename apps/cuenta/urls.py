from django.urls import path

from .views import CuentaListar, CuentaCreate


urlpatterns = [
    path('listar/', CuentaListar.as_view(), name="cuenta_listar"),
    path('crear/', CuentaCreate.as_view(),  name="cuenta_crear"),
]
