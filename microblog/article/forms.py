from django import forms
from django.utils.translation import ugettext_lazy as _


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'placeholder': _('Search'), 'class': 'form-control'}
    ))