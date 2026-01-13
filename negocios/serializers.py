from rest_framework import serializers
from .models import TipoNegocio, Negocio

class TipoNegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoNegocio
        fields = ('id', 'nombre')


class NegocioSerializer(serializers.ModelSerializer):
    propietario = serializers.ReadOnlyField(source='propietario.id')

    class Meta:
        model = Negocio
        fields = (
            'id',
            'nombre',
            'tipo_negocio',
            'propietario',
            'activo',
            'creado_en',
        )

    def create(self, validated_data):
        validated_data['propietario'] = self.context['request'].user
        return super().create(validated_data)

