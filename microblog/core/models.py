from django.db import models
from solo.models import SingletonModel


class Navigation(models.Model):
    name = models.CharField(max_length=80, verbose_name='Nazwa', unique=True)
    url = models.URLField(verbose_name='Url', unique=True)
    ordering = models.PositiveIntegerField(verbose_name='Kolejność', unique=True)

    class Meta:
        verbose_name = 'Nawigacja'
        verbose_name_plural = 'Nawigacja'

    def __str__(self):
        return self.name


class SiteMeta(SingletonModel):
    title = models.CharField(max_length=255, verbose_name='Tytuł')
    subheading = models.CharField(max_length=255, verbose_name='Podtytuł')
    description = models.CharField(max_length=255, verbose_name='Opis')
    keywords = models.CharField(max_length=255, verbose_name='Słowa kluczowe')
    author = models.CharField(max_length=255, verbose_name="Autor")
    image = models.ImageField(verbose_name="Obraz")

    def __str__(self):
        return "Ustawienia strony"

    class Meta:
        verbose_name = "Ustawienia strony"


class Footer(SingletonModel):
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    github = models.URLField(blank=True)

    def __str__(self):
        return "Stopka"

    class Meta:
        verbose_name = "Stopka"


from .signals import *