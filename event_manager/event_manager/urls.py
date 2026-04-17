"""
PROJEKT URLs
event_manager/urls.py
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    # homepage http://127.0.0.1:8000 (example.com)
    path("", include("pages.urls")),
    #
    # http://127.0.0.1:8000/admin
    path("admin/", admin.site.urls),
    #
    # Alle URLs der App events (events/show, events/3)
    path("events/", include("events.urls")),
    path("api/events/", include("events.api.urls")),
    #
    # Alle Endpunkte der external_app
    path("external/", include("external_app.urls")),
]

# im DEBUG Modus Debugtoolbar sein
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
