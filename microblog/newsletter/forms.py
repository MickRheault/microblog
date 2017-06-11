from django.forms import ModelForm, TextInput

from .models import EmailBase


class NewsletterForm(ModelForm):
    class Meta:
        model = EmailBase
        fields = ('name', 'email')
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
            })
        }