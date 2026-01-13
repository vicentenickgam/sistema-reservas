from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import TipoRecurso, Recurso
from .serializers import TipoRecursoSerializer, RecursoSerializer
from .permissions import IsOwnerOrAdminRecurso

class TipoRecursoViewSet(ModelViewSet):
    queryset = TipoRecurso.objects.all()
    serializer_class = TipoRecursoSerializer
    permission_classes = [IsAuthenticated]


class RecursoViewSet(ModelViewSet):
    serializer_class = RecursoSerializer

    def get_queryset(self):
        queryset = Recurso.objects.filter(activo=True)
        negocio_id = self.request.query_params.get('negocio')
        if negocio_id:
            queryset = queryset.filter(negocio_id=negocio_id)
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated(), IsOwnerOrAdminRecurso()]
