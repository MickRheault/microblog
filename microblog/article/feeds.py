from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse_lazy

from .models import Article


class LatestArticlesFeed(Feed):
    title = 'Najnowsze Artykuły'
    link = "/"

    def items(self):
        return Article.objects.published()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.desc

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse_lazy('article:detail', args=[item.slug])