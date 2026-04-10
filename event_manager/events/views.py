# events/views.py
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Category, Event
from .forms import CategoryForm


class EventListView(ListView):
    """Liste aller Events.

    /events
    Template: events/event_list.html
    Zugriff im Template auf das QS: object_list
    qs = Event.objects.all()
    """

    model = Event
    # category => Name im Event-Model (select_related macht Inner join auf category)
    # https://docs.djangoproject.com/en/6.0/ref/models/querysets/#select-related
    queryset = Event.objects.select_related("category")


def category_create(request):
    """Eine neue Kategorie anlegen.

    GET: leeres Formular anzeigen
    POST: Formulardaten in DB eintragen und neue
    Kategorie erstellen (wenn valide)

    events/categories/create
    """
    if request.method == "POST":
        # Formular mit eingehenden Daten
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()  # model.save()
            # weiterleitung auf Übersicht der Kategorien
            # return redirect("events:categories")
            # Weiterleiten auf neue kategorie
            return redirect("events:category-detail", pk=category.pk)
    else:
        # ein leeres Formular erstellen:
        form = CategoryForm()

    return render(
        request,
        "events/category_form.html",
        {"form": form},
    )


def category_detail(request, pk: int):
    """Eine Kategorie-Detailseite.

    events/categories/3
    """
    # category = Category.objects.get(pk=pk)
    # Hole Objekt oder löse 404 Fehler aus
    category = get_object_or_404(Category, pk=pk)
    # category.events.count()
    return render(
        request,
        "events/category_detail.html",
        {
            "category": category,
        },
    )


def categories(request):
    """Auflisten aller Kategorien.

    events/categories
    """
    qs = Category.objects.all()
    context = {"categories": qs}

    return render(
        request,
        "events/categories.html",
        context,
    )


def qs_test(request):
    """Eine Funktion zum Testen von Queries.
    akutell nicht per URL erreichbar (keine Verlinkung)
    """
    # Alle Kategorie-Objekte selektieren (Select * from event_category)
    qs = Category.objects.all()
    print(f"Alle Kategorien: {qs}")

    # Alle Kategorien die mit dem Buchstaben K anfangen
    # Select * from categeory where name LIKE "K%" and name LIKE "%o"
    # Filter resultieren immer in UND
    qs = Category.objects.all()  # keine DB-Anfrage
    qs = qs.filter(name__startswith="K")
    qs = qs.filter(name__endswith="o")
    print(f"Alle Kategorien mit K: {qs}")
    print(f"SQL-Abfrage: {str(qs.query)}")  # Zeigt die eigentliche SQL-Anfrage

    # Ein Objekt selektieren
    # Objekt mit ID 1 (pk mappt auf Primary Key)
    sport = Category.objects.get(pk=1)
    # alle Sport-Events (über das Kategorie-Objekt via related_name aus Model
    # kann man alle Events selektieren, die der Kategorie zugeteilt sind
    sport_events = sport.events.all()  # type: ignore
    print("Sport Objekte:", sport_events)

    anzahl_events: int = Event.objects.count()
    print("Anzahl Event in der DB:", anzahl_events)

    events_mit_s = Event.objects.all().filter(name__contains="s")
    print(events_mit_s)

    # Alle Kategorien, deren Events ein kleines s im Namen haben
    categories_mit_s = Category.objects.filter(events__name__contains="s")
    print("Kategorien mit Events mit s:", categories_mit_s)
    print("SQL:", str(categories_mit_s.query))

    return HttpResponse("-".join(map(str, qs)))
