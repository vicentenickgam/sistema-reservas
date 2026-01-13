from rest_framework.permissions import BasePermission

class IsOwnerOrAdminReserva(BasePermission):
    """
    Permite que solo el usuario que creó la reserva,
    el propietario del negocio o un admin pueda modificar/cancelar.
    """
    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_staff or
            obj.usuario == request.user or
            obj.negocio.propietario == request.user
        )
