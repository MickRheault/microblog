from django.core.management.base import BaseCommand
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.utils import timezone
from django.utils.html import strip_tags

from article.templatetags.markdown import markdownify

from newsletter.models import EmailBase, SpecialOffer


class Command(BaseCommand):
    help = 'Sends newsletter to all emails in database'

    def handle(self, *args, **options):
        now = timezone.now()
        email_list = [obj.email for obj in EmailBase.objects.filter(verified=True)]
        offers = SpecialOffer.objects.filter(send_date__year=now.year,
                                             send_date__month=now.month,
                                             send_date__day=now.day,
                                             send=False)

        for offer in offers:
            email = EmailMultiAlternatives(
                offer.title,
                strip_tags(markdownify(offer.body)),
                settings.EMAIL,
                bcc=email_list,
            )
            email.attach_alternative(markdownify(offer.body), "text/html")
            email.send()

            offer.send = True
            offer.save()
