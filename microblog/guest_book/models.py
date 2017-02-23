from django.db import models


class GuessBookEntry(models.Model):
    author = models.CharField(max_length=70, verbose_name='Autor')
    text = models.CharField(max_length=400, verbose_name='Tekst')
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Wpis'
        verbose_name_plural = 'Wpisy'
        ordering = ['-pk']

    def __str__(self):
        return self.text

    @property
    def desc(self):
        text = self.text

        if len(text) > 120:
            text = text[:120] + '...'

        return text
