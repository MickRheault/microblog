from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^captcha/', include('captcha.urls')),
    url('^markdown/', include('django_markdown.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^other/', include('other.urls', namespace='other')),
    url(r'^tag/', include('tag.urls', namespace='tag')),
    url(r'^api/v0.1/', include('api.urls', namespace='api')),
    url(r'^', include('article.urls', namespace='article')),
]

if 'guest_book' in settings.INSTALLED_APPS:
    urlpatterns = [url(r'^guest-book/', include('guest_book.urls', namespace='guest-book'))] + urlpatterns

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)