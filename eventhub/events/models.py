from django.db import models
from django.core.exceptions import ValidationError
from eventhub.venues.models import Venue
from eventhub.categories.models import Category


class Event(models.Model):

    class Meta:
        ordering = ['event_date', 'event_time']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()
    event_time = models.TimeField()
    venue = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE,
        related_name='events'
    )
    categories = models.ManyToManyField(
        Category,
        related_name='events',
        blank=True
    )
    max_attendees = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return self.title

    def clean(self):
        if self.max_attendees is not None and self.max_attendees < 0:
            raise ValidationError({'max_attendees': 'Maximum attendees cannot be negative.'})

    def spots_remaining(self):
        """Return max_attendees as spots (0 means unlimited)."""
        return self.max_attendees if self.max_attendees > 0 else None
