from django import forms
from eventhub.events.models import Event
from eventhub.venues.models import Venue
from eventhub.categories.models import Category


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('is_published', 'created_at', 'updated_at')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter event title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your event...',
                'rows': 4,
            }),
            'event_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'event_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
            }),
            'venue': forms.Select(attrs={'class': 'form-select'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'max_attendees': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0 = unlimited',
                'min': 0,
            }),
        }
        labels = {
            'title': 'Event Title',
            'event_date': 'Date',
            'event_time': 'Time',
            'max_attendees': 'Maximum Attendees (0 for unlimited)',
        }
        help_texts = {
            'max_attendees': 'Leave as 0 for unlimited capacity.',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if len(title) < 3:
            raise forms.ValidationError('Title must be at least 3 characters long.')
        return title

    def clean_max_attendees(self):
        value = self.cleaned_data.get('max_attendees', 0)
        if value is not None and value < 0:
            raise forms.ValidationError('Maximum attendees cannot be negative.')
        return value


class EventEditForm(forms.ModelForm):
    created_at_display = forms.CharField(
        required=False,
        disabled=True,
        label='Created at',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Event
        exclude = ('created_at', 'updated_at')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'event_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'venue': forms.Select(attrs={'class': 'form-select'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'max_attendees': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['created_at_display'].initial = self.instance.created_at.strftime('%Y-%m-%d %H:%M')
