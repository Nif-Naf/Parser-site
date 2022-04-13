from .models import External

from django.forms import ModelForm, TextInput

class Parsing_form(ModelForm):
    """A form for searching in the table."""
    
    class Meta: 

        model = External

        exclude = ()
        field = ['url']

        widgets = {
                "url": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите адрес',
                    'type': 'text'
                }),
        }