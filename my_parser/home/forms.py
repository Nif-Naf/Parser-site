
from .models import External, Result, Search

from django.forms import ModelForm, TextInput, URLInput

class Parsing_form(ModelForm):
    """Форма для парсера."""

    class Meta: 

        model = External

        exclude = ()
        field = ['url']

        widgets = {
                "url": URLInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите адрес',
                    'type': 'link'
                }),
        }

class Search_form(ModelForm):
    """Форма для поиска"""

    class Meta:

        model = Search

        exclude = ()
        field = ['search']

        widgets = {
                "search_object": TextInput(attrs={
                    'class': 'form-search',
                    'placeholder': 'Что хотим найти?',
                    'type': 'text'
                })
        }