from .models import feedback
from django.forms import ModelForm, TextInput, Textarea


class FeedbackForm(ModelForm):
    class Meta:
        model = feedback
        fields = ['author_name', 'feedback_text']
        widgets = {
            "author_name": TextInput(attrs=
            {
                'class': "u-input u-input-rectangle u-white u-border-1 u-border-grey-30 u-block-e702-6",
                'placeholder': "Введите Ваше имя",

            }),
            "feedback_text": TextInput(attrs=
            {
                'class': "u-input u-input-rectangle u-white u-border-1 u-border-grey-30 u-block-e702-9",
                'placeholder': "Отзыв"
            })
        }