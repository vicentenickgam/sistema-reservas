from rest_framework.routers import DefaultRouter
from .views import TipoRecursoViewSet, RecursoViewSet

router = DefaultRouter()
router.register(r'tipos-recurso', TipoRecursoViewSet)
router.register(r'recursos', RecursoViewSet)

urlpatterns = router.urls
