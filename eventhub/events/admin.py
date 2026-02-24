from django.contrib import admin
from eventhub.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'venue', 'event_date', 'event_time', 'is_published')
    list_filter = ('is_published', 'event_date')
    search_fields = ('title', 'description')
