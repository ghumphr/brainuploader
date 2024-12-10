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

class OwnerFlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        # Note: the deck field requires careful validation on modification
        fields = ['next_review', 'times_right_in_a_row', 'front', 'back', 'deck']
        read_only_fields = ['id',]

class PublicFlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = []
        read_only_fields = ['front', 'back', 'deck', 'id',]

class StaffFlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = []
        read_only_fields = ['front', 'back', 'deck', 'id',]

class AdminFlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = '__all__'

class OwnerDeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ['user', 'name', 'description',]
        read_only_fields = ['id',]

class PublicDeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = []
        read_only_fields = ['id', 'user', 'name', 'description',]

class StaffDeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = []
        read_only_fields = ['id', 'user', 'name', 'description',]

class AdminDeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = '__all__'
