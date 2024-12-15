from django.shortcuts import render, get_object_or_404
from brainuploader.permissions import CanAccessFlashcard
from brainuploader.permissions import CanAccessDeck
from rest_framework import generics
from django.db.models import Q
from rest_framework import viewsets
from django.contrib.auth.models import User
from brainuploader.models import Deck
from brainuploader.models import Flashcard
from rest_framework import status, permissions, renderers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from brainuploader.serializers import UserFlashcardSerializer, AdminFlashcardSerializer, PublicFlashcardSerializer, StaffFlashcardSerializer
from brainuploader.serializers import UserDeckSerializer, AdminDeckSerializer, PublicDeckSerializer, StaffDeckSerializer
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import Http404

# Create your views here.

# We plan to rely on the Django REST framework, which automatically escapes HTML
# entities. This is much less tedious and error-prone than doing it ourselves.


# This is used for the user signup
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# This is used for listing user profiles
def user_catalog(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


# This is used for showing the user profiles themselves
def user_page(request, username):
    user = get_object_or_404(User, username=username)
    
    # This grabs a list of the decks that we are allowed to view
    decks = DeckViewSet(request=request).get_queryset().filter(user=user)

    return render(request, 'user_profile.html', {'user': user, 'decks': decks})


# This is used for showing the decks
def deck_page(request, deck_id):

    # Retrieve the deck (if we are allowed to view it)
    deck = DeckViewSet(request=request).get_queryset().filter(id=deck_id).first()

    if deck is None:
        raise Http404

    # Now retrieve the flashcards (if we are allowed to view them)
    flashcards = FlashcardViewSet(request=request).get_queryset().filter(deck=deck)

    return render(request, 'deck.html', {'deck': deck, 'flashcards': flashcards})



# see for more details on generics: https://www.django-rest-framework.org/api-guide/generic-views/

# This implements the CRUD REST API for Flashcards.
# Object-level validation takes place in the permission class.
# Note that since we want field-level permissions checking, we need to do additional checks
# (which currently take place on the serializer).
# The really great thing about these is we can use them to pull querysets for use outside of the REST API.

class FlashcardViewSet(viewsets.ModelViewSet):

    permission_classes = [CanAccessFlashcard]

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return AdminFlashcardSerializer
        if self.request.user.is_staff:
            return StaffFlashcardSerializer
        if self.request.user.is_authenticated:
            return UserFlashcardSerializer
        return PublicFlashcardSerializer

    def get_queryset(self):
        """
        This view should return a list of all the flashcards in decks
        owned by the currently authenticated user or in public decks.
        """
        user = self.request.user
        if(user.is_authenticated):
            if(user.is_staff or user.is_superuser):
                return Flashcard.objects.all()
            else:
                return Flashcard.objects.all().filter(Q(deck__is_public=True) | Q(deck__user=user))
        else:
            return Flashcard.objects.all().filter(deck__is_public=True)



# This implements the CRUD REST API for Decks
# Object-level validation takes place in the permission class
# Note that since we want field-level permissions checking on write,
# we need to do additional checks (which currently take place on the serializer)

class DeckViewSet(viewsets.ModelViewSet):

    permission_classes = [CanAccessDeck]

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return AdminDeckSerializer
        if self.request.user.is_staff:
            return StaffDeckSerializer
        if self.request.user.is_authenticated:
            return UserDeckSerializer
        return PublicDeckSerializer

    def get_queryset(self):
        """
        This view should return a list of all the decks
        owned by the currently authenticated user or public.
        """
        user = self.request.user
        if(user.is_authenticated):
            if(user.is_staff or user.is_superuser):
                return Deck.objects.all()
            # Return all public decks and all user decks
            return Deck.objects.all().filter(user==user).union(Deck.objects.all().filter(is_public=True))
        return Deck.objects.all().filter(is_public=True)

