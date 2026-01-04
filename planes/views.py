from rest_framework.viewsets import ModelViewSet
from .models import Plan, NegocioPlan
from .serializers import PlanSerializer, NegocioPlanSerializer

class PlanViewSet(ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class NegocioPlanViewSet(ModelViewSet):
    queryset = NegocioPlan.objects.all()
    serializer_class = NegocioPlanSerializer
