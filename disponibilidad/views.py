from rest_framework.viewsets import ModelViewSet
from .models import Disponibilidad
from .serializers import DisponibilidadSerializer

class DisponibilidadViewSet(ModelViewSet):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer
