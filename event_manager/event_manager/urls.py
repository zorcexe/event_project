"""
PROJEKT URLs
event_manager/urls.py
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    # http://127.0.0.1:8000/admin
    path("admin/", admin.site.urls),
    # Alle URLs der App events (events/show, events/3)
    path("events/", include("events.urls")),
]

# im DEBUG Modus Debugtoolbar sein
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
