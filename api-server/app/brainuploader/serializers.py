from rest_framework import serializers
from brainuploader.models import Flashcard
from brainuploader.models import Deck
from django.core.exceptions import PermissionDenied

class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ['id', 'deck', 'next_review', 'times_right_in_a_row', 'front', 'back',]

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ['id', 'user', 'name', 'description',]

class UserFlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        # Note: the deck field requires careful validation on modification
        fields = ['next_review', 'times_right_in_a_row', 'front', 'back', 'deck']
        read_only_fields = ['id',]

    # This makes sure the destination deck belongs to the current user
    def to_internal_value(self, data):
        if("deck" in data):
            request = self.context.get('request', None)
            deck = Deck.objects.get(pk=data["deck"])
            if(deck is None or deck.user != request.user):
                raise PermissionDenied("Illegal deck parameter.")
        return super(UserFlashcardSerializer, self).to_internal_value(data)

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

class UserDeckSerializer(serializers.ModelSerializer):
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
