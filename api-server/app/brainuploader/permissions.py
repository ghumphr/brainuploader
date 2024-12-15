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

class CanAccessDeck(permissions.BasePermission):
    """
    Custom permission to allow full access to a deck to owner and superuser, read-only access to
    staff, read-only access to anyone if deck is public, no access to non-owner/non-staff/non-superuser
    if deck is not public.
    """

    def has_object_permission(self, request, view, deck):
        if deck.is_public and request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser():
            return True
        if request.user.is_staff() and request.method in permissions.SAFE_METHODS:
            return True
        if deck.user == request.user:
            return True
        return False

class CanAccessFlashcard(permissions.BasePermission):
    """
    Custom permission to allow full access to a flashcard to deck owner and superuser, read-only access to
    staff, read-only access to anyone if flashcard's deck is public, no access to non-owner/non-staff/non-superuser
    if flashcard's deck is not public.
    """
    def has_object_permission(self, request, view, flashcard):
        if request.user.is_superuser():
            return True
        if request.user.is_staff() and request.method in permissions.SAFE_METHODS:
            return True
        deck = Deck.objects.get(flashcard.deck)
        if deck.is_public and request.method in permissions.SAFE_METHODS:
            return True
        if deck.user == request.user:
            return True
        return False

