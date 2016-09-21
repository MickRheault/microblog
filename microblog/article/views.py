from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Article
from .forms import SearchForm


class ArticleMixin(object):
    def get_queryset(self):
        queryset = Article.objects.published().select_related('author')
        queryset = queryset.prefetch_related('tags')
        return queryset


class ArticleSearchMixin(ArticleMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['searchform'] = SearchForm()

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.GET.get('search'):
            queryset = queryset.filter(title__icontains=self.request.GET.get('search'))
        return queryset


class ArticleListView(ArticleSearchMixin, ListView):
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 5


class ArticleDetailView(ArticleMixin, DetailView):
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'


class ArticleAuthorListView(ArticleSearchMixin, ListView):
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        slug = self.kwargs.get('slug')

        # in case of None return 404
        if not slug:
            raise Http404

        queryset = super().get_queryset()
        queryset = queryset.filter(author__username=slug)

        return queryset
