from django.db import models
from negocios.models import Negocio

class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    max_servicios = models.IntegerField()
    max_recursos = models.IntegerField()

    def __str__(self):
        return self.nombre


class NegocioPlan(models.Model):
    negocio = models.ForeignKey(
        Negocio,
        on_delete=models.CASCADE,
        related_name='planes'
    )
    plan = models.ForeignKey(
        Plan,
        on_delete=models.PROTECT,
        related_name='negocios'
    )
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.negocio} - {self.plan}"
