from django import forms

from captcha.fields import CaptchaField, BaseCaptchaTextInput

from .models import GuessBookEntry


class EntryForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        fields = ('author', 'text')
        model = GuessBookEntry
        widgets = {
            'author': forms.TextInput(
                attrs={'required': True, 'class': 'form-control', 'placeholder': 'Type your name...'}
            ),
            'text' : forms.Textarea(
                attrs={'required': True, 'placeholder': 'Say something...', 'class': 'form-control', 'rows': '3'}
            ),
            'captcha' : BaseCaptchaTextInput(
                attrs={'required': True, 'class': 'form-control'}
            )
        }
