from django.conf.urls import url
from django.views.decorators.cache import cache_page
from django.conf import settings

from .views import TagsListView

urlpatterns = [
    url(r'(?P<slug>\w+)/$', cache_page(settings.CACHE_TIME)(TagsListView.as_view()), name='list')
]
