from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, RegisterView, MeView, MyTokenObtainPairView

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path("api/token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('auth/register/', RegisterView.as_view()),
    path('auth/me/', 
    MeView.as_view()),
]

urlpatterns += router.urls
