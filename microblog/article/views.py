from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Article


class ArticleMixin(object):

    @staticmethod
    def get_queryset():
        queryset = Article.objects.published().select_related('author')
        queryset = queryset.prefetch_related('tags')
        return queryset


class ArticleListView(ArticleMixin, ListView):
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'


class ArticleDetailView(ArticleMixin, DetailView):
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'
