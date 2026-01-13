from rest_framework import serializers
from .models import Disponibilidad

class DisponibilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibilidad
        fields = '__all__'

    def validate(self, data):
        if data['hora_fin'] <= data['hora_inicio']:
            raise serializers.ValidationError(
                "La hora de fin debe ser mayor a la hora de inicio."
            )
        if data['intervalo_min'] <= 0:
            raise serializers.ValidationError(
                "El intervalo debe ser mayor a 0 minutos."
            )
        return data
