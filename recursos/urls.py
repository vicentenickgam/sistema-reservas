from rest_framework.routers import DefaultRouter
from .views import RecursoViewSet, TipoRecursoViewSet

router = DefaultRouter()
router.register(r'recursos', RecursoViewSet, basename='recurso')
router.register(r'tipos-recurso', TipoRecursoViewSet, basename='tipo-recurso') 

urlpatterns = router.urls
