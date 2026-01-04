from rest_framework.viewsets import ModelViewSet
from .models import TipoRecurso, Recurso
from .serializers import TipoRecursoSerializer, RecursoSerializer

class TipoRecursoViewSet(ModelViewSet):
    queryset = TipoRecurso.objects.all()
    serializer_class = TipoRecursoSerializer


class RecursoViewSet(ModelViewSet):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer
