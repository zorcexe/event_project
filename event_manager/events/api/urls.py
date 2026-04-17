"""
events/api/urls.py

URLs der Event API
"""

from django.urls import path

from .views import CategoryListCreateAPIView

urlpatterns = [
    # api/events/categories
    path("categories", CategoryListCreateAPIView.as_view(), name="category-api-list"),
]
