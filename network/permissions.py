from rest_framework.permissions import BasePermission


class IsActiveStaff(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff and request.user.is_active)  # create value into boolean
