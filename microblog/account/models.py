from django.db import models
from django.contrib.auth.models import AbstractUser
from core.utils import avatar_directory_path


class User(AbstractUser):
    avatar = models.ImageField(verbose_name='Awatar', upload_to=avatar_directory_path)
    about_me = models.CharField(verbose_name='O mnie', max_length=255)

    class Meta:
        verbose_name = 'Użytkownik'
        verbose_name_plural = 'Użytkownicy'

    def __str__(self):
        return self.username
