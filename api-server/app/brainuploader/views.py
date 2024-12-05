from django.shortcuts import render
from .permissions import IsOwner
from .permissions import IsDeckOwner
from rest_framework import generics

# Create your views here.

from brainuploader.models import Flashcard
from brainuploader.models import Deck
from rest_framework import status, permissions, renderers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from .models import Flashcard
from .serializers import FlashcardSerializer
from .serializers import DeckSerializer
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# see for more details on generics: https://www.django-rest-framework.org/api-guide/generic-views/

class FlashcardCreateAPIView(generics.CreateAPIView):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    permission_classes = [permissions.IsAuthenticated]

class FlashcardDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    permission_classes = [permissions.IsAuthenticated, IsDeckOwner]

class FlashcardQueryAPIView(generics.ListAPIView):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeckCreateAPIView(generics.CreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeckDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

class DeckQueryAPIView(generics.ListAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [permissions.IsAuthenticated]




# There are two major components to the API:  Search and CRUD
# Decks have metadata objects associated with them, supporting Read and Update


## Flashcard CRUD

### Flashcard Create
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@renderer_classes([renderers.JSONRenderer])
def rest_create_flashcard(request, deck_id):
    try:
        deck = Deck.objects.get(pk=deck_id)
        # FIXME: we should possibly not distinguish between "not found" and "no permission" in production
        if(deck.owner != request.user):
            return Response({'error': 'You do not have permission to create cards in this deck.'}, status=status.HTTP_403_FORBIDDEN)
        flashcard = Flashcard(
            deck=deck,
            next_review=timezone.now(),
            times_right_in_a_row=0,
            front = "",
            back = ""
        )
        flashcard.save()
        serializer = FlashcardSerializer(flashcard)
        return Response(serializer.data)
    except Deck.DoesNotExist:
        return Response({'error': 'Deck not found.'}, status=status.HTTP_404_NOT_FOUND)

### Flashcard Read/Update/Delete
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@renderer_classes([renderers.JSONRenderer])
def flashcard_detail_view(request, flashcard_id):
    try:
        flashcard = Flashcard.objects.get(pk=flashcard_id)
        # FIXME: we should possibly not distinguish between "not found" and "no permission" in production
        if(flashcard.deck.owner != request.user):
            return Response({'error': 'You do not have permission to view this flashcard.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = FlashcardSerializer(flashcard)
        return Response(serializer.data)
    except Flashcard.DoesNotExist:
        return Response({'error': 'Flashcard not found.'}, status=status.HTTP_404_NOT_FOUND)


### Flashcard Search
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@renderer_classes([renderers.JSONRenderer])
def flashcard_query_view(request):
    # TODO: implement search criteria
    queryset = Flashcard.query_flashcards()
    return Response(FlashcardSerializer(queryset, many=True).data)


### Deck Create

### Deck Read
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@renderer_classes([renderers.JSONRenderer])
def deck_detail_view(request, deck_id):
    try:
        deck = Deck.objects.get(pk=deck_id)
        # FIXME: we should possibly not distinguish between "not found" and "no permission" in production
        if(deck.owner != request.user):
            return Response({'error': 'You do not have permission to view this deck.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = DeckSerializer(deck)
        return Response(deck.data)
    except Deck.DoesNotExist:
        return Response({'error': 'Deck not found.'}, status=status.HTTP_404_NOT_FOUND)

### Deck Update

### Deck Delete

### Deck Search
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@renderer_classes([renderers.JSONRenderer])
def deck_query_view(request):
    # TODO: implement search criteria
    queryset = Deck.query_decks()
    return Response(DeckSerializer(queryset, many=True).data)

### Deck Metadata Read

### Deck Metadata Update

