"""
events/api/serializers.py

Serializer wandeln eingehende JSON-Daten in Python um und ausgehende Python-Daten
in JSON.

Eingehende Daten:
curl -X POST -d='{"name":"bob", "age":3}' 127.0.0.1:8000/api/events

Ausgehende Daten
qs = Event.objects.all()
"""

from rest_framework import serializers

from events.models import Category, Event


class EventInlineSerializer(serializers.ModelSerializer):
    """serializisert die Events und wird im Category-Serializer genutzt"""

    class Meta:
        model = Event
        fields = ("name", "min_group")


class CategorySerializer(serializers.ModelSerializer):
    """ModelSerializer erstellt aus Model einen Serializer."""

    # stellt jetzt die Events auch im Serializer dar
    events = EventInlineSerializer(many=True)

    class Meta:
        model = Category
        fields = "__all__"  # ["id", "events"]
