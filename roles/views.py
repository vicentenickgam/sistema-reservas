from rest_framework.viewsets import ModelViewSet
from .models import Rol, UsuarioRol
from .serializers import RolSerializer, UsuarioRolSerializer

class RolViewSet(ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class UsuarioRolViewSet(ModelViewSet):
    queryset = UsuarioRol.objects.all()
    serializer_class = UsuarioRolSerializer
