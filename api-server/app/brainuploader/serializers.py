from rest_framework import serializers
from brainuploader.models import Flashcard
from brainuploader.models import Deck
from django.core.exceptions import PermissionDenied
from django.utils.html import escape


# Base class for all Flashcard serializers
class FlashcardSerializer(serializers.ModelSerializer):

    # No HTML is allowed in the internal representation of any field
    # While it would be more elegant to store the data as-is and remove html
    # tags on display, that is also more dangerous.
    #
    def to_internal_value(self, data):
        data = super(FlashcardSerializer, self).to_internal_value(data)
        for k in data.keys():
            data[k] = escape(data[k])
        return(data)


# Base class for all Deck serializers
class DeckSerializer(serializers.ModelSerializer):

    # No HTML is allowed in the internal representation of any field
    # While it would be more elegant to store the data as-is and remove html
    # tags on display, that is also more dangerous.
    #
    def to_internal_value(self, data):
        data = super(DeckSerializer, self).to_internal_value(data)
        for k in data.keys():
            data[k] = escape(data[k])
        return(data)

class UserFlashcardSerializer(FlashcardSerializer):
    class Meta:
        model = Flashcard
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

class PublicFlashcardSerializer(FlashcardSerializer):
    class Meta:
        model = Flashcard
        fields = []
        read_only_fields = ['front', 'back', 'deck', 'id',]

class StaffFlashcardSerializer(FlashcardSerializer):
    class Meta:
        model = Flashcard
        fields = []
        read_only_fields = ['front', 'back', 'deck', 'id',]

class AdminFlashcardSerializer(FlashcardSerializer):
    class Meta:
        model = Flashcard
        fields = '__all__'

class UserDeckSerializer(DeckSerializer):
    class Meta:
        model = Deck
        fields = ['user', 'name', 'description',]
        read_only_fields = ['id',]

class PublicDeckSerializer(DeckSerializer):
    class Meta:
        model = Deck
        fields = []
        read_only_fields = ['id', 'user', 'name', 'description',]

class StaffDeckSerializer(DeckSerializer):
    class Meta:
        model = Deck
        fields = []
        read_only_fields = ['id', 'user', 'name', 'description',]

class AdminDeckSerializer(DeckSerializer):
    class Meta:
        model = Deck
        fields = '__all__'
