from django.db import models

from apps.grupo.models import Grupo
from apps.cliente.models import Cliente


# Create your models here.
class Miembro(models.Model):
    grupo_id = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
