from django.shortcuts import render
from .permissions import IsOwner
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


class FlashcardDetailAPIView(generics.RetrieveAPIView):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
# TODO: removed for prototyping purposes only
#    permission_classes = [permissions.IsAuthenticated, IsOwner]

class DeckDetailAPIView(generics.RetrieveAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
# TODO: removed for prototyping purposes only
#    permission_classes = [permissions.IsAuthenticated, IsOwner]

class FlashcardQueryAPIView(generics.ListAPIView):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
# TODO: removed for prototyping purposes only
#    permission_classes = [permissions.IsAuthenticated, IsOwner]

class DeckQueryAPIView(generics.ListAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
# TODO: removed for prototyping purposes only
#    permission_classes = [permissions.IsAuthenticated, IsOwner]

@api_view(['GET'])
#@permission_classes([permissions.IsAuthenticated])
@renderer_classes([renderers.JSONRenderer])
def rest_get_flashcard(request, flashcard_id):
    try:
        flashcard = Flashcard.objects.get(pk=flashcard_id)
        # Note: we should possibly not distinguish between "not found" and "no permission"
# TODO: for the prototype, we are disabling authentication
#        if(flashcard.owner != request.user):
#            return Response({'error': 'You do not have permission to view this flashcard.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = FlashcardSerializer(flashcard)
        return Response(serializer.data)
    except Flashcard.DoesNotExist:
        return Response({'error': 'Flashcard not found.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
#@permission_classes([permissions.IsAuthenticated])
@renderer_classes([renderers.JSONRenderer])
def rest_get_deck(request, deck_id):
    try:
        deck = Deck.objects.get(pk=deck_id)
        # Note: we should possibly not distinguish between "not found" and "no permission"
# TODO: for the prototype, we are disabling authentication
#        if(deck.owner != request.user):
#            return Response({'error': 'You do not have permission to view this deck.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = DeckSerializer(deck)
        return Response(deck.data)
    except Deck.DoesNotExist:
        return Response({'error': 'Deck not found.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
#@permission_classes([permissions.IsAuthenticated])
@renderer_classes([renderers.JSONRenderer])
def rest_query_flashcards(request):
    # TODO: implement search criteria
    queryset = Flashcard.query_flashcards()
    return Response(FlashcardSerializer(queryset, many=True).data)

@api_view(['GET'])
#@permission_classes([permissions.IsAuthenticated])
@renderer_classes([renderers.JSONRenderer])
def rest_query_decks(request):
    # TODO: implement search criteria
    queryset = Deck.query_decks()
    return Response(DeckSerializer(queryset, many=True).data)



