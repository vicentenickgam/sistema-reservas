from rest_framework.viewsets import ModelViewSet
from .models import TipoNegocio, Negocio
from .serializers import TipoNegocioSerializer, NegocioSerializer

class TipoNegocioViewSet(ModelViewSet):
    queryset = TipoNegocio.objects.all()
    serializer_class = TipoNegocioSerializer


class NegocioViewSet(ModelViewSet):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer
