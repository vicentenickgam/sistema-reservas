from django.db import models
from usuarios.models import Usuario

class TipoNegocio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Tipo de negocio"
        verbose_name_plural = "Tipos de negocio"

    def __str__(self):
        return self.nombre


class Negocio(models.Model):
    nombre = models.CharField(max_length=150)
    tipo_negocio = models.ForeignKey(
        TipoNegocio,
        on_delete=models.PROTECT,
        related_name='negocios'
    )
    propietario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='negocios'
    )
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Negocio"
        verbose_name_plural = "Negocios"

    def __str__(self):
        return self.nombre
