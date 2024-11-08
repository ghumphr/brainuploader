from django.contrib import admin
from .models import Flashcard

class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('deck', 'last_right', 'times_right_in_a_row', 'front', 'back')
    search_fields = ('deck', 'last_right', 'times_right_in_a_row', 'front', 'back')
    list_filter = ('deck', 'last_right', 'times_right_in_a_row', 'front', 'back')
    list_filter = ('deck', 'last_right', 'times_right_in_a_row', 'front', 'back')
    list_display_links = ('deck', 'last_right', 'times_right_in_a_row', 'front', 'back')
    fields = ('deck', 'last_right', 'times_right_in_a_row', 'front', 'back')
    
admin.site.register(Flashcard, FlashcardAdmin)


