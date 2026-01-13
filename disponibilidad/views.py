from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Disponibilidad
from .serializers import DisponibilidadSerializer
from .permissions import IsOwnerOrAdminDisponibilidad

class DisponibilidadViewSet(ModelViewSet):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer

    def get_queryset(self):
        queryset = Disponibilidad.objects.filter(activo=True)
        recurso_id = self.request.query_params.get('recurso')
        if recurso_id:
            queryset = queryset.filter(recurso_id=recurso_id)
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated(), IsOwnerOrAdminDisponibilidad()]
