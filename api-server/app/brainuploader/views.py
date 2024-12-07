from django.shortcuts import render
from .permissions import IsOwner
from .permissions import IsDeckOwner
from rest_framework import generics

# Create your views here.

from rest_framework import viewsets
from django.contrib.auth.models import User
from brainuploader.models import Deck
from brainuploader.models import Flashcard
from rest_framework import status, permissions, renderers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from .serializers import FlashcardSerializer
from .serializers import DeckSerializer
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# We plan to rely on the Django REST framework, which automatically escapes HTML
# entities. This is much less tedious and error-prone than doing it ourselves.



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# see for more details on generics: https://www.django-rest-framework.org/api-guide/generic-views/

class FlashcardViewSet(viewsets.ModelViewSet):
#    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer

    def get_queryset(self):
        """
        This view should return a list of all the flashcards in decks
        owned by the currently authenticated user or in public decks.
        """
        user = self.request.user
        user_viewset = Flashcard.objects.none()
        if(user is not None):
                user_viewset = Flashcard.objects.all().filter(deck__user=user)
        else:
                user_viewset = Flashcard.objects.none()
        public_viewset = Flashcard.objects.all().filter(deck__is_public=True)
        return public_viewset.union(user_viewset)


#class FlashcardQueryAPIView(generics.ListAPIView):
#    queryset = Flashcard.objects.all()
#    serializer_class = FlashcardSerializer
#    permission_classes = [permissions.IsAuthenticated]

class DeckViewSet(viewsets.ModelViewSet):
#    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    def get_queryset(self):
        """
        This view should return a list of all the decks
        owned by the currently authenticated user or public.
        FIXME: this doesn't address public decks yet
        """
        user = self.request.user
        return Deck.objects.all().filter(user==user).union(Deck.objects.all().filter(is_public=True))


#class DeckQueryAPIView(generics.ListAPIView):
#    queryset = Deck.objects.all()
#    serializer_class = DeckSerializer
#    permission_classes = [permissions.IsAuthenticated]
