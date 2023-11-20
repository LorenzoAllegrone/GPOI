from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from Archivio.models import Libro
from .serializers import LibroSerializer

class LibroCreateView(generics.CreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer