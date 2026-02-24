from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from eventhub.categories.models import Category
from eventhub.categories.forms import CategoryCreateForm
from eventhub.events.models import Event


class CategoryListView(ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'
    paginate_by = 12


def category_detail_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    events = Event.objects.filter(categories=category, is_published=True).order_by('event_date')[:15]
    context = {'category': category, 'events': events}
    return render(request, 'categories/category_detail.html', context)


def category_create_view(request):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryCreateForm()
    return render(request, 'categories/category_form.html', {'form': form})
