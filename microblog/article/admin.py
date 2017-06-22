from django.contrib import admin
from django.utils.text import slugify
from django.forms.widgets import Textarea
from django.core.urlresolvers import reverse

from markdownx.admin import AdminMarkdownxWidget

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'link', 'creation_date',)
    fields = ('title', 'desc', 'text', 'image', 'tags', 'status')
    list_filter = ('status',)
    readonly_fields = ('status',)

    def link(self, obj):
        link = reverse('article:preview', kwargs={'pk': obj.id})
        return '<a href="%s">%s</a>' % (link, link)

    link.allow_tags = True

    def save_model(self, request, obj, form, change):
        obj.author = request.user

        # Slugify title and save it as slug
        obj.slug = slugify(form.cleaned_data['title'], allow_unicode=True)

        super().save_model(request, obj, form, change)

    def formfield_for_dbfield(self, db_field, **kwargs):
        # Setup widget to specified field
        if db_field.name == 'desc':
            kwargs['widget'] = Textarea
        if db_field.name == 'text':
            kwargs['widget'] = AdminMarkdownxWidget

        return super(ArticleAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Article, ArticleAdmin)
