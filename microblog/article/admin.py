from slugify import slugify

from django.contrib import admin
from django.utils import timezone

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'creation_date',)
    fields = ('title', 'text', 'image', 'publish', 'tags')

    def save_model(self, request, obj, form, change):
        obj.author = request.user

        # Auto update publish date when publish is true
        if form.cleaned_data['publish'] is True:
            obj.publish_date = timezone.now()

        # Slugify title and save it as slug
        obj.slug = slugify(form.cleaned_data['title'])

        super().save_model(request, obj, form, change)

admin.site.register(Article, ArticleAdmin)
