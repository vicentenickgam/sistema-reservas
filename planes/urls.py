from rest_framework.routers import DefaultRouter
from .views import PlanViewSet, NegocioPlanViewSet

router = DefaultRouter()
router.register(r'planes', PlanViewSet)
router.register(r'negocio-planes', NegocioPlanViewSet)

urlpatterns = router.urls
