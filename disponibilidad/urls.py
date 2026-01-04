from rest_framework.routers import DefaultRouter
from .views import DisponibilidadViewSet

router = DefaultRouter()
router.register(r'disponibilidades', DisponibilidadViewSet)

urlpatterns = router.urls
