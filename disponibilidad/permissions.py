from rest_framework.permissions import BasePermission

class IsOwnerOrAdminDisponibilidad(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.recurso.negocio.propietario == request.user
