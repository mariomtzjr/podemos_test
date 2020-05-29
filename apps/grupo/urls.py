from django.urls import path

from .views import GrupoListar, GrupoCreate, GrupoDelete


urlpatterns = [
    path('listar/', GrupoListar.as_view(), name="grupo_listar"),
    path('crear/', GrupoCreate.as_view(), name="grupo_crear"),
    path('eliminar/<str:id>', GrupoDelete.as_view(), name="grupo_eliminar"),
]
