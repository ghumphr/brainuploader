from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsReadable(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view it unless it is public.
    """

    def has_object_permission(self, request, view, obj):
        return obj.is_public or obj.user == request.user

class IsDeckOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.deck.user == request.user

class IsDeckReadable(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.deck.is_public or obj.user == request.user
