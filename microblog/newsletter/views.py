from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.http import Http404

from .forms import NewsletterForm
from .models import Raport, EmailBase, BannedEmail, BannedEmailDomain


class NewsletterVerficationView(View):
    http_method_names = ['post']
    form = NewsletterForm
    raport = Raport
    template_name = "newsletter/report.html"

    def post(self, request, *args, **kwargs):
        self.raport = self.raport.get_solo()
        f = self.form(request.POST)

        if f.is_valid():
            return self.form_valid(request, f)
        else:
            return self.form_invalid(request, f)

    def form_valid(self, request, form):
        context = {
            'title': self.raport.email_confirm_title,
            'body': self.raport.email_confirm
        }

        token = get_random_string(170)
        while EmailBase.objects.filter(token=token).exists():
            token = get_random_string(170)

        obj = form.save(commit=False)
        email_domain = obj.email.split("@")[1]

        if BannedEmail.objects.filter(email=obj.email).exists():
            raise Http404
        if BannedEmailDomain.objects.filter(domain__icontains=email_domain).exists():
            raise Http404

        obj.token = token
        obj.save()

        html = render_to_string("newsletter/email/verification.html", {
            'token': token,
            'domain': settings.DOMAIN
        })
        txt = render_to_string("newsletter/email/verification.txt", {
            'token': token,
            'domain': settings.DOMAIN
        })

        send_mail('Potwierdzenie adresu', html_message=html, message=txt,
                  from_email=settings.EMAIL, recipient_list=[obj.email, ], fail_silently=False)

        return render(request, self.template_name, context)

    def form_invalid(self, request, form):
        context = {
            'title': self.raport.fail_title,
            'body': self.raport.fail
        }

        return render(request, self.template_name, context)


class NewsletterEmailVerficationView(View):
    http_method_names = ['get']
    template_name = "newsletter/report.html"

    def get(self, request, *args, **kwargs):
        token = kwargs.get('token')

        obj = get_object_or_404(EmailBase, token=token)
        obj.verified = True
        obj.save()

        raport = Raport.get_solo()
        context = {
            'title': raport.email_confirm_title,
            'body': raport.email_confirm
        }

        return render(request, self.template_name, context)


class NewsletterCancelView(View):
    http_method_names = ['get']
    template_name = "newsletter/report.html"

    def get(self, request, *args, **kwargs):
        token = kwargs.get('token')

        obj = get_object_or_404(EmailBase, token=token)

        if not obj.verified:
            raise Http404

        obj.delete()

        raport = Raport.get_solo()
        context = {
            'title': raport.cancel,
            'body': raport.cancel_title
        }

        return render(request, self.template_name, context)
