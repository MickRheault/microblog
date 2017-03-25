from django.db import models
from django.conf import settings

from tag.models import Tag
from core.utils import image_directory_path

from .utils import validate_title


class PublishedManager(models.Manager):
    use_for_related_fields = True

    def published(self, **kwargs):
        return self.filter(publish=True, **kwargs)


class Article(models.Model):
    title = models.CharField(max_length=80, verbose_name='Tytuł', unique=True, validators=[validate_title])
    slug = models.SlugField(max_length=80, verbose_name='Slug', unique=True)
    text = models.TextField(verbose_name='Tekst')
    desc = models.CharField(verbose_name='Opis', default='', max_length=400)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Autor')
    creation_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, verbose_name='Obraz', upload_to=image_directory_path)
    publish = models.BooleanField(default=False, verbose_name='Opublikuj')
    publish_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='Tagi', related_name='articles')

    objects = PublishedManager()

    class Meta:
        verbose_name = 'Artykuł'
        verbose_name_plural = 'Artykuły'
        ordering = ['-pk']

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return None
