from django.conf.urls import url
from django.views.decorators.cache import cache_page
from django.conf import settings

from .views import ArticleListView, ArticleDetailView, ArticleAuthorListView, \
    ArticlePreviewView, SearchView, ChangeArticleStatus, ArticleYearView
from .feeds import LatestArticlesFeed

urlpatterns = [
    url(r'^article/change/status/$', ChangeArticleStatus.as_view(), name='change_status'),
    url(r'^preview/(?P<pk>\d+)/$', ArticlePreviewView.as_view(), name='preview'),
    url(r'^latest/feed/$', LatestArticlesFeed()),
    url(r'^author/(?P<slug>\w+)/$', cache_page(settings.CACHE_TIME)(ArticleAuthorListView.as_view()),
        name='author-list'),
    url(r'^year/(?P<year>\d+)/$', cache_page(settings.CACHE_TIME)(ArticleYearView.as_view()), name='year'),
    url(r'^search/', SearchView.as_view(), name='search'),
    url(r'^(?P<slug>[\w-]+)/$', cache_page(settings.CACHE_TIME)(ArticleDetailView.as_view()), name='detail'),
    url(r'^$', ArticleListView.as_view(), name='list'),
]
