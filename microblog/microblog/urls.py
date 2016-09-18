from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^captcha/', include('captcha.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^other/', include('other.urls', namespace='other')),
    url(r'^tag/', include('tag.urls', namespace='tag')),
    url(r'^guest-book/', include('guest_book.urls', namespace='guest-book')),
    url(r'^', include('article.urls', namespace='article')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
