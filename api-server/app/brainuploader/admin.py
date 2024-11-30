from django.contrib import admin
from .models import Flashcard
from .models import Deck

class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('deck', 'next_review', 'times_right_in_a_row', 'front', 'back')
    search_fields = ('deck', 'next_review', 'times_right_in_a_row', 'front', 'back')
    list_filter = ('deck', 'next_review', 'times_right_in_a_row', 'front', 'back')
    list_filter = ('deck', 'next_review', 'times_right_in_a_row', 'front', 'back')
    list_display_links = ('deck', 'next_review', 'times_right_in_a_row', 'front', 'back')
    fields = ('deck', 'next_review', 'times_right_in_a_row', 'front', 'back')
    
admin.site.register(Flashcard, FlashcardAdmin)


class DeckAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'description',)
    search_fields = ('user', 'name', 'description',)
    list_filter = ('user', 'name', 'description',)
    list_filter = ('user', 'name', 'description',)
    list_display_links = ('user', 'name', 'description',)
    fields = ('user', 'name', 'description',)
    
admin.site.register(Deck, DeckAdmin)

