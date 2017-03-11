from django.db import models
from django.conf import settings

from core.utils import image_directory_path


class Other(models.Model):
    title = models.CharField(verbose_name='Tytuł', max_length=70, unique=True)
    slug = models.SlugField(verbose_name='Slug', unique=True)
    text = models.TextField(verbose_name='Tekst')
    image = models.ImageField(upload_to=image_directory_path, verbose_name='Obraz', blank=True)
    creation_date = models.DateTimeField(verbose_name='Data utworzenia', auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name = 'Reszta'
        verbose_name_plural = 'Inne'

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return None
