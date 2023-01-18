from rest_framework import permissions


class IsActive(permissions.BasePermission):
    """
        Allow access only to "is_active" users
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_active

class OwnProfile(permissions.BasePermission):
    """
        Allow access only if is users own profile
    """
    def has_object_permission(self, request, view, obj):
        """ Verifies if user is trying to update it's profile """

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
