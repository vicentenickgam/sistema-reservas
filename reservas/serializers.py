from rest_framework import serializers
from .models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

    def validate(self, data):
        # Validación básica de horarios
        if data['hora_fin'] <= data['hora_inicio']:
            raise serializers.ValidationError("La hora de fin debe ser mayor a la hora de inicio.")

        # Validación de solapamiento de reservas para el mismo recurso
        solapadas = Reserva.objects.filter(
            recurso=data['recurso'],
            fecha=data['fecha'],
            hora_inicio__lt=data['hora_fin'],
            hora_fin__gt=data['hora_inicio'],
            estado__in=['pendiente', 'confirmada']
        )
        if self.instance:
            solapadas = solapadas.exclude(pk=self.instance.pk)

        if solapadas.exists():
            raise serializers.ValidationError("El recurso ya tiene otra reserva en este horario.")

        return data
