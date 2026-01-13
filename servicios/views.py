from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Servicio
from .serializers import ServicioSerializer
from .permissions import IsOwnerOrAdminServicio

class ServicioViewSet(ModelViewSet):
    serializer_class = ServicioSerializer

    def get_queryset(self):
        queryset = Servicio.objects.filter(activo=True)
        negocio_id = self.request.query_params.get('negocio')
        if negocio_id:
            queryset = queryset.filter(negocio_id=negocio_id)
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated(), IsOwnerOrAdminServicio()]
