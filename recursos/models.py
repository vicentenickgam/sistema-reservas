from django.db import models
from negocios.models import Negocio

class TipoRecurso(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Recurso(models.Model):
    negocio = models.ForeignKey(
        Negocio,
        on_delete=models.CASCADE,
        related_name='recursos'
    )
    tipo_recurso = models.ForeignKey(
        TipoRecurso,
        on_delete=models.PROTECT,
        related_name='recursos'
    )
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nombre} - {self.negocio}"
