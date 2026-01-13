from rest_framework.permissions import BasePermission

class IsOwnerOrAdminRecurso(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_staff or
            obj.negocio.propietario == request.user
        )
