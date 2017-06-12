from django.core.management.base import BaseCommand
from django.utils import timezone

from newsletter.models import EmailBase


class Command(BaseCommand):
    help = 'Clear unverified'

    def handle(self, *args, **options):
        email_list = EmailBase.objects.filter(verified=False,
                                              added__lt=timezone.now() - timezone.timedelta(days=1))
        email_list.delete()
