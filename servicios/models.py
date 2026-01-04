from django.db import models
from negocios.models import Negocio

class Servicio(models.Model):
    negocio = models.ForeignKey(
        Negocio,
        on_delete=models.CASCADE,
        related_name='servicios'
    )
    nombre = models.CharField(max_length=150)
    duracion_min = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - {self.negocio}"
