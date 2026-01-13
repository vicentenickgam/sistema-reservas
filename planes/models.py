from django.db import models
from negocios.models import Negocio

class Plan(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    max_servicios = models.PositiveIntegerField()
    max_recursos = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Planes"

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
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Plan del negocio"
        verbose_name_plural = "Planes del negocio"
        constraints = [
            models.UniqueConstraint(
                fields=['negocio', 'activo'],
                condition=models.Q(activo=True),
                name='un_solo_plan_activo_por_negocio'
            )
        ]

    def __str__(self):
        return f"{self.negocio} - {self.plan}"
