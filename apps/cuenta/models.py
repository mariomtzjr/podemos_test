from django.db import models

from apps.grupo.models import Grupo


# Create your models here.
class Cuenta(models.Model):
    ESTATUS = [
        ('DESEMBOLSADA', 'DESEMBOLSADA'),
        ('CERRADA', 'CERRADA'),
    ]
    id = models.CharField(max_length=5, primary_key=True)
    grupo_id = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name="grupos")
    estatus = models.CharField(max_length=15, choices=ESTATUS, default='DESEMBOLSADA')
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    saldo = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return str(self.id)
