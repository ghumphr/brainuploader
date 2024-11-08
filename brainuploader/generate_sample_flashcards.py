import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brainuploader.settings')
import django

django.setup()

from django.contrib.auth.models import User

admin_user = User.objects.get(is_superuser=True)

from brainuploader.models import Deck
from brainuploader.models import Flashcard

deck = Deck(user=admin_user, name="Test Deck", description="This is just a test deck.")
deck.save()

flashcard0 = Flashcard(deck=deck, times_right_in_a_row=0, front="The rain in Spain falls mainly on the ____?", back="plain", last_right="1990-01-01")
flashcard0.save()

flashcard1 = Flashcard(deck=deck, times_right_in_a_row=0, front="What is the airspeed of an unladen swallow ____?", back="Blue! No, .... AAAAAGH!!", last_right="1990-01-01")
flashcard1.save()

flashcard2 = Flashcard(deck=deck, times_right_in_a_row=0, front="If a plane from North Korea crashes in the USA, where do they bury the survivors?", back="They don't bury the survivors.", last_right="1990-01-01")
flashcard2.save()

flashcard3 = Flashcard(deck=deck, times_right_in_a_row=0, front="True or false? This sentence is true.", back="False!", last_right="1990-01-01")
flashcard3.save()

flashcard4 = Flashcard(deck=deck, times_right_in_a_row=0, front="True or false? This sentence is true.", back="True!", last_right="1990-01-01")
flashcard4.save()

