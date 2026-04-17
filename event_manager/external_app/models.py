"""
Diese Models.py wurden mit folgedem Befehl erstellt

uv run manage.py inspectdb --database external > external_app/models.py

Einige Felder wurden manuell nachbearbeitet, z.b. CharField statt TextField,
Datum statt Text

In den Meta-Settings sind wichtig:
- managed = False => Django verwaltet die Tabellen nicht
- db_table => das ist der DB-Table in der externen Datenbank

Das Model ist nur das Interface zur Datenbank.

"""

from django.db import models


class Company(models.Model):
    name = models.CharField()
    city = models.CharField()

    class Meta:
        managed = False
        db_table = "company"


class Sales(models.Model):
    company = models.ForeignKey(
        Company,
        models.DO_NOTHING,
        related_name="sales",
        db_column="company_id",
    )
    product_name = models.CharField()
    quantity = models.IntegerField()
    price_per_unit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    sold_at = models.DateField()

    class Meta:
        managed = False
        db_table = "sales"
        ordering = ["price_per_unit"]
