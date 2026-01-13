from rest_framework import serializers
from .models import TipoRecurso, Recurso
from planes.models import NegocioPlan

class TipoRecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRecurso
        fields = ('id', 'nombre')


class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = (
            'id',
            'negocio',
            'tipo_recurso',
            'nombre',
            'activo',
            'creado_en',
        )

    def validate(self, data):
        negocio = data['negocio']
        plan_activo = NegocioPlan.objects.filter(
            negocio=negocio,
            activo=True
        ).first()

        if not plan_activo:
            raise serializers.ValidationError(
                "El negocio no tiene un plan activo."
            )

        total_recursos = Recurso.objects.filter(
            negocio=negocio,
            activo=True
        ).count()

        if total_recursos >= plan_activo.plan.max_recursos:
            raise serializers.ValidationError(
                "Has alcanzado el límite de recursos según tu plan."
            )

        return data
