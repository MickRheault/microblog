from django.shortcuts import render
from django.views.generic import ListView
from django.http import Http404

from article.views import ArticleSearchMixin


class TagsListView(ArticleSearchMixin, ListView):
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        slug = self.kwargs.get('slug')

        # in case of None return 404
        if not slug:
            return Http404

        queryset = super().get_queryset()
        queryset = queryset.filter(tags__slug__exact=slug)

        return queryset
