from .models import External, Result

from django.forms import ModelForm, TextInput, URLInput

class Parsing_form(ModelForm):
    """A form for searching in the table."""

    class Meta: 

        model = External

        exclude = ()
        field = ['url']

        widgets = {
                "url": URLInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите адрес',
                    'type': 'text'
                }),
        }

class Js_form(ModelForm):

    class Meta:

        model = Result

        exclude = ()
        field = ['url', 'domains', 'create_data', 'update_data', 'country', 'is_dead', 
        'a', 'ns', 'cname', 'mx', 'txt']