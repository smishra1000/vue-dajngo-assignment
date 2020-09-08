from django.contrib import admin
from . models import Participant


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name','participant_type','ranking')
    ordering = ('ranking',)
    search_fields = ('email', 'first_name', 'last_name','participant_type','ranking')   



# admin.site.register(Participant)