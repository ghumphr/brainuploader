from rest_framework import serializers
from .models import Flashcard

class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ['id', 'category', 'last_right', 'times_right_in_a_row', 'front', 'back', 'user',]


