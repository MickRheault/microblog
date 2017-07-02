from django.forms import ModelForm, TextInput

from .models import EmailBase


class NewsletterForm(ModelForm):
    class Meta:
        model = EmailBase
        fields = ('name', 'email')
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'IMIĘ'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-MAIL'
            })
        }