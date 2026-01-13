from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Plan, NegocioPlan
from .serializers import PlanSerializer, NegocioPlanSerializer
from .permissions import IsOwnerOrAdminPlan
from roles.permissions import IsAdminUserCustom

class PlanViewSet(ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated, IsAdminUserCustom]


class NegocioPlanViewSet(ModelViewSet):
    queryset = NegocioPlan.objects.all()
    serializer_class = NegocioPlanSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsOwnerOrAdminPlan()]
