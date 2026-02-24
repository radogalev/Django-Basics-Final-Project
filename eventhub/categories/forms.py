from django import forms
from eventhub.categories.models import Category


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description', 'icon')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Music, Sports, Art',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Brief description of this category',
            }),
            'icon': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional icon class (e.g. music)',
            }),
        }
        labels = {
            'icon': 'Icon (optional)',
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 2:
            raise forms.ValidationError('Category name must be at least 2 characters long.')
        if Category.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError('A category with this name already exists.')
        return name
