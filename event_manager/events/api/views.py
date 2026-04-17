# events/api/views.py
from rest_framework import generics

from .serializers import CategorySerializer
from events.models import Category


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    """
    View zum Anlegen und Auflisten von kategorie Objekten.
    Ein- und ausgehende Daten werden via serializer_class
    serialisiert.

    GET api/events/categories => Liste von Kategorien
    POST api/events/categories => Eintragen einer Kategorie
    """

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
