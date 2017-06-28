from django.core.management.base import BaseCommand
from django.utils import timezone

from article.models import Article


class Command(BaseCommand):
    def handle(self, *args, **options):
        obj_list = Article.objects.filter(status=Article.ACCEPTED,
                                          to_publish__gte=timezone.now() - timezone.timedelta(seconds=10),
                                          to_publish__lte=timezone.now() + timezone.timedelta(seconds=60))

        for obj in obj_list:
            obj.published()
            obj.save()
