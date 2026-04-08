"""
PROJEKT URLs
event_manager/urls.py
"""

from django.contrib import admin
from django.urls import path, include
from first.views import hello

urlpatterns = [
    # http://127.0.0.1:8000/admin
    path("admin/", admin.site.urls),
    # Alle URLs der App events (events/show, events/3)
    path("events/", include("events.urls")),
    # path("hello", hello, name="hello"),
]
