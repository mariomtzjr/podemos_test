from django.db import models


# Create your models here.
class Grupo(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)
