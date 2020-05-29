from django.urls import path

from .views import ClienteListar, ClienteCreate, ClienteUpdate


urlpatterns = [
    path('listar/', ClienteListar.as_view(), name="cliente_listar"),
    path('crear/', ClienteCreate.as_view(), name="cliente_crear"),
    path('editar/<id>', ClienteUpdate.as_view(), name="cliente_editar"),
]
