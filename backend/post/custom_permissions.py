from rest_framework import permissions


class IsAuthorOrStaffOrReadOnlyPermission(permissions.BasePermission):
    """
    permission check is current user staff or object author
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author or request.user.is_staff


class IsStaffPermission(permissions.BasePermission):
    """
    permission check is current user staff
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff
