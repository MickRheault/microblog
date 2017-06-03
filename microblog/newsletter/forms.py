from django.forms import ModelForm, TextInput

from .models import EmailBase


class NewsletterForm(ModelForm):
    class Meta:
        model = EmailBase
        fields = ('name', 'email')
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control mx-sm-3'
            }),
            'email': TextInput(attrs={
                'class': 'form-control mx-sm-3'
            })
        }