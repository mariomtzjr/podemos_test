from django.urls import path

from .views import MiembrosListar, MiembroUpdate, MiembroCreate, MiembroDelete

urlpatterns = [
    path('listar/', MiembrosListar.as_view(), name="miembros_listar"),
    path('crear/', MiembroCreate.as_view(), name="miembro_crear"),
    path('editar/<int:id>', MiembroUpdate.as_view(), name="miembro_editar"),
    path('eliminar/<int:id>', MiembroDelete.as_view(), name="miembro_eliminar"),
]
