from rest_framework import permissions


class IsCurrentUserOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        is_the_user = request.user == obj.user
        is_admin = request.user.is_superuser
        if request.method in permissions.SAFE_METHODS:
            return True
        return is_the_user or is_admin
