from django.urls import path

from .views import TransaccionListar, TransaccionCreate


urlpatterns = [
    path('listar/', TransaccionListar.as_view(), name="transaccion_listar"),
    path('crear/', TransaccionCreate.as_view(),  name="transaccion_crear"),
]
