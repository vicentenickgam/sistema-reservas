from django.db import models
from recursos.models import Recurso
from django.core.exceptions import ValidationError

class Disponibilidad(models.Model):
    recurso = models.ForeignKey(
        Recurso,
        on_delete=models.CASCADE,
        related_name='disponibilidades'
    )
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    intervalo_min = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.recurso} - {self.hora_inicio}-{self.hora_fin}"
