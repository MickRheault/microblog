from django.shortcuts import render
from django.views.generic import ListView

from .models import Article


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    queryset = Article.objects.published()
