from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView, CreateView

from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

from .models import GuessBookEntry
from .forms import EntryForm


class EntriesList(TemplateView):
    template_name = 'guest_book/guest_book.html'
    model = GuessBookEntry
    form_class = EntryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entries'] = self.model.objects.all()
        context['form'] = self.form_class

        return context


class CreateEntry(CreateView):
    form_class = EntryForm

    def get_context_data(self, **kwargs):
        context = {}

        # Generate new captcha and pass it to json
        context['cptch_key'] = CaptchaStore.generate_key()
        context['cptch_image'] = captcha_image_url(context['cptch_key'])

        return context

    def form_valid(self, form):
        self.object = form.save()

        html = (render_to_string('guest_book/snippets/entry_item.html', {
            'id': self.object.id,
            'author': self.object.author,
            'text': self.object.text,
            'creation_date': self.object.creation_date,
            'desc': self.object.desc,
        }))

        context = self.get_context_data()

        context['result'] = True
        context['html'] = html

        return JsonResponse(context)

    def form_invalid(self, form):
        context = self.get_context_data()

        context['result'] = False

        return JsonResponse(context)
