from rest_framework import serializers
from brainuploader.models import Flashcard
from brainuploader.models import Deck
from django.core.exceptions import PermissionDenied
from django.utils.html import escape


# Base class for all Flashcard serializers
# Note: This serializer is responsible for removing *all* HTML from *all* fields on Flashcards
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
# Note: This serializer is responsible for removing *all* HTML from *all* fields on Decks
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

# This serializer is used for serializing flashcards for authenticated users
# It ensures that the deck belongs to the current user
class UserFlashcardSerializer(FlashcardSerializer):
    class Meta:
        model = Flashcard
        fields = ['next_review', 'times_right_in_a_row', 'front', 'back', 'deck', 'id',]
        read_only_fields = ['id',]

    # Makes sure that the source deck (if it exists) belongs to the current user
    # Also, make sure the destination deck belongs to the current user
    def to_internal_value(self, data):

        # First, call the current method on the parent object
        return super(UserFlashcardSerializer, self).to_internal_value(data)

        # This should never return None because otherwise, what is the current user?
        request = self.context.get('request', None)
        if request is None:
            raise PermissionDenied("User actions require a current user.")

        # If a user is changing the deck, we need to make sure the change is authorized.
        # 1. A user may move a card from one of their own decks into another of their own decks
        # 2. A user may create a card in one of their own decks
        # 3. Any other changes to the deck key by users are denied
        # Also, every card must belong to a deck
        # Aside from users and admins, no one should be modifying anything

        # If the deck is being updated, make sure the update is legal
        if("deck" in data):

            # First, make sure that the current deck (if any) belongs to the current user
            instance = self.instance  # Access the instance if it exists (for updates)
            if instance:
                previous_deck = instance.deck
                if previous_deck:
                    pd = Deck.objects.get(pk=previous_deck)
                    if pd is None or pd.user != request.user:
                        raise PermissionDenied("You do not own this card.")

            # Next, make sure that the destination deck belongs to the current user
            deck = Deck.objects.get(pk=data["deck"])
            if(deck is None or deck.user != request.user):
                raise PermissionDenied("Illegal deck parameter.")

        # If the deck is not being updated, the card must already be in a deck owned by the user
        else:
            instance = self.instance  # Access the instance if it exists (for updates)
            if instance:
                pd = instance.deck
                if pd is None or pd.user != request.user:
                    raise PermissionDenied("You do not own this card.")
            else:
                raise PermissionDenied("A flashcard must belong to a deck.")


# This serializer is used to allow unauthenticated users to see public flashcards
class PublicFlashcardSerializer(FlashcardSerializer):
    class Meta:
        model = Flashcard
        fields = ['front', 'back', 'deck', 'id',]
        read_only_fields = ['front', 'back', 'deck', 'id',]

# This serializer allows staff members to see flashcards
class StaffFlashcardSerializer(FlashcardSerializer):
    class Meta:
        model = Flashcard
        fields = ['front', 'back', 'deck', 'id',]
        read_only_fields = ['front', 'back', 'deck', 'id',]

# This serializer gives admins unrestricted access to flashcards
class AdminFlashcardSerializer(FlashcardSerializer):
    class Meta:
        model = Flashcard
        fields = '__all__'

# This serializer allows authorized users to modify their own decks
class UserDeckSerializer(DeckSerializer):
    class Meta:
        model = Deck
        fields = ['user', 'name', 'description', 'id',]
        read_only_fields = ['id',]

# This serializer grants anonymous users read-only access to decks
class PublicDeckSerializer(DeckSerializer):
    class Meta:
        model = Deck
        fields = ['id', 'user', 'name', 'description',]
        read_only_fields = ['id', 'user', 'name', 'description',]

# This serializer grants staff members read-only access to decks
class StaffDeckSerializer(DeckSerializer):
    class Meta:
        model = Deck
        fields = ['id', 'user', 'name', 'description',]
        read_only_fields = ['id', 'user', 'name', 'description',]

# This serializer grants the admin unrestricted access to decks
class AdminDeckSerializer(DeckSerializer):
    class Meta:
        model = Deck
        fields = '__all__'
