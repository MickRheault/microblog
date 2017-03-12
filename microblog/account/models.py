from django.db import models
from django.contrib.auth.models import AbstractUser
from core.utils import avatar_directory_path


class User(AbstractUser):
    avatar = models.ImageField(verbose_name='Awatar', upload_to=avatar_directory_path, blank=True)
    about_me = models.TextField(verbose_name='O mnie', blank=True)

    class Meta:
        verbose_name = 'Użytkownik'
        verbose_name_plural = 'Użytkownicy'

    def __str__(self):
        return self.username
