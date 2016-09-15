from django.conf.urls import url

from .views import entries_list, create_entry

urlpatterns = [
    url(r'^$', entries_list, name='index'),
    url(r'^create-entry/$', create_entry)
]
