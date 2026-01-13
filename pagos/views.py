from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Pago
from .serializers import PagoSerializer
from .permissions import IsOwnerOrAdminPago

class PagoViewSet(ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsOwnerOrAdminPago()]

    def get_queryset(self):
        queryset = Pago.objects.all()
        usuario_id = self.request.query_params.get('usuario')
        plan_id = self.request.query_params.get('plan')
        if usuario_id:
            queryset = queryset.filter(usuario_id=usuario_id)
        if plan_id:
            queryset = queryset.filter(negocio_plan_id=plan_id)
        return queryset
