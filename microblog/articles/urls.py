from django.conf.urls import url

from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='list'),
    url(r'(?P<slug>[\w-]+)/$', ArticleDetailView.as_view(), name='detail')
]
