from rest_framework.viewsets import ModelViewSet
from .models import Servicio
from .serializers import ServicioSerializer

class ServicioViewSet(ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
