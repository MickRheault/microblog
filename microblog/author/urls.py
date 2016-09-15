from django.conf.urls import url

from .views import AuthorListView

urlpatterns = [
    url(r'(?P<slug>\w+)/$', AuthorListView.as_view(), name='list')
]
