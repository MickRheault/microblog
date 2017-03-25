from django.contrib import admin
from django.utils import timezone
from django.utils.text import slugify
from django.forms.widgets import Textarea
from django.core.urlresolvers import reverse

from django_markdown.admin import AdminMarkdownWidget

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'link', 'creation_date',)
    fields = ('title', 'desc', 'text', 'image', 'publish', 'tags')

    def link(self, obj):
        link = reverse('article:detail', kwargs={'slug': obj.slug})
        return '<a href="%s">%s</a>' % (link, link)

    link.allow_tags = True

    def save_model(self, request, obj, form, change):
        obj.author = request.user

        # Auto update publish date when publish is true
        if form.cleaned_data['publish'] is True:
            obj.publish_date = timezone.now()

        # Slugify title and save it as slug
        obj.slug = slugify(form.cleaned_data['title'], allow_unicode=True)

        super().save_model(request, obj, form, change)

    def formfield_for_dbfield(self, db_field, **kwargs):
        # Setup widget to specified field
        if db_field.name == 'desc':
            kwargs['widget'] = Textarea
        if db_field.name == 'text':
            kwargs['widget'] = AdminMarkdownWidget

        return super(ArticleAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Article, ArticleAdmin)
