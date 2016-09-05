from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    slug = models.CharField(max_length=50, verbose_name=_('Slug'))
    created_by = models.ForeignKey(User, verbose_name=_('Created by'))
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return self.title
