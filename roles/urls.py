from rest_framework.routers import DefaultRouter
from .views import RolViewSet, UsuarioRolViewSet

router = DefaultRouter()
router.register(r'roles', RolViewSet)
router.register(r'usuarios-roles', UsuarioRolViewSet)

urlpatterns = router.urls
