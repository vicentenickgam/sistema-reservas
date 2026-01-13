from rest_framework import serializers
from .models import Plan, NegocioPlan

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = (
            'id',
            'nombre',
            'precio',
            'max_servicios',
            'max_recursos',
            'activo',
        )

class NegocioPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = NegocioPlan
        fields = (
            'id',
            'negocio',
            'plan',
            'fecha_inicio',
            'fecha_fin',
            'activo',
            'creado_en',
        )

    def validate(self, data):
        fecha_inicio = data.get('fecha_inicio', getattr(self.instance, 'fecha_inicio', None))
        fecha_fin = data.get('fecha_fin', getattr(self.instance, 'fecha_fin', None))

        if fecha_inicio and fecha_fin and fecha_fin <= fecha_inicio:
            raise serializers.ValidationError(
                "La fecha fin debe ser mayor a la fecha inicio."
            )
        return data

