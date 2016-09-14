from django.shortcuts import render
from django.views.generic import DetailView

from .models import Other


class OtherDetailView(DetailView):
    template_name = 'other/other_detail.html'
    context_object_name = 'other'
    model = Other
