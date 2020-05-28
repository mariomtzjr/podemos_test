from django.db import models

from apps.cuenta.models import Cuenta


# Create your models here.
class Transaccion(models.Model):
    id = models.IntegerField(primary_key=True)
    cuenta_id = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    monto = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return str(self.id)
