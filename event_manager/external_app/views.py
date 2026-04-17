from django.shortcuts import render

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
