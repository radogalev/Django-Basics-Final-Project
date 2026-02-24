from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def format_event_datetime(event):
    """Format event date and time as a readable string."""
    if not event:
        return ''
    return f"{event.event_date.strftime('%b %d, %Y')} at {event.event_time.strftime('%H:%M')}"


@register.filter
def truncate_description(text, length=100):
    """Truncate text to specified length with ellipsis."""
    if not text or len(text) <= length:
        return text or ''
    part = text[:length]
    truncated = part.rsplit(' ', 1)[0] if ' ' in part else part
    return truncated + '...'


@register.filter
def capacity_display(value):
    """Display capacity: 0 means unlimited."""
    if value is None or value == 0:
        return 'Unlimited'
    return str(value)
