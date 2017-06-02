from django.core.management.base import BaseCommand

from core.signals import clear_cache


class Command(BaseCommand):
    help = 'Clear all cache'

    def handle(self, *args, **options):
        clear_cache()
