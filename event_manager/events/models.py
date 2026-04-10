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

    class Meta:
        # https://docs.djangoproject.com/en/6.0/ref/models/options/
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        """String-Repräsentation eines Kategorie-Objekts, zb. in Admin"""
        return self.name

    def save(self):
        print("mach was")
        return super().save()


class Event(models.Model):
    """Ein Ereignis in der Zukunft."""

    class Group(models.IntegerChoices):
        BIG = 10, "große Gruppe"
        SMALL = 5, "kleine Gruppe"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,  # models.PROTECT, models.SET_NULL, models.SET_DEFAULT
        related_name="events",  # related Beziehung
    )
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField()
    min_group = models.IntegerField(choices=Group.choices, default=Group.SMALL)

    def __str__(self) -> str:
        return self.name
