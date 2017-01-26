from django.conf.urls import url

from .views import ArticleList, ArticleListLast, ArticleDetail, \
    TagList, TagListLast, TagDetail, \
    UserListView

urlpatterns = [
    # article
    url(r'^article/all/$', ArticleList.as_view()),
    url(r'^article/last/(?P<limit>\d+)/$', ArticleListLast.as_view()),
    url(r'^article/(?P<pk>\d+)/$', ArticleDetail.as_view()),
    # tag
    url(r'^tag/all/$', TagList.as_view()),
    url(r'^tag/last/(?P<limit>\d+)/$', TagListLast.as_view()),
    url(r'^tag/(?P<pk>\d+)/$', TagDetail.as_view()),
    # user
    url(r'^user/all/$', UserListView.as_view()),
]
