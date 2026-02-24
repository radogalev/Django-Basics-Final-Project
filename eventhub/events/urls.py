from django.urls import path
from eventhub.events import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('events/', views.EventListView.as_view(), name='event_list'),
    path('events/create/', views.event_create_view, name='event_create'),
    path('events/<int:pk>/', views.event_detail_view, name='event_detail'),
    path('events/<int:pk>/edit/', views.event_edit_view, name='event_edit'),
    path('events/<int:pk>/delete/confirm/', views.event_delete_confirm_view, name='event_delete_confirm'),
    path('events/<int:pk>/delete/', views.event_delete_view, name='event_delete'),
]
