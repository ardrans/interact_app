from rest_framework import permissions

class IsOwnerOrApp(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated and request.user.is_staff:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user