import os

from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1][1:]
    allowed_ext = ['jpg', 'png', 'jpeg', 'pdf', 'txt', 'mp3', 'mp4', 'avi', 'mkv']

    if ext not in allowed_ext:
        raise ValidationError('Niewspierane rozszerzenie.')


class File(models.Model):
    title = models.CharField(max_length=60, verbose_name='Tytuł')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    creation_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(verbose_name='Wyślij plik', upload_to='file/', validators=[validate_file_extension])

    class Meta:
        verbose_name = 'Plik'
        verbose_name_plural = 'Pliki'
        ordering = ['-pk']

    def __str__(self):
        return self.title

    @property
    def file_url(self):
        return '<a href="%s">%s</a>' % (self.file.url, self.file.url)

    @property
    def extension(self):
        return os.path.splitext(self.file.name)[1]
