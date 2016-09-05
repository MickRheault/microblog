from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Article(models.Model):
    title = models.CharField(max_length=80, verbose_name=_('Title'))
    slug = models.SlugField(max_length=80, verbose_name=_('Slug'))
    text = models.TextField(verbose_name=_('Text'))
    author = models.ForeignKey(User, verbose_name=_('Author'))
    creation_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, verbose_name=_('Image'))
    publish = models.BooleanField(default=False, verbose_name=_('Publish'))

    @property
    def desc(self):
        return self.text[:77] + '...'
