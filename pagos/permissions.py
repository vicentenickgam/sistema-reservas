from rest_framework.permissions import BasePermission

class IsOwnerOrAdminPago(BasePermission):
    """
    Solo el usuario que realiza el pago o admin puede crear/editar pagos.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.usuario == request.user
