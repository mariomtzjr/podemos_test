from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Se comenta para resolver la importación circular
# from apps.cuenta.models import Cuenta


# Create your models here.
class CalendarioPago(models.Model):

    CALENDARIO_CHOICES = [
        ('PENDIENTE', 'PENDIENTE'),
        ('PAGADO', 'PAGADO'),
        ('PARCIAL', 'PARCIAL'),
        ('ATRASADO', 'ATRASADO'),
    ]
    id = models.IntegerField(primary_key=True)
    cuenta_id = models.ForeignKey('cuenta.Cuenta', on_delete=models.CASCADE)
    num_pago = models.IntegerField()
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_pago = models.DateField()
    estatus = models.CharField(max_length=15, choices=CALENDARIO_CHOICES, default='PENDIENTE')

    def __str__(self):
        return str(self.id)
