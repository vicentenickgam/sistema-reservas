from django.db import models
from usuarios.models import Usuario
from negocios.models import Negocio
from servicios.models import Servicio
from recursos.models import Recurso

class Reserva(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada_cliente', 'Cancelada por cliente'),
        ('cancelada_negocio', 'Cancelada por negocio'),
        ('reprogramada', 'Reprogramada'),
    ]

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='reservas'
    )
    negocio = models.ForeignKey(
        Negocio,
        on_delete=models.CASCADE,
        related_name='reservas'
    )
    servicio = models.ForeignKey(
        Servicio,
        on_delete=models.PROTECT,
        related_name='reservas'
    )
    recurso = models.ForeignKey(
        Recurso,
        on_delete=models.PROTECT,
        related_name='reservas'
    )
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estado = models.CharField(
        max_length=30,
        choices=ESTADOS,
        default='pendiente'
    )

    def __str__(self):
        return f"Reserva {self.id} - {self.fecha}"
