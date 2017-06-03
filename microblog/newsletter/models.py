from django.db import models

from solo.models import SingletonModel


class EmailBase(models.Model):
    name = models.CharField(max_length=120, verbose_name="Twoje imię")
    email = models.EmailField(verbose_name="Twój adres e-mail", unique=True)
    added = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")
    token = models.CharField(max_length=255, unique=True)
    verified = models.BooleanField(verbose_name="Zweryfikowany", default=False)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Baza emaili'

    def __str__(self):
        return self.email


class Raport(SingletonModel):
    email_confirm_title = models.CharField(max_length=255, blank=True, verbose_name="Tytuł")
    email_confirm = models.TextField(verbose_name="Potwierdz email", blank=True)
    fail_title = models.CharField(max_length=255, blank=True, verbose_name="Tytuł")
    fail = models.TextField(verbose_name="Komunikat niepowodznia", blank=True)
    success_title = models.CharField(max_length=255, blank=True, verbose_name="Tytuł")
    success = models.TextField(verbose_name="Komunikat udanej rejestracji", blank=True)
    cancel_title = models.CharField(max_length=255, blank=True, verbose_name="Tytuł")
    cancel = models.TextField(verbose_name="Komunikat udanej rejestracji", blank=True)


class BannedEmail(models.Model):
    email = models.EmailField(unique=True, db_index=True, verbose_name="Email")

    class Meta:
        verbose_name = 'Zakazany email'
        verbose_name_plural = 'Zakazane emaile'

    def __str__(self):
        return self.email


class BannedEmailDomain(models.Model):
    domain = models.CharField(max_length=100, db_index=True, verbose_name="Domena")

    class Meta:
        verbose_name = 'Zakazana domena'
        verbose_name_plural = 'Zakazane domeny'

    def __str__(self):
        return self.domain


class SpecialOffer(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    body = models.TextField("Tekst")
    send = models.BooleanField("Wysłane", default=False)
    send_date = models.DateField("Kiedy wysłać", blank=True, null=True)

    class Meta:
        verbose_name = 'Specjalna oferta'
        verbose_name_plural = 'Specjalne oferty'

    def __str__(self):
        return self.title

