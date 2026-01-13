from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import TipoNegocio, Negocio
from .serializers import TipoNegocioSerializer, NegocioSerializer
from .permissions import IsOwnerOrAdmin
from roles.permissions import IsAdminUserCustom

class TipoNegocioViewSet(ModelViewSet):
    queryset = TipoNegocio.objects.all()
    serializer_class = TipoNegocioSerializer
    permission_classes = [IsAuthenticated, IsAdminUserCustom]


class NegocioViewSet(ModelViewSet):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        else:
            return [IsAuthenticated(), IsOwnerOrAdmin()]
