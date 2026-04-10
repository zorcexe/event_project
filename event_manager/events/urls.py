# events/urls.py (URLs der Event-App)
from django.urls import path
from .views import categories, category_detail, category_create, EventListView

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
]
