from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name="routes"),
    path('notes/', views.get_notes, name="notes"),
    path('notes/<str:pk>/update/', views.update_note, name="update_note"),
    path('notes/<str:pk>', views.get_single_note, name="selected_note")
]