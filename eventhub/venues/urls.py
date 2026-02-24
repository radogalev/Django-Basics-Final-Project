from django.urls import path
from eventhub.venues import views

urlpatterns = [
    path('', views.VenueListView.as_view(), name='venue_list'),
    path('create/', views.venue_create_view, name='venue_create'),
    path('<int:pk>/', views.venue_detail_view, name='venue_detail'),
    path('<int:pk>/edit/', views.venue_edit_view, name='venue_edit'),
    path('<int:pk>/delete/confirm/', views.venue_delete_confirm_view, name='venue_delete_confirm'),
    path('<int:pk>/delete/', views.venue_delete_view, name='venue_delete'),
]
