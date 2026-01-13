from rest_framework import serializers
from .models import Pago
from planes.models import NegocioPlan

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

    def validate_negocio_plan(self, value):
        if not NegocioPlan.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El plan seleccionado no existe")
        return value
