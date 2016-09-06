from django.shortcuts import render
from django.views.generic import ListView

from .models import Article


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        queryset = Article.objects.published().select_related('author')
        queryset = queryset.prefetch_related('tags')
        return queryset
