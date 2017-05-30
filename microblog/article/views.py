from django.contrib.syndication.views import Feed
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.db.models import Q

from .models import Article


class ArticleMixin(object):
    def get_queryset(self):
        queryset = Article.objects.published().select_related('author')
        queryset = queryset.prefetch_related('tags')
        return queryset


class ArticleListView(ArticleMixin, ListView):
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 5


class ArticleDetailView(ArticleMixin, DetailView):
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'


class ArticlePreviewView(DetailView):
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if request.user.is_staff or self.object.author == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_queryset(self):
        queryset = Article.objects.all().select_related('author')
        queryset = queryset.prefetch_related('tags')
        return queryset


class ArticleAuthorListView(ArticleMixin, ListView):
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


class LatestArticlesFeed(Feed):
    title = 'Najnowsze Artykuły'
    link = "/"

    def items(self):
        return Article.objects.published()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.desc

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse_lazy('article:detail', args=[item.slug])


class SearchView(ArticleMixin, ListView):
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')

        if q:
            queryset = queryset.filter(Q(title__icontains=q)|Q(author__username__iexact=q))
        return queryset