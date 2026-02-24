from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from eventhub.events.models import Event
from eventhub.events.forms import EventCreateForm, EventEditForm
from eventhub.categories.models import Category
from eventhub.venues.models import Venue


def home_view(request):
    featured = Event.objects.filter(is_published=True).order_by('event_date')[:3]
    context = {
        'featured_events': featured,
        'total_events': Event.objects.filter(is_published=True).count(),
        'total_venues': Venue.objects.count(),
        'total_categories': Category.objects.count(),
    }
    return render(request, 'events/home.html', context)


class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    paginate_by = 9

    def get_queryset(self):
        qs = Event.objects.filter(is_published=True).select_related('venue').prefetch_related('categories')
        category_id = self.request.GET.get('category')
        if category_id:
            qs = qs.filter(categories__id=category_id).distinct()
        sort = self.request.GET.get('sort', 'date')
        if sort == 'date':
            qs = qs.order_by('event_date', 'event_time')
        elif sort == 'title':
            qs = qs.order_by('title')
        elif sort == 'venue':
            qs = qs.order_by('venue__name')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def event_detail_view(request, pk):
    event = get_object_or_404(Event.objects.select_related('venue').prefetch_related('categories'), pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})


def event_create_view(request):
    if request.method == 'POST':
        form = EventCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventCreateForm()
    return render(request, 'events/event_form.html', {'form': form, 'is_edit': False})


def event_edit_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventEditForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventEditForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form, 'event': event, 'is_edit': True})


def event_delete_confirm_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_confirm_delete.html', {'event': event})


def event_delete_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return redirect('event_delete_confirm', pk=pk)


def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)
