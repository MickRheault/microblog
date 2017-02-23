from django.db import models


class Navigation(models.Model):
    name = models.CharField(max_length=80, verbose_name='Nazwa', unique=True)
    url = models.URLField(verbose_name='Url', unique=True)
    ordering = models.PositiveIntegerField(verbose_name='Kolejność', unique=True)

    class Meta:
        verbose_name = 'Nawigacja'
        verbose_name_plural = 'Nawigacja'

    def __str__(self):
        return self.name
