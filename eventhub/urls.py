from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'eventhub.events.views.custom_404_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('eventhub.events.urls')),
    path('venues/', include('eventhub.venues.urls')),
    path('categories/', include('eventhub.categories.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
