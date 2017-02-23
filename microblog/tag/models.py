from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Tytuł', unique=True)
    slug = models.CharField(max_length=50, verbose_name='Slug', unique=True)
    created_by = models.ForeignKey(User, verbose_name='Utworzony przez')
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tagi'

    def __str__(self):
        return self.title
