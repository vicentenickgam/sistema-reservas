from rest_framework.viewsets import ModelViewSet
from .models import Pago
from .serializers import PagoSerializer

class PagoViewSet(ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
