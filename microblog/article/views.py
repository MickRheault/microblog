from django.views.generic import ListView, DetailView, View
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.db.models.functions import ExtractYear

from .models import Article
from newsletter.forms import NewsletterForm
from tag.models import Tag
from core.models import Link


class ArticleMixin(object):
    def get_queryset(self):
        queryset = Article.objects.published().select_related('author')
        queryset = queryset.prefetch_related('tags')
        return queryset


class ArticleListView(ArticleMixin, ListView):
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['newsletterform'] = NewsletterForm()

        return context


class ArticleDetailView(ArticleMixin, DetailView):
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tags'] = Tag.objects.filter(articles__status=Article.PUBLISHED).annotate(Count("articles")).\
            filter(articles__count__gt=0).order_by('-articles__count').values('slug', 'title', 'articles__count')
        context['related_articles'] = Article.objects.published().\
            filter(tags__in=self.object.tags.all()).distinct().\
            exclude(pk=self.object.pk).values('slug', 'title')[:4]
        context['links'] = Link.objects.all()
        context['articles_years'] = Article.objects.published().annotate(year=ExtractYear('publish_date')).\
            values('year').annotate(c=Count('id')).values('year', 'c').order_by('-year')

        return context


class ArticlePreviewView(DetailView):
    template_name = 'articles/article_preview.html'
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
    paginate_by = 7

    def get_queryset(self):
        slug = self.kwargs.get('slug')

        # in case of None return 404
        if not slug:
            raise Http404

        queryset = super().get_queryset()
        queryset = queryset.filter(author__username=slug)

        return queryset


class SearchView(ArticleMixin, ListView):
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 7

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')

        if q:
            queryset = queryset.filter(Q(title__icontains=q)|Q(tags__title__iexact=q)).distinct()
        return queryset


class ArticleYearView(ArticleMixin, ListView):
    template_name = 'articles/article_list.html'
    paginate_by = 7
    context_object_name = 'articles'

    def get_queryset(self):
        year = self.kwargs.get('year')

        # in case of None return 404
        if not year:
            raise Http404

        queryset = super().get_queryset()
        queryset = queryset.filter(publish_date__year=year)
        return queryset


class ChangeArticleStatus(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff and not request.user.is_superuser:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        id = request.POST.get('id', None)
        url = request.POST.get('url', None)
        transition_method = [key for key in request.POST.keys() if key.startswith("___")]

        if not id or not url or len(transition_method) != 1:
            raise Http404

        transition_method = transition_method[0][3:]

        obj = get_object_or_404(Article, pk=int(id))

        if transition_method not in [method.name for method in list(Article.get_available_status_transitions(obj))]:
            raise Http404

        getattr(obj, transition_method)()
        obj.save()
        messages.info(request, "Pomyślnie zmieniono status")

        return redirect(url)
