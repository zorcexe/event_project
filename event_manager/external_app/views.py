from django.shortcuts import render
from django.db.models import Sum, F, Min, Avg

from .models import Company, Sales


def company_list(request):
    """Stelle alle Firmen in einer Liste dar."""
    return render(
        request,
        "external_app/company_list.html",
        {
            "company_list": Company.objects.all(),
        },
    )


def sales_list(request):
    """
    da wir im Template in der Tabelle den Firmennamen ausgeben
    (sale.company), würde pro Datensatz ein Lookup auf den
    Company-Table gemacht. Um das zu verhindern, können wir
    mit select_related einen INNER JOIN machen.
    """
    return render(
        request,
        "external_app/sales_list.html",
        {
            "sales_list": Sales.objects.select_related("company"),
        },
    )


def sales_list_grouped(request):

    # Gruppiere bei product_name und summiere die Quantitäte
    qs = Sales.objects.values("product_name").annotate(
        total_quantity=Sum("quantity"),  # summiert alle Quantitäten auf
        total_price=Sum(F("quantity") * F("price_per_unit")),
    )

    return render(
        request,
        "external_app/sales_list_grouped.html",
        {"sales_list": qs},
    )
