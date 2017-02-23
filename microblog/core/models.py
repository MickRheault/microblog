from django.db import models
from django.utils.translation import ugettext_lazy as _


class Navigation(models.Model):
    name = models.CharField(max_length=80, verbose_name=_('Name'), unique=True)
    url = models.URLField(verbose_name=_('Url'), unique=True)
    ordering = models.PositiveIntegerField(verbose_name=_('Ordering'), unique=True)

    class Meta:
        verbose_name = _('Navigation')
        verbose_name_plural = _('Navigation')

    def __str__(self):
        return self.name
