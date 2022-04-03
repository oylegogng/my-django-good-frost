from .models import Application
from django.forms import ModelForm, TextInput, Textarea


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'phone']

        widgets = {
            "name": TextInput(attrs=
            {
                'class': "u-input u-input-rectangle u-white u-border-1 u-border-grey-30 u-block-e702-6",
                'placeholder': "Введите Ваше имя",

        }),
            "phone": TextInput(attrs=
            {
                 'class': "u-input u-input-rectangle u-white u-border-1 u-border-grey-30 u-block-e702-9",
                'placeholder': "8(999)99999999"
        })
        }
