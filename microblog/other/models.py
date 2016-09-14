from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from core.utils import image_directory_path


class Other(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=70, unique=True)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True)
    text = models.TextField(verbose_name=_('Text'))
    image = models.ImageField(upload_to=image_directory_path, verbose_name=_('Image'), blank=True)
    creation_date = models.DateTimeField(verbose_name=_('Creation Date'), auto_now_add=True)
    author = models.ForeignKey(User)

    class Meta:
        verbose_name = _('Other')
        verbose_name_plural = _('Others')

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return None
