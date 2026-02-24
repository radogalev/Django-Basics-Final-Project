from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.inclusion_tag('partials/event_card.html')
def render_event_card(event):
    """Render a reusable event card partial."""
    return {'event': event}


@register.inclusion_tag('partials/venue_card.html')
def render_venue_card(venue):
    """Render a reusable venue card partial."""
    return {'venue': venue}


@register.simple_tag
def event_count_by_venue(venue):
    """Return the count of published events for a venue."""
    return venue.events.filter(is_published=True).count()
