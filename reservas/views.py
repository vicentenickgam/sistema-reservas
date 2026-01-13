from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Reserva
from .serializers import ReservaSerializer
from .permissions import IsOwnerOrAdminReserva

class ReservaViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    def get_queryset(self):
        queryset = Reserva.objects.all()
        usuario_id = self.request.query_params.get('usuario')
        negocio_id = self.request.query_params.get('negocio')
        recurso_id = self.request.query_params.get('recurso')
        if usuario_id:
            queryset = queryset.filter(usuario_id=usuario_id)
        if negocio_id:
            queryset = queryset.filter(negocio_id=negocio_id)
        if recurso_id:
            queryset = queryset.filter(recurso_id=recurso_id)
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsOwnerOrAdminReserva()]

    def perform_create(self, serializer):
        if self.request.user != serializer.validated_data['usuario'] and not self.request.user.is_staff:
            raise PermissionDenied("No tienes permiso para crear esta reserva.")
        serializer.save()
