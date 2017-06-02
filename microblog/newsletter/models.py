from django.db import models


class EmailBase(models.Model):
    name = models.CharField(max_length=120, verbose_name="Twoje imię")
    email = models.EmailField(verbose_name="Twój adres e-mail")
    added = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")

    class Meta:
        verbose_name = 'Baza emaili'
