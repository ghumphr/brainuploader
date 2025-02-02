from rest_framework import serializers
from brainuploader.models import Flashcard
from brainuploader.models import Deck
from django.core.exceptions import PermissionDenied
from django.utils.html import escape


class FlashcardSerializer(serializers.ModelSerializer):
    """
    Base class for all Flashcard serializers
    Note: This serializer is responsible for removing *all* HTML from *all* fields on Flashcards
    """

    # No HTML is allowed in the internal representation of any field
    # While it would be more elegant to store the data as-is and remove html
    # tags on display, that is also more dangerous.
    #
    def to_internal_value(self, data):
        data = super(FlashcardSerializer, self).to_internal_value(data)
        for k in data.keys():
            data[k] = escape(data[k])
        return(data)


class DeckSerializer(serializers.ModelSerializer):
    """
    Base class for all Deck serializers
    Note: This serializer is responsible for removing *all* HTML from *all* fields on Decks
    """

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
    """
    This serializer is used for serializing flashcards for authenticated users
    It ensures that the deck belongs to the current user
    This is more complex than I would like, but we need field-level permission validation.
    """

    class Meta:
        model = Flashcard
        fields = ['next_review', 'times_right_in_a_row', 'front', 'back', 'deck', 'id',]
        read_only_fields = ['id',]

    # Makes sure that the source deck (if it exists) belongs to the current user
    # Also, make sure the destination deck belongs to the current user
    def to_internal_value(self, data):

        # First, call the current method on the parent object
        data = super(UserFlashcardSerializer, self).to_internal_value(data)

        # This should never return None because otherwise, what is the current user?
        request = self.context.get('request', None)
        if request is None:
            raise PermissionDenied("User actions require a current context.")

        # If a user is changing the deck, we need to make sure the change is authorized.
        # 1. A user may move a card from one of their own decks into another of their own decks
        # 2. A user may create a card in one of their own decks
        # 3. Any other changes to the deck key by users are denied
        # Also, every card must belong to a deck
        # Aside from users and admins, no one should be modifying anything
        # Most of these checks *should* be made elsewhere, but the destination deck owner must be checked here.

        # If the deck is being updated, make sure the update is legal
        if("deck" in data):

# The code below is commented out because it *should* not be necessary
#
#            # First, make sure that the current deck (if any) belongs to the current user.
#            # This should never be triggered due to the permissions model.
#            instance = self.instance  # Access the instance if it exists (for updates)
#            if instance:
#                previous_deck = instance.deck
#                if previous_deck:
#                    pd = Deck.objects.get(pk=previous_deck)
#                    if pd is None or pd.user != request.user:
#                        raise PermissionDenied("You do not own this card.")

            # Make sure that the destination deck belongs to the current user.
            # This is the important part - this check can't be performed at the object level.
            deck = Deck.objects.get(pk=data["deck"])
            if(deck is None or deck.user != request.user):
                raise PermissionDenied("Illegal deck parameter.")

# The code below is commented out because it *should* not be necessary
#
#        # If the deck is not being updated, the card must already be in a deck owned by the user.
#        # This should never be triggered due to the permissions model.
#        else:
#            instance = self.instance  # Access the instance if it exists (for updates)
#            if instance:
#                pd = instance.deck
#                if pd is None or pd.user != request.user:
#                    raise PermissionDenied("You do not own this card.")
#            else:
#                raise PermissionDenied("A flashcard must belong to a deck.")

        return data


class PublicFlashcardSerializer(FlashcardSerializer):
    """
    This serializer is used to allow unauthenticated users to see public flashcards
    """

    class Meta:
        model = Flashcard
        fields = ['front', 'back', 'deck', 'id',]
        read_only_fields = ['front', 'back', 'deck', 'id',]

class StaffFlashcardSerializer(FlashcardSerializer):
    """
    This serializer allows staff members to see flashcards
    """

    class Meta:
        model = Flashcard
        fields = ['front', 'back', 'deck', 'id',]
        read_only_fields = ['front', 'back', 'deck', 'id',]

class AdminFlashcardSerializer(FlashcardSerializer):
    """
    This serializer gives admins unrestricted access to flashcards
    """

    class Meta:
        model = Flashcard
        fields = '__all__'

class UserDeckSerializer(DeckSerializer):
    """
    This serializer allows authorized users to modify their own decks
    """

    class Meta:
        model = Deck
        fields = ['user', 'name', 'description', 'id',]
        read_only_fields = ['id',]

class PublicDeckSerializer(DeckSerializer):
    """
    This serializer grants anonymous users read-only access to public decks
    """

    class Meta:
        model = Deck
        fields = ['id', 'user', 'name', 'description',]
        read_only_fields = ['id', 'user', 'name', 'description',]

class StaffDeckSerializer(DeckSerializer):
    """
    This serializer grants staff members read-only access to decks
    """

    class Meta:
        model = Deck
        fields = ['id', 'user', 'name', 'description',]
        read_only_fields = ['id', 'user', 'name', 'description',]

class AdminDeckSerializer(DeckSerializer):
    """
    This serializer grants the admin unrestricted access to decks
    """

    class Meta:
        model = Deck
        fields = '__all__'
