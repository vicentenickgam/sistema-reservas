from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Rol, UsuarioRol
from .serializers import RolSerializer, UsuarioRolSerializer
from .permissions import IsAdminUserCustom

class RolViewSet(ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [IsAuthenticated, IsAdminUserCustom]


class UsuarioRolViewSet(ModelViewSet):
    queryset = UsuarioRol.objects.all()
    serializer_class = UsuarioRolSerializer
    permission_classes = [IsAuthenticated, IsAdminUserCustom]
