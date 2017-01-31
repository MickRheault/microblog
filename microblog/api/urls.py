from django.conf.urls import url

from rest_framework.authtoken.views import obtain_auth_token

from .views import ArticleList, ArticleListLast, ArticleDetail, ArticleCreateView, ArticleDeleteView, \
    TagList, TagListLast, TagDetail, TagCreateView, TagDeleteView, \
    UserListView

urlpatterns = [
    url(r'^get-token/$', obtain_auth_token),
    # article
    url(r'^article/all/$', ArticleList.as_view()),
    url(r'^article/last/(?P<limit>\d+)/$', ArticleListLast.as_view()),
    url(r'^article/(?P<pk>\d+)/$', ArticleDetail.as_view()),
    url(r'^article/add/$', ArticleCreateView.as_view()),
    url(r'^article/delete/(?P<pk>\d+)/$', ArticleDeleteView.as_view()),
    # tag
    url(r'^tag/all/$', TagList.as_view()),
    url(r'^tag/last/(?P<limit>\d+)/$', TagListLast.as_view()),
    url(r'^tag/(?P<pk>\d+)/$', TagDetail.as_view()),
    url(r'^tag/add/$', TagCreateView.as_view()),
    url(r'tag/delete/(?P<pk>\d+)/$', TagDeleteView.as_view()),
    # user
    url(r'^user/all/$', UserListView.as_view()),
]
