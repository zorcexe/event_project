# external_app/urls.py

from django.urls import path

from .views import company_list, sales_list, sales_list_grouped

urlpatterns = [
    # */companies
    path("companies", company_list, name="company-list"),
    path("sales", sales_list, name="sales-list"),
    path("salesgrouped", sales_list_grouped, name="sales-list-grouped"),
]
