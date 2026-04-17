# events/urls.py (URLs der Event-App)
from django.urls import path
from .views import (
    say_hello,
    categories,
    category_detail,
    category_update,
    category_create,
    EventListView,
    EventCreateView,
)

# ist nötig für den url-tag im Template: app_name:path_name,
# z.B. events:category-detail
app_name = "events"

# hier liegen die anderen Pfad-Teile
urlpatterns = [
    # /events/categories
    path("categories", categories, name="categories"),
    # /events/categories/3
    # <int:pk> => matche Integer, das Keyword-Argument lautet pk
    path(
        "categories/<int:pk>",
        category_detail,
        name="category-detail",
    ),
    # events/categories/3/update
    path(
        "categories/<int:pk>/update",
        category_update,
        name="category-update",
    ),
    path(
        "categories/create",
        category_create,
        name="category-create",
    ),
    # /events
    path(
        "",
        EventListView.as_view(),
        name="event-list",
    ),
    # /events/create
    path(
        "create",
        EventCreateView.as_view(),
        name="event-create",
    ),
    path(
        "hello",
        say_hello,
        name="hello"
    )
]
