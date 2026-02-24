from django.db import models
from django.core.exceptions import ValidationError


class Venue(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField(default=0)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Venue'
        verbose_name_plural = 'Venues'

    def __str__(self):
        return self.name

    def clean(self):
        if self.capacity is not None and self.capacity < 0:
            raise ValidationError({'capacity': 'Capacity cannot be negative.'})
