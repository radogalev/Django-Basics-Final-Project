from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from eventhub.venues.models import Venue
from eventhub.venues.forms import VenueCreateForm, VenueEditForm
from eventhub.events.models import Event


class VenueListView(ListView):
    model = Venue
    template_name = 'venues/venue_list.html'
    context_object_name = 'venues'
    paginate_by = 9


def venue_detail_view(request, pk):
    venue = get_object_or_404(Venue, pk=pk)
    events = Event.objects.filter(venue=venue, is_published=True).order_by('event_date')[:10]
    context = {'venue': venue, 'upcoming_events': events}
    return render(request, 'venues/venue_detail.html', context)


def venue_create_view(request):
    if request.method == 'POST':
        form = VenueCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venue_list')
    else:
        form = VenueCreateForm()
    return render(request, 'venues/venue_form.html', {'form': form, 'is_edit': False})


def venue_edit_view(request, pk):
    venue = get_object_or_404(Venue, pk=pk)
    if request.method == 'POST':
        form = VenueEditForm(request.POST, instance=venue)
        if form.is_valid():
            form.save()
            return redirect('venue_detail', pk=venue.pk)
    else:
        form = VenueEditForm(instance=venue)
    return render(request, 'venues/venue_form.html', {'form': form, 'venue': venue, 'is_edit': True})


def venue_delete_confirm_view(request, pk):
    venue = get_object_or_404(Venue, pk=pk)
    event_count = Event.objects.filter(venue=venue).count()
    return render(request, 'venues/venue_confirm_delete.html', {
        'venue': venue,
        'event_count': event_count,
    })


def venue_delete_view(request, pk):
    venue = get_object_or_404(Venue, pk=pk)
    if request.method == 'POST':
        venue.delete()
        return redirect('venue_list')
    return redirect('venue_delete_confirm', pk=pk)
