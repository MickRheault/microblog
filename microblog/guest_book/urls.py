from django.conf.urls import url

from .views import EntriesList, CreateEntry

urlpatterns = [
    url(r'^$', EntriesList.as_view(), name='index'),
    url(r'^create-entry/$', CreateEntry.as_view())
]
