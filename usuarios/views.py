from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response

from .models import Usuario
from .serializers import UsuarioSerializer, MyTokenObtainPairSerializer
from .permissions import IsAdminOrSelf
from roles.models import UsuarioRol, Rol


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        if self.action == 'create':
            return []
        elif self.action in ['list', 'destroy']:
            return [IsAuthenticated(), IsAdminOrSelf()]
        else:
            return [IsAuthenticated(), IsAdminOrSelf()]

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        roles = UsuarioRol.objects.filter(usuario=user)\
            .values_list('rol__nombre', flat=True)

        return Response({
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "roles": list(roles),
            "is_staff": user.is_staff,
        })
    
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        rol_nombre = request.data.get("rol")

        if rol_nombre not in ["CLIENTE", "PROPIETARIO"]:
            return Response(
                {"error": "Rol no permitido"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        rol = Rol.objects.get(nombre=rol_nombre)
        UsuarioRol.objects.create(usuario=user, rol=rol)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer