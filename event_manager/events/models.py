from django.db import models


class Category(models.Model):
    """Kategorie für Events.

    Tabellenname: events_category
    """

    created_at = models.DateTimeField(auto_now_add=True)  # einmalig
    updated_at = models.DateTimeField(auto_now=True)  # bei jedem Update des Objekts
    name = models.CharField(max_length=100)  # Varchar 100
    sub_title = models.CharField(max_length=100, null=True, blank=True)
    # optional:
    # null=True => darf in der DB NULL sein, blank=True => darf im Formular leer sein
    description = models.TextField(null=True, blank=True)
