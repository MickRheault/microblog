from django.conf.urls import url

from .views import NewsletterVerficationView, NewsletterEmailVerficationView, NewsletterCancelView

urlpatterns = [
    url(r'verify/$', NewsletterVerficationView.as_view(), name='verify'),
    url(r'verify/(?P<token>[\w]+)/$', NewsletterEmailVerficationView.as_view(), name='verify_email'),
    url(r'cancel/(?P<token>[\w]+)/$', NewsletterCancelView.as_view(), name='cancel')
]
