from django import forms

from .models import GuessBookEntry


class EntryForm(forms.ModelForm):

    class Meta:
        fields = ('author', 'text')
        model = GuessBookEntry
        widgets = {
            'author': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Type your name...'}
            ),
            'text' : forms.Textarea(
                attrs={'required': True, 'placeholder': 'Say something...', 'class': 'form-control', 'rows': '3'}
            )
        }
