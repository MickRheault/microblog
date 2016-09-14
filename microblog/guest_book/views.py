from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

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
        entry.is_valid()
        entry = entry.save()
        html = (render_to_string('guest_book/snippets/entry_item.html', {
            'id': entry.id,
            'author': entry.author,
            'text': entry.text
        }))
        response_data['result'] = 'Create post successful!'
        response_data['html'] = html

        return JsonResponse(response_data)
    else:
        return JsonResponse({"nothing to see": "this isn't happening"})
