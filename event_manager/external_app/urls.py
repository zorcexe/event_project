# external_app/urls.py

from django.urls import path

from .views import company_list

urlpatterns = [
    # */companies
    path("companies", company_list, name="company-list"),
]
