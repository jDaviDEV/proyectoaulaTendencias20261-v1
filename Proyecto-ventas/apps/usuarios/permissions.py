from rest_framework.permissions import BasePermission
 
 
class EsAdministrador(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.rol == 'administrador'
        )
 
 
class EsVendedorOAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.rol in ['vendedor', 'administrador']
        )
 
 
class EsContadorOAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.rol in ['contador', 'administrador']
        )