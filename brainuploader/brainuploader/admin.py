from django.contrib import admin
from .models import Flashcard

class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_right', 'times_right_in_a_row', 'front', 'back')
    search_fields = ('user', 'last_right', 'times_right_in_a_row', 'front', 'back')
    list_filter = ('user', 'last_right', 'times_right_in_a_row', 'front', 'back')
    list_filter = ('user', 'last_right', 'times_right_in_a_row', 'front', 'back')
    list_display_links = ('user', 'last_right', 'times_right_in_a_row', 'front', 'back')
    fields = ('user', 'last_right', 'times_right_in_a_row', 'front', 'back')
    
admin.site.register(Flashcard, FlashcardAdmin)


