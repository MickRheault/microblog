from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

from .models import GuessBookEntry
from .forms import EntryForm


def entries_list(request):
    entries = GuessBookEntry.objects.all().order_by('-pk')
    return render(request, 'guest_book/guest_book.html', {'form': EntryForm,
                                                          'entries': entries})


def create_entry(request):
    if request.method == 'POST':
        response_data = {}

        entry = EntryForm(request.POST)
        if entry.is_valid():
            entry = entry.save()
            html = (render_to_string('guest_book/snippets/entry_item.html', {
                'id': entry.id,
                'author': entry.author,
                'text': entry.text
            }))
            response_data['result'] = True
            response_data['html'] = html

            # Generate new captcha and pass it to json
            response_data['cptch_key'] = CaptchaStore.generate_key()
            response_data['cptch_image'] = captcha_image_url(response_data['cptch_key'])

            return JsonResponse(response_data)
        else:
            response_data['result'] = False
            response_data['cptch_key'] = CaptchaStore.generate_key()
            response_data['cptch_image'] = captcha_image_url(response_data['cptch_key'])

            return JsonResponse(response_data)

    else:
        return JsonResponse({"nothing to see": "this isn't happening"})
