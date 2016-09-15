from django.conf.urls import url

from .views import TagsListView

urlpatterns = [
    url(r'(?P<slug>\w+)/$', TagsListView.as_view(), name='list')
]
