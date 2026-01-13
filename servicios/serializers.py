from rest_framework import serializers
from .models import Servicio
from planes.models import NegocioPlan

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = (
            'id',
            'negocio',
            'nombre',
            'duracion_min',
            'precio',
            'activo',
            'creado_en',
        )

    def validate(self, data):
        # Obtener el negocio: del patch si existe, o de la instancia si es update
        negocio = data.get('negocio', getattr(self.instance, 'negocio', None))
        if not negocio:
            raise serializers.ValidationError("El negocio es obligatorio.")

        # Verificar que el negocio tenga un plan activo
        plan_activo = NegocioPlan.objects.filter(
            negocio=negocio,
            activo=True
        ).first()

        if not plan_activo:
            raise serializers.ValidationError(
                "El negocio no tiene un plan activo."
            )

        # Contar servicios activos, excluyendo el actual si es update
        total_servicios = Servicio.objects.filter(
            negocio=negocio,
            activo=True
        )
        if self.instance:
            total_servicios = total_servicios.exclude(id=self.instance.id)
        total_servicios = total_servicios.count()

        # Validar límite de servicios según el plan
        if total_servicios >= plan_activo.plan.max_servicios:
            raise serializers.ValidationError(
                "Has alcanzado el límite de servicios según tu plan."
            )

        return data
