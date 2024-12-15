from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# A flashcard deck
# Decks store all flashcards and link them to users and also link flashcards by topic
class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=127)
    description = models.CharField(max_length=4094)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# A flashcard
# Each flashcard is stored in a deck
class Flashcard(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    next_review = models.DateTimeField()
    times_right_in_a_row = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    front = models.CharField(max_length=16382)
    back = models.CharField(max_length=16382)

    def __str__(self):
        return "Q:" + self.front + "\n" + "A:" + self.back

