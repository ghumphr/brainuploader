from rest_framework import serializers
from .models import Flashcard
from .models import Deck

class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ['id', 'deck', 'next_review', 'times_right_in_a_row', 'front', 'back',]

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ['id', 'user', 'name', 'description',]

