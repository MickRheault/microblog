from django.db.models.signals import post_save, post_delete
from django.core.cache import cache


def clear_cache(**kwargs):
    cache.clear()


post_save.connect(clear_cache)
post_delete.connect(clear_cache)
