from django.contrib import admin
from brainuploader.models import Flashcard
from brainuploader.models import Deck
from django.forms import Textarea
from django.db import models

# Set up admin interface for Flashcard model
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('deck', 'next_review', 'times_right_in_a_row', 'front', 'back')
    search_fields = ('deck', 'next_review', 'times_right_in_a_row', 'front', 'back')
    list_filter = ('deck', 'next_review', 'times_right_in_a_row', 'front', 'back')
    list_filter = ('deck', 'next_review', 'times_right_in_a_row', 'front', 'back')
    list_display_links = ('deck', 'next_review', 'times_right_in_a_row', 'front', 'back')
    fields = ('deck', 'next_review', 'times_right_in_a_row', 'front', 'back')
    
admin.site.register(Flashcard, FlashcardAdmin)


# Set up admin interface for Deck model
class DeckAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'description', 'is_public',)
    search_fields = ('user', 'name', 'description', 'is_public',)
    list_filter = ('user', 'name', 'description', 'is_public',)
    list_filter = ('user', 'name', 'description', 'is_public',)
    list_display_links = ('user', 'name', 'description', 'is_public',)
    fields = ('user', 'name', 'description', 'is_public',)
    
admin.site.register(Deck, DeckAdmin)

