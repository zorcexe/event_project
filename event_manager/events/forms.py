from django import forms

from .models import Category, Event


class CategoryForm(forms.ModelForm):
    # ModelForm erstellt auf Basis von model ein Formular
    class Meta:
        model = Category
        fields = "__all__"  # ("name", "description")


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d %H:%M"), attrs={"type": "datetime-local"}
            ),
            # "category": forms.RadioSelect(),
        }

        labels = {
            "sub_title": "Genre",
            "date": "Termin am",
            "description": "Infos",
        }
