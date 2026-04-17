
# Django mit externer Read-Only Datenbank

Ziel:
Eine bestehende SQLite-Datenbank in Django **nur lesend** nutzen.

---

## 1. Projekt erstellen

```bash
uv init read_only_project
cd read_only_project

uv add django==5.2

uv run django-admin startproject project .
uv run python manage.py startapp external_app
````

---

## 2. Datenbanken vorbereiten

Lege beide Dateien ins Projektverzeichnis:

```
db.sqlite3                # Django Default DB
external_data.sqlite3     # externe DB (readonly)
```

---

## 3. settings.py anpassen

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "external": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "external_data.sqlite3",
    },
}

INSTALLED_APPS = [
    ...
    "external_app",
]

DATABASE_ROUTERS = ["project.db_router.ExternalReadOnlyRouter"]
```

---

## 4. Models generieren

```bash
uv run python manage.py inspectdb --database=external > external_app/models.py
```

Hinweis (Windows):
inspectdb erzeugt manchmal UTF-16 → Datei in UTF-8 speichern, sonst SyntaxError beim Import.

---

## 5. Models prüfen und optimieren (sehr wichtig)

`inspectdb` liefert nur eine grobe Vorlage. Du musst nacharbeiten.

Beispiel:

```python
class Company(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "company"
```

```python
class Sales(models.Model):
    company = models.ForeignKey(
        Company,
        models.DO_NOTHING,
        db_column="company_id",
        related_name="sales"
    )
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    sold_at = models.DateField()

    class Meta:
        managed = False
        db_table = "sales"
        ordering = ["-sold_at"]
```

Wichtige Punkte:

* managed = False
  → Django verwaltet die Tabelle nicht

* db_table
  → muss exakt dem DB-Namen entsprechen

* Datentypen verbessern
  → TextField → CharField
  → Float → Decimal
  → Text → DateField

* ForeignKey korrekt mappen (`db_column`)

Wichtiges Konzept:

> Das Model ist hier nur ein **Interface zur DB**, nicht die Quelle der Wahrheit.

---

## 6. Database Router (zentrales Konzept)

```python
class ExternalReadOnlyRouter:
    route_app_labels = {"external_app"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "external"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            raise RuntimeError("Read-only database: writes are not allowed.")
        return None

    def allow_migrate(self, db, app_label, **hints):
        if app_label in self.route_app_labels:
            return False
        return None
```

Funktionsweise:

* db_for_read
  → leitet SELECTs auf die externe DB

* db_for_write
  → blockiert Writes explizit (wichtig!)

* allow_migrate
  → verhindert Schemaänderungen

Wichtiger Punkt:

* None bedeutet: Django entscheidet selbst (meist default DB)
* False bedeutet: hart blockiert

---

## 7. Warum keine Migrationen?

Externe DB gehört nicht Django.

Probleme ohne Schutz:

* Tabellen würden verändert
* Daten könnten beschädigt werden
* Schema gehört oft einem anderen System

Deshalb Kombination:

* managed = False
* allow_migrate = False

Wichtige Erkenntnis:

> Migration kann „erfolgreich“ sein, ohne die DB zu verändern.

Beispiel:

```python
AlterModelOptions (ordering)
```

→ wird ausgeführt, erzeugt aber kein SQL

---

## 8. View

```python
from django.shortcuts import render
from .models import Company

def company_list(request):
    companies = Company.objects.prefetch_related("sales")
    return render(request, "external_app/company_list.html", {
        "companies": companies
    })
```

---

## 9. Template

```html
<h1>Companies</h1>

<table border="1">
    <tr>
        <th>Name</th>
        <th>City</th>
        <th>Sales</th>
    </tr>

    {% for company in companies %}
    <tr>
        <td>{{ company.name }}</td>
        <td>{{ company.city }}</td>
        <td>{{ company.sales.count }}</td>
    </tr>
    {% endfor %}
</table>
```

---

## 10. URLs

```python
# external_app/urls.py
from django.urls import path
from .views import company_list

urlpatterns = [
    path("companies/", company_list, name="company_list"),
]
```

```python
# project/urls.py
from django.urls import path, include

urlpatterns = [
    path("", include("external_app.urls")),
]
```

---

## 11. Ablauf im System

1. Request kommt rein
2. View nutzt ORM
3. Router entscheidet DB
4. Query geht an externe DB
5. Ergebnis wird gerendert

---

## 12. Typische Fehler

* UTF-16 Encoding (Windows)
* falscher db_table Name
* app_label falsch gesetzt
* Router nicht korrekt registriert
* managed=True → Django verändert DB
