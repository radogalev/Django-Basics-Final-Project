from django.urls import path
from eventhub.categories import views

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category_list'),
    path('create/', views.category_create_view, name='category_create'),
    path('<int:pk>/', views.category_detail_view, name='category_detail'),
]
