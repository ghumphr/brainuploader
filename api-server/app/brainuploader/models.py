from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# A flashcard deck
# Decks store all flashcards and link them to Users
# It is intended for each Deck to cover a single topic
# Anyone can view the contents of a public Deck, but only the user/superuser/staff can view a Deck that is not public
class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=127)
    description = models.TextField(max_length=4094)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# A flashcard
# Each Flashcard is stored in a Deck
class Flashcard(models.Model):

    # Note: decks shouldn't actually be null, but null=True is required because the default value depends on request data
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, null=True)

    next_review = models.DateTimeField(auto_now_add=True)
    times_right_in_a_row = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    front = models.TextField(max_length=16382, blank=True)
    back = models.TextField(max_length=16382, blank=True)

    def __str__(self):
        return "Q:" + self.front + "\n" + "A:" + self.back

