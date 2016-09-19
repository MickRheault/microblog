from django.conf.urls import url

from .views import ArticleListView, ArticleDetailView, ArticleAuthorListView

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='list'),
    url(r'author/(?P<slug>\w+)/$', ArticleAuthorListView.as_view(), name='author-list'),
    url(r'(?P<slug>[\w-]+)/$', ArticleDetailView.as_view(), name='detail'),
]
