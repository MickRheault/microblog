from django.core.management.base import BaseCommand
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils import timezone

from newsletter.models import EmailBase
from article.models import Article


class Command(BaseCommand):
    help = 'Sends newsletter to all emails in database'

    def handle(self, *args, **options):
        email_list = [obj.email for obj in EmailBase.objects.filter(verified=True)]
        articles = Article.objects.filter(publish_date__month=(timezone.now() - timezone.timedelta(days=7)).month,
                                          publish=True)

        if not articles.exists():
            return

        html = render_to_string("newsletter/articles_monthly.html", {
            'articles': articles,
            'domain': settings.DOMAIN
        })
        txt = render_to_string("newsletter/articles_monthly.txt", {
            'articles': articles,
            'domain': settings.DOMAIN
        })

        email = EmailMultiAlternatives (
            'Najnowsze artykuły',
            txt,
            settings.EMAIL,
            bcc=email_list,
        )
        email.attach_alternative(html, "text/html")
        email.send()
