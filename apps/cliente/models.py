from django.db import models


# Create your models here.
class Cliente(models.Model):
    id = models.CharField(max_length=7, primary_key=True)
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.id
