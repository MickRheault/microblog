from django.db import models
from django.utils.translation import ugettext_lazy as _


class GuessBookEntry(models.Model):
    author = models.CharField(max_length=70, verbose_name=_('Author'))
    text = models.CharField(max_length=400, verbose_name=_('Text'))
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Entry')
        verbose_name_plural = _('Entries')

    def __str__(self):
        return self.text

    @property
    def desc(self):
        text = self.text

        if len(text) > 120:
            text = text[:120] + '...'

        return text
