from django.db import models
from django.conf import settings
from django.utils import timezone

from django_fsm import FSMIntegerField, transition, TransitionNotAllowed

from tag.models import Tag
from core.utils import image_directory_path

from .utils import validate_title


class PublishedManager(models.Manager):
    use_for_related_fields = True

    def published(self, **kwargs):
        return self.filter(status=Article.PUBLISHED, **kwargs).order_by('-publish_date')


class Article(models.Model):
    DRAFT = 0
    ACCEPTED = 1
    PUBLISHED = 2
    HIDDEN = 3

    STATUS_CHOICES = (
        (DRAFT, 'Wersja Robocza'),
        (ACCEPTED, 'Zaakceptowane'),
        (PUBLISHED, 'Opublikowane'),
        (HIDDEN, 'Ukryte'),
    )

    title = models.CharField(max_length=80, verbose_name='Tytuł', unique=True, validators=[validate_title])
    slug = models.SlugField(max_length=80, verbose_name='Slug', unique=True)
    text = models.TextField(verbose_name='Tekst')
    desc = models.CharField(verbose_name='Opis', default='', max_length=400)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Autor')
    creation_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, verbose_name='Obraz', upload_to=image_directory_path)
    publish_date = models.DateTimeField(blank=True, null=True, db_index=True)
    tags = models.ManyToManyField(Tag, verbose_name='Tagi', related_name='articles')
    status = FSMIntegerField(choices=STATUS_CHOICES, default=DRAFT, protected=True, db_index=True)
    to_publish = models.DateTimeField(blank=True, null=True, verbose_name="Kiedy opublikować")

    objects = PublishedManager()

    class Meta:
        verbose_name = 'Artykuł'
        verbose_name_plural = 'Artykuły'
        ordering = ['-pk']
        index_together = [
            ["status", "publish_date"],
            ["status", "to_publish"],
        ]

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return None

    @transition(field=status, source=DRAFT, target=ACCEPTED, custom=dict(admin=True))
    def accepted(self):
        self.to_publish = None

    @transition(field=status, source=ACCEPTED, target=PUBLISHED)
    def published(self):
        self.publish_date = timezone.now()
        self.to_publish = None

    @transition(field=status, source=ACCEPTED, target=DRAFT)
    def back_to_draft(self):
        self.to_publish = None

    @transition(field=status, source=PUBLISHED, target=HIDDEN)
    def hidden(self):
        self.to_publish = None

    @transition(field=status, source=HIDDEN, target=DRAFT)
    def draft(self):
        self.publish_date = None
        self.to_publish = None
