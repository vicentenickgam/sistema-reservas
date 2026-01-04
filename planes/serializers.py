from rest_framework import serializers
from .models import Plan, NegocioPlan

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class NegocioPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = NegocioPlan
        fields = '__all__'
