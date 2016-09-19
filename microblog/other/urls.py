from django.conf.urls import url

from .views import OtherDetailView

urlpatterns = [
    url(r'(?P<slug>[\w-]+)/$', OtherDetailView.as_view(), name='detail')
]
