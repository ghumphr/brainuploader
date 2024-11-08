from django.shortcuts import render
from .permissions import IsOwner
from rest_framework import generics

# Create your views here.

from brainuploader.models import Flashcard
from rest_framework import status, permissions, renderers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from .models import Flashcard
from .serializers import FlashcardSerializer


class FlashcardDetailAPIView(generics.RetrieveAPIView):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@renderer_classes([renderers.JSONRenderer])
def rest_get_flashcard(request, flashcard_id):
    try:
        flashcard = Flashcard.objects.get(pk=flashcard_id)
        # Note: we should possibly not distinguish between "not found" and "no permission"
        if(flashcard.owner != request.user):
            return Response({'error': 'You do not have permission to view this flashcard.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = FlashcardSerializer(flashcard)
        return Response(serializer.data)
    except Flashcard.DoesNotExist:
        return Response({'error': 'Flashcard not found.'}, status=status.HTTP_404_NOT_FOUND)
