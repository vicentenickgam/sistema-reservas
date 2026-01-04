from django.db import models
from recursos.models import Recurso

class Disponibilidad(models.Model):
    recurso = models.ForeignKey(
        Recurso,
        on_delete=models.CASCADE,
        related_name='disponibilidades'
    )
    dia_semana = models.IntegerField(
        choices=[
            (0, 'Lunes'),
            (1, 'Martes'),
            (2, 'Miércoles'),
            (3, 'Jueves'),
            (4, 'Viernes'),
            (5, 'Sábado'),
            (6, 'Domingo'),
        ]
    )
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    intervalo_min = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.recurso} - {self.get_dia_semana_display()}"
