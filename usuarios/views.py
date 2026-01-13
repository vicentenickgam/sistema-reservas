from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Usuario
from .serializers import UsuarioSerializer
from .permissions import IsAdminOrSelf

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        if self.action == 'create':
            return []
        elif self.action in ['list', 'destroy']:
            return [IsAuthenticated(), IsAdminOrSelf()]
        else:
            return [IsAuthenticated(), IsAdminOrSelf()]
