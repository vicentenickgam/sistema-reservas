from rest_framework import serializers
from .models import Rol, UsuarioRol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ('id', 'nombre')


class UsuarioRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRol
        fields = ('id', 'usuario', 'rol')

    def validate(self, data):
        if UsuarioRol.objects.filter(
            usuario=data['usuario'],
            rol=data['rol']
        ).exists():
            raise serializers.ValidationError(
                "El usuario ya tiene este rol asignado."
            )
        return data

