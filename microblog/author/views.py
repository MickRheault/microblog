from django.shortcuts import render
from django.views.generic import ListView
from django.http import Http404

from articles.models import Article


class AuthorListView(ListView):
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        slug = self.kwargs.get('slug')

        # in case of None return 404
        if not slug:
            return Http404

        queryset = Article.objects.published()
        queryset = queryset.filter(author__username=slug)
        queryset = queryset.select_related('author')
        queryset = queryset.prefetch_related('tags')

        return queryset