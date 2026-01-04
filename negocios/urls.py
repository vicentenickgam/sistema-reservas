from rest_framework.routers import DefaultRouter
from .views import TipoNegocioViewSet, NegocioViewSet

router = DefaultRouter()
router.register(r'tipos-negocio', TipoNegocioViewSet)
router.register(r'negocios', NegocioViewSet)

urlpatterns = router.urls
