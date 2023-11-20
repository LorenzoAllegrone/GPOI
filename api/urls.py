from django.urls import path
from .views import LibroCreateView
urlpatterns = [
    path('crea_libro/', LibroCreateView.as_view(), name = 'libro_create')
]