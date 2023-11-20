from rest_framework import serializers
from Archivio.models import Libro
class LibroSerializer(serializers.ModelSerializer):
    class meta:
        model = Libro
        fields = ['id','titolo','autore','genere']

