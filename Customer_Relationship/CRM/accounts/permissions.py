from rest_framework.permissions import BasePermission

class IsManager(BasePermission):
    """
    Allows access only to users with the 'Manager' role.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and hasattr(request.user, 'employee') and request.user.employee.position == 'Manager'

class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_superuser
    
class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and hasattr(request.user, 'customer')  # Example condition