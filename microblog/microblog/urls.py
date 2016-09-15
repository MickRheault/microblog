from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^other/', include('other.urls', namespace='other')),
    url(r'^tag/', include('tags.urls', namespace='tag')),
    url(r'^author/', include('author.urls', namespace='author')),
    url(r'^guest-book/', include('guest_book.urls', namespace='guest-book')),
    url(r'^', include('articles.urls', namespace='articles')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
